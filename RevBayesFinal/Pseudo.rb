#######################
# Reading in the Data #
#######################



### I used the template provided in the RevBayes webpage  ###
#This tutorial can be found in http://revbayes.github.io/tutorials.html  /Species tree estimation/concatenation of multiple   genes/example script# 
      
###### This just defines a single model for all sites #######
# read in each data matrix together which will create a vector of objects
data = readDiscreteCharacterData("data/conRB.nex")


# Now we get some useful variables from the data. We need these later on.
#this allow to explore the input data
num_loci = data.size()
# get the number of species
n_species <- data[1].ntaxa()
# get the taxon information (e.g. the taxon names)
taxa <- data[1].taxa()
n_branches <- 2 * n_species - 1 # number of branches in a rooted tree

# We set our move index
mi = 0



######################
# Species-Tree model #
######################

### I am stil trying to understan why the values of speciation and extinction are set up with different distibributions, my understanding so far is that we can have a sense of the rate of speciation, whereas for the relative extinction we only can model probability of that extinction happens alonf the tree, I might be wrong and confused, but I am still trying to understand better this###

# Specify a prior on the diversification and turnover rate
speciation ~ dnGamma(2,2) # this a bernoulli distribution with value of 1 that take the probability of p and 0 the probablity of 1-p, first argument is the parameter value of the shape, and the secon argument is the value of the rate#
relativeExtinction ~ dnBeta(1,1) #A beta distribution probability, first argument is the alpha shape parameter value of the shape, and the secon argument is beta value of the shape #

### I am confuse on how we can estimate extinction by multiplying speciation "rate" with the relative extinction
# now transform the diversification and turnover rates into speciation and extinction rates
extinction := speciation * relativeExtinction

### I specify an age from the literature that say that this group should be around 40 ish mya, but I don't know if this value of the mean and 2.5 standar deviation aproximate this value of 40 ish mya 
# specify a prior on the root age (our informed guess is about young as 5 and old as 50 mya I used here the more extreme ends)
root ~ dnNormal(mean=35,sd=2.5,min=0.0, max=Inf)

#the way they have this set up seems to be they ask how many lineage are represented in the data of the know lineage(species) recognized. 

sampling_fraction <- 8 / 9 # 8 out of the 9 recognized species of Pseudoxiphophorus, one species have not been collected in at least 50 years, and just one hypothesis (the morphological one, posses representatives of this species)  

# create some moves that change the stochastic variables
# all moves are sliding and scaling proposals
moves[++mi] = mvSlide(speciation,delta=1,tune=true,weight=2)
moves[++mi] = mvSlide(relativeExtinction,delta=1,tune=true,weight=2)
moves[++mi] = mvScale(speciation,lambda=1,tune=true,weight=2)
moves[++mi] = mvScale(relativeExtinction,lambda=1,tune=true,weight=2)
moves[++mi] = mvSlide(root,delta=1,tune=true,weight=0.2)


# construct a variable for the tree drawn from a birth death process
psi ~ dnBDP(lambda=speciation, mu=extinction, rootAge=root, rho=sampling_fraction, taxa=taxa )

moves[++mi] = mvNarrow(psi, weight=5.0)
moves[++mi] = mvNNI(psi, weight=1.0)
moves[++mi] = mvFNPR(psi, weight=3.0)
moves[++mi] = mvGPR(psi, weight=3.0)
moves[++mi] = mvSubtreeScale(psi, weight=3.0)
moves[++mi] = mvNodeTimeSlideUniform(psi, weight=15.0)




###############
# Clock Model #
###############

for ( i in 1:num_loci ) { 
   log_clock_rate[i] ~ dnUniform(-8,4)
   clock_rate[i] := 10^log_clock_rate[i]
   
   moves[++mi] = mvSlide(log_clock_rate[i], weight=1.0)
}


######################
# Substitution Model #
######################


for ( i in 1:num_loci ) {

    #### specify the HKY substitution model applied uniformly to all sites ###
    kappa[i] ~ dnLognormal(0,1)
    moves[++mi] = mvScale(kappa[i],weight=1)


    pi_prior[i] <- v(1,1,1,1) 
    pi[i] ~ dnDirichlet(pi_prior[i])
    moves[++mi] = mvSimplexElementScale(pi[i],weight=2)


    #### create a deterministic variable for the rate matrix ####
    Q[i] := fnHKY(kappa[i],pi[i]) 

}




#############################
# Among Site Rate Variation #
#############################


for ( i in 1:num_loci ) {

    alpha_prior[i] <- 0.05
    alpha[i] ~ dnExponential( alpha_prior[i] )
    gamma_rates[i] := fnDiscretizeGamma( alpha[i], alpha[i], 4, false )

    # add moves for the stationary frequencies, exchangeability rates and the shape parameter
    moves[++mi] = mvScale(alpha[i],weight=2)

}

###################
# PhyloCTMC Model #
###################



for ( i in 1:num_loci ) { 
    # the sequence evolution model
    seq[i] ~ dnPhyloCTMC(tree=psi, Q=Q[i], branchRates=clock_rate[i], siteRates=gamma_rates[i], type="DNA")

    # attach the data
    seq[i].clamp(data[i])
}




#############
# THE Model #
#############

# We get a handle on our model.
# We can use any node of our model as a handle, here we choose to use the topology.
mymodel = model(psi)

# Monitors to check the progression of the program
monitors[1] = mnScreen(printgen=100, root)
monitors[2] = mnModel(filename="Pseudo1.log",printgen=10, separator = TAB)
monitors[3] = mnFile(filename="Pseudo1.trees",printgen=10, separator = TAB, psi)

# Here we use a plain MCMC. You could also set nruns=2 for a replicated analysis
# or use mcmcmc with heated chains.
nruns=2 
mymcmc = mcmc(mymodel, monitors, moves)

# This should be sufficient to obtain enough MCMC samples
mymcmc.burnin(generations=5000,tuningInterval=100)
mymcmc.run(generations=5000000)


# Now, we will analyze the tree output.
# Let us start by reading in the tree trace
treetrace = readTreeTrace("Pseudo1.trees", treetype="clock")
# and get the summary of the tree trace
#treetrace.summarize()

mapTree(treetrace,"output/Pseudo1.tree")

# you may want to quit RevBayes now
q()

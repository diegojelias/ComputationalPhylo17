Final Assingment Using RevBayes
===============================


Methods: 
========
The phylogenetics relationships of the genus Pseudoxiphophorus (Poecilinae:Poeciliidae) was infer using a bayesian approach 
using the software RevBayes (Hohna......) using a data set of 1 mitochondrial gene (cyt b) and 5 nuclear loci: 2 exons (SREB2 and SH3PX3)
and 3 introns (UNG, POLB and FEN1), under concatenation of multiple genes. assuming the same substitution model (HKY) for all 
the loci under study, even if this assumption is not biologically realistic, we can compare the results of this approach analyzing this dataset
under other models and in a partition scheme later on. 

We visually inspects two different runs, one that only ran for 100,000 iterations (generations) and one that run for 2,000,000 iterations (generations) 
the performance of the runs, were visually assessed using the software tracer (Rambaud.....) and the topology are recovered with a maximum a posteriori tree (MAP tree)
representation of the distribution of trees generated during the MCMCM run. 

A script of the analysis is provided in 
For the script of this analysis a template was obtain from the RevBayes repository (http://revbayes.github.io/tutorials.html)
for the MCMC analysis of 2,000,000 generations, 2 independent runs were set up, but a error in the way the script was set up: 
see line 161, were the number of runs (nruns=2) was not passed as an argument of the function mymcmc (........) which lead to that the analysis 
only realize one single run. this mistake did not allow me to check for convergence of the parameters and topology for the present analysis.   
 
 
Results: 
=========
For the MCMC run in RevBayes with 100,000 iterations(generations), effective sampling size for posterior and prior did not mix properly (see Ta supplementary figure 1) 
for the longer run 2,000,000 iterations(generations) all parameters mix well and effective sample size is higher than the cutoff of 200. convergence of results  in independent runs could not be evaluated do the 
error in the RevBayes script. but posterior independent runs will be performed to asses convergence not only of the MCMC run but as well convergence of parameters space sampled and effective sampling size 
of independent runs. 

**Table 1 Effective sampling size of two independent runs of different length of iterations
![example image](ESS.png)

MCMC run 											Efective Sampling Size				
No. of iterations (generations)				Posterior 	Likelihood	Prior	alpha (exchangeability) 	Kappa (substitution model)
100,000											75			260		38				>200							>200
2,000,000									  >1000		   >1000   >1000			>200							>200

Tree topology was compared among the short (100,000 iterations) and the long (2,000,000 iterations) 


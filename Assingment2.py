#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 09:40:45 2017

@author: diegoelias
"""
"""
The following assingment is still incomplete, I have some problems making the loop, to reduce the difference in the problem 2b, automatically (working on fixing this)
I am still working in problem 2c, took me a while resolve partially 2b, but working to finish 2c

Part of this code was the results of disscusion with Alec Turner, Pamela Hart and the discussion in the slack channel
as well some ideas come from stack overflow on how to code for draw a random number 2a #5
"""
"""
The following function "multidecreasing" allow for multiplication of all the consecutive decreasing numbers from a range of intengers.

multidecreasing(Max, Min)
Max = to the maximum integer 
Min = to the minimun integer 

for example given the argument (5,3) the function multidecreasing will allow for multiplication of the intengers in the range from 5 to 3;
multidecreasing (5,3) = 5*4*3 = 60
"""
def multdecreasing (Max, Min):
    Max2 = Max
    Min2 = Min 
    num = 1
 
    for i in range(Max2, Min2-1,  -1):
        #print(i)
        num *= i
    #return(num)
    print('The product of the consecutive decreasing integers from', str(Max), 'to', str(Min), 'is = ', str(num))
multdecreasing(11, 10)


"""
This function provide the factorial of any number, 
The number can be provided as argument in the variable Factof
"""
def Facto(f):
    nf = f
    fact = 1
    for j in range (nf, 1, -1):
        fact = fact*j
    print('the factorial of' , str(nf), 'is = ', str(fact))

"""
Binomial coeficient (all calculations)

"""
def Binocoef (n,k):
    n2 = n
    k2 = k
    nk = n - k
    numn = 1
    numk = 1
    numnk = 1
    if k2 > n2:
        print('The binomial coefficient is = 0; when k>n the binomial coefficient is undefined')
    else:
        for i in range (n2, 1, -1):
            numn = numn*i
        for j in range (nk, 1, -1):
            numk = numk*j
        for k in range (k2, 1, -1):
            numk = numk*k
        binomial = (numn/(numk*numnk))
        print('the binomial coefficient when', str(n), "choose", str(k), 'is = ', str(binomial))

"""
Binomial coefficient (simplified calculation)
"""
def simpbincoef (n,k):
    n3 = n
    k3 = k
    A = (n3*(n3 - 1))
    B = (n3 - k3 + 1)
    numk3 = 1
    num3 = 1
    if k3 > n3:
        print('The binomial coefficient is = 0; when k>n the binomial coefficient is undefined')
    else:
        for i in range (B, n3 + 1 ):
            num3= num3*i
        for j in range (k3, 1, -1):
            numk3 = numk3*j 
        simpbin = num3/numk3
        #print(simpbin)
        print('the binomial coefficient when', str(n), "choose", str(k), 'is = ', str(simpbin))

"""
Simplified binomial coeficient to be used in the calculation of probability  mass function (PMF)
is the same than the previous function, but this function only store the values of the results and 
do not print any text in the screen
"""
def bincoefberno (n,k):
    n4 = n
    k4 = k
    A = (n4*(n4 - 1))
    B = (n4 - k4 + 1)
    numk4 = 1
    num4 = 1
    if k4 > n4:
        print('The binomial coefficient is = 0; when k>n the binomial coefficient is undefined therefore the PMF = 0')
    else:
        for i in range (B, n4 + 1 ):
            num4= num4*i
        for j in range (k4, 1, -1):
            numk4 = numk4*j 
        simpbin = num4/numk4
        return simpbin
        #print('the binomial coefficient when', str(n), "choose", str(k), 'is = ', str(simpbin))

"""
PFM of k success in Bernoulli trial
"""
"""
def PMF (n,k,prob):
    n4 = n
    k4 = k
    p = prob
    nminusk = n4 - k4
    nchoosek = bincoefberno(n,k)
    comprob = 1 - p 
    Praisek = pow(p,k4)
    lastsegment = pow(comprob,nminusk)
    #return nchoosek*(pow(prob,k))*(pow(1-prob,n-k))
    #pmf = ((nchoosek*(pow(p,4)))*(pow(comprob,nminusk)))
    pmf = (nchoosek*Praisek)*lastsegment
    #print = nchoosek
    #print = Praisek
    return pmf
"""
def PMF (n,k,prob):
    nchoosek = bincoefberno(n,k)
    return nchoosek*(pow(prob,k))*(pow(1-prob,n-k))
    
"""
Sampling from a discrete distribution
"""
Dist = list(range(11))


elements = np.array([0, 1, 2, 3, 4, 5])
probabilites = np.array([0.1, 0.1, 0.1, 0.5, 0.1, 0.1])
np.random.choice(elements, 100, p=list(probabilites))

"""
Hill Climbing
The backbone of this code was developed by Pamela Hart and myself

"""
def hillclimb(n,k,p,d):
    pCurr= p
    diff = d
    precision = 0.001
    while (diff > precision):
        pUp= pCurr+diff
        pDown= pCurr-diff
        likelipCurr=PMF(n,k,pCurr)
        likelipUp=PMF(n,k,pUp)
        likelipDown=PMF(n,k,pDown)
        maxlik = max(likelipCurr,likelipUp, likelipDown )
        while (likelipCurr > likelipUp) or (likelipCurr > likelipDown):
            pCurr = pCurr
            print (pCurr)
            while (likelipCurr != maxlik):
                #print(likelipCurr)
                while likelipUp > likelipCurr:
                    pCurr = pUp
                    pUp = pCurr+diff
                    likelipCurr=PMF(n,k,pCurr)
                    likelipUp=PMF(n,k,pUp)
                    likelipDown=PMF(n,k,pDown)
                    print(pCurr,likelipCurr)
                while likelipDown > likelipCurr:
                    pCurr = pDown
                    pDown = pCurr-diff
                    likelipCurr=PMF(n,k,pCurr)
                    likelipUp=PMF(n,k,pUp)
                    likelipDown=PMF(n,k,pDown)
                    print(pCurr, likelipCurr)
        #if likelipCurr > likelipUp and likelipCurr > likelipDown:
                break
            return(pCurr, likelipCurr)
import random
def randks():
    p=0.3
    n=5
    d= 0.1
    PCurr=p
    diff=d
    precision=0.001
    listak=[]
    MLs=[]
    LR=[]
    for i in range (8)
        listak.append(random.randrange(0,n=+1,1))
        k==listak
    print (listak)
    for k in listak: 
        print(k)
        ML = hillclimb(n,p,k,d)
        MLs.append(ML)
    print(len(MLs))



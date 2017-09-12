"""
This module contains the functions required for the 
optimization of the replicas: 
given a defined number of replicas, optimization means 
producing sigma-parameters that give a sequence of 
replicas with an exchange probability of roughly the target value.

The optimization is made for a collection of replicas of non-interacting dimers 
which is a good approximation since the interacting potential does not enter 
in the swap acceptation rate and has a weak influence on the probability 
distribution of the dimer's length.

The central part of the optimization procedure is the 
probability distribution of the dimer's length s, 
p_\sigma(s) = \frac{exp(-\beta f(s)}{Z_\sigma} where 
f(s) is the dimer interaction energy. Then the probability to 
swap the configurations of two replicas is p_1^N, 
where p_1 is the probability to swap a single dimer and N is the number 
of dimerized atoms. 
p_1 = [\int ds exp(-\beta f_\sigma1 (s)) exp(-\beta f_\sigma2(s))]^2/ Norm
with Norm = \int ds exp(-2\beta f_\sigma1(s)) * \int ds exp(-2\beta f_\sigma2(s))

"""

import math

def f(s,sigma,q):
   """
   Dimer interaction strength in units of 1/beta
   """
   return (1.0 + s**2/(2*q*sigma**2))**q - 1.0
   

   
def integ(func,rng,npoints):
   """
   Integrade func(x) over an integral defined by the tuple rng 
   using npoints points. Just a first order integration as the 
   integrand is well defined and smooth. 
   """
   ds = (rng[1]-rng[0])/(npoints-1)
   intg = 0.0
   for i in xrange(npoints):
      cs = rng[0] + i*ds
      intg = intg + func(cs)
      
   return intg*ds
   

def prob(sig1,sig2,q,gamma,N, rng, npoints):
   """
   Probability two swap between two replicas of non-interacting N dimers with 
   parameters q, sig1 and sig2. gamma is the boosting factor of metadynamics, 
   rng and npoints are respectively numerical integrations interval and points.
   
   Makes use of three wrapper functions that call f(s,sigma,q) previously deifned.
   Returns the probability.
   
   """
   def z1(s):
      return math.exp(-2*f(s,sig1,q)/gamma)
      
   def z2(s):
      return math.exp(-2*f(s,sig2,q)/gamma)
         
   def numf(s):
      return math.exp(-(f(s,sig1,q)+f(s,sig2,q))/gamma)
   
   Z1 = integ(z1,rng,npoints)
   Z2 = integ(z2,rng,npoints)
   num = integ(numf, rng,npoints)

   return (num**2/(Z1*Z2))**N


def findopt(sigstart,ptarg,q,gamma,N, nsigmaint=20, intres=100, epsend = 0.01, escloop = 200):
   """
   Given a starting value of sigma, say sigma1, find sigma2 that gives roughly the 
   target acceptation rate of a swap between two replicas with those values of sigma.
   INPUT:
           sigstart  =  sigma value of the first replica
	   ptarg     =  target swap probability
	   q         =  interaction strength exponent
	   gamma     =  Metadynamics boosting factor
	   N         =  number of dimers
	   nsigmaint =  range of integration in sigma-units. sigma will be determined 
	                as the largest one used by the algorithm.
	   intres    =  integral resolution, defined as the number of integration points 
	                in an interval of length sigma defined as in the previous case.
	   epsend    =  accuracy required to break the bisection loop
	   escloop   =  maximum bisection iterations before giving up
	   
	   
   This function returns a tuple with the best value of sigma and the expected 
   acceptance probability.
   """
   sigend=2*sigstart
   intpoints=nsigmaint*intres
   p = prob(sigstart,sigend,q,gamma,N, (0,nsigmaint*sigend), intpoints)
   while p > ptarg:
      sigend = sigend + sigstart
      p = prob(sigstart,sigend,q,gamma,N, (0,nsigmaint*sigend), intpoints)
   
   sigint=nsigmaint*sigend
   
   sL=sigstart
   sR=sigend
   sM = (sL+sR)/2
   for i in xrange(escloop):
      pL = prob(sigstart,sL,q,gamma,N, (0,sigint), intpoints) - ptarg
      pR = prob(sigstart,sR,q,gamma,N, (0,sigint), intpoints) - ptarg
      sM=(sL+sR)/2
      pM = prob(sigstart,sM,q,gamma,N, (0,sigint), intpoints) - ptarg
      
      if pL*pM < 0:
         sR=sM
      else:
         sL=sM
      
      if abs(pM) < epsend:
         break

   sM = (sR+sL)/2
   pM = prob(sigstart,sM,q,gamma,N, (0,sigint), intpoints)
   
   return (sM,pM)

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:57:42 2017

@author: zoe.steier
"""

# Rosalind Independent Allels

##Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, 
#who in the 0th generation has genotype AaBb. Tom has two children in the 1st generation,
#each of whom has two children, and so on. 
# Each organism always mates with an organism having genotype Aa Bb.
#Return: The probability that at least N AaBb organisms will belong to the k-th 
#generation of Tom's family tree (don't count the AaBb mates at each level). 
#Assume that Mendel's second law holds for the factors.

#Sample Dataset
sample = ('2 1')
#Sample Output
sampleout = 0.684

s = input('Enter k and N: ') # k = generation, N = number of AaBb organisms
splitin = s.split()
k = int(splitin[0])
N = int(splitin[1])

import math
# calculate factorials for combinations

def nChoosek(n, k):
    '''Calculate combinations n choose k using math factorial function.'''
    f = math.factorial
    ans = f(n) // f(k) // f(n-k) # nChoosek = n!/(k!(n-k)!)
    return(ans)
    
# the probability of getting exactly some offspring of AaBb is the binomial coefficient (same as nchoosek) * p(AaBb) *p(not AaBb)
    
# the total probability of at least N offspring is 1 - p(everything less than N)
    
tot = 1 # starting probability
# offspring per generation = 2**k
pAaBb = 0.25
pnot = 0.75
for i in range(N):
    tot -= nChoosek(2**k, i) * pAaBb**i * pnot**(2**k - i)
    
print(tot)
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:57:42 2017

@author: zoe.steier
"""

# Rosalind Independent Allels

##Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, 
#who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation,
# each of whom has two children, and so on. 
# Each organism always mates with an organism having genotype Aa Bb.
#Return: The probability that at least NN Aa Bb organisms will belong to the kk-th 
#generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

#Sample Dataset
sample = ('2 1')
#Sample Output
sampleout = 0.684

s = input('Enter k and N: ') # k = generation, N = number of AaBb organisms
splitin = s.split()
k = int(splitin[0])
N = int(splitin[1])

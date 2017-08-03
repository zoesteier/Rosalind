# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:31:27 2017

@author: zoe.steier
"""

# Rosalind Partial Permutations

#Given: Positive integers nn and kk such that 100≥n>0100≥n>0 and 10≥k>010≥k>0.
#Return: The total number of partial permutations P(n,k)P(n,k), modulo 1,000,000.
#
#Sample Dataset
sample = ('21 7')
#Sample Output
sampleout = 51200


# Find the number of permutations
inputnum = input('Enter n and k: ').split()
n = int(inputnum[0])
k = int(inputnum[1])

def partperm(n, k, base):
    'Find modulo of partial permutations of n.'''
    mod = 1
    for i in range(n, n-k, -1):
        mod = ((mod*i) % base)
    return(mod)

base = 10**6
ans = partperm(n, k, base)
print(ans)
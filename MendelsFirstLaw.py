# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Mendel's First Law


# Given: Given: Three positive integers kk, mm, and nn, representing a population containing k+m+nk+m+n organisms: kk individuals are homozygous dominant for a factor, mm are heterozygous, and nn are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Sample dataset
# 2 2 2

#sampleoutput
# 0.78333


# Get k, m, n from input
s = input('Enter k (homozygous dominant), m (heterozygous), and n (homozygous recessive): ')
k, m, n = int(s.split()[0]), int(s.split()[1]), int(s.split()[2])

# Calculate the probability of organisms with a dominant allele mating
tot = k + m + n # total number of individuals
# probability of choosing individuals from total pool
K = k/tot
M = m/tot
N = n/tot

# The total probability is the sum of three probabilities:
    # Choosing k either first or second, p(dom) = 1
    # Choosing m then n, or n then m, p(dom) = 0.5
    # Choosing m then m, p(dom) = 0.75
    
pA = K + M*k/(tot-1) + N*k/(tot-1)
pB = (M*n/(tot-1) + N*m/(tot-1))*0.5
pC = M*(m-1)/(tot-1)*0.75
pdom = pA + pB + pC

# Return probability of child with dominant allele
print(pdom)
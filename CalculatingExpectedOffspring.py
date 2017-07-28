# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Calculating Expected Offspring

# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
#AA-AA
#AA-Aa
#AA-aa
#Aa-Aa
#Aa-aa
#aa-aa

#Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

import numpy as np

# Sample dataset
sample = '1 0 0 1 0 1'
# Sample output
sampleout = 3.5
# uncomment for real dataset
s = input('Enter number of couples of each genotype: ')

# uncomment for testing the sample dataset
#s = sample #s is the DNA string

# convert the input string into list of integers
slist = s.split() #turn string into a list
slistint = []
for gen in range(len(slist)):
    slistint.append(int(slist[gen]))
prob = np.array(slistint)  
offspringpergen = np.array([2, 2, 2, 1.5, 1, 0]) # number of dominant offspring expected for each genotype pair
domoffspring = prob*offspringpergen
totaldom = sum(domoffspring)
print(totaldom)
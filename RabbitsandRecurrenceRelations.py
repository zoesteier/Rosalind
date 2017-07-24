# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Rabbits and Recurrence Relations


# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months, 
# if we begin with 1 pair and in each generation, every pair of reproduction-age 
# rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# Sample dataset
sample = '5 3'
sampleoutput = '19'

# uncomment for real dataset
s = input('Enter n and k: ')

# uncomment for testing the sample dataset
#s = sample #s is the DNA string

# convert the input string into integers n and k
slist = s.split() #turn string into a list
n = int(slist[0]) # time in months
k = int(slist[1]) # number of pairs in each litter of rabbits


# Rule: rabbit pairs at time n = rpairs(n-1) + rpairs(n-2)*3
def rabbitpairs(n,k):
    '''# Calculate rabbit pairs at time n months by the rule
    rpairs(n) = rpairs(n-1) + rpairs(n-2)*k.'''
    
    # initial conditions
    if n == 1:
        rpairs = 1
    elif n == 0:
        rpairs = 0
        
    else: # calculate based on the rule
        rpairs = rabbitpairs(n-1,k) + rabbitpairs(n-2,k)*k
    return rpairs

rpairs = rabbitpairs(n,k)

print(rpairs)

# test the sample dataset
#if str(rpairs) == sampleoutput:
#    print('Correct sample output')
#else:
#    print('Incorrect sample output')
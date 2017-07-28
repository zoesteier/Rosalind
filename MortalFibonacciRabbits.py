# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Mortal Fibonacci Rabbits

# Given: Positive integers n≤100 and m≤20.
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

# Sample dataset
sample = '6 3'
sampleoutput = '4'

# uncomment for real dataset
s = input('Enter n and m: ')

# uncomment for testing the sample dataset
#s = sample #s is the DNA string

# convert the input string into integers n and m
slist = s.split() #turn string into a list
n = int(slist[0]) # time in months
m = int(slist[1]) # number of pairs in each litter of rabbits

# use dynamic programmng
# create a memo for dynamic programming
memo = {} # key is (n,m), value is [immature rabbits, mature]

# Rule: rabbit pairs at time n = immature(n-1) + 2*mature(n-1) - immature(n-m)
def mortalpairs(n,m):
    '''# Calculate rabbit pairs at time n months by the rule
    rpairs(n) = = immature(n-1) + 2*mature(n-1) - immature(n-m).'''
    
    args = (n,m) # keys in the memo
    if args in memo:
        rpairs = memo[args]
        #rtot = sum(rpairs) # total number of rabbits is sum of the list
        return(rpairs)
        
    # initial conditions
    if n == 1:
        rpairs = [1, 0]
    elif n == 2:
        rpairs = [0, 1]
    elif n < 1:
        rpairs = [0,0]
        
    else: # calculate based on the rule
        immature = mortalpairs(n-1,m)[1] # new offspring from previous mature
        mature = mortalpairs(n-1,m)[0] + mortalpairs(n-1,m)[1] - mortalpairs(n-m,m)[0]
        # mature = previous immature + previous mature - immature m months ago
        rpairs = [immature, mature]
    memo[args] = rpairs
    return rpairs

rpairs = mortalpairs(n,m)
rtot = sum(rpairs) # total number of rabbits is sum of list

#print(rpairs)
#print(memo)
print(rtot)
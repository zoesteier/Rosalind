# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Counting Point Mutations


# Given: Two DNA strings ss and tt of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t)dH(s,t).

# Sample dataset
# see txt file
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

#sampleoutput
# 7

# uncomment for real dataset
#s = input('Enter n and k: ')

# uncomment for testing the sample dataset
#s = sample #s is the DNA string

# Pseudocode
# Read in two sequences
# For each base, check if different and update hamming distance
# Return hamming distance

# Read txt file into sequences
filename = 'CountingPointMutations.txt'
f = open(filename, 'r')
s = '' # first sequence
t = '' # second sequence
count = 0 # initialize number of sequences seen to 0
for line in f.readlines():
    if count == 0: # first sequence
        s += line.strip()
        if line[-1] == '\n': # end of the first sequence
            count += 1
    else:
        t += line.strip() # second sequence
f.close()

# Calculate the hamming distance between the two sequences
ham = 0
for char in range(len(s)):
    if s[char] == t[char]:
        ham +=0
    else:
        ham += 1  

print(ham)

# test the sample dataset
#if str(rpairs) == sampleoutput:
#    print('Correct sample output')
#else:
#    print('Incorrect sample output')
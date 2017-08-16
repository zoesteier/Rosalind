# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:00:49 2017

@author: zoe.steier
"""

# Rosalind Introduction to Random Strings

#Given: A DNA string ss of length at most 100 bp and an array AA containing at most 20 numbers between 0 and 1.
#Return: An array BB having the same length as AA in which B[k]B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k]A[k] will match ss exactly.

#Sample Dataset
samplestring = 'ACGATACAA'
samplearray = '0.129 0.287 0.423 0.476 0.641 0.742 0.783'
#Sample Output
sampleout = '-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009'


# array A contains GC content
# array B with B[k] = log10(probability) that random string with GC content A[k] will match s exactly

import numpy as np


# Get DNA string and array as inputs

#dataset = 'IntroductiontoRandomStringsSample.txt'
dataset = 'IntroductiontoRandomStrings.txt'
f = open(dataset)
s = f.readline().strip() # DNA string
a = f.readline().strip() # gc content string
f.close()


#s = samplestring
#a = samplearray
strlist = a.split()
A = []
for i in strlist:
    A.append(float(i))

B = [] # initialize B array to hold the output
for gc in A: # loop through each possible gc content contained in A
    # find probabilities of each base
    pg = gc/2
    pc = gc/2
    pa = (1-gc)/2
    pt = (1-gc)/2
    pdict = {'A': pa, 'T': pt, 'G': pg, 'C': pc} # store probability of getting each base
    # calculate probability of generating DNA string s from these probabilities
    P = 0 # initialize log(probabilities)
    for base in s:
        P += np.log10(pdict[base])
    B.append(P)

# format B for printing by converting list to nparray, nparray to string, strip brackets
# alternatively, use str.replace(',', '')
Barray = np.array_str(np.array(B)).strip('[]')    
print(Barray)

# another way to read lines
#f = open(dataset)
#trytoread = f.readlines()
#sread = trytoread[0].strip()
#aread = trytoread[1].strip()
#f.close()
    
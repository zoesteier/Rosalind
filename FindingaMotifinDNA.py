# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Finding a Motif in DNA

# Given: Two DNA strings ss and tt (each of length at most 1 kbp).
# Return: All locations of tt as a substring of s.  (1-based numbering)

# Sample dataset
# GATATATGCATATACTT
# ATAT

#sampleoutput
# 2 4 10

# Get DNA strings from input file
#dataset = 'FindingaMotifinDNASample.txt'
dataset = 'FindingaMotifinDNA.txt'
f = open(dataset)
s = f.readline().strip() # the longer string
t = f.readline().strip() # the shorter string
f.close()

# Make string of indices where t occurs in s
indlist = [] # list to store locations of motif
last = 0 # initialize the location of the previously found index to 0
start = -1 # location to start searching
# if find returns -1, there is no found index
while last >= 0:
    last = s.find(t, start+1)
    start = last
    if last >= 0:
        indlist.append(last)

# add 1 to all indices to match the solution
# convert list to a string output
motif = '' # string to store locations of the motif
for index in indlist:
    index += 1 # add 1 to each index
    if motif != '':
        motif += ' '
    motif += str(index)
        
# Return string of indices
print(motif)

## test if gives correct sample output
#if motif == '2 4 10':
#    print('correct')
#else:
#    print('incorrect')
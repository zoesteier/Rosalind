# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:52:28 2017

@author: zoe.steier
"""

# Rosalind Finding a Shared Motif

#Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#Return: A longest common substring of the collection.

#Sample Dataset
#>Rosalind_1
#GATTACA
#>Rosalind_2
#TAGACCA
#>Rosalind_3
#ATACA

#Sample Output
#AC

import numpy as np

def readfasta(filename):
    '''Read sequences from a fasta file. Output list of sequence strings and list of corresponding IDs.'''
    sequences = []
    IDs = []
    fastafile = open(filename, 'r')
    seq = ''
    for line in fastafile.readlines():
        if line[0] == '>': # start of a new fasta sequence
            if seq != '':
                sequences.append(seq) # add the previous sequence to the sequence list
            ID = line[1:-1] # remove > and /n at beginning and end of line
            seq = ''
            IDs.append(ID) # add ID to list
        else:
            seq += line.strip() # remove end of line characters 
    sequences.append(seq) # add the final sequence to the sequence list
    fastafile.close()
    return(sequences, IDs)
    
sample = 'FindingaSharedMotifSample.fa'
#s = sample
s = 'FindingaSharedMotif.fa'

# read sequences from fasta
seqs, IDs = readfasta(s)

# find the shortest seq, because lcs must be contained in the shortest seq
lengths = np.zeros(len(seqs))
for i in range(len(seqs)):
    lengths[i] = len(seqs[i])
minind = np.argmin(lengths)
minseq = seqs[minind]

# find every possible substring of seq (long to short), store in memo
memo = [] # list of substrings tested
lcs = ''
for i in range(len(minseq)):
    for j in range(len(minseq)):
        substring = minseq[i:(len(minseq)-j)]
        if len(substring) <= len(lcs):
            break
        if substring in memo:
            break
        else:
            memo.append(substring)
        # search for substring in rest of sequences
        islcs = True
        #print(substring)
        for seq in seqs:
            if substring not in seq:
                islcs = False
                #print('break')
                break
        if islcs == True: # if minseq is a substring of all seqs
            lcs = substring
            print('lcs: ' + lcs)
print(lcs)
                
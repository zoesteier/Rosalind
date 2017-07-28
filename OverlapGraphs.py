# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Overlap Graphs

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3O3. You may return edges in any order.

# Sample dataset
#>Rosalind_0498
#AAATAAA
#>Rosalind_2391
#AAATTTT
#>Rosalind_2323
#TTTTCCC
#>Rosalind_0442
#AAATCCC
#>Rosalind_5013
#GGGTGGG

# Sample output
#Rosalind_0498 Rosalind_2391
#Rosalind_0498 Rosalind_0442
#Rosalind_2391 Rosalind_2323

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

# read in data
#fasta = 'OverlapGraphsSample.fa'
fasta = 'OverlapGraphs.fa'
seqs, ids = readfasta(fasta)

# Create adjacency list for overlap of 3
overlap = 3
adj = []
# loop through all sequences (O(n^2))
for i in range(len(seqs)):
    for j in range(len(seqs)):
        if i != j: # don't look for looping edges 
            if seqs[i][-3:] == seqs[j][0:3]:
                edge = ids[i] + ' ' + ids[j]
                print(edge)
                adj.append(edge)

                
            


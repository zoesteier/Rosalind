# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Consensus and Profile

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. 
# (If several possible consensus strings exist, then you may return any one of them.)

# Sample dataset
#>Rosalind_1
#ATCCAGCT
#>Rosalind_2
#GGGCAACT
#>Rosalind_3
#ATGGATCT
#>Rosalind_4
#AAGCAACC
#>Rosalind_5
#TTGGAACT
#>Rosalind_6
#ATGCCATT
#>Rosalind_7
#ATGGCACT

#sampleoutput
#ATGCAACT
#A: 5 1 0 0 5 5 0 0
#C: 0 0 1 4 2 0 6 1
#G: 1 1 6 3 0 1 0 0
#T: 1 5 0 0 0 1 1 6


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

# generate the profile
def makeprofile(sequences):
    '''Make a profile (nparray) from a list of DNA strings.'''
    profile = np.zeros((4, len(sequences[0])))   
    for seqnum in range(len(sequences)):
        for basenum in range(len(sequences[0])):
            if sequences[seqnum][basenum] == 'A':
                profile[0, basenum] += 1
            elif sequences[seqnum][basenum] == 'C':
                profile[1, basenum] += 1
            elif sequences[seqnum][basenum] == 'G':
                profile[2, basenum] += 1
            elif sequences[seqnum][basenum] == 'T':
                profile[3, basenum] += 1
    intp = profile.astype(int) # convert from floats to ints
    return(intp)
    
# convert the profile into a readable format
def printprofile(profile):
    'Input a DNA profile (nparray) and output the properly printed matrix.'''
    # initiate strings for all four bases
    bases = ['A: ', 'C: ', 'G: ', 'T: ']  
    for prof in range(len(bases)):
        for e in profile[prof]:
            if len(bases[prof]) != 3:
                bases[prof] += ' '
            bases[prof] += str(e)
        print(bases[prof])
    return(bases)

def makeconsensus(profile):
    '''Input a DNA profile (nparray) and output a consensus sequence string.'''
    consensus = ''
    maxbase = np.argmax(profile, axis = 0) # find index of max val of each column
    basedict = {0:'A', 1:'C', 2:'G', 3:'T'}
    for base in maxbase:
        consensus += basedict[base]                
    return(consensus)
    
# Get DNA strings from input file
#fasta = 'ConsensusandProfileSample.fa'
fasta = 'ConsensusandProfile.fa'
    
# read the fasta file
sequences, IDs = readfasta(fasta)
# generate the profile
profile = makeprofile(sequences)
## generate consensus from the profile
consensus = makeconsensus(profile)
## print the consensus
print(consensus)
## print the profile
stringprofile = printprofile(profile)
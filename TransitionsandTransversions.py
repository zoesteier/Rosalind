# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:41:02 2017

@author: Zoë
"""

# Rosalind Transitions and Transversions

#Given: Two DNA strings s1s1 and s2s2 of equal length (at most 1 kbp).
#Return: The transition/transversion ratio R(s1,s2)R(s1,s2).
#
#Sample Dataset
#>Rosalind_0209
#GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
#AGTACGGGCATCAACCCAGTT
#>Rosalind_2200
#TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
#GGTACGAGTGTTCCTTTGGGT
#Sample Output
sampleout = 1.21428571429

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
    
sample = 'TransitionsandTransversionsSample.fa'
s = sample
s = 'TransitionsandTransversions.fa'

# read sequences from fasta
seqs, IDs = readfasta(s)
seq1 = seqs[0]
seq2 = seqs[1]

# Calculate transitions and transversions
# use dicts to represent ts and tv
tsdict = {'A':'G', 'G':'A','C':'T','T':'C'}
ts = 0 # transitions
tv = 0 # transversions
for char in range(len(seq1)):
    if seq1[char] != seq2[char]: # if there is a mismatch
        if seq2[char] == tsdict[seq1[char]]: # it's a transition
            ts += 1
        else:
            tv += 1
        
R = ts/tv # trasition/transversion ratio
print(R) 

#if abs(R-sampleout) < 0.0001:
#    print('Sample is correct')
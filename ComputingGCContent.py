# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Computing GC Content


# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the 
# GC-content of that string. Rosalind allows for a default error of 0.001 in all 
# decimal answers unless otherwise stated; please see the note on absolute error 
# below.

# Sample dataset
# see fasta file

#sample = '>Rosalind_6404
#CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
#TCCCACTAATAATTCTGAGG
#>Rosalind_5959
#CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
#ATATCCATTTGTCAGCAGACACGC
#>Rosalind_0808
#CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
#TGGGAACCTGCGGGCAGTAGGTGGAAT'

#sampleoutput = 'Rosalind_0808
#60.919540'

# uncomment for real dataset
#s = input('Enter n and k: ')

# uncomment for testing the sample dataset
#s = sample #s is the DNA string

# Pseudocode
# Read fasta file into sequences
# Compute GC content of each string
# Find string with highest GC content
# Return string ID and GC content

# Store sequence ID and GC content in a dictionary
GCdict = {}

# Read fasta file into sequences
filename = 'ComputingGCContent.fa'
fastafile = open(filename, 'r')
for line in fastafile.readlines():
    if line[0] == '>': # start of a new fasta sequence
        ID = line[1:-1] # remove > and /n at beginning and end of line
        seq = ''
    else:
        seq += line.strip() # remove end of line characters    
    
        # calculate gc content of the sequence (gets replaced if )
        gccontent = (seq.count('G') + seq.count('C'))/len(seq)*100
        GCdict[ID] = gccontent       
fastafile.close()  

# Find string with highest GC content
maxGCcontent = max(GCdict.values())
for key in GCdict.keys():
    if abs(GCdict[key] - maxGCcontent) < 0.001:
        maxID = key
print(GCdict)

print(maxID)
print(maxGCcontent)

# test the sample dataset
#if str(rpairs) == sampleoutput:
#    print('Correct sample output')
#else:
#    print('Incorrect sample output')
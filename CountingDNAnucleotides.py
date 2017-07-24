# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Counting DNA nucleotides


# Given: A DNA string ss of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.

# Sample dataset
sample = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
sampleoutput = '20 12 17 21'

seq = input('Enter a DNA sequence: ')

#seq = sample
# for testing the sample dataset, uncomment

acount = seq.count('A')
ccount = seq.count('C')
gcount = seq.count('G')
tcount = seq.count('T')

print(acount, ccount, gcount, tcount)

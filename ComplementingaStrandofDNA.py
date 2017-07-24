# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Complementing a Strand of DNA


# Given: A DNA string ss of length at most 1000 bp.
#Return: The reverse complement scsc of ss

# Sample dataset
sample = 'AAAACCCGGT'
sampleoutput = 'ACCGGGTTTT'

# uncomment for real dataset
s = input('Enter a DNA sequence: ')

# uncomment for testing the sample dataset
#s = sample #s is the DNA string

# find the reverse complement (sc) of s
reverseds = s[::-1] # reverses the original string
complementdict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'} # dictionary of complement base pairs
sc = '' # initialize reverse complement string
for letter in reverseds:
    sc += complementdict[letter]

print(sc)

# test the sample dataset
#if sc == sampleoutput:
#    print('Correct sample output')
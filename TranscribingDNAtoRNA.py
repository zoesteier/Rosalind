# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind transcribing DNA into RNA


# Given: A DNA string tt having length at most 1000 nt.
# Return: The transcribed RNA string of tt.

# Sample dataset
sample = 'GATGGAACTTGACTACGTAAATT'
sampleoutput = 'GAUGGAACUUGACUACGUAAAUU'

# uncomment for real dataset
t = input('Enter a DNA sequence: ')

# comment for testing
#t = sample #t is the DNA string
# for testing the sample dataset, uncomment

# replace all occurrences of 'T' in the DNA string with 'U' in the RNA string
u = t.replace('T', 'U')

print(u)

# test the sample dataset
#if u == sampleoutput:
#    print('Correct sample output')
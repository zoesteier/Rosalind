# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 14:52:25 2017

@author: zoe.steier
"""

# Rosalind Calculating Protein Mass

#Given: A protein string PP of length at most 1000 aa.
#Return: The total weight of PP. Consult the monoisotopic mass table.

#Sample Dataset
sample = 'SKADYEK'
#Sample Output
#821.392

s = sample
s = input('Enter the protein string: ')

# Create a dictionary of monoisotopic masses
masses = 'MonoisotopicMass.txt' # contains monoisotopic mass for each AA and Water
f = open(masses, 'r')
AAlist = (f.read().split()) # makes a list of AA, mass
massdict = {} # key is codon, value is AA
count = 1 # count odd (mass) or even (AA)
for elem in range(len(AAlist)):
    if elem % 2 == 1: # if odd, it's mass, AA is previous
        massdict[AAlist[elem-1]] = float(AAlist[elem])
f.close()

# Calculate mass of protein = sum(AA) + Water (ignore the water)
totalmass = 0
for AA in s:
    totalmass += massdict[AA]
print(totalmass)
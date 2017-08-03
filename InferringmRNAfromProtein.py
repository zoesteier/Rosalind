# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:20:47 2017

@author: Zoë
"""

# Rosalind Interring mRNA from Protein

#Given: A protein string of length at most 1000 aa.
#Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
#
#Sample Dataset
sample = 'MA'
#Sample Output
sampleout = 12

#%% Make a dictionary to store the genetic code
RNAproteincode = 'GeneticCode.txt' # contains codons and corresponding AA
f = open(RNAproteincode, 'r')
AAlist = (f.read().split()) # makes a list of codon, AA
codedict = {} # key is codon, value is AA
reversedict = {} # key is AA, value is list of codons
count = 1 # count odd (codon) or even (AA)
for elem in range(len(AAlist)):
    if elem % 2 == 1: # if odd, it's an AA, codon is previous
        codedict[AAlist[elem-1]] = AAlist[elem]
        if AAlist[elem] in reversedict.keys():
            reversedict[AAlist[elem]].append(AAlist[elem-1])
        else:
            reversedict[AAlist[elem]] = [AAlist[elem-1]]
f.close()

#%%
# Get protein string from input
p = input('Enter protein sequence: ')

# Calculate number of codons for each AA and stop from the reversedict
# make a new dict to store key AA and value number of codons
codonoptions = {}
for key in reversedict.keys():
    codonoptions[key] = len(reversedict[key])
    
# The number of options for RNA strings from a protein is the product of the codon options and stop options. This is a large number, so use the modulo 10^6.
# naive
total = 1
runningmod = codonoptions['Stop']
for amino in p:
    total *= codonoptions[amino]
    runningmod *= codonoptions[amino]
    if runningmod > 1000000:
        runningmod = runningmod % 1000000
total *= codonoptions['Stop']
print('runningmod')
print(runningmod)
modtotal = total % 1000000 # mod 10^6
print('total mod')
print(modtotal)
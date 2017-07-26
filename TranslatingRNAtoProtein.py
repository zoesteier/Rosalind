# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:28:01 2017

@author: zoe.steier
"""

# Rosalind Translating RNA into Protein


# Given: Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

# Return: The protein string encoded by s.

# Sample dataset
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

#sampleoutput
# MAMAPRTEINSTRING

# Get RNA string from input file
#RNA = 'TranslatingRNAtoProteinSample.txt'
RNA = 'TranslatingRNAtoProtein.txt'
f = open(RNA, 'r')
s = f.read()
f.close()

# Make a dictionary to store the genetic code
RNAproteincode = 'GeneticCode.txt' # contains codons and corresponding AA
f = open(RNAproteincode, 'r')
AAlist = (f.read().split()) # makes a list of codon, AA
codedict = {} # key is codon, value is AA
count = 1 # count odd (codon) or even (AA)
for elem in range(len(AAlist)):
    if elem % 2 == 1: # if odd, it's an AA, codon is previous
        codedict[AAlist[elem-1]] = AAlist[elem]
f.close()

# Translate RNA to protein
def translateRNAprotein(RNAseq):
    '''Input RNA sequence as a string. Output protein AA sequence as string.'''
    p = ''
    # Read 3 bases at a time. Look up AA in dictionary.
    for codonnum in range(0, len(RNAseq), 3):
        codon = RNAseq[codonnum:(codonnum + 3)]
        AA = codedict[codon]
        if AA == 'Stop':
            return(p)
        p += AA
    return(p)
    
# Return protein string p
p = translateRNAprotein(s)
print(p)
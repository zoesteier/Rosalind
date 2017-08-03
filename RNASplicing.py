# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:04:42 2017

@author: zoe.steier
"""

#Rosalind RNA Splicing

#Given: A DNA string ss (of length at most 1 kbp) and a collection of substrings 
# of ss acting as introns. All strings are given in FASTA format.
#Return: A protein string resulting from transcribing and translating the exons of s.

# Sample dataset
#>Rosalind_10
#ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
#>Rosalind_12
#ATCGGTCGAA
#>Rosalind_15
#ATCGGTCGAGCGTGT

#Sample Output
sampleout = 'MVYIADKQHVASREAYGHMFKVCA'

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
    
sample = 'RNASplicingSample.fa'
s = sample
s = 'RNASplicing.fa'
s = 'RNASplicing3.fa'

# read sequences from fasta
seqs, IDs = readfasta(s)

fullseq = seqs[0] # the rest are introns

# find locations of introns within the full sequence and splice out introns
# must find intron locations and splice in two separate steps because introns aren't listed sequentially
intronlocs = [] # list to store locations of the introns
for intron in range(1, len(seqs)):
    index = fullseq.index(seqs[intron]) # location of intron within full sequence
    intronlocs.append(index)
    
# splice out introns: this did not work correctly
#intronlocs.sort() # sort the introns in order
#splicedseq = ''
#exonstart = 0
#for intron in range(len(intronlocs)):
#    index = intronlocs[intron] # location of the start of an intron
#    splicedseq += fullseq[exonstart:index] # add the previous exon to the spliced sequence
#    exonstart = index + len(seqs[intron + 1]) # next exon starts at end of intron
#    #print(exonstart)
#splicedseq += fullseq[exonstart:] # add the final exon
#print(len(fullseq))
#print(intronlocs)
#print(splicedseq)
#print(len(splicedseq))

# translate spliced sequence into protein (use TranslatingRNAtoProtein)
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
#        print(codon)
#        print(AA)
        if AA == 'Stop':
            #print('got stop')
            return(p)
        p += AA
    return(p)    


# transcribe DNA to RNA
#rna = splicedseq.replace('T', 'U')
# find the protein sequence
#p = translateRNAprotein(rna)
#print(p)

## try importing function from file
#import TranslatingRNAtoProtein as translate
#pimporttest = translate.translateRNAprotein(rna)
#print('this is the test')
#print(pimporttest)

## try another method to remove introns
intronlist = seqs[1:]
splc = fullseq[:]
for intron in intronlist:
    splc = splc.replace(intron, '')
splcrna = splc.replace('T', 'U')
protein = translateRNAprotein(splcrna)
print(protein)

# debug code
#final = 0
#for i in range(len(seqs)):
#    #print(len(seqs[i]))
#    if i == 0:
#        final += len(seqs[i])
#    else:
#        final -= len(seqs[i])
#print('correct protein length')
#print(final/3)

#if p == sampleout:
#    print('Sample is correct')
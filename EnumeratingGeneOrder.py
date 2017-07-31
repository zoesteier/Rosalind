# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:31:27 2017

@author: zoe.steier
"""

# Rosalind Enumerating Gene Orders

#Given: A positive integer n≤7n≤7.
#Return: The total number of permutations of length nn, followed by a list of all such permutations (in any order).

#Sample Dataset
#3

#Sample Output
#6
#1 2 3
#1 3 2
#2 1 3
#2 3 1
#3 1 2
#3 2 1

import numpy as np
import itertools

# Find the number of permutations
n = int(input('Enter n: '))
permutations = np.math.factorial(n)
print(permutations)

xlist = np.array(range(n)) + 1
permlist = list(itertools.permutations(xlist))

# print the list of permutations
for i in permlist:
#    perm = str(i).strip('(),')
#    print(perm)
    permstr = str(i[0])
    for item in range(1,len(i)):
        permstr += ' '
        permstr += str(i[item])
    print(permstr)

# This program generates a random poem from Raymond Queneau's 10 poems in Cent Mille Milliards de Poemes.
# Each line of the new generated poem comes from a randomly chosen one of the 10 poems.

##############

#!/usr/bin/env python

##############

import codecs
import random
import math
import sys

############## initialization
nPoems = 3
nLinesPerPoem = 2

newAllThePoemsInAnArray = []

############## prepare text file

# open file and remove BOM characters
with codecs.open("queneauToy.txt", "r", "utf-8-sig") as allThePoems:
    allThePoemsInAnArray = map(str, allThePoems.readlines())

allThePoems.close()

# stack poem lines in a single array and remove blank lines
for line in allThePoemsInAnArray:
    if line.split('\n')[0] != '':
        newAllThePoemsInAnArray.append(line.split('\n')[0])


################ generate poem(s)

randomPoem = []
nLinesDoneCumul = 0

# loop over lines
for iLine in range(1,nLinesPerPoem+1):
    poemNumber = int(math.ceil(nPoems*random.random()))
    idxOfLine  = nLinesPerPoem*(poemNumber-1) + nLinesDoneCumul   
    line = newAllThePoemsInAnArray[idxOfLine]
    line = line.strip()
    nLinesDoneCumul = nLinesDoneCumul + 1
    print line




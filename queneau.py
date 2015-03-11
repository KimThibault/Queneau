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
    allThePoemsInAnArray = allThePoems.readlines()


# stack poem lines in a single array and remove blank lines
newAllThePoemsInAnArray = [line.strip() for line in allThePoemsInAnArray if line.strip()!='']


################ generate poem(s)

randomPoem = []

# loop over lines
for nLinesDoneCumul in range(nLinesPerPoem):
    poemNumber = int(math.ceil(nPoems*random.random()))
    idxOfLine  = nLinesPerPoem*(poemNumber-1) + nLinesDoneCumul   
    line = newAllThePoemsInAnArray[idxOfLine]
    line = line.strip()
    print line


#!/usr/bin/env python
import collections
import sys
import numpy as np
#from collections import namedtuple

pedInFile = sys.argv[1]
#TriPosOutFile = sys.argv[2]

#d = collections.defaultdict(dict)
with open(pedInFile) as file:
    for line in file:
        bigList = []
        indList = []
        pos = line.split("\t")[0]
        indList = line.split("\t")[3:]
        for ind in range(len(indList)):
            alleles = indList[ind].split()
            for a in alleles:
                bigList.append(a)
        s = set(bigList)
        if len(s) > 2:
            #print(s)
            print(pos)

#with open(outfilename, 'w') as out_file:

    #for smallList in bigList:
        #for pos in d[chrom]:
#        setd = set(smallList[4]) # This corresponds to the string snp eg. "AAGTANT"
#        setd.discard('N') # Where the magic happens
#        AlleleLength = len(setd)
#            #For position more than bi-allele
#        if (AlleleLength <= 2 and 'NN' not in smallList[4]):
#            out_file.write(smallList[0] + '\t' + smallList[1] + '\t' + smallList[2] + '\t' + smallList[3] + '\t' + smallList[4] + '\t' + smallList[5] + '\t' + smallList[6] + '\n')
#            print (smallList[0], "and pos ", smallList[1], 'corresponds to', AlleleLength)

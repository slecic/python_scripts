#!/usr/bin/env python                                                                                                                               
import os

for file in os.listdir("/dss/dsslegfs01/pr53da/pr53da-dss-0024/rawdata/Bisulfite-Seq/PublicRRBS/Parus_major"):
        if ".fastq.gz" in file:
            filename = file
            filename = filename.strip()
            firstpart, secondpart = filename.strip().split(".", 1)
            print(firstpart)
            with open("/dss/dsslegfs01/pr53da/pr53da-dss-0024/projects/2022_EpiMachineLearning/Bisulfate_Conversion/Genomes/Parus.major.v1.1/run_sa\
mple_names_space.txt") as fd:
                 for line in fd:
                     line = line.strip()
                     old, new = line.strip().split(" ", 1)
                     if old in firstpart: # if the file from the dicetory corresponds to the file from the list rename it    

                        os.rename(old.strip() + ".fastq.gz", new.strip() + ".fastq.gz")


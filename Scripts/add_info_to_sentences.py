#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Add info to the small file containing all the sentences for the perception experiment

import sys, re, os
import csv

#Open both tables
bigtable = open("/home/lucas/Documents/CloudStation/SDL/PhD/Corpora/Files_treated-for-prosody/Files_WHISF_prosody/tableau_quantitatif_SynCart_interpolated.csv")
smalltable = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/Files_to_consider.csv")

#Open output file
csvoutput = ("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/table_files_expe-perception.csv")
csvfile = open(csvoutput, 'w')

#parse csvs
readerbigtable = csv.DictReader(bigtable, skipinitialspace=True, delimiter="\t")
readersmalltable = csv.DictReader(smalltable, skipinitialspace=True, delimiter="\t")

#Get header
header = readerbigtable.fieldnames

# ~ print(header)

list_sentences_perceptionXP = []

for row in readersmalltable:
	xmlfile = row['filename']
	list_sentences_perceptionXP.append(xmlfile)

#Write header in output
writer = csv.DictWriter(csvfile, fieldnames=header, delimiter="\t")
writer.writeheader()

#Loop on big and small table, then write rows to the output
for row in readerbigtable:
	xmlfile = row['sentence_key']
	for sentence in list_sentences_perceptionXP:
		if sentence == xmlfile:
			writer.writerow(row)
			pass
			# ~ print(row)
		else:
			pass


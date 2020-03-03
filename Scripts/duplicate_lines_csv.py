#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Add info to the small file containing all the sentences for the perception experiment

import sys, re, os
import csv

#Open table
tablein = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Expe_perception_verif_methodo_2.csv")

#Open output file
csvoutput = ("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/TOCHECK.csv")
csvfile = open(csvoutput, 'w')


#parse csvs
readertablein = csv.DictReader(tablein, skipinitialspace=True, delimiter="\t")

#Get header
header = readertablein.fieldnames
header.append('audio-type')
# ~ print(header)

#Write header in output
writer = csv.DictWriter(csvfile, fieldnames=header, delimiter="\t")
writer.writeheader()


for row in readertablein:
	if row["OK_Expe_perception"] == "YES":
		# ~ print(row)
		row1 = row
		row2 = row
		row3 = row
		# ~ row1['audio-type'] = "orig"
		# ~ row2['audio-type'] = "clair"
		# ~ print(row1)
		# ~ row3['audio-type'] = "delex"
		writer.writerow(row1)
		writer.writerow(row2)
		writer.writerow(row3)

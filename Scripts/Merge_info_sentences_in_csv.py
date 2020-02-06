#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Check whether the sentences gathered are the last turn of the speaker

import sys, re, os, csv
from lxml import etree as ET

#Open Table wavtoconsider
tablewavtoconsider = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/wavtoconsidervraiexpe.csv", "r")

#Open table quantitatif
tablequantitatif = open("/home/lucas/Documents/CloudStation/SDL/PhD/Corpora/tableau_quantitatif.csv", "r")

#Open table spk
tablespk = open("/home/lucas/Documents/CloudStation/SDL/PhD/Corpora/BRAT/Table_BRAT_FINAL.csv", "r")

#Open tablewhatIwant
tablewhatiwant = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/table_files_expe-perception.csv", "r")

#Open headerwiw txt file, containing all variables I want in the final file:
fwiw = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/headerwiw.txt", "r")
wiw = fwiw.read()

#Open outputfile
foutput = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/table_TODEL.csv", "w")

#Csv readers
readerwav = csv.DictReader(tablewavtoconsider, skipinitialspace=True, delimiter="\t")
readerquant = csv.DictReader(tablequantitatif, skipinitialspace=True, delimiter="\t")
readerspk = csv.DictReader(tablespk, skipinitialspace=True, delimiter="\t")
readerwhatIwant = csv.DictReader(tablewhatiwant, skipinitialspace=True, delimiter="\t")

#Get headers
headerwav = readerwav.fieldnames
headerquant = readerquant.fieldnames
headerspk = readerspk.fieldnames
headerwiw = readerwhatIwant.fieldnames

list_sent_OK = []

for row in readerwav:
	sentkey = row["file"]
	list_sent_OK.append(sentkey)
	# ~ writer.writer(row)

#Dictreader for the output file
writer = csv.DictWriter(foutput, fieldnames=headerspk, delimiter="\t")
writer.writeheader()

for row in readerspk:
	if row["sentence_key"] in list_sent_OK:
		# ~ list_spk.append(row["sentence_key"])
		# ~ print(row)
		writer.writerow(row)

		




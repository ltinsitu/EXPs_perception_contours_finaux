#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, shutil, csv
#shutil to copy files

#Defining folders
folderin = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/REAL_EXPE_Ibex/ForMBROLA/"
folderout = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/REAL_EXPE_Ibex/Audio_TG_MBROLA_delexicalised/"

#Reading csv file
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/table_files_REAL-expe-perception.csv", "r")
readertable = csv.DictReader(table, skipinitialspace=True, delimiter="\t")

list_TGs = []

for row in readertable:
	if row["OK_Expe_perception"] == "YES":
		list_TGs.append(row["sentence_key"]+"_delexicalised.TextGrid")

for tg in list_TGs:
	filepath = folderin+tg
	
	shutil.copy2(filepath, folderout)
	print("Moving:", filepath)

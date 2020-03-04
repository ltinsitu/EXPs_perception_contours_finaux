#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, shutil, csv
from os import walk

path = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Fillers/AllFillers/AllFillers_cut/"


#Reading csv file
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Expe_perception_verif_methodo_2_fillers.csv", "r")
readertable = csv.DictReader(table, skipinitialspace=True, delimiter="\t")

list_OKEXPE = []

for row in readertable:
	textexpe = row["texte_expe"]
	textexpe = textexpe.lower()
	# ~ if re.search(r"(.*)(.(\?|!))", textexpe):
		# ~ print(textexpe)
	textexpe = re.sub(r"(.*)(.(\?|!))", "\g<1>", textexpe)
	# ~ textexpe = textexpe.replace("!", "")
	# ~ textexpe = textexpe.replace("?", "")
	textexpe = textexpe.replace(" ", "_")
	textexpe = textexpe.replace("’", "_")
	# ~ print(textexpe)

	list_OKEXPE.append(textexpe)
	

fpath = os.listdir(path)

for files in fpath:
	# ~ if fileinfolder in list_OKEXPE:
	if files.endswith(".TextGrid"):
		filename = files.split(".")
		list_FILES.append(filename[0])
		if not filename[0] in list_OKEXPE:
			print(filename[0])
			# ~ pass

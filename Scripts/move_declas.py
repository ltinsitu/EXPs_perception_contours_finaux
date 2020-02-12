#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, shutil, csv
from os import walk

#Pathin
pathin = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_all-sent-types/Files_cut_orig/"

#Pathout
pathout = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Files_cut_orig/"

#Reading csv file
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Expe_perception_verif_methodo_2.csv", "r")
readertable = csv.DictReader(table, skipinitialspace=True, delimiter="\t")

listdecla = []

for stuff in os.walk(pathin):
	for files in stuff:
		for f in files:
			if f.endswith(".wav"):
				listdecla.append(f.replace(".wav", ""))

for row in readertable:
	if row["OK_Expe_perception"] == "YES":
		if row["type-de-phrase"] == "decla":
			if row["sentence_key"] in listdecla:
				filename = row["sentence_key"]+".wav"
				print("COPYING", filename, "in", pathout)
				shutil.copy2(pathin+filename, pathout)

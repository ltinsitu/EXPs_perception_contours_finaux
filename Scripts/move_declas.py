#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, shutil, csv
from os import walk

#Pathin
pathin = "/media/sda4/lucas/Téléchargements/Corpus/Corpus_data/ATRAITER/ESLO/ESLO2-decla-cut/"

#Pathout
pathout = "/home/lucas/Documents/CloudStation/SDL/PhD/Corpora/Audio/ESLO2-decla-cut/"

#Reading csv file
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/table_files_REAL-expe-perception.csv", "r")
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

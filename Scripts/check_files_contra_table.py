#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, shutil, csv
from os import walk

path = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/Audio_TG_MBROLA_delexicalised/"


#Reading csv file
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/table_files_REAL-expe-perception.csv", "r")
readertable = csv.DictReader(table, skipinitialspace=True, delimiter="\t")

list_OKEXPE = []

for row in readertable:
	if row["OK_Expe_perception"] == "YES":
		filename = row["sentence_key"]
		list_OKEXPE.append(filename)

fpath = os.listdir(path)


for files in fpath:
	fileinfolder = files.split("_delexicalised")[0]
	if fileinfolder in list_OKEXPE:
		print(fileinfolder)

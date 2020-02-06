#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, shutil, csv
from os import walk

#Define paths where are the files needed to be removed
path1 = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/Audio_TG/"
path2 = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/Audio_TG_MBROLA_delexicalised/"
path3 = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/ForMBROLA/"

#Define a path where to copy files (to check them before removing)
pathtocopy = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/TOCHECKTHENREMOVEWT075/"

#Reading csv file
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/table_files_REAL-expe-perception.csv", "r")
readertable = csv.DictReader(table, skipinitialspace=True, delimiter="\t")

list_OKEXPE = []

for row in readertable:
	if row["OK_Expe_perception"] == "YES":
		filename = row["sentence_key"]
		list_OKEXPE.append(filename)

fpath1 = os.listdir(path1)
fpath2 = os.listdir(path2)
fpath3 = os.listdir(path3)

for files in fpath1:
	fileinfolder = files.split(".")[0]
	if fileinfolder not in list_OKEXPE:
		print(fileinfolder)

for files in fpath2:
	fileinfolder = files.split("_delexicalised")[0]
	if fileinfolder not in list_OKEXPE:
		print(files)

for files in fpath3:
	if "delexicalised" in files:
		fileinfolder = files.split("_delexicalised")[0]
		# ~ print(fileinfolder)
		if fileinfolder not in list_OKEXPE:
			print(files)
	else:
		fileinfolder = files.split(".")[0]
		# ~ print(fileinfolder)
		if fileinfolder not in list_OKEXPE:
			print(files)
##This does not work, I try with another os method
# ~ for stuff in os.walk(path1):
	# ~ for files in stuff:
		# ~ print(files)
		# ~ for f in files:
			# ~ print(f)
			# ~ filesinfolder = f.split(".")[0]
			# ~ if filesinfolder not in list_OKEXPE:
				# ~ print(filesinfolder)
			# ~ file, extension = os.path.splitext('/path/to/somefile.ext'

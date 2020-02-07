#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Verify that syllable numbers in the csv file correspond to syllable number in each textgrid.

import sys, re, os, csv
import glob
from praatio import tgio

#Folder where TGs are stored
foldertg = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_all-sent-types/Files_cut_orig/"

#Import csv file
csvfile = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_all-sent-types/table_files_REAL-expe-perception.csv", "r")

#Csv reader
reader = csv.DictReader(csvfile, skipinitialspace=True, delimiter="\t")

#Initiating two empty lists. One that will contain strings (sentence_key + syllnum), and one containing only sentence_key.
list_sentkey_syllnum = []
list_sentkey = []

#Start looping on all sentences
for row in reader:
	#We take only sentences OK for the experience
	if row["OK_Expe_perception"] == "YES":
		#We add to the lists needed informations
		list_sentkey.append(row["sentence_key"])
		list_sentkey_syllnum.append(row["sentence_key"]+"#"+str(row["num_syll_OK_Expe_perception"]))


#We initiate a new list containing all TGs name in the foldertg
list_TG = []

for (dirpath, dirnames, filenames) in os.walk(foldertg):
	for f in filenames:
		if f.endswith(".TextGrid"):
			# ~ print(f)
			TGname = f.strip(".TextGrid")
			list_TG.append(TGname)
	
##THIS THING IS JUST TO CHECK SOMETHING###
#Then we can verify if all TGs are in the csv and vice versa
for TG in list_TG:
	if not TG in list_sentkey:
		print("Problem")
	else:
		# ~ print("OK")
		pass
############################################

##THIS IS JUST TO SPLIT SENTKEY AND SYLLNUM, NOT SURE IF NECESSARY AT SOME POINT
# ~ listinfo = []
# ~ for string in list_sentkey_syllnum:
	# ~ listinfo.append(string.split("#"))

# ~ for info in listinfo:
	# ~ print(info)
#####################################################

#We initiate a new list containing all TGs PATH (needed for opening them later)
tgpaths = glob.glob(foldertg+"*.TextGrid")

# ~ counttg = 0

#We start looping on all TGs
for tgfile in tgpaths:
	# ~ counttg +=1
	#We get the name of the TG
	tgname = tgfile.replace(foldertg, "")
	tgname = tgname.strip(".TextGrid")
	#Opening TGs with praat-textgrids
	tg = tgio.openTextgrid(tgfile)
	#Getting the syllable tier
	sylltier = tg.tierDict["syll"]
	
	#Getting the infos for each interval in the syllable tier
	sylls = sylltier.entryList

	#Initiating a counter for number of syllables
	countsyll = 0

	#Excluding pauses if any
	for s in sylls:
		if not re.match("_", s[2]):
			countsyll += 1
	
	#To check if there are pauses in our TGs (since we don't want them)
	if not len(sylls) == countsyll:
		print("In TG file:", tgname, "\n", "There were", len(sylls), "syllables", "but excluding pauses there were", countsyll, "syllables")
	
	#Create strings with TGname and syllnumber
	strTGsyllnum = tgname+"#"+str(countsyll)
	##The next two lines I print everything, then making modifications in the table will be easier
	# ~ strings_list = strTGsyllnum.split("#")
	# ~ print(strings_list[0], "\t", strings_list[1])
	##If I want to print only the unmatching TGs:
	if strTGsyllnum in list_sentkey_syllnum:
		print("OK")
		# ~ pass
	else:
		# ~ strings_list = strTGsyllnum.split("#")
		# ~ print(strings_list[0], "\t", strings_list[1])
		pass

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Tout est dans le titre

import sys, re, os, csv

#Defining folders
folder = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/ForMBROLA_pitchorig/"
folderout = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/Audio_REAL_expe_Pitch_orig/"


#Reading csv file
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/table_files_REAL-expe-perception.csv", "r")
reader = csv.DictReader(table, skipinitialspace=True, delimiter="\t")

#Get header
header = reader.fieldnames
# ~ print(header)

#Defining the first part of the command
commandstart = "/usr/bin/mbrola /home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/ForMBROLA/Database_voices/"

#Start the loop
for row in reader:
	# ~ print(row)
	if row["OK_Expe_perception"] == "YES":
		# ~ if row["OK_praat_seg"] == "NO":
		sentkey = row["sentence_key"]
		filepho = sentkey + "_delexicalised.pho"
		fileoutput = sentkey + "_delexicalised.wav"
		pathoutput = folderout+fileoutput
		# ~ print(pathoutput)
		if row["spk_sex"] == "M":
			commandsex = "fr3/fr3"
		elif row["spk_sex"] == "F":
			commandsex = "fr2/fr2"
		command = commandstart + commandsex + " " + folder + filepho + " " + pathoutput
		print(sentkey, row["spk_sex"])
		print(command)
		os.system(command)

# ~ filepho = "001-de-0-WE2_A001_1952s875_delexicalised.pho"
# ~ fileoutput = "outputtest.wav"

# ~ command = "/usr/local/bin/mbrola /home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/ForMBROLA/Files_SAMPA_original/fr1/fr1 " + folder + filepho + " " + folder + fileoutput

# ~ os.system(command)

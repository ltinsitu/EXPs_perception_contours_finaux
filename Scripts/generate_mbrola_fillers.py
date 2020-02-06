#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Tout est dans le titre

import sys, re, os, csv
from os import walk

#Defining folders
folder = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/Fillers/Laure/Oldnames_segmented_cut/"
folderout = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/Fillers/Laure/Fillers_Laure_delexicalised/"

#Defining the first part of the command
commandstart = "/usr/bin/mbrola /home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/ForMBROLA/Database_voices/fr4/fr4"

for (dirpath, dirnames, filenames) in walk(folder):
	for file in filenames:
		if file.endswith(".pho"):
			filepho = dirpath+file
			# ~ print(filepho)
			fileoutput = file.strip(".pho") + ".wav"
			# ~ print(fileoutput)
			pathoutput = folderout + fileoutput
			# ~ print(pathoutput)
			command = commandstart + " " + filepho + " " + pathoutput
			print(command)
			os.system(command)
			
			
#Start the loop
# ~ for row in reader:
	# ~ if row["OK_Expe_perception"] == "YES":
		# ~ if row["OK_praat_seg"] == "NO":
			# ~ sentkey = row["sentence_key"]
			# ~ filepho = sentkey + "_delexicalised.pho"
			# ~ fileoutput = sentkey + "_delexicalised.wav"
			# ~ pathoutput = folderout+fileoutput
			# ~ print(pathoutput)
			# ~ if row["spk_sex"] == "M":
				# ~ commandsex = "fr1/fr1"
			# ~ elif row["spk_sex"] == "F":
				# ~ commandsex = "fr4/fr4"
			# ~ command = commandstart + commandsex + " " + folder + filepho + " " + pathoutput
			# ~ print(sentkey, row["spk_sex"])
			# ~ print(command)
			# ~ os.system(command)

# ~ filepho = "001-de-0-WE2_A001_1952s875_delexicalised.pho"
# ~ fileoutput = "outputtest.wav"

# ~ command = "/usr/local/bin/mbrola /home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/ForMBROLA/Files_SAMPA_original/fr1/fr1 " + folder + filepho + " " + folder + fileoutput

# ~ os.system(command)

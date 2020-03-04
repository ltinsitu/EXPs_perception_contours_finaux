#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Tout est dans le titre

import sys, re, os, csv

#Defining folders
folderin = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Fillers/AllFillers/FORMBROLA_clair/"
folderout = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Fillers/Fillers_clair/"


#Reading csv file
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Expe_perception_verif_methodo_2_fillers.csv", "r")
reader = csv.DictReader(table, skipinitialspace=True, delimiter="\t")

#Get header
header = reader.fieldnames
# ~ print(header)

#Defining the first part of the command
commandstart = "/usr/bin/mbrola /home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/MBROLA_synthesis_program/Database_voices/"

#Start the loop
for row in reader:
	textexpe = row["texte_expe"]
	textexpe = textexpe.lower()
	textexpe = re.sub(r"(.*)(.(\?|!))", "\g<1>", textexpe)
	textexpe = textexpe.replace(" ", "_")
	textexpe = textexpe.replace("’", "_")
	print(textexpe)
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
	# ~ command = commandstart + commandsex + " " + folderin + filepho + " " + pathoutput
	# ~ print(sentkey, row["spk_sex"])
	# ~ print(command)
	# ~ os.system(command)

# ~ command = "/usr/local/bin/mbrola /home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/ForMBROLA/Files_SAMPA_original/fr1/fr1 " + folder + filepho + " " + folder + fileoutput


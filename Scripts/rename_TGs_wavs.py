#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Rename files according to newkey

import sys, re, os, shutil, csv
#shutil to copy files

#Define folders
folderin = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Audio_Expe_verif_methodo2/"
folderinfillers = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Audio_files/FILLERSTOCHANGEAUDIO/FIllerschanged/"
folderout_mbrola = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Audio_files/XP_mbrola/"
folderout_delex = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Audio_files/XP_delex/"
# ~ folderoutfiller = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Audio_files/FILLERSTOCHANGEAUDIO/"

#csv table
csvfile = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Expe_perception_verif_methodo_3_BOTH.csv", "r")

#Csv reader
reader = csv.DictReader(csvfile, skipinitialspace=True, delimiter="\t")

#Start looping on all sentences
for row in reader:
	#Take into account only 40 sentences for expe
	# ~ if row["OK_Expe_perception"] == "YES":
	#We get the old and new key
	oldkey = row["OLD_sentence_key"]
	newkey = row["sentence_key"]
	# ~ print(oldkey, newkey)
	# ~ print(newkey)
	#Filepath is the whole path, oldfilename only the name of the file, newfilename how to rename it
	filepath = folderin+oldkey+".mp3"
	oldfilename = oldkey+".mp3"
	newfilename = newkey+".mp3"
	if row["TOCHANGE_FI"] == "YES":
		filepath = folderinfillers+newkey+".mp3"
		if row["XP_type"] == "XP_delex":
			# ~ print(filepath, folderout_delex)
			shutil.copy2(filepath, folderout_delex)
		if row["XP_type"] == "XP_mbrola":
			# ~ print(filepath, folderout_mbrola)
			shutil.copy2(filepath, folderout_mbrola)
	else:
		if row["XP_type"] == "XP_delex":
			# ~ print(newkey, oldkey)
			# ~ print("Moving wav:", filepath)
			shutil.copy2(filepath, folderout_delex)
			new_dst_wav = os.path.join(folderout_delex, newfilename)
			os.rename(folderout_delex+oldfilename, new_dst_wav)
			pass
		elif row["XP_type"] == "XP_mbrola":
			# ~ print(newkey, oldkey)
			# ~ print("Moving wav:", filepath)
			shutil.copy2(filepath, folderout_mbrola)
			new_dst_wav = os.path.join(folderout_mbrola, newfilename)
			os.rename(folderout_mbrola+oldfilename, new_dst_wav)
			pass
		else:
			print("problem")



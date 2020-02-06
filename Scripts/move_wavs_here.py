#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Generate newkeys for ibex expe and renaming wav files in a new folder

import sys, re, os, shutil, csv
from os import walk
#shutil to copy files

#Defining folders
folderin_original = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/"
folderout_original = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/new_ori/"

folderin_delex = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/"
folderout_delex = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/new_delex/"

folderin_mbrolaclair = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/"
folderout_mbrolaclair = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/new_clair/"


#Reading csv file
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/table_files_expe-perception.csv", "r")
readertable = csv.DictReader(table, skipinitialspace=True, delimiter="\t")

##Defining which files are in which folders
#Original audio
files_orig = []

for (dirpath, dirnames, filenames) in walk(folderin_original):
	files_orig.extend(filenames)
	break

#MBROLA clair audio
files_clair = []

for (dirpath, dirnames, filenames) in walk(folderin_mbrolaclair):
	files_clair.extend(filenames)
	break

#MBROLA delex
files_delex = []

for (dirpath, dirnames, filenames) in walk(folderin_delex):
	files_delex.extend(filenames)
	break

#We start looping on the csv
for row in readertable:
	#Take into account only 
	if row["expe_sentence_key"]+".wav" in files_orig:
		# ~ print(row["expe_sentence_key"])
		expekey = row["expe_sentence_key"]
		ibexkey = row["ibex_sentence_key"]
		listibexkey = ibexkey.split("-")
		listibexkey.insert(1, "OR")
		oldfilename_orig = expekey+".wav"
		newfilename_orig = "-".join(listibexkey)+".wav"
		print("COPYING", folderin_original+oldfilename_orig)
		shutil.copy2(folderin_original+oldfilename_orig, folderout_original)
		new_dst_orig = os.path.join(folderout_original, newfilename_orig)
		os.rename(folderout_original+oldfilename_orig, new_dst_orig)
	if row["expe_sentence_key"]+"_mbrola_normal_interpolated.wav" in files_clair:
		# ~ print(row["expe_sentence_key"])
		expekey = row["expe_sentence_key"]
		ibexkey = row["ibex_sentence_key"]
		listibexkey = ibexkey.split("-")
		listibexkey.insert(1, "MC")
		oldfilename_clair = expekey+"_mbrola_normal_interpolated.wav"
		newfilename_clair = "-".join(listibexkey)+".wav"
		print("COPYING", folderin_mbrolaclair+oldfilename_clair)
		shutil.copy2(folderin_mbrolaclair+oldfilename_clair, folderout_mbrolaclair)
		new_dst_clair = os.path.join(folderout_mbrolaclair, newfilename_clair)
		os.rename(folderout_mbrolaclair+oldfilename_clair, new_dst_clair)
	if row["expe_sentence_key"]+"_mbrola_delexicalised.wav" in files_delex:
		# ~ print(row["expe_sentence_key"])
		expekey = row["expe_sentence_key"]
		ibexkey = row["ibex_sentence_key"]
		listibexkey = ibexkey.split("-")
		listibexkey.insert(1, "MD")
		oldfilename_delex = expekey+"_mbrola_delexicalised.wav"
		newfilename_delex = "-".join(listibexkey)+".wav"
		print("COPYING", folderin_delex+oldfilename_delex)
		shutil.copy2(folderin_delex+oldfilename_delex, folderout_delex)
		new_dst_delex = os.path.join(folderout_delex, newfilename_delex)
		os.rename(folderout_delex+oldfilename_delex, new_dst_delex)

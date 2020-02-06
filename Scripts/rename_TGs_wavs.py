#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Rename files according to newkey

import sys, re, os, shutil, csv
#shutil to copy files

#Define folders
folderin = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/Audio_REAL_expe/"
folderout = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/REAL_EXPE_Ibex/Audio_REAL_expe/New names/"
# ~ folderoutwav2 = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/New_Audio_files2/"
# ~ folderintg = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/TextGrids_EXPE/"
# ~ folderouttg = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/New_TGs/"
# ~ folderouttg2 = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/New_TGs2/"

#csv table
csvfile = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXP_perception_contours_finaux/table_files_REAL-expe-perception.csv", "r")

#Csv reader
reader = csv.DictReader(csvfile, skipinitialspace=True, delimiter="\t")

#Start looping on all sentences
for row in reader:
	#Take into account only 40 sentences for expe
	if row["OK_Expe_perception"] == "YES":
		#We get the old and new key
		oldkey = row["sentence_key"]
		newkey = row["expe_sentence_key"]
		#Filepath is the whole path, oldfilename only the name of the file, newfilename how to rename it
		filepath = folderin+oldkey+"_delexicalised.wav"
		# ~ filepathtg = folderintg+oldkey+".TextGrid"
		oldfilename = oldkey+"_delexicalised.wav"
		# ~ oldfilenametg = oldkey+".TextGrid"
		newfilename = newkey+"_delexicalised.wav"
		# ~ newfilenametg = newkey+".TextGrid"
		print("Moving wav:", filepath)
		shutil.copy2(filepath, folderout)
		new_dst_wav = os.path.join(folderout, newfilename)
		os.rename(folderout+oldfilename, new_dst_wav)
		# ~ print("Moving TG:", filepathtg)
		# ~ shutil.copy2(filepathtg, folderouttg)
		# ~ new_dst_tg = os.path.join(folderouttg2, newfilenametg)
		# ~ os.rename(folderouttg+oldfilenametg, new_dst_tg)

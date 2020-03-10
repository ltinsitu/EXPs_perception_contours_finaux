#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Rename files according to newkey

import sys, re, os, shutil, csv
#shutil to copy files

#Define folders
folderin = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Audio_Expe_verif_methodo2/"
folderout = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Audio_Expe_verif_methodo2/New_names/"
# ~ folderoutwav2 = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/New_Audio_files2/"
# ~ folderintg = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/TextGrids_EXPE/"
# ~ folderouttg = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/New_TGs/"
# ~ folderouttg2 = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/New_TGs2/"

#csv table
csvfile = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Expe_perception_verif_methodo_2_ALL.csv", "r")

#Csv reader
reader = csv.DictReader(csvfile, skipinitialspace=True, delimiter="\t")

#Start looping on all sentences
for row in reader:
	#Take into account only 40 sentences for expe
	# ~ if row["OK_Expe_perception"] == "YES":
	#We get the old and new key
	oldkey = row["OLD_sentence_key"]
	newkey = row["sentence_key"]
	#Filepath is the whole path, oldfilename only the name of the file, newfilename how to rename it
	filepath = folderin+oldkey+".mp3"
	# ~ filepathtg = folderintg+oldkey+".TextGrid"
	oldfilename = oldkey+".mp3"
	# ~ oldfilenametg = oldkey+".TextGrid"
	newfilename = newkey+".mp3"
	# ~ newfilenametg = newkey+".TextGrid"
	# ~ print("Moving wav:", filepath)
	shutil.copy2(filepath, folderout)
	new_dst_wav = os.path.join(folderout, newfilename)
	os.rename(folderout+oldfilename, new_dst_wav)
	# ~ print("Moving TG:", filepathtg)
	# ~ shutil.copy2(filepathtg, folderouttg)
	# ~ new_dst_tg = os.path.join(folderouttg2, newfilenametg)
	# ~ os.rename(folderouttg+oldfilenametg, new_dst_tg)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, shutil, csv
from os import walk

#Pathin
pathin = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/OKdelex/"

#Pathout
pathout = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Audio_Expe_verif_methodo2/"

#Reading csv file
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Expe_perception_verif_methodo_2.csv", "r")
readertable = csv.DictReader(table, skipinitialspace=True, delimiter="\t")

listfiles = []

for stuff in os.walk(pathin):
	for files in stuff:
		for f in files:
			if f.endswith(".wav"):
				listfiles.append(f.replace(".wav", ""))
				# ~ print(f)

for row in readertable:
	if row["audio_type"] == "delex":
		newkey = row["sentence_key"]
		oldkey = row["OLDsentence_key"]
		oldfilename = oldkey+".wav"
		newfilename = newkey+".wav"
		filepath = pathin+oldfilename
		shutil.copy2(filepath, pathout)
		new_dst_wav = os.path.join(pathout, newfilename)
		os.rename(pathout+oldfilename, new_dst_wav)







# ~ for row in readertable:
	# ~ if row["OK_Expe_perception"] == "YES":
		# ~ if row["type-de-phrase"] == "decla":
			# ~ if row["sentence_key"] in listfiles:
				# ~ filenamewav = row["sentence_key"]+".wav"
				# ~ filenameTG = row["sentence_key"]+".TextGrid"
				# ~ filenamePitch = row["sentence_key"]+".Pitch"
				# ~ print("COPYING", filenamewav, "in", pathout)
				# ~ print("COPYING", filenameTG, "in", pathout)
				# ~ print("COPYING", filenamePitch, "in", pathout)
				# ~ shutil.copy2(pathin+filenamewav, pathout)
				# ~ shutil.copy2(pathin+filenameTG, pathout)
				# ~ shutil.copy2(pathin+filenamePitch, pathout)
			# ~ else:
				# ~ print("Problem with: ", row["sentence_key"])
		# ~ elif row["type-de-phrase"] == "yes-no":
			# ~ if row["sentence_key"] in listfiles:
				# ~ filenamewav = row["sentence_key"]+".wav"
				# ~ filenameTG = row["sentence_key"]+".TextGrid"
				# ~ filenamePitch = row["sentence_key"]+".Pitch"
				# ~ print("COPYING", filenamewav, "in", pathout)
				# ~ print("COPYING", filenameTG, "in", pathout)
				# ~ print("COPYING", filenamePitch, "in", pathout)
				# ~ shutil.copy2(pathin+filenamewav, pathout)
				# ~ shutil.copy2(pathin+filenameTG, pathout)
				# ~ shutil.copy2(pathin+filenamePitch, pathout)
			# ~ else:
				# ~ print("Problem with: ", row["sentence_key"])

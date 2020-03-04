#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, shutil, csv
from os import walk

#Pathin
pathin = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Fillers/AllFillers/FORMBROLA_clair/"

#Pathout
pathout = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Fillers/AllFillers/FORMBROLA_clair/"

for stuff in os.walk(pathin):
	for files in stuff:
		# ~ print(files)
		if type(files) is list:
			for f in files:
				f = f.replace(".wav", "")
				f = f.replace(".TextGrid", "")
				f = f.replace(".PitchTier", "")
				print(f)
				# ~ if not f.endswith(".Pitch"):
					# ~ print("COPYING", f, "in", pathout)
					# ~ shutil.copy2(pathin+f, pathout)

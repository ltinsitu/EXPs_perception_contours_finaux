#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, shutil, csv
from os import walk

#Pathin
pathin = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/FORMBROLA_delex/"

#Pathout
pathout = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Files_delex/"

for stuff in os.walk(pathin):
	for files in stuff:
		for f in files:
			if f.endswith("_delexicalised.TextGrid"):
				print("COPYING", f, "in", pathout)
				shutil.copy2(pathin+f, pathout)

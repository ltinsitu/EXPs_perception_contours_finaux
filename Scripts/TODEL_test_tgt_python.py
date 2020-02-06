#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os
import csv
import textgrids
import io, codecs
from praatio import tgio

filetest = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_wh_final/Audio_TG/WE2_A001_1952s875.TextGrid"



fi = io.open(filetest, "r", encoding='utf-16-be')

tg = tgio.openTextgrid(filetest)

sylltier = tg.tierDict["syll"]

# ~ print(sylltier)
sylls = sylltier.entryList

print("Number of syllables interval:", len(sylls))

countsyll = 0

for s in sylls:
	if not re.match("_", s[2]):
		countsyll += 1

print("Number of syllables (excluding pauses):", countsyll)

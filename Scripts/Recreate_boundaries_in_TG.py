#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Since using WebMAUS for automatic segmentation makes praat boundaries funny, this script recreates the boundaries with the right start/stop time.

import sys, re, os, csv
import glob
from praatio import tgio

#Folder where TGs are stored
foldertg = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Fillers/Lucas/FILLERSLUCAS/TestMOVEBOUNDARY/"

folderoutput = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Fillers/Lucas/FILLERSLUCAS/TestMOVEBOUNDARY/TESTS/"

#Browse TG path
tgpaths = glob.glob(foldertg+"*.TextGrid")

#Create lists that will contain the modified tiers
list_phones = []
list_kanmaus = []
list_words = []

#We start looping on all TGs
for tgfile in tgpaths:
	# ~ counttg +=1
	#We get the name of the TG
	tgname = tgfile.replace(foldertg, "")
	tgname = tgname.replace(".TextGrid", "")
	#Opening TGs with praat-textgrids
	tg = tgio.openTextgrid(tgfile)
	#We get the problematic tiers
	phones = tg.tierDict[tg.tierNameList[0]]
	kanmaus = tg.tierDict[tg.tierNameList[2]]
	words = tg.tierDict[tg.tierNameList[3]]
	##looping through intervals in problematic tiers
	#Phones tier
	for start, stop, label in phones.entryList:
		# ~ print([start, stop, label])
		list_phones.append([start, stop, label])
	#KanMaus tier
	for start, stop, label in kanmaus.entryList:
		# ~ print([start, stop, label])
		list_kanmaus.append([start, stop, label])
	#Words tier
	for start, stop, label in words.entryList:
		# ~ print([start, stop, label])
		list_words.append([start, stop, label])

	##For each problematic tier, we replace each stoptime with the next starttime
	#Phones tier
	for i, j in zip(list_phones, list_phones[1:]):
		i[1] = j[0]
	#KanMaus tier
	for k, l in zip(list_kanmaus, list_kanmaus[1:]):
		# ~ print(k[1], l[0])
		k[1] = l[0]
	#Words tier
	for m, n in zip(list_words, list_words[1:]):
		# ~ print(m[1], n[0])
		m[1] = n[0]

	#Just to print the result
	# ~ for entries in list_phones:
		# ~ print(entries)
	# ~ for entries in list_kanmaus:
		# ~ print(entries)
	# ~ for entries in list_words:
		# ~ print(entries)
	
	##We need to get the final stoptime, else a new boundary is created at the very end
	#We get the final stoptime from the uncorrupted ortho tier
	ortho = tg.tierDict[tg.tierNameList[5]]
	list_ortho = []
	#We put everything in a list, and then get the last element. Even if the ortho tier has only one interval it is harmless
	for start, stop, label in ortho.entryList:
		list_ortho.append([start, stop, label])
	finalstop = list_ortho[-1][1]
	
	#Changing the stoptime of the last element in each list
	list_phones[-1][1] = finalstop
	list_kanmaus[-1][1] = finalstop
	list_words[-1][1] = finalstop
		
	#Now we can change the tiers with the new lists we created
	phones.entryList = list_phones
	kanmaus.entryList = list_kanmaus
	words.entryList = list_words
	
	#Saving tg to newdir
	tg.save(folderoutput+tgname+".TextGrid")

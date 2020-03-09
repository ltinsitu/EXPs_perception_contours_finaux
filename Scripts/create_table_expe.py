#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, csv

#Open input and output file
csvfile = open("//home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Expe_perception_verif_methodo_2_ALL.csv", 'r')

#parse csvs
reader = csv.DictReader(csvfile, skipinitialspace=True, delimiter="\t")

#Get header
header = reader.fieldnames
# ~ print(header)

#For ibex
ibex1 = '\t[["'
ibex2 = '",'
ibex3 = '], "Question", {q: "<div style=\\"width: 40em;\\"><audio autoplay controls preload=\\"auto\\"><source src=\''
url = "https://raw.github.com/ltinsitu/EXPs_perception_contours_finaux/tree/master/Expe_perception_verif_methodo_2/Audio_Expe_verif_methodo2/"
mclair = "MBROLA-clair/"
mdelex = "MBROLA-delexicalised/"
orig = "Originals/"
#We'll need to comment the filename, it's enough to add the comment tag <!-- at the end of ibex4, and closing it with --> at the beginning of ibex5
ibex4 = "\'type=\'audio/mpeg\'></source></audio><br><br><br>"
ibex5 = '<br>Est-ce que cette phrase vous donne l\'impression d\'être une question ?''</div>", as: ["Oui", "Non"]}],'

#Item counters
counteritemyd = 1
counteritemwi = 21

#Type item, all the same
typeitem = "expe"


#For the practices
ibex1prac = '\t["'
ibex2prac = '\", "Question", {q: "<div style=\\"width: 40em;\\"><audio autoplay controls preload=\\"auto\\"><source src=\''
typeitemprac = "practice"
urlpractice = "https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/"
ibex5prac = '<br><br><br>Selon vous, est-ce que cette phrase pourrait être un ordre ?''</div>", as: ["Oui", "Non"]}],'

dir_practices = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/PILOT_EXPE_Ibex/Audio/Practices/"


#Some comments to introduce practices
# ~ print("\t//\n\t//Some practice items\n\t//\n\n")

# ~ f_prac = []
# ~ for (dirpath, dirnames, filenames) in os.walk(dir_practices):
	# ~ for f in filenames:
		# ~ if f.endswith("mp3"):
			# ~ if f[3:5] == "OR":
				# ~ folderprac = "Originals/"
				# ~ print(ibex1prac, typeitemprac, ibex2prac, urlpractice, folderprac, f, ibex4, ibex5prac, sep="", end="\n")
			# ~ if f[3:5] == "MD":
				# ~ folderprac = "MBROLA-delexicalised/"
				# ~ print(ibex1prac, typeitemprac, ibex2prac, urlpractice, folderprac, f, ibex4, ibex5prac, sep="", end="\n")
			# ~ if f[3:5] == "MC":
				# ~ folderprac = "MBROLA-clair/"
				# ~ print(ibex1prac, typeitemprac, ibex2prac, urlpractice, folderprac, f, ibex4, ibex5prac, sep="", end="\n")

# ~ #Comments to introduce expe stim
# ~ print("\n\n\t//\n\t//Experimental stim\n\t//\n\n")


#For the expe stimuli
for row in reader:
	if row["ibex_sentence_key"].startswith("PI"):
		list_ibex_key = row["ibex_sentence_key"].split("-")
		oldkey_lastpart = "-".join(list_ibex_key[1:])
		if row["type-de-phrase"] == "decla":
			MCdecla = "PI-MC-"+oldkey_lastpart+".mp3"
			ORdecla = "PI-OR-"+oldkey_lastpart+".mp3"
			print(ibex1, typeitem, ibex2, counteritemyd, ibex3, url, mclair, MCdecla, ibex4, ibex5, sep="", end="\n")
			print(ibex1, typeitem, ibex2, counteritemyd, ibex3, url, orig, ORdecla, ibex4, ibex5, sep="", end="\n")
			counteritemyd += 1
		elif row["type-de-phrase"] == "yes-no":
			MCyesno = "PI-MC-"+oldkey_lastpart+".mp3"
			ORyesno = "PI-OR-"+oldkey_lastpart+".mp3"
			print(ibex1, typeitem, ibex2, counteritemyd, ibex3, url, mclair, MCyesno, ibex4, ibex5, sep="", end="\n")
			print(ibex1, typeitem, ibex2, counteritemyd, ibex3, url, orig, ORyesno, ibex4, ibex5, sep="", end="\n")
			counteritemyd += 1
		elif row["type-de-phrase"] == "wh-in-situ":
			MCwhinsitu = "PI-MC-"+oldkey_lastpart+".mp3"
			MDwhinsitu = "PI-MD-"+oldkey_lastpart+".mp3"
			print(ibex1, typeitem, ibex2, counteritemwi, ibex3, url, mclair, MCwhinsitu, ibex4, ibex5, sep="", end="\n")
			print(ibex1, typeitem, ibex2, counteritemwi, ibex3, url, mdelex, MDwhinsitu, ibex4, ibex5, sep="", end="\n")
			counteritemwi += 1
		else:
			pass

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, csv

#Open input and output file
csvfile = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Expe_perception_verif_methodo_3_BOTH.csv", 'r')

#parse csvs
reader = csv.DictReader(csvfile, skipinitialspace=True, delimiter="\t")

#Get header
header = reader.fieldnames
# ~ print(header)


#For ibex
ibex1 = '\t[["'
ibex2 = '",'
ibex3 = '], "Question", {q: "<div style=\\"width: 40em;\\"><audio autoplay controls preload=\\"auto\\"><source src=\''
url1 = "https://github.com/ltinsitu/EXPs_perception_contours_finaux/blob/master/Expe_perception_verif_methodo_3/Audio_files/"
# ~ mclair = "MBROLA-clair/"
# ~ mdelex = "MBROLA-delexicalised/"
# ~ orig = "Originals/"
#We'll need to comment the filename, it's enough to add the comment tag <!-- at the end of ibex4, and closing it with --> at the beginning of ibex5
ibex4 = ".mp3?raw=true\'type=\'audio/mpeg\'></source></audio><br><br><br><!--"
ibex5 = '--><br>Est-ce que cette phrase vous donne l\'impression d\'être <br><strong>'
ibex6 = '</strong>''</div>", as: ["Oui", "Non"]}],'

# ~ #Item counters
# ~ counteritemyd = 1
# ~ counteritemwi = 21

# ~ #Type item, all the same
# ~ typeitem = "expe"


# ~ #For the practices
# ~ ibex1prac = '\t["'
# ~ ibex2prac = '\", "Question", {q: "<div style=\\"width: 40em;\\"><audio autoplay controls preload=\\"auto\\"><source src=\''
# ~ typeitemprac = "practice"
# ~ urlpractice = "https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/"
# ~ ibex5prac = '<br><br><br>Selon vous, est-ce que cette phrase pourrait être un ordre ?''</div>", as: ["Oui", "Non"]}],'

# ~ dir_practices = "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/PILOT_EXPE_Ibex/Audio/Practices/"


# ~ #Some comments to introduce practices
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

#Comments to introduce expe stim
# ~ print("\n\n\t//\n\t//Experimental stim\n\t//\n\n")


#For the stimuli
for row in reader:
	#Define task question type
	if row["task_question_type"] == "is.it.question":
		taskQ = "une question ?"
	if row["task_question_type"] == "is.it.decla":
		taskQ = "une phrase affirmative ?"
	#XP mbrola
	if row["XP_type"] == "XP_mbrola":
		#Define folder mbrola
		url2 = "XP_mbrola/"
		#Test sentences
		if int(row["item"]) < 49:
			stimtype = "TM"
			item = int(row["item"])
			#Print with sentence key in the html code
			print(ibex1, stimtype, ibex2, item, ibex3, url1, url2, row["sentence_key"], ibex4, row["sentence_key"], ibex5, taskQ, ibex6, sep="", end="\n")
			# #Print WITHOUT sentence key in the html code
			# print(ibex1, stimtype, ibex2, item, ibex3, url, row["sentence_key"], ibex4, ibex5, sep="", end="\n")
			# ~ pass
		#Fillers
		else:
			stimtype = "FM"
			#Define new task Q with exclamatives
			if row["task_question_type"] == "is.it.question":
				taskQ = "une question ?"
			if row["task_question_type"] == "is.it.decla":
				taskQ = "une exclamative ?"
			item = int(row["item"])
			#Print with sentence key in the html code
			print(ibex1, stimtype, ibex2, item, ibex3, url1, url2, row["sentence_key"], ibex4, row["sentence_key"], ibex5, taskQ, ibex6, sep="", end="\n")
			# #Print WITHOUT sentence key in the html code
			# print(ibex1, stimtype, ibex2, item, ibex3, url, row["sentence_key"], ibex4, ibex5, sep="", end="\n")
			# ~ print(row["item"])
			# ~ pass
	#XP delex	
	if row["XP_type"] == "XP_delex":
		#Define folder mbrola
		url2 = "XP_delex/"
		#Test sentences
		if int(row["item"]) < 41:
			stimtype = "TD"
			item = int(row["item"]) + 96
			#Print with sentence key in the html code
			print(ibex1, stimtype, ibex2, item, ibex3, url1, url2, row["sentence_key"], ibex4, row["sentence_key"], ibex5, taskQ, ibex6, sep="", end="\n")
			# #Print WITHOUT sentence key in the html code
			# print(ibex1, stimtype, ibex2, item, ibex3, url, row["sentence_key"], ibex4, ibex5, sep="", end="\n")
			# ~ pass
		#Fillers
		else:
			stimtype = "FD"
			#Define new task Q with exclamatives
			if row["task_question_type"] == "is.it.question":
				taskQ = "une question ?"
			if row["task_question_type"] == "is.it.decla":
				taskQ = "une exclamative ?"
			item = int(row["item"]) + 96
			#Print with sentence key in the html code
			print(ibex1, stimtype, ibex2, item, ibex3, url1, url2, row["sentence_key"], ibex4, row["sentence_key"], ibex5, taskQ, ibex6, sep="", end="\n")
			# #Print WITHOUT sentence key in the html code
			# print(ibex1, stimtype, ibex2, item, ibex3, url, row["sentence_key"], ibex4, ibex5, sep="", end="\n")
			# ~ print(row["item"])
			# ~ pass
	#First the expe stimuli
	# if int(row["item"]) < 61:
		# # ~ print(row["item"])
		# list_sentence_key = row["sentence_key"].split("-")
		# stimtype = "T"
		# item = int(row["item"])
		# #Print with sentence key in the html code
		# # ~ print(ibex1, stimtype, ibex2, item, ibex3, url, row["sentence_key"], ibex4, row["sentence_key"], ibex5, sep="", end="\n")
		# #Print WITHOUT sentence key in the html code
		# print(ibex1, stimtype, ibex2, item, ibex3, url, row["sentence_key"], ibex4, ibex5, sep="", end="\n")
		# # ~ oldkey_lastpart = "-".join(list_ibex_key[1:])
		# # ~ else:
			# # ~ pass
	# #Then the fillers
	# else:
		# # ~ print(row["item"])
		# list_sentence_key = row["sentence_key"].split("-")
		# # ~ print(list_sentence_key[3])
		# stimtype = "F"
		# item = int(row["item"])
		# #Print with sentence key in the html code
		# # ~ print(ibex1, stimtype, ibex2, item, ibex3, url, row["sentence_key"], ibex4, row["sentence_key"], ibex5, sep="", end="\n")
		# #Print WITHOUT sentence key in the html code
		# print(ibex1, stimtype, ibex2, item, ibex3, url, row["sentence_key"], ibex4, ibex5, sep="", end="\n")


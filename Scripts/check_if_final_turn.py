#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Check whether the sentences gathered are the last turn of the speaker

import sys, re, os, csv
from lxml import etree as ET

#path to xml files
xmldir = "/home/lucas/Documents/CloudStation/SDL/PhD/Corpora/Save_transcriptions/ATRAITER/ESLO/ESLO2/"

#Open table containing all sentences
table = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/table_files_REAL-expe-perception.csv", "r")

#Table reader
readertable = csv.DictReader(table, skipinitialspace=True, delimiter="\t")

#We start looping on sentences
for row in readertable:
	#Only the potential sentences for the expe
	#I comment it here cause 
	# ~ if row["OK_Expe_perception"] == "YES":
	#We get the sentence_key, sepaker, the Synctime for declas/questionline for questions and the xml filename
	sentence_key = row["sentence_key"]
	speaker = row["locuteur"]
	if row["type-de-phrase"] == "decla":
		synctime = sentence_key.split("_")[2]
		synctime = synctime.replace("s", ".")
		# ~ print(synctime)
	else:
		questionline = sentence_key.split("_")[2]
	namefilexml = "WE2_"+sentence_key.split("_")[1]+".xml"
	#We open the xml and readlines
	filexml = open(xmldir+namefilexml, "r")
	linesfilexml = filexml.readlines()
	#Initiate line counter
	linecount = 0
	#Start looping on each line
	#We need to make the list iterable first
	linesfilexml = iter(linesfilexml)
	for line in linesfilexml:
		linecount += 1
		#We look for question tag
		if re.search(r'<question line=\"\d+\">', line):
			#We get the question line
			questionlinexml = re.findall(r"<question line=\"(\d+)\">", line)[0]
			#Only for questions
			if not row["type-de-phrase"] == "decla":
				#Only for lines matching sentences to consider for the expe
				if questionline == questionlinexml:
					#We get the speaker. The regex returns a list of one element which is a fucking tuple of 4 elements. WTF. We need the 2 and 4 elements of the tuple (this corresponds to the two speakers). But there might only one. I fucking love regex.
					spkrxml = re.findall(r"<Turn speaker=\"(([a-z]{3}\d)(\s([a-z]{3}\d))*)\".+>", line)
					#We get the two potential speakers (2nd and 4th elements in the tuple). Might be the case that the second spkr (var spkrxml2) is empty.
					if spkrxml:
						spkrxml1 = spkrxml[0][1]
						spkrxml2 = spkrxml[0][3]
						#Just to be sure it's the same speaker in the xml than the table
						if (speaker in spkrxml1) or (speaker
						in spkrxml2):
							#We iterate on the next line (THAT'S SO FUCKING COOL)
							line = next(linesfilexml)
							#A while loop I never use it but it works now I'm so happyyyy
							while not re.search("<Turn", line):
								line = next(linesfilexml)
							nextspkr = re.findall(r"<Turn speaker=\"(([a-z]{3}\d)(\s([a-z]{3}\d))*)\".+>", line)
							if nextspkr:
								nextspkr1 = nextspkr[0][1]
								nextspkr2 = nextspkr[0][3]
								if (speaker in nextspkr1) or (speaker in nextspkr2):
									print("Problem:", row["type-de-phrase"], sentence_key)
							#Sometimes my approach just don't work, in this case I give up
							else:
								print("To check manually: "+sentence_key)
					#Sometimes my approach just don't work, in this case I give up
					else:
						print("To check manually: "+sentence_key)
		#We do the same thing for the synctime for declaratives
		elif re.search(r'<Sync time=\"(\d+\.\d+)\"/>', line):
				synctimexml = re.findall(r'<Sync time=\"(\d+\.\d+)\"/>', line)
				synctimexml = synctimexml[0]
				#We select only decla
				if row["type-de-phrase"] == "decla":
					if synctime == synctimexml:
						#We iterate on the next line (THAT'S SO FUCKING COOL)
						line = next(linesfilexml)
						#A while loop I never use it but it works now I'm so happyyyy
						while not re.search("<Turn", line):
							line = next(linesfilexml)
						nextspkr = re.findall(r"<Turn speaker=\"(([a-z]{3}\d)(\s([a-z]{3}\d))*)\".+>", line)
						if nextspkr:
							nextspkr1 = nextspkr[0][1]
							nextspkr2 = nextspkr[0][3]
							if (speaker in nextspkr1) or (speaker in nextspkr2):
								print("Problem:", row["type-de-phrase"], sentence_key)
						#Sometimes my approach just don't work, in this case I give up
						else:
								print("To check manually: "+sentence_key)

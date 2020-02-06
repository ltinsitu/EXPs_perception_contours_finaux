#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re, os, csv

#Open input and output file
csvfile = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/table_files_expe-perception.csv", 'r')
csvout = open("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/table_new_files_expe-perception.csv", 'w')


#parse csvs
reader = csv.DictReader(csvfile, skipinitialspace=True, delimiter="\t")
# ~ print(reader)

#Get header
header = reader.fieldnames
header.append("ibex_sentence_key")
print(header)

# ~ list_sentences_perceptionXP = []

writer = csv.DictWriter(csvout, fieldnames=header, delimiter="\t")
writer.writeheader()


# ~ for row in reader:
	# ~ oldkey = row['sentence_key']
	# ~ numstim = row["numstimtodel"]
	# ~ if not numstim:
		# ~ numstim = "000"
	# ~ codesentence = ""
	# ~ if row["type-de-phrase"] == "decla":
		# ~ codesentence = "de"
	# ~ elif row["type-de-phrase"] == "yes-no":
		# ~ codesentence = "yn"
	# ~ elif row["type-de-phrase"] == "wh-in-situ":
		# ~ codesentence = "wi"
	# ~ elif row["type-de-phrase"] == "wh-ex-situ":
		# ~ codesentence = "we"
	# ~ eske = ""
	# ~ if row["presence-eske"] == "NO":
		# ~ eske = 0
	# ~ elif row["presence-eske"] == "YES":
		# ~ eske = 1
	# ~ sep = "-"
	# ~ newkey = numstim+sep+codesentence+sep+str(eske)+sep+oldkey
	# ~ row["expe_sentence_key"] = newkey
	# ~ writer.writerow(row)
	# ~ list_sentences_perceptionXP.append(xmlfile)

for row in reader:
	oldkey = row["expe_sentence_key"]
	listoldkey = oldkey.split("-")
	oldkey_firstpart = "-".join(listoldkey[0:3])
	# ~ print(oldkey_firstpart)
	if row["OK_Expe_perception"] == "YES":
		typeofexpe = "PI"
	else:
		typeofexpe = "NO"
	sex = row["spk_sex"]
	sep = "-"
	newkey = typeofexpe+sep+oldkey_firstpart+sep+sex+sep+row["sentence_key"]
	print(newkey)
	row["ibex_sentence_key"] = newkey
	writer.writerow(row)


# ~ for i in list_sentences_perceptionXP:
	# ~ print(i)

#Write header in output
# ~ writer = csv.DictWriter(csvfile, fieldnames=header, delimiter="\t")
# ~ writer.writeheader()

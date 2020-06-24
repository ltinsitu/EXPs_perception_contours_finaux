#To load results from an Ibex experiment

#Load the ibextor program, as well as plyr lib to modify dfs
library(ibextor)
library(plyr)


##Define paths
#results file
f_results <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/IBEX/results/results"
f_output_MBROLA <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Results_methodo3_mbrola.csv"
f_output_DELEX <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Results_methodo3_delex.csv"
f_output_MBROLA_fillers <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Results_methodo3_MBROLA_fillers.csv"
f_output_DELEX_fillers <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Results_methodo3_DELEX_fillers.csv"

#We need to replace "Formit" by "Form" in the results files, else ibextor doesn't work
results_lines <- readLines(f_results)
results_lines_ok  <- gsub(pattern = "Formit", replace = "Form", x = results_lines)
results_lines_ok <- gsub("'", "", results_lines_ok)

results_lines_ok <- gsub('"', '', results_lines_ok)
#Need to replace Tristan's comment which includes apostrophes
# results_lines_ok <- gsub("1585748064,4e1cc0cd8a4a548d96ea356fb6538aa2,Formit,6,0,endexpe,NULL,commentexpe,C\'est assez compliqué au début de savoir si l\'on doit répondre \"est ce que ca me semble être une question\" ou \'est ce que c\'est vraiment une question\". Je crois une petit retour arrière serait pas mal\%2C j\'ai cliqué un peu vite sur certains et après coup j\'aurais peutetre choisi la réponse inverse. \%0AMerci en tout cas\%2C\%0ALes bisous docteur Tual",
                         # "1585748064,4e1cc0cd8a4a548d96ea356fb6538aa2, Formit,6,0,endexpe,NULL,commentexpe,compliquederepondre",
                         # results_lines_ok)
writeLines(results_lines_ok, con=f_results)


#We use Ibex to get results and participants questionnaire
results <- get_results_q(f_results)
subjinfo <- get_subj_info(f_results, form_name = c("intro"))
#This next line doesnt work because of ' and " in the comments
subjinfo2 <- get_subj_info(f_results, form_name = c("endexpe"))


#We merge the two df
subjinfo$subj <- as.numeric(rownames(subjinfo))
subjinfo2$subj <- as.numeric(rownames(subjinfo))
res <- merge(subjinfo, results, by = "subj")
res <- merge(subjinfo2, res, by = "subj")

#Remove the practice else it stimlist is not same for all rows
res <- res[which(res$type != "practiceD" & res$type != "practiceM"), ]

#Add a column for reaction time (sum of all questions rts)
dfrt <- aggregate(res$quest_rt, by=list(subj=res$subj), FUN=sum)
dfrt$totalrt <- dfrt$x/1000/60
dfrt <- do.call("rbind", replicate(120, dfrt, simplify = FALSE))

dfrt <- dfrt[order(dfrt$subj), ]
totalrt <- as.list(dfrt$totalrt)

#Doesnt work because not same number of trials per participant
# res <- data.frame(res, do.call(rbind, totalrt))
# res <- rename(res, c("do.call.rbind..totalrt." = "totalrt"))

##We split the stimulus full-name to create new cols
#First a regex to get the filename
res$stimulus <- sub(".*(Audio_files\\/XP_.+\\/)(.*)\\.mp3.*", "\\2", res$question)

#Get time speaker passed expe in a normal format
res$date_ok <- as.POSIXct(as.integer(sub("(.*)_.*", "\\1",
                                  as.character(res$subj_uid))), origin = "1970-01-01")


#Split it on - and save it
stimlist <- strsplit(res$stimulus, '-')
#Create a new df with everything
res <- data.frame(res, do.call(rbind, stimlist))
#Rename the cols
res <- rename(res, c("X1"="stim_number", "X2"="XP_type", "X3"="task_q_type", "X4"="sentence_type",
                     "X5"="audio_type", "X6"="item2", "X7"="list", "X8"="presence_eske", "X9"="syll_num",
                     "X10"="spk_id", "X11"="spk_sex", "X12"="orig_filename"))

etcol <- colnames (res)

#Everything as factor
res[sapply(res, is.character)] <- lapply(res[sapply(res, is.character)], as.factor)

#Create a separate dataset for each experiment
resXPmbrola <- res[which(res$type == "FM" | res$type == "TM"), ]
resXPdelex <-  res[which(res$type == "FD" | res$type == "TD"), ]

#Subset only expe trials, put fillers apart
resXPmbrolafillers <- resXPmbrola[which(resXPmbrola$type == "FM"), ]
resXPdelexfillers <- resXPdelex[which(resXPdelex$type == "FD"), ]

resXPmbrolafillers <- droplevels(resXPmbrolafillers)
resXPdelexfillers <- droplevels(resXPdelexfillers)

resXPmbrola <- resXPmbrola[which(resXPmbrola$type == "TM"), ]
resXPdelex <- resXPdelex[which(resXPdelex$type == "TD"), ]

resXPmbrola <- droplevels(resXPmbrola)
resXPdelex <- droplevels(resXPdelex)

##TODODefine right answers
# res$rightanswer[res$sentence_type == "de" & res$answer == "Non"] <- "Yes"
# res$rightanswer[res$sentence_type == "de" & res$answer == "Oui"] <- "No"
# res$rightanswer[res$sentence_type == "yn" & res$answer == "Non"] <- "No"
# res$rightanswer[res$sentence_type == "yn" & res$answer == "Oui"] <- "Yes"

#DOESNT workWe add order of presentation of stimuli for each participants
# resXPmbrola$num_sequence <- c(1:48)
# resXPdelex$num_sequence <- c(1:40)

#Everything as factor
resXPmbrola[sapply(resXPmbrola, is.character)] <- lapply(resXPmbrola[sapply(resXPmbrola, is.character)], as.factor)
resXPdelex[sapply(resXPdelex, is.character)] <- lapply(resXPdelex[sapply(resXPdelex, is.character)], as.factor)
resXPmbrolafillers[sapply(resXPmbrolafillers, is.character)] <- lapply(resXPmbrolafillers[sapply(resXPmbrolafillers, is.character)], as.factor)
resXPdelexfillers[sapply(resXPdelexfillers, is.character)] <- lapply(resXPdelexfillers[sapply(resXPdelexfillers, is.character)], as.factor)

#INCLUDE PITCH INFOS
#Open pitch table
tablepitch <- read.csv("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/table_Pitch_expe_percep_verif2.csv",
         header = T)

#Rename column filename of tablepitch to match res
names(tablepitch)[names(tablepitch)=="filename"] <- "orig_filename"

#Merge the two dfs
resXPmbrola <- merge(resXPmbrola, tablepitch, by = "orig_filename")
resXPdelex <- merge(resXPdelex, tablepitch, by = "orig_filename")

#Reorder by subject
resXPmbrola <- resXPmbrola[order(resXPmbrola$subj),]
resXPdelex <- resXPdelex[order(resXPdelex$subj),]

#Everything as factor
resXPmbrola <- droplevels(resXPmbrola)
resXPmbrola[sapply(resXPmbrola, is.character)] <- lapply(resXPmbrola[sapply(resXPmbrola, is.character)], as.factor)

resXPdelex <- droplevels(resXPdelex)
resXPdelex[sapply(resXPdelex, is.character)] <- lapply(resXPdelex[sapply(resXPdelex, is.character)], as.factor)

##Writing the table into a csv file
write.csv(resXPmbrola, file = f_output_MBROLA)
write.csv(resXPdelex, file = f_output_DELEX)

write.csv(resXPmbrolafillers, file = f_output_MBROLA_fillers)
write.csv(resXPdelexfillers, file = f_output_DELEX_fillers)



#To load results from an Ibex experiment

#Load the ibextor program, as well as plyr lib to modify dfs
library(ibextor)
library(plyr)

##Define paths
#results file
f_results <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/PILOT_EXPE_Ibex/Perception_contours_finaux_wh/results/results"
f_output <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/Expé_perception_contours_finaux/EXP_perception_contours_finaux/PILOT_EXPE_Ibex/Results_PILOT.csv"

#We need to replace "Formit" by "Form" in the results files, else ibextor doesn't work
results_lines <- readLines(f_results)
results_lines_ok  <- gsub(pattern = "Formit", replace = "Form", x = results_lines)
writeLines(results_lines_ok, con=f_results)

#We use Ibex to get results and participants questionnaire
results <- get_results_q(f_results)
subjinfo <- get_subj_info(f_results)

#We merge the two df
subjinfo$subj <- as.numeric(rownames(subjinfo))
res <- merge(subjinfo, results, by = "subj")

#We add order of presentation of stimuli for each participants
res$num_sequence <- c(1:33)

##We split the stimulus full-name to create new cols
#First a regex to get the filename
res$stimulus <- sub(".*(PI-.*mp3).*", "\\1", res$question)

#Split it on - and save it
stimlist <- strsplit(res$stimulus, '-')
#Create a new df with everything
res <- data.frame(res, do.call(rbind, stimlist))
#Rename the cols
res <- rename(res, c("X1"="type_of_expe", "X2"="audio_type", "X3"="numfile",
                     "X4"="sentence_type", "X5"="pres_eske", "X6"="spksex", "X7"="orig_filename"))

etcol <- colnames (res)
#Everything as factor
res[sapply(res, is.character)] <- lapply(res[sapply(res, is.character)], as.factor)

##Two subsets for each expe
#First qd, removing pi, pe and wi
resqd <- res[which(res$sentence_type != "pi"), ]
resqd <- resqd[which(resqd$sentence_type != "pe"), ]
resqd <- resqd[which(resqd$sentence_type != "wi"), ]

resqd <- droplevels(resqd)

#Second wi, selecting only wi
reswi <- res[which(res$sentence_type == "wi"), ]

reswi <- droplevels(reswi)


##Writing the table into a csv file
write.csv(res, file = f_output)

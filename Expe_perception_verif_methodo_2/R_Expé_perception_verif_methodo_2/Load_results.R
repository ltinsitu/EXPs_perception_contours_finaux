#To load results from an Ibex experiment

#Load the ibextor program, as well as plyr lib to modify dfs
library(ibextor)
library(plyr)

##Define paths
#results file
f_results <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/IBEX/results/results"
f_output <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Results_methodo2.csv"

#We need to replace "Formit" by "Form" in the results files, else ibextor doesn't work
results_lines <- readLines(f_results)
#results_lines_ok  <- gsub(pattern = "Formit", replace = "Form", x = results_lines)
#writeLines(results_lines_ok, con=f_results)

#We use Ibex to get results and participants questionnaire
results <- get_results_q(f_results)
subjinfo <- get_subj_info(f_results)

#We merge the two df
subjinfo$subj <- as.numeric(rownames(subjinfo))
res <- merge(subjinfo, results, by = "subj")

#We add order of presentation of stimuli for each participants
#TOCHANGE ONCE WE HAVE THE WHOLE EXPE SET UP
res$num_sequence <- c(1:120)

##We split the stimulus full-name to create new cols
#First a regex to get the filename
res$stimulus <- sub(".*<br>(\\d{3}.*)<br>.*", "\\1", res$question)

#Split it on - and save it
stimlist <- strsplit(res$stimulus, '-')
#Create a new df with everything
res <- data.frame(res, do.call(rbind, stimlist))
#Rename the cols
res <- rename(res, c("X1"="stim_number", "X2"="sentence_type", "X3"="audio_type",
                     "X4"="item2", "X5"="list", "X6"="presence_eske", "X7"="syll_num",
                     "X8"="spk_id", "X9"="spk_sex", "X10"="orig_filename"))

etcol <- colnames (res)
#Everything as factor
res[sapply(res, is.character)] <- lapply(res[sapply(res, is.character)], as.factor)

#Subset only expe trials, put fillers apart
resfillers <- res[which(res$type == "F"), ]
resfillers <- droplevels(resfillers)
res <- res[which(res$type == "T"), ]
res <- droplevels(res)


#PLOT JUST FOR FUN
# library(ggplot2)
# plotres <- ggplot(res, aes(audio_type, ..count..)) + geom_bar(aes(fill = answer))
# plotres + facet_grid(. ~ sentence_type)
# 
# plotfillers <- ggplot(resfillers, aes(audio_type, ..count..)) + geom_bar(aes(fill = answer))
# plotfillers + facet_grid(. ~ sentence_type)

##Writing the table into a csv file
write.csv(res, file = f_output)


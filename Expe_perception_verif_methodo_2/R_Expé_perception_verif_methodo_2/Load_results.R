#To load results from an Ibex experiment

#Load the ibextor program, as well as plyr lib to modify dfs
library(ibextor)
library(plyr)

##Define paths
#results file
f_results <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/IBEX/results/results"
f_output <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Results_methodo2.csv"
f_output_fillers <- "/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Results_methodo2_fillers.csv"

#We need to replace "Formit" by "Form" in the results files, else ibextor doesn't work
results_lines <- readLines(f_results)
results_lines_ok  <- gsub(pattern = "Formit", replace = "Form", x = results_lines)
writeLines(results_lines_ok, con=f_results)

#Need to replace Tristan's comment which includes apostrophes
# results_lines_ok <- gsub(pattern = "1585748064,4e1cc0cd8a4a548d96ea356fb6538aa2,
#                          Formit,6,0,endexpe,NULL,commentexpe,
#                          C'est assez compliqué au début de savoir si l'on doit répondre
#                          \"est ce que ca me semble être une question\"
#                          ou 'est ce que c'est vraiment une question\".
#                          Je crois une petit retour arrière serait pas mal%2C
#                          j'ai cliqué un peu vite sur certains et après coup
#                          j'aurais peutetre choisi la réponse inverse.
#                          %0AMerci en tout cas%2C%0ALes bisous docteur Tual",
#                          replace = "1585748064,4e1cc0cd8a4a548d96ea356fb6538aa2,
#                          Formit,6,0,endexpe,NULL,commentexpe,compliquederepondre",
#                          x = results_lines_ok)

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

#We add order of presentation of stimuli for each participants
res$num_sequence <- c(1:123)

#Remove the practice else it stimlist is not same for all rows
res <- res[which(res$type != "practice"), ]

#Add a column for reaction time (sum of all questions rts)
dfrt <- aggregate(res$quest_rt, by=list(subj=res$subj), FUN=sum)
dfrt$totalrt <- dfrt$x/1000/60
dfrt <- do.call("rbind", replicate(120, dfrt, simplify = FALSE))

dfrt <- dfrt[order(dfrt$subj), ]
totalrt <- as.list(dfrt$totalrt)

res <- data.frame(res, do.call(rbind, totalrt))
res <- rename(res, c("do.call.rbind..totalrt." = "totalrt"))

##We split the stimulus full-name to create new cols
#First a regex to get the filename
res$stimulus <- sub(".*(Audio_Expe_verif_methodo2\\/|Audio\\/Practices\\/.+\\/)(.*)\\.mp3.*", "\\2", res$question)

#Get time speaker passed expe in a normal format
res$date_ok <- as.POSIXct(as.integer(sub("(.*)_.*", "\\1",
                                  as.character(res$subj_uid))), origin = "1970-01-01")


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

# #PLOT JUST FOR FUN
library(ggplot2)
#Plot percentage  
library(dplyr)

resplot <- res %>%
  group_by(audio_type, sentence_type, answer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))

plotrespercent <- ggplot(resplot, aes(x = factor(audio_type),
                                      y = perc*100,
                                      fill = factor(answer)))+
  geom_bar(stat="identity") +
  labs(x = "Audiotype", y = "percent", fill = "Answer")

plotrespercent + facet_grid(. ~ sentence_type)

resplotfillers  <- resfillers %>%
  group_by(audio_type, sentence_type, answer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))

plotresfillerspercent <- ggplot(resplotfillers, aes(x = factor(audio_type),
                                      y = perc*100,
                                      fill = factor(answer)))+
  geom_bar(stat="identity") +
  labs(x = "Audiotype", y = "percent", fill = "Answer")

plotresfillerspercent + facet_grid(. ~ sentence_type)

##Writing the table into a csv file
write.csv(res, file = f_output)
write.csv(resfillers, file = f_output_fillers)


##TEST AREA
resyn <- res[which(res$sentence_type == "yn"), ]
resynde <- resyn[which(resyn$audio_type == "DE"), ]

resynde <- droplevels(resynde)

resplotynde <- resplotynde %>%
  group_by(item, answer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))

plotreynde <- ggplot(resplotynde, aes(x = factor(item),
                                      y = perc*100,
                                      fill = factor(answer)))+
  geom_bar(stat="identity") +
  labs(x = "item", y = "percent", fill = "Answer")

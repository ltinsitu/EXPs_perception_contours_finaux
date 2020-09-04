#Libraries
library(lme4)
library (effects)
library(ggplot2)
library(dplyr)

#Open table
resmbrola <- read.csv("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Results_methodo3_mbrola.csv", header = TRUE)
resdelex <- read.csv("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Results_methodo3_delex.csv", header = TRUE)
# resdelex <- read.csv("/home/lucas/delex.csv", header = TRUE)
resfillersmbrola <- read.csv("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Results_methodo3_MBROLA_fillers.csv", header = TRUE)
resfillersdelex  <- read.csv("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_3/Results_methodo3_DELEX_fillers.csv", header = TRUE)



#Everything as factor
resmbrola <- droplevels(resmbrola)
resmbrola[sapply(resmbrola, is.character)] <- lapply(resmbrola[sapply(resmbrola, is.character)], as.factor)

resdelex <- droplevels(resdelex)
resdelex[sapply(resdelex, is.character)] <- lapply(resdelex[sapply(resdelex, is.character)], as.factor)


#Models mbrola
#Contrasts
contrasts(resmbrola$sentence_type) <- cbind(c(-1,1))
contrasts(resmbrola$audio_type) <- cbind(c(-1,1))
contrasts(resmbrola$task_q_type) <- cbind(c(-1,1))
contrasts(resmbrola$spk_sex) <- cbind(c(-1,1))

#Model on whole data, analyzing experimental H
m.resmbrola <- glmer(data = resmbrola, rightanswer ~ task_q_type + sentence_type + audio_type +
                 (1| item2) + (1| subj), family = binomial)
summary(m.resmbrola)
plot(allEffects(m.resmbrola))

#Models delex
#Contrasts
contrasts(resdelex$sentence_type) <- cbind(c(-1,1))
contrasts(resdelex$spk_sex) <- cbind(c(-1,1))

#Model on whole data, analyzing experimental H
m.resdelex <- glmer(data = resdelex, rightanswer ~ task_q_type * sentence_type +
                       (1| item2) + (1| subj), family = binomial)
summary(m.resdelex)
plot(allEffects(m.resdelex))


#Plot percentage MBROLA 
resmbrolaplot <- resmbrola %>%
  group_by(task_q_type, audio_type, sentence_type, rightanswer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))


plotresmbrolapercent <- ggplot(resmbrolaplot, aes(x = factor(sentence_type),
                                      y = perc*100,
                                      fill = factor(rightanswer)))+
  geom_bar(stat="identity") +
  labs(x = "Audiotype", y = "percent", fill = "Right Answer")

plotresmbrolapercent + facet_grid(. ~ audio_type + task_q_type)

plotresmbrolaitem <- ggplot(resmbrolaplot, aes(x = factor(item2),
                                             y = perc*100,
                                             fill = factor(rightanswer)))+
  geom_bar(stat="identity") +
  labs(x = "item num", y = "percent", fill = "Right Answer")

plotresmbrolaitem + facet_grid(rows = resmbrolaplot$task_q_type)

#Plot percentage DELEX 
resdelexplot <- resdelex %>%
  group_by(task_q_type, sentence_type, rightanswer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))

plotresdelexpercent <- ggplot(resdelexplot, aes(x = factor(sentence_type),
                                                  y = perc*100,
                                                  fill = factor(rightanswer)))+
  geom_bar(stat="identity") +
  labs(x = "sentence type", y = "percent", fill = "Right Answer")

plotresdelexpercent + facet_grid(. ~ task_q_type)

resdelexplotitems <- resdelex %>%
  group_by(item2, task_q_type, sentence_type, rightanswer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))

plotresdelexitem <- ggplot(resdelexplotitems, aes(x = factor(item2),
                                             y = perc*100,
                                             fill = factor(rightanswer)))+
  geom_bar(stat="identity") +
  labs(x = "item num", y = "percent", fill = "Right Answer")

plotresdelexitem + facet_grid(. ~ task_q_type)


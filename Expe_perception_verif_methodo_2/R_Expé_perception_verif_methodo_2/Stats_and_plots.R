#Open table
res <- read.csv("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Results_methodo2.csv", header = TRUE)

#Models
library(lme4)
library (effects)

#Contrasts
contrasts(res$sentence_type) <- cbind(c(-.5,.5))
contrasts(res$audio_type) <- cbind(c(-.5,.5))

#Model on whole data, analyzing experimental H
m.res <- glmer(data = res, answer ~ sentence_type * audio_type +
                 (1| item) + (1| subj), family = binomial )
summary(m.res)
plot(allEffects(m.res))

#Model taking pitch value into account
m.res.pitch <- glmer(data = res, answer ~ diffmeanst  + (1| item) +
                       (1| subj), family = binomial)
summary(m.res.pitch)
plot(allEffects(m.res.pitch))

#Same model as before only on yn data
resyn <- res[which(res$sentence_type == "yn"), ]
resyn <- droplevels(resyn)

m.res.yn.pitch <- glmer(data = resyn, answer ~ diffmeanst + (1| item) +
                          (1| subj), family = binomial)
summary(m.res.yn.pitch)
plot(allEffects(m.res.yn.pitch))







#Other plots
library(ggplot2)
library(dplyr)

#Scatterplot answer vs slope
scatterres <- res %>%
  group_by(orig_filename, diffmeanst, answer) %>%
  summarise(count=n()) %>%
  mutate(perc=count/sum(count))


plotscatterres <- ggplot(scatterres, aes(x = diffmeanst,
                                      y = perc*100,
                                      fill = factor(answer)))+
  geom_bar(stat="identity") +
  labs(x = "Audiotype", y = "percent", fill = "Right Answer")


scatterresyes <- scatterres[which(scatterres$answer == "Oui"), ]
plot(scatterresyes$perc ~ scatterresyes$diffmeanst)

abline(lm(scatterresyes$perc  ~ scatterresyes$diffmeanst), col="red") # regression line (y~x) 

#Only on yn data
resyn <- res[which(res$sentence_type == "yn"), ]
resyn <- droplevels(resyn)

scatterresyn <- resyn %>%
  group_by(orig_filename, diffmeanHz, answer) %>%
  summarise(count=n()) %>%
  mutate(perc=count/sum(count))

scatteresyesyn <- scatterresyn[which(scatterresyn$answer == "Oui"), ]

plot(scatteresyesyn$perc*100 ~ scatteresyesyn$diffmeanHz)
abline(lm(scatteresyesyn$perc*100  ~ scatteresyesyn$diffmeanHz), col="red") # regression line (y~x) 

#Only V0 yn data
scatterv0  <- resyn %>%
  group_by(orig_filename, pitchstv0mean, answer) %>%
  summarise(count=n()) %>%
  mutate(perc=count/sum(count))

scatterv0 <- scatterv0[which(scatterv0$answer == "Oui"), ]

plot(scatterv0$perc*100 ~ scatterv0$pitchstv0mean)
abline(lm(scatterv0$perc*100  ~ scatterv0$pitchstv0mean), col="red") # regression line (y~x) 

#Plot percentage  
resplot <- res %>%
  group_by(audio_type, sentence_type, rightanswer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))

plotrespercent <- ggplot(resplot, aes(x = factor(audio_type),
                                      y = perc*100,
                                      fill = factor(rightanswer)))+
  geom_bar(stat="identity") +
  labs(x = "Audiotype", y = "percent", fill = "Right Answer")

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

##TEST AREA

#YNDE
resyn <- res[which(res$sentence_type == "yn"), ]
resynde <- resyn[which(resyn$audio_type == "DE"), ]

resynde <- droplevels(resynde)

resplotynde <- resynde %>%
  group_by(item, answer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))

plotreynde <- ggplot(resplotynde, aes(x = factor(item),
                                      y = perc*100,
                                      fill = factor(answer)))+
  geom_bar(stat="identity") +
  labs(x = "item", y = "percent", fill = "Answer")

#YNORIG
resynorig <- resyn[which(resyn$audio_type == "OR"), ]
resynorig <- droplevels(resynorig)

resplotynorig <- resynorig %>%
  group_by(item, answer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))

plotynorig <- ggplot(resplotynorig, aes(x = factor(item),
                                        y = perc*100,
                                        fill = factor(answer)))+
  geom_bar(stat="identity") +
  labs(x = "item", y = "percent", fill = "Answer")

#YNCLAIR
resyncl <- resyn[which(resyn$audio_type == "CL"), ]
resyncl <- droplevels(resyncl)

resplotyncl <- resyncl %>%
  group_by(item, answer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))

plotyncl <- ggplot(resplotyncl, aes(x = factor(item),
                                    y = perc*100,
                                    fill = factor(answer)))+
  geom_bar(stat="identity") +
  labs(x = "item", y = "percent", fill = "Answer")

#ALLYN
resplotyn <- resyn  %>%
  group_by(item, audio_type, answer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))

plotyn <- ggplot(resplotyn, aes(x = factor(audio_type),
                                y = perc*100,
                                fill = factor(answer)))+
  geom_bar(stat="identity") +
  labs(x = "item", y = "percent", fill = "Answer")

plotyn + facet_grid(. ~ item)
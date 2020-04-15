#Open table
res <- read.csv("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Results_methodo2.csv", header = TRUE)

#Libraries
library(lme4)
library (effects)
library(ggplot2)
library(dplyr)

#Models
#Contrasts
contrasts(res$sentence_type) <- cbind(c(-.5,.5))
contrasts(res$audio_type) <- contr.sum(3)

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

#Same model solo on yn delexicalised data
resynde <- resyn[which(resyn$audio_type == "DE"), ]
resynde <- droplevels(resynde)

m.res.ynde.pitch <- glmer(data = resynde, answer ~ diffmeanst + (1| subj) +
                            (1| item),
                          family = binomial)
summary(m.res.ynde.pitch)
plot(allEffects(m.res.ynde.pitch))

m2.res.ynde.pitch <- glmer(data = resynde, answer ~ diffmeanst + (1| subj),
                          family = binomial)
summary(m2.res.ynde.pitch)
plot(allEffects(m2.res.ynde.pitch))

#Other plots


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
  group_by(orig_filename, diffmeanst, answer) %>%
  summarise(count=n()) %>%
  mutate(perc=count/sum(count))

scatteresyesyn <- scatterresyn[which(scatterresyn$answer == "Oui"), ]

plot(scatteresyesyn$perc*100 ~ scatteresyesyn$diffmeanst)
abline(lm(scatteresyesyn$perc*100  ~ scatteresyesyn$diffmeanst), col="red") # regression line (y~x) 

#Only on ynde data
resynde <- resyn[which(resyn$audio_type == "DE"), ]
resynde <- droplevels(resynde)

scatterresynde <- resynde %>%
  group_by(orig_filename, diffmeanst, answer) %>%
  summarise(count=n()) %>%
  mutate(perc=count/sum(count))

scatteresyesynde <- scatterresynde[which(scatterresynde$answer == "Oui"), ]

plot(scatteresyesynde$perc*100 ~ scatteresyesynde$diffmeanst)
abline(lm(scatteresyesynde$perc*100  ~ scatteresyesynde$diffmeanst), col="red") # regression line (y~x) 

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


#TEST BARITEMS
resyn %>%  
  mutate(answer = factor(answer)) %>% 
  ggplot(aes(x = item)) +
  geom_bar(aes(fill = answer), position = "fill") +
  scale_x_continuous("Items", breaks = resyn$item, labels = resyn$item) +
  ggtitle("Answers for yn items") -> plotitemsresyn

plotitemsresyn

resynde <- resyn[which(resyn$audio_type == "DE"), ]
resynde <- droplevels(resynde)

resynde %>%  
  mutate(answer = factor(answer)) %>% 
  ggplot(aes(x = item)) +
  geom_bar(aes(fill = answer), position = "fill") +
  scale_x_continuous("Items", breaks = resynde$item, labels = resynde$item) +
  ggtitle("Answers for ynde items") -> plotitemsresynde

plotitemsresynde

resynor <- resyn[which(resyn$audio_type == "OR"), ]
resynor <- droplevels(resynor)

resynor %>%  
  mutate(answer = factor(answer)) %>% 
  ggplot(aes(x = item)) +
  geom_bar(aes(fill = answer), position = "fill") +
  scale_x_continuous("Items", breaks = resynor$item, labels = resynor$item) +
  ggtitle("Answers for ynOR items") -> plotitemsresynor

plotitemsresynor

#ONLY GENUINE YN WITH NO PITCH PROBLEMS
#all
resyn <- res[which(res$sentence_type == "yn"), ]
resynok <- resyn[which(resyn$yntype == "genuine"), ]
resynok <- resynok[which(resynok$problempitch == "NO"), ]
resynok <- droplevels(resynok)

resynok %>%  
  mutate(answer = factor(answer)) %>% 
  ggplot(aes(x = item)) +
  geom_bar(aes(fill = answer), position = "fill") +
  scale_x_continuous("Items", breaks = resynok$item,
                     labels = resynok$item) +
  ggtitle("Answers for resynOK items") -> plotitemsresynok

plotitemsresynok

#orig
resynokorig <- resynok[which(resynok$audio_type == "OR"), ]
resynokorig <- droplevels(resynokorig)

resynokorig %>%  
  mutate(answer = factor(answer)) %>% 
  ggplot(aes(x = item)) +
  geom_bar(aes(fill = answer), position = "fill") +
  scale_x_continuous("Items", breaks = resynokorig$item,
                     labels = resynokorig$item) +
  ggtitle("Answers by items for genuine yn, ORIG audio") -> plotitemsresynokorig

plotitemsresynokorig

#de
resynokde <- resynok[which(resynok$audio_type == "DE"), ]
resynokde <- droplevels(resynokde)

resynokde %>%  
  mutate(answer = factor(answer)) %>% 
  ggplot(aes(x = item)) +
  geom_bar(aes(fill = answer), position = "fill") +
  scale_x_continuous("Items", breaks = resynokde$item,
                     labels = resynokde$item) +
  ggtitle("Answers by items for genuine yn, DELEX audio") -> plotitemsresynokde

plotitemsresynokde

#Stats on only resynOK
#All yn
m.res.pitch.ynok <- glmer(data = resynok, answer ~ diffmeanst  + (1| item) +
                       (1| subj), family = binomial)
summary(m.res.pitch.ynok)
plot(allEffects(m.res.pitch.ynok))

#Only delex
m.res.pitch.ynokde <- glmer(data = resynokde, answer ~ diffmeanst  +
                            (1| subj), family = binomial)
summary(m.res.pitch.ynokde)
plot(allEffects(m.res.pitch.ynokde))

#Scatterplot only delex
scatterresynokde <- resynokde %>%
  group_by(orig_filename, diffmeanst, answer) %>%
  summarise(count=n()) %>%
  mutate(perc=count/sum(count))


scatterresynokdeyes <- scatterresynokde[which(scatterresynokde$answer == "Oui"), ]
plot(scatterresynokdeyes$perc ~ scatterresynokdeyes$diffmeanst)

abline(lm(scatterresynokdeyes$perc  ~ scatterresynokdeyes$diffmeanst), col="red") # regression line (y~x) 



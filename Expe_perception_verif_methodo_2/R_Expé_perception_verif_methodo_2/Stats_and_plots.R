#Open table
res <- read.csv("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Results_methodo2.csv", header = TRUE)
resfillers <- read.csv("/home/lucas/Documents/CloudStation/SDL/PhD/Prosodie/Expés_Prosodie/EXPs_perception_contours_finaux/Expe_perception_verif_methodo_2/Results_methodo2_fillers.csv", header = TRUE)


#Everything as factor
res <- droplevels(res)
res[sapply(res, is.character)] <- lapply(res[sapply(res, is.character)], as.factor)


#Libraries
library(lme4)
library (effects)
library(ggplot2)
library(dplyr)

#Models
#Contrasts
contrasts(res$sentence_type) <- cbind(c(-1,1))
contrasts(res$audio_type) <- contr.sum(3)
contrasts(res$spk_sex) <- cbind(c(-1,1))

#Model on whole data, analyzing experimental H
m.res <- glmer(data = res, rightanswer ~ sentence_type * audio_type + spk_sex+
                 (1| item) + (1| subj), family = binomial)
summary(m.res)
plot(allEffects(m.res))


#Model taking pitch value into account
m.res.pitch <- glmer(data = res, answer ~ diffmeanst  
                     + (1| item) +
                       (1| subj), family = binomial)
summary(m.res.pitch)
plot(allEffects(m.res.pitch))

#Same model as before only on yn data
resyn <- res[which(res$sentence_type == "yn"), ]
resyn <- droplevels(resyn)

contrasts(resyn$answer)
contrasts(resyn$sentence_type) <- cbind(c(-1,1))
contrasts(resyn$audio_type) <- contr.sum(3)

m.res.yn.pitch <- glmer(data = resyn, answer ~ diffmeanst 
                        + (1| item) +
                          (1| subj), family = binomial)
summary(m.res.yn.pitch)
plot(allEffects(m.res.yn.pitch))


m.res.yn.pitch.inter <- glmer(data = resyn, answer ~ 
                              diffmeanst  * audio_type
                        + (1| item) +
                          (1| subj), family = binomial)

summary(m.res.yn.pitch.inter)
plot(allEffects(m.res.yn.pitch.inter))

#Diffmeanst decla
resdecla <- res[which(res$sentence_type == "de"), ]
resdecla <- droplevels(resdecla)

mean(resyn$diffmeanst)
mean(resdecla$diffmeanst)

contrasts(resdecla$rightanswer) 
contrasts(resdecla$sentence_type) <- cbind(c(-1,1))
contrasts(resdecla$audio_type) <- contr.sum(3)

m.res.decla.pitch.inter <- glmer(data = resdecla, rightanswer ~ 
                                diffmeanst  * audio_type
                              + (1| item) +
                                (1| subj), family = binomial)
summary(m.res.decla.pitch.inter)
plot(allEffects(m.res.decla.pitch.inter))

#Same model solo on yn delexicalised data
resynde <- resyn[which(resyn$audio_type == "DE"), ]
resynde <- droplevels(resynde)

m.res.ynde.pitch <- glmer(data = resynde, answer ~ diffmeanst
                          + (1| subj) +
                            (1| item),
                          family = binomial)
summary(m.res.ynde.pitch)
plot(allEffects(m.res.ynde.pitch))

m2.res.ynde.pitch <- glmer(data = resynde, answer ~ diffmeanst + (1| subj),
                          family = binomial)
summary(m2.res.ynde.pitch)
plot(allEffects(m2.res.ynde.pitch))

#Only on orig
m.res.ynorig.pitch <- glmer(data = resynorig, answer ~ diffmeanst
                            + (1| subj) +
                              (1| item),
                            family = binomial)
summary(m.res.ynorig.pitch)
plot(allEffects(m.res.ynorig.pitch))

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

#Inverted plot
plot(scatteresyesyn$diffmeanst ~ scatteresyesyn$perc)
abline(lm(scatteresyesyn$diffmeanst ~ scatteresyesyn$perc), col="red") # regression line (y~x) 

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

plotyn <- ggplot(resplotyn, aes(x = factor(item),
                                y = perc*100,
                                fill = factor(answer)))+
  geom_bar(stat="identity") +
  #Find a way to make x labels readable
  #scale_x_discrete(limits=resyn$item,breaks=resyn$item[seq(1,length(resyn$item),by=2)]) +
  labs(x = "item", y = "percent", fill = "Answer")

plotyn + facet_grid(rows =  resplotyn$audio_type)

#ALL items including yn and decla
resplot2 <- res  %>%
  group_by(item, sentence_type, audio_type, rightanswer) %>% 
  summarise(count=n()) %>% 
  mutate(perc=count/sum(count))


plotallitems <- ggplot(resplot2, aes(x = factor(item),
                                y = perc*100,
                                fill = factor(rightanswer)))+
  geom_bar(stat="identity") +
  #Find a way to make x labels readable
  #scale_x_discrete(limits=resyn$item,breaks=resyn$item[seq(1,length(resyn$item),by=2)]) +
  labs(x = "item", y = "percent", fill = "Right Answer")

plotallitems + facet_grid(rows =  resplot2$audio_type)



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

plotitemsresynok + facet_grid(resynok$audio_type)

#lineplot
resynok %>%  
  mutate(answer = factor(answer)) %>% 
  ggplot(aes(x = item)) +
  geom_line(aes(fill = answer, y = audio_type), position = "fill") +
  scale_x_continuous("Items", breaks = resynok$item,
                     labels = resynok$item) +
  ggtitle("Answers for resynOK items") -> plotitemsresynok

resynok %>%  
  mutate(answer = factor(answer)) %>% 
  ggplot(aes(x=item, y=answer, group=audio_type)) +
  geom_line(aes(linetype=audio_type))+
  geom_point() 

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

#stats resynokde
contrasts

#cl
resynokcl <- resynok[which(resynok$audio_type == "CL"), ]
resynokcl <- droplevels(resynokcl)

resynokcl %>%  
  mutate(answer = factor(answer)) %>% 
  ggplot(aes(x = item)) +
  geom_bar(aes(fill = answer), position = "fill") +
  scale_x_continuous("Items", breaks = resynokcl$item,
                     labels = resynokcl$item) +
  ggtitle("Answers by items for genuine yn, CLAIR audio") -> plotitemsresynokcl

plotitemsresynokcl

#Stats on only resynOK
#All yn
m.res.pitch.ynok <- glmer(data = resynok, answer ~ diffmeanst  + (1| item) +
                       (1| subj), family = binomial)
summary(m.res.pitch.ynok)
plot(allEffects(m.res.pitch.ynok))

#Only delex
m.res.pitch.ynokde <- glmer(data = resynokde, answer ~ diffmeanst  +
                            (1| subj) + (1| item), family = binomial)
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

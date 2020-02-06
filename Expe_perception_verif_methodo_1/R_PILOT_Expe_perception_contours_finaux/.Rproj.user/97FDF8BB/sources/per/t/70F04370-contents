##Load libraries
library(ggplot2)
library(lmerTest)
library(lme4)

##Plotting the results
#Yes-no and declaratives
plotqd <- ggplot(resqd, aes(audio_type, ..count..)) + geom_bar(aes(fill = answer))
plotqd + facet_grid(. ~ sentence_type)

#Wh-in-situ
plotwi <- ggplot(reswi, aes(audio_type, ..count..)) + geom_bar(aes(fill = answer))
plotwi

###Models
##Yes-no and declaratives
#Coding the contrasts (deviation coding)
contrasts(resqd$sentence_type) <- cbind(c(-.5,.5))
contrasts(resqd$audio_type) <- cbind(c(-.5,.5))

m.qd.0 <- glmer(data = resqd, answer ~ sentence_type * audio_type + (1| item) + (1| subj), family = binomial )
summary(m.qd.0)

##Wh-in-situ
contrasts(reswi$audio_type) <- cbind(c(-.5,.5))

#With 8 participants, I obtain a singular fit. If I remove random intercepts for subj it's gone. Including random slopes for audio_type doesn't help.
m.wi.0 <- glmer(data = reswi, answer ~ audio_type + (1| item) + (1| subj), family = binomial )
summary(m.wi.0)

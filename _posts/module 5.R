setwd("C:/Users/quinn/OneDrive - Tilburg University/Documenten/Universiteit/Master/Blok 3/Complex Systems/Assignment")
dat <-read.csv("Actigraph.csv")
dat$time1 <- 1:length(dat$time)
dat <- dat %>% slice(1:42553) #42553

library(Hmisc)
library(grid)
library(ggplot2)
library(dplyr)
library(doremi)
library(tseriesChaos)
library(phaseR)


plot(dat$HR, type='l', xlab="Time in seconds", ylab = 'Heartrate')

#making HR change vector
dat$HR_lag1 <- Lag(dat$HR,1)
dat$HR_lead1 <- Lag(dat$HR,-1)
dat$HR_change <- (dat$HR_lead1 - dat$HR_lag1)/2

plot(dat$HR_change,type='l', xlab = "Time in seconds", ylab =" Change in heartrate")

#plotting vector field with HR_change
ggplot(data=dat,aes(x=time,y=HR))+
  geom_segment(aes(xend=time,yend=HR+HR_change),arrow=arrow(length=unit(.05,"cm")))+
  stat_density2d(aes(colour=..level..))+


plot(dat$HR,dat$HR_change, xlab='Heartrate', ylab='Change in heartrate', main= "Heart rate monitoring")
abline(a=0,b=0,lty=2,col=2)

#Differentiating through the GOLD method
gold_vec<-doremi::calculate.gold(dat$HR, time= dat$time1,embedding=7,n=2)
print(goldvec$dsignal)

#Using the GOLD vector in linear regression 
mod1 <- lm(HR_change~poly(HR,3), data=dat)
summary(mod1)

mod2 <- lm(gold_vec$dsignal[1:42547,2]~poly(gold_vec$dsignal[1:42547,2],3), data=dat)
summary(mod2)


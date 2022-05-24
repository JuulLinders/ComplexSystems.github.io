##This file contains the code for module 4. It first plots the data, then installs
##the required functions. After that the tests are run and necessary codes are run.

##Plotting the data
plot(data$HR, type = "l", xlab = "Time", ylab = "Heartrate", main = "Plot Heartrate")

##Installing the functions
install.packages("tseries")
install.packages("ecp")
install.packages("nonlinearTseries")
install.packages("randtests")
install.packages("Rcpp")
library(mgcv)
library(tseries)
library(ecp)
library(nonlinearTseries)
library(randtests)

##1. Bartels.rank test
bartels.rank.test(data$HR, alternative = "two.sided")

Plotpacf <- pacf(na.exclude(data$HR),lag.max = 1000)
plot(Plotpacf, main = "Plot partial ACF")

##2. KPSS test
kpss.test(na.exclude(data$HR), lshort=TRUE, 
          null="Level")

##3. Change point analysis
ts <- matrix(na.exclude(data2$HR))
print(ts)
# Increase R for more permutations and run time 
e.out <- ecp::e.divisive(ts, R=5, sig.lvl=.002) 
df.e <- length(which(e.out$p.values<.002))
e.out$estimates


##4. Variance for change point analysis
variance = c()
interval = 1000

for (i in 1:length(data$HR - interval)){
  variance[i] <- var(data$HR[i:(i+interval)])
}

variance


variance2 = c()
interval2 = 5000
for (i in 1:length(data$HR - interval2)){
  variance2[i] <- var(data$HR[i:(i+interval2)])
}

variance2

plot(c(1:length(variance2)), variance2, type = 'l', ylab = "Variance", xlab = "time", main = "Variance over fixed interval 5000") 

##5. Comparing shifts with activities at particular time
frame <- data.frame(data$HR, data$X, data$time)
View(frame)


##This file contains the code for module 10. It first installs
##the required functions. The data is plotted and after that the analyses are performed.


##1. Loading the packages

knitr::opts_chunk$set(echo = TRUE)
# Load packages
require(nonlinearTseries)
require(MFDFA)
install.packages("DFA")
source("~/OneDrive/Tilburg/ifultools/R/it_util.R")

data <- read.csv("~/Downloads/Actigraph.csv")
HR <- data$HR
time <- data$time

##1. Need to mean center?
plot(data$HR, type = "l", xlab = "Time", ylab = "Heartrate", main = "Plot Heartrate")
##yes:
data <- as.numeric(scale(data$HR, center = TRUE, scale = FALSE))
plot(datacentered, type= "l")

##2. DFA analysis
set.seed(23)
data = rnorm(5000)
scale.min = 16
scale.max = length(data)/4
scale.num = length(logScale(scale.min = scale.min, 
                      scale.max = scale.max,
                      scale.ratio = 1.25))
print(scale.num)
dfa.analysis = dfa(time.series = data, npoints = scale.num, window.size.range = c(scale.min, scale.max), do.plot = FALSE)
data.estimation = estimate(dfa.analysis, do.plot=TRUE)

##The results do not point to multifractality, yet to show how it should be performed
##the analyses for a multifractal DFA are run below. 

###3. multifractal DFA analysis 
scale <- logScale(scale.min = scale.min, scale.max = scale.max, scale.ratio = 2)
q <- -10:10 # range of q order exponents
m <- 1 # detrending order 
mfdfa.out <- MFDFA(data, scale = scale, q = q, m = 1)
plot(mfdfa.out$spec$hq, mfdfa.out$spec.Dq, type = "b", pch = 19,
     xlab ="h(q)", ylab = 'D(h)', main = "multifractal singularity spectrum")
lines(mfdfa.out$spec$hq, mfdfa.out$spec$Dq, type = "b", col = "red")


## The results. This plot confirms that there are no signs of multifractality.
matplot(mfdfa.out$line, type='l', pch=19, add=FALSE, xlab="log Scale", ylab="log Fq", main = "Monofractal")


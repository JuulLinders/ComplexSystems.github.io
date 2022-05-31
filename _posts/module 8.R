data <-read.csv("Actigraph.csv")

#install.packages('rEDM)
library(rEDM)
library(dplyr)
library(ggplot2)
library(lubridate)
library(chron)
library(tseriesChaos)
library(nonlinearTseries)
df <- data %>% select('time', 'HR')
df1 <- df %>% slice(37414:46450)   #40329 is one day, 11:00 37414, 10:00 34489 -, 01:00 46150

second(df1$time)

plot(df1$HR, type = "l", xlab = "Time", ylab = "Heartrate", main = "Heartrate timeseries")

plot1 <- ggplot(data=df1, aes(x=time, y=HR, group =1), xaxp = c(0,1000,5)) + geom_line(color="black") + xlab("Time") + ylab("Heartrate") + ggtitle("Heartrate timeseries")
plot1


df1$time <- 1:length(df1$time)
df1$HR <- as.numeric(scale(df1$HR))
lib_point <- c(1,floor(max(length(df1$HR))/2))
pred_point <- c(floor(max(length(df1$HR))/2)+1,max(length(df1$HR)))
rho_emd_HR <- EmbedDimension(dataFrame = df1, lib = lib_point, pred = pred_point, maxE = 9, tau = -1, columns='HR', target ='HR', numThreads = 8) #--> best dimensions is 4



###simplex projection
simplex_out <- Simplex(dataFrame = df1, lib = lib_point, pred = pred_point, E=8, tau = -1, 
                       columns='HR', target ='HR') 

plot(simplex_out$Observations,type='l', xlab = "Time", ylab="Value", main = "HR Simplex Projection")
lines(simplex_out$Predictions,type='l',col="blue")

simplex_out$Observations
simplex_out$Predictions

## FNN and Cao's method
fnn.out = false.nearest(df1$HR, m = 15, t = 50, d = 1, eps = sd(df1$HR)/10)
plot(fnn.out)

emb.dim = estimateEmbeddingDim(df1$HR, time.lag = 1, max.embedding.dim = 12) #<- best is 4

###simplex projection #2
sim <- simplex(df1$HR,lib=lib_point,pred=pred_point,E=c(2:8),tau = -1)
sim$rho # --> best dimension is 4


###smap
smap <- s_map(df1,E=4,lib= lib_point,pred= pred_point,theta=seq(0,2,0.1))

theta_max <- smap[which.max(smap$rho),"theta"][1]
theta_max # --> 0.9

#determine nonlinearity
rho_theta<- PredictNonlinear(dataFrame = df1, lib = lib_point, pred = pred_point, E=4, columns='HR', target ='HR')
rho_theta$rho
### compute error
ComputeError(simplex_out$Observations, simplex_out$Predictions)

#----------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------#
df2 <- data %>% select('time', 'HR', 'Vector.Magnitude')
df2$time <- 1:length(df2$time)
df2 <- df2 %>% slice(37414:46450)


### convergent cross mapping
require(Kendall)
require(tidyverse)
require(broom)

xcor_out <- ccf(df2$HR,df2$Vector.Magnitude,lag.max=6,type="correlation",plot = FALSE)$acf

cmap <- CCM(dataFrame = df2, E = 4, Tp = 0, columns = "Vector.Magnitude", target = "HR", libSizes = "10 4000 100", sample = 100, showPlot = TRUE ) 

cmap$`Vector.Magnitude:HR`
abline(h = max(abs(xcor_out)), col="black",lty=2)

##Testing for causal directionality
knitr::kable(tidy(Kendall::MannKendall(cmap$`HR:Vector.Magnitude`)))
knitr::kable(tidy(Kendall::MannKendall(cmap$`Vector.Magnitude:HR`)))

#determining optimal lag value
tau1 <- timeLag(df$HR, technique = "ami", lag.max = 100, do.plot = T)

smap_uni <- SMap(dataFrame = df2, lib = lib_point, pred = pred_point, Tp = 240, E=4, tau = tau1,columns='HR', target ='HR', embedded = FALSE, theta=0)
univariate_stats <- compute_stats(smap_uni$predictions$Observations,smap_uni$predictions$Predictions)
univariate_stats
?SMap()

  
plot(smap_uni$predictions$Observations,type='l', xlab = "Time", ylab="Value", main = "HR Simplex Projection")
lines(smap_uni$Predictions$Predictions,type='l',col="red", lwd = 5)

smap_multi <- block_lnlp(block = df2, method= "s-map", lib = lib_point, pred = pred_point, columns= c("HR", "Vector.Magnitude"), first_column_time = TRUE, stats_only = FALSE, theta=0, save_smap_coefficients = TRUE)


# Extract our metrics
multivariate_rho <- smap_multi$stats$rho[1]
smap_multi$stats$rho[1]
smap_multi$stats$mae[1]
smap_multi$stats$rmse[1]


mv_out <- Multiview(dataFrame = df2, lib= lib_point, pred = pred_point, E=4, target= "HR", columns = "HR Vector.Magnitude")
multiview_stats <- compute_stats(mv_out$Predictions$Observations,mv_out$Predictions$Predictions)
multiview_stats

library(mgcv)
library(tseries)
library(ecp)
library(nonlinearTseries)
library(randtests)
library(ggplot)
library(lubridate)
library(tseriesChaos)
library(plot3D)
library(scatterplot3d)





RR <- read.csv("Actigraph.csv")

HR <- RR$HR


#======== Determining Lag =========================================
tau.acp <- timeLag(HR, technique = "acf", lag.max = (15000), do.plot = T)
tau.acp <- timeLag(HR, technique = "ami", lag.max = (15000), do.plot = T)

#delay = either 10000 or 3500

#======== Determining M =========================================
#false nearest neighbour method delay = 3500
fnn.out = false.nearest(HR, m = 15, t = 50, d = 3500, eps = sd(HR)/10)
plot(fnn.out)

#7 dimensions

#Cao's method (1997)
emb.dim = estimateEmbeddingDim(HR, time.lag = 3500, max.embedding.dim = 15)

#7/8 dimensions

#======== Phase space reconstruction and plot ======================
HR.takens <- buildTakens(HR, 7, 3500)
head(HR.takens)


#2d plot
plot(HR.takens[,2], HR.takens[,1], type='l')

#plotting subset to visualize time component
lines3D(HR.takens[,1], HR.takens[,2], HR.takens[,3], t= "l", col = jet.col(10), asp = 1 )
lines3D(HR.takens[,1][1:10000], HR.takens[,2][1:10000], HR.takens[,3][1:10000], t= "l", col = jet.col(10), asp = 1 )
lines3D(HR.takens[,1][10000:20000], HR.takens[,2][10000:20000], HR.takens[,3][10000:20000], t= "l", col = jet.col(10), asp = 1 )
lines3D(HR.takens[,1][20000:30000], HR.takens[,2][20000:30000], HR.takens[,3][20000:30000], t= "l", col = jet.col(10), asp = 1 )
lines3D(HR.takens[,1][30000:40000], HR.takens[,2][30000:40000], HR.takens[,3][30000:40000], t= "l", col = jet.col(10), asp = 1 )









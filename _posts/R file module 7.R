library(nonlinearTseries)
library(crqa)

        
data <- read.csv("Actigraph.csv")
HR <- data$HR

#subset 1
rqa <-crqa(ts1 = HR[1:30000], ts2 = HR[1:30000], delay = 3500, embed = 7, rescale = 0, radius = 20 , method = "rqa", datatype = 'continuous')
rqa <- rqa(time.series = HR[1:60000], time.lag = 3500, embedding.dim = 7, radius = 20, distanceToBorder = 2, do.plot = TRUE)


#subset 2
rqa <-crqa(ts1 = HR[30000:60000], ts2 = HR[30000:60000], delay = 3500, embed = 7, rescale = 0, radius = 20 , method = "rqa", datatype = 'continuous')
rqa <- rqa(time.series = HR[30000:60000], time.lag = 3500, embedding.dim = 7, radius = 20, distanceToBorder = 2, do.plot = TRUE)



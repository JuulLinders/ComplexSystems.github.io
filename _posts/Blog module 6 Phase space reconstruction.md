## Blog Module 6 Phase-Space Reconstruction

In the previous module we learned about attractor dynamics and how we can apply
different techniques to visualize these dynamics. In this module we will learn about phase space reconstruction. The main goal of this module is to construct a multi-dimensional system from a single dimensional time series. Similarly to the other modules, we will use the heart rate time series to guide the reader through the techniques that are used in order to create this multi-dimensional system. The heart rate time series is depicted below. 

``` 
data <- read.csv("Actigraph.csv")
plot(data$HR, type = "l", xlab = "Time", ylab = "Heartrate", main = "Plot Heartrate")

```

![image](https://user-images.githubusercontent.com/78364132/169965814-fb68c871-22f9-4216-94a0-1758c6778e3e.png)

*Figure 1: heart rate time series*

First, we should think about whether it is useful to apply phase space reconstruction to a heart rate time series. Does it make sense that the single-dimensional time series can be reconstructed as a multi-dimensional system? One could very well imagine heart rate to have more dimensions since the heart rate is part of the system of the human body. Multiple factors can influence heart rate: activity of the human, mental state and even the weather can influence heart rate (Ozheredov et al., 2017). Thus it is valid to apply the phase space reconstruction technique to the heart rate time series. 

This module will consists of three steps: determining the optimal delay, determining the embedding dimensions and visualizing the multi-dimensional system.

### Delay
By determining the appropriate time delay we are able to maximally seperate the trajectories. We can use two methods in order to find this delay: 
- Find the first zero crossing of the autocorrelation function

We might remember this function from module 4 where we used it to confirm that the heart rate time series has memory. For those who did not read module 4 the autocorrelation function defines how data points in a time series are related, on average, to the preceding data points (Box, Jenkins, & Reinsel, 1994)

- Find the first local minimum of the mutual information function

“The average mutual information I(X; Y) is a measure of the amount of “information” that the random variables X and Y provide about one another. Notice from Definition that when X and Y are statistically independent, we have I(X; Y) = 0, which means that X and Y do not provide any information about one another.” (Vadlamudi et al. 2018). We aim to find the delay where our time series and the delayed time series give no information about one another. This is the point that maximally seperates the trajectories.

Note that the two methods often obtain different ”optimal” delays. One should take the size of the time series into account when determining a delay. Choosing a high delay relative to the length of the time series will cause more missing data. However, Grassberger & Schreiber (1991) found that the outcome of the phase space reconstruction is rather robust if the right embedding dimension is chosen.
	
Applying both techniques to the heart rate time series results in the following plots.

```
tau.acp <- timeLag(HR, technique = "acf", lag.max = (15000), do.plot = T)
```
![image](https://user-images.githubusercontent.com/78364132/168767980-45650b13-c4b0-484e-8f21-59c800152c78.png)

*Figure 2: autocorrelation plot*

The first zero crossing of the autocorrelation function would suggest a lag of 10000. Since the length of our time series is approximately 60000 we would be able to use this delay.
```
tau.acp <- timeLag(HR, technique = "ami", lag.max = (15000), do.plot = T)
```
![image](https://user-images.githubusercontent.com/78364132/168768036-ae3d2ca8-8608-4530-aad5-cf9624d58572.png)

*Figure 3: average mutual information plot*

First local minimum of the average mutual information function is found with a delay of approximately 3500. Since 3500 is a rather small lag it will result in little missing data. In future steps this lag will be used.

### Embedding dimensions
Similarly to determining the delay, we will pose two techniques for determining the number of embedding dimensions: False Nearest Neighbors and Cao’s (1997) method.

Using the False Nearest Neighbors method with parameters delay = 3500  m = 15, t = 50, d = 3500, eps = sd(HR)/10) provides us with the following plot.
```
fnn.out = false.nearest(HR, m = 15, t = 50, d = 3500, eps = sd(HR)/10)
plot(fnn.out)
```
![image](https://user-images.githubusercontent.com/78364132/168768653-32353169-857f-4523-b036-3535e2c2b8dc.png)

*Figure 4: false nearest neighbours plot*

Using the elbow rule we determine that 7 is the optimal embedding dimension.
Using Cao's method (1997) we obtain the following plot:
```
emb.dim = estimateEmbeddingDim(HR, time.lag = 3500, max.embedding.dim = 15)
```
![image](https://user-images.githubusercontent.com/78364132/168768869-16d3240c-d61e-4b6d-b62d-2ace23c90e7a.png)

*Figure 5: Cao's method plot*


Similarly to the False Nearest Neighbors method we find that 7 dimensions is appropriate for our time series.


### Visualizing the multi-dimensional system
Using the obtained parameters for the lag and dimensions we aim to visualize the multi dimensional system. Since we use more than three dimensions our visualization will always be a simplification of the actual system. Plotting the first three dimensions of our system results in a big colored ball of fuzz.
```
lines3D(HR.takens[,1], HR.takens[,2], HR.takens[,3], t= "l", col = jet.col(10), asp = 1 )
```

![image](https://user-images.githubusercontent.com/78364132/168776247-d6e89110-7ffb-4698-8a48-036b4f3d502c.png)

*Figure 6: 3D plot first three dimensions*


It is very hard to say anything useful about this plot, therefore we will aim to visualize the time component.
By plotting subsets of our matrix we might be able to say something about the trajectory over time.

```
lines3D(HR.takens[,1][1:10000], HR.takens[,2][1:10000], HR.takens[,3][1:10000], t= "l", col = jet.col(10), asp = 1 )
lines3D(HR.takens[,1][10000:20000], HR.takens[,2][10000:20000], HR.takens[,3][10000:20000], t= "l", col = jet.col(10), asp = 1 )
lines3D(HR.takens[,1][20000:30000], HR.takens[,2][20000:30000], HR.takens[,3][20000:30000], t= "l", col = jet.col(10), asp = 1 )
lines3D(HR.takens[,1][30000:40000], HR.takens[,2][30000:40000], HR.takens[,3][30000:40000], t= "l", col = jet.col(10), asp = 1 )
```

Index 1 to 10000           |  Index 10000 to 20000  
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/78364132/168777522-7050e62f-2c48-42f1-832d-af8c2cb542f5.png)  |  ![image](https://user-images.githubusercontent.com/78364132/168777581-206a9aae-7eaf-439a-a437-5f9216dd260a.png)


Index 20000 to 30000           |  Index 30000 to 40000  
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/78364132/168778081-4e80606d-4b6a-4186-9313-f20532896990.png) |  ![image](https://user-images.githubusercontent.com/78364132/168778108-8608f04e-4367-43cd-9e5a-eaaad7a8c6d3.png)

The figures differ significantly, meaning that there is a change over time. However, we can still say little about what the dimension could represent.
We notice that the Figure that represents index 20000 to 30000 contains less lower (dark blue) values than the other Figures.
Naturally, we only plotted the first three dimensions and one should check all the plots before coming to a conclusion. In addition, specific quantitative properties can be derived using Recurrence Quantification Analysis (RQA). Fortunately, we will cover this topic in the next module, so stay tuned!


## References
Ozheredov, V. A., Chibisov, S. M., Blagonravov, M. L., Khodorovich, N. A., Demurov, E. A., Goryachev, V. A., ... & Meladze, Z. A. (2017). Influence of geomagnetic activity and earth weather changes on heart rate and blood pressure in young and healthy population. International journal of biometeorology, 61(5), 921-929.

Vadlamudi, C. V., & Vadlamudi, S. P. D. (2018). Mathematical Essentials. In Handbook of statistics (Vol. 38, pp. 53-73). Elsevier.

GRASSBERGER, Peter; SCHREIBER, Thomas; SCHAFFRATH, Carsten. Nonlinear time sequence analysis. International Journal of Bifurcation and Chaos, 1991, 1.03: 521-547.





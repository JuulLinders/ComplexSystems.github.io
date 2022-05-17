## Blog Module 6 Phase-Space Reconstruction

In the previous module we learned about attractor dynamics and how we can apply
different techniques to visualize these dynamics. In this module we will learn about phase space reconstruction. The main goal of this module is to construct a multi-dimensional system from a single dimensional time series. Similarly to the other modules, we will use the heart rate time series to guide the reader through the techniques that are used in order to create this multi-dimensional system.

First, we should think about whether it is useful to apply phase space reconstruction to a heart rate time series. Does it make sense that the single-dimensional time series can be reconstructed as a multi-dimensional system? One could very well imagine heart rate to have more dimensions since the heart rate is part of the system of the human body. Multiple factors can influence heart rate: activity of the human, mental state and even the weather can influence heart rate (Ozheredov et al., 2017). Thus it is valid to apply the phase space reconstruction technique to the heart rate time series. 

This module will consists of three steps: determining the optimal delay, determining the embedding dimensions and visualizing the multi-dimensional system.

# Delay
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
The first zero crossing of the autocorrelation function would suggest a lag of 10000. Since the length of our time series is approximately 60000 we would be able to use this delay.
```
tau.acp <- timeLag(HR, technique = "ami", lag.max = (15000), do.plot = T)
```
![image](https://user-images.githubusercontent.com/78364132/168768036-ae3d2ca8-8608-4530-aad5-cf9624d58572.png)
First local minimum of the average mutual information function is found with a delay of approximately 3500.






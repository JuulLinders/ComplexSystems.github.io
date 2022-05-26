#Empirical dynamic modeling
In this module we will learn about empirical dynamic modeling (EDM) and how it can help us understand complex systems. We can break it down into 4 different steps. 1. Determining the dimensionality of the system. 2. Determining whether it is a nonlinear dynamical system. 3. Finding causal variables and 4. forecasting.

## The data
We will be using the same data as the other modules, mainly the dataset from Rossi et al. (2020), ‘Multilevel Monitoring of Activity and Sleep in Healthy People’. Where participants were monitored one full day through their heartrate, their relative movement in space and the time among others. We focused on one participant to conduct EDM on their measured timeseries.

Firstly we are going to check for the optimal embedding dimension for our heart rate data. We have already done this in module 6, phase space reconstruction, through False Nearest Neighbors (FNN) and Cao’s method. Now we are going to find to the amount of embedding dimension by optimizing for predictive skill

![CCM vector magnitude-HR](https://user-images.githubusercontent.com/106141937/170389991-e6b85d0d-3363-43a2-807a-5d8f89c96510.png)

```
knitr::kable(tidy(Kendall::MannKendall(cmap$`HR:Vector.Magnitude`)))
knitr::kable(tidy(Kendall::MannKendall(cmap$`Vector.Magnitude:HR`)))
```

# Empirical dynamic modeling
In this module we will learn about empirical dynamic modeling (EDM) and how it can help us understand complex systems. We can break it down into 4 different steps. 1. Determining the dimensionality of the system. 2. Determining whether it is a nonlinear dynamical system. 3. Finding causal variables and 4. forecasting.

## The data
We will be using the same data as the other modules, mainly the dataset from Rossi et al. (2020), ‘Multilevel Monitoring of Activity and Sleep in Healthy People’. Where participants were monitored one full day through their heartrate, their relative movement in space and the time among others. We focused on one participant to conduct EDM on their measured timeseries. Because of computational limitations we will be using a subset of the data. instead of the full day we are limiting the dataset between 23:00 and 01:00. 

![Module 8 HR timeseries](https://user-images.githubusercontent.com/106141937/170733573-2ac738ea-b25b-4d21-a818-fee6a449e034.png)
*Figure 1, Heartrate timeseries from 23:00 till 01:00



## Finding the embedding dimensions
Firstly we are going to check for the optimal embedding dimension for our heart rate data. We have already done this in module 6, phase space reconstruction, through False Nearest Neighbors (FNN) and Cao’s method. Now we are going to find to the amount of embedding dimension by optimizing for predictive skill and comparing that to previous methods.

### 1. False nearest neighbors 

![Module 8 FNN](https://user-images.githubusercontent.com/106141937/170729036-68425e7c-3dda-4d89-8010-923293b6157e.png)

*Figure 2, False nearest neighbors
### 2. Cao's method for estimating embedding dimensions
![module 8 Cao's method](https://user-images.githubusercontent.com/106141937/170729570-48114002-05a9-4bae-a132-83cf895d29e6.png)

*Figure 3, Cao's method for estimating embedding dimensions
### 3. optimizing for predictive skill

```
EmbedDimension(dataFrame = df1, lib = lib_point, pred = pred_point, maxE = 9, tau = -1, columns='HR', target ='HR', numThreads = 8)
```
![module 8 ED](https://user-images.githubusercontent.com/106141937/170729095-bd708c91-7e20-404d-b46e-a331f9a81ee5.png)
*Figure 4 estimating embedding dimensions for optimizing predictive skill

Judging from figure 4 it would seem like there are 4 embedding dimensions. These results are comprable with the Cao's method as the latter also estimates 4 embedding dimensions. However, the FNN is not entirely clear and it looks like it favors 2 dimensions. We will continu using 4 dimensions since we will also try to optimize our forecasting.

![CCM vector magnitude-HR](https://user-images.githubusercontent.com/106141937/170389991-e6b85d0d-3363-43a2-807a-5d8f89c96510.png)

```
knitr::kable(tidy(Kendall::MannKendall(cmap$`HR:Vector.Magnitude`)))
knitr::kable(tidy(Kendall::MannKendall(cmap$`Vector.Magnitude:HR`)))
```

## Determining nonlinearity
Nonlinearity can also be defined as state depedency of a nonlinear dynamicl system. This means that the nonlinearity of a system is reflected by the degree of state dependency. It can be tested through sequential locally weighted global linear map analysis, or S-map. The parameter Rho quantifies the level of state depency where rho = 0 means no state dependency and therefore indicates a linear stochastic system. When rho > 0, it indicates for a nonlinear dynamical system.

## Finding Causality
It might be possible to find a causal variable to help explain the heartrate variability in our timeseries. Alongside heartrate, vector magnitude was also measured. This construct is measured by movement derived from raw acceleration expressed in Newton-meter. It is very much plausible that an increase in vector magnitude might cause heartrate to go up as well. Convergent cross mapping is a tool that uses convergence as a criteria to determine causality. It reconstructs the state space using different library lengths from different time series.



### References
Chang, C. W., Ushio, M., & Hsieh, C. H. (2017). Empirical dynamic modeling for beginners. Ecological research, 32(6), 785-796.

Rossi, A., Da Pozzo, E., Menicagli, D., Tremolanti, C., Priami, C., Sirbu, A., Clifton, D., Martini, C., & Morelli, D. (2020). Multilevel Monitoring of Activity and Sleep in Healthy People (version 1.0.0). PhysioNet. https://doi.org/10.13026/cerq-fc86.

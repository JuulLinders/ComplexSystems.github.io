# Empirical dynamic modeling
In this module we will learn about empirical dynamic modeling (EDM) and how it can help us understand complex systems. We can break it down into 4 different steps. 1. Determining the dimensionality of the system. 2. Determining whether it is a nonlinear dynamical system. 3. Finding causal variables and 4. forecasting.

## The data
We will be using the same data as the other modules, mainly the dataset from Rossi et al. (2020), ‘Multilevel Monitoring of Activity and Sleep in Healthy People’. Where participants were monitored one full day through their heartrate, their relative movement in space and the time among others. We focused on one participant to conduct EDM on their measured timeseries. Because of computational limitations we will be using a subset of the data. instead of the full day we are limiting the dataset between 23:00 and 01:00. 

![Module 8 HR timeseries](https://user-images.githubusercontent.com/106141937/170733573-2ac738ea-b25b-4d21-a818-fee6a449e034.png)

*Figure 1: Heartrate timeseries from 23:00 till 01:00*



## Finding the embedding dimensions
Firstly we are going to check for the optimal embedding dimension for our heart rate data. We have already done this in module 6, phase space reconstruction, through False Nearest Neighbors (FNN) and Cao’s method. Now we are going to find to the amount of embedding dimension by optimizing for predictive skill and comparing that to previous methods.

### 1. False nearest neighbors 

![Module 8 FNN](https://user-images.githubusercontent.com/106141937/170729036-68425e7c-3dda-4d89-8010-923293b6157e.png)

*Figure 2: False nearest neighbors*
### 2. Cao's method for estimating embedding dimensions
![module 8 Cao's method](https://user-images.githubusercontent.com/106141937/170729570-48114002-05a9-4bae-a132-83cf895d29e6.png)

*Figure 3: Cao's method for estimating embedding dimensions*
### 3. Optimizing for predictive skill

```
EmbedDimension(dataFrame = df1, lib = lib_point, pred = pred_point, maxE = 9, tau = -1, columns='HR', target ='HR', numThreads = 8)
```
![module 8 ED](https://user-images.githubusercontent.com/106141937/170729095-bd708c91-7e20-404d-b46e-a331f9a81ee5.png)
*Figure 4: estimating embedding dimensions for optimizing predictive skill*

Judging from figure 4 it would seem like there are 4 embedding dimensions. These results are comprable with the Cao's method as the latter also estimates 4 embedding dimensions. However, the FNN is not entirely clear and it looks like it favors 2 dimensions. We will continu using 4 dimensions since we will also try to optimize our forecasting.

## Determining nonlinearity
Nonlinearity can also be defined as state depedency of a nonlinear dynamicl system. This means that the nonlinearity of a system is reflected by the degree of state dependency. It can be tested through sequential locally weighted global linear map analysis, or S-map. The parameter Rho quantifies the level of state depency where theta = 0 means no state dependency and therefore indicates a linear stochastic system. When theta > 0, it indicates for a nonlinear dynamical system.

```
PredictNonlinear(dataFrame = df1, lib = lib_point, pred = pred_point, E=4, columns='HR', target ='HR')
```
![linearity](https://user-images.githubusercontent.com/106141937/170838948-9a3951ec-96f9-4192-8e14-921d9fb68325.png)
*Figure 5: testing for linearity with theta on the x-axis and rho (prediction skill) on the y-axis*

Figure 5 seems to indicate a negative slope however, almost all values of data are near one. This means it is still possible that the sytem is nonlinear. We do have to keep in mind that this might not be the case.

## Finding causality
It might be possible to find a causal variable to help explain the heartrate variability in our timeseries. Alongside heartrate, vector magnitude was also measured. This construct is measured by movement derived from raw acceleration expressed in Newton-meter. It is very much plausible that an increase in vector magnitude might cause heartrate to go up as well. Convergent cross mapping is a tool that uses convergence as a criteria to determine causality. It reconstructs the state space using different library lengths from different time series.

```
xcor_out <- ccf(df2$HR,df2$Vector.Magnitude,lag.max=6,type="correlation",plot = FALSE)$acf
cmap <- CCM(dataFrame = df2, E = 4, Tp = 0, columns = "Vector.Magnitude", target = "HR", libSizes = "10 1000 50", sample = 100, showPlot = TRUE )

knitr::kable(tidy(Kendall::MannKendall(cmap$`HR:Vector.Magnitude`)))
knitr::kable(tidy(Kendall::MannKendall(cmap$`Vector.Magnitude:HR`)))
```

![Module 8 HR-VM](https://user-images.githubusercontent.com/106141937/170876722-d8e788fd-c096-4d4e-bdc9-f04fc09a6d44.png)

*Figure 6: convergent cross mapping between heartrate and vector.magnitude*

CCM analysis clearly shows a unidirectional causality of the form vector magnitude causing heartrate variablity. This is in line with our expectation that the movement (or acceleration) causes heartrate to to change as well.

## Forecasting
In order check our forecasting skill we will run three different types of analysis and compare them against each other. Today we will discuss the univariate, multivariate and the multiview approach using S-map once more. Univariate is simply running the analysis with only the heartrate variable, with multivariate the vector.magnitude variable is added. Lastly multiview combines multiple possible dimensions of heartrate to extract information for prediction. Before running these analysis optimal parameters have been estimated. To run the analysis this code was used:

```
tau1 <- timeLag(df$HR, technique = "ami", lag.max = 100, do.plot = T)

smap_uni <- SMap(dataFrame = df2, lib = lib_point, pred = pred_point, E=4, tau = tau1,columns='HR', target ='HR', embedded = FALSE, theta=0) #7 minutes to run
univariate_stats <- compute_stats(smap_uni$predictions$Observations,smap_uni$predictions$Predictions)

multivariate_rho <- smap_multi$stats$rho[1]

mv_out <- Multiview(dataFrame = df2, lib= lib_point, pred = pred_point, E=4, target= "HR", columns = "HR Vector.Magnitude")
multiview_stats <- compute_stats(mv_out$Predictions$Observations,mv_out$Predictions$Predictions)
```

| Method  | RHO| MAE| RMSE |
| ------------- | ------------- | ------------- | ------------- |
| Univariate | 0.9956666 | 0.5906755 | 1.046011 |
| Multivariate | 0.9954919| 0.8167552 | 1.176071 |
| Multiview | 0.9356755 | 9.742067 | 10.91309 |

*Table 1: comparing various forecasting analysis by their forecasting skill (RHO), Mean absolute error (MAE) and root mean square error (RMSE)*

Our best predictior, looking at table 1, was the univariate analysis. It has the best predition skill and also the lowest error values of the three. It should be noted that all of these methods had a very high prediction skill score, but clearly multiview performed the worst. These high scores of course look amazing, but they are based on a prediction horizon of one. This means it only predicts one second in the future and that is perticularly useful. Therefore we will run our best performing model (univariate analysis) for multiple prediction horizons to see how it will hold up. 

| Prediction horizon  | RHO| MAE| RMSE |
| ------------- | ------------- | ------------- | ------------- |
| 1 (second)| 0.9956666 | 0.5906755 | 1.046011 |
| 60 (1 minute)| 0.8929397 | 7.726559 | 8.394948 |
| 120 (2 minutes)| 0.7675503 | 15.58628 | 16.27243 |
| 180 (3 minutes)| 0.6410092 | 21.23214 | 22.03917 |
| 240 (4 minutes)| 0.4641346 | 24.72418 | 25.63775 |

*Table 2: comparing prediction horizons in univarite (S-map) analysis and their performance in forecasting skill (RHO), Mean absolute error (MAE) and root mean square error (RMSE)*

Naturally we see a steady decline of prediction skill and incline in error rate the further we forecast in the future. At one and two minutes the prediction skill is still pretty good but after 3 and especially 4 minutes it dips too low to consider that sufficient.

## Conclusion

Using empirical dynamic modeling we were able to analyse our timeseries and make a forecasting model. We compared three different methods to estimate the embedding dimensions and found that FNN and optimizing for prediction skill were comprable to one another. Using CCM we confirmed our expectation that there is a unidirectional causal relationship between heartrate and vector magnitude, with vector magnitude causing heartrate variablity. Trying 3 different types of analysis we found that our univariate analysis performed better over multivariate en multiview analysis. Our final univariate model can predict 2 minutes into the future with fairly high accuracy.

### References
Chang, C. W., Ushio, M., & Hsieh, C. H. (2017). Empirical dynamic modeling for beginners. Ecological research, 32(6), 785-796.

Rossi, A., Da Pozzo, E., Menicagli, D., Tremolanti, C., Priami, C., Sirbu, A., Clifton, D., Martini, C., & Morelli, D. (2020). Multilevel Monitoring of Activity and Sleep in Healthy People (version 1.0.0). PhysioNet. https://doi.org/10.13026/cerq-fc86.

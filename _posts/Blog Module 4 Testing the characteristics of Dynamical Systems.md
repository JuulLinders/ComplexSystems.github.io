## Module 4 Testing the characteristics of Dynamical Systems
Complex systems have been introduced in the previous module. This module will provide a short recap of some important features, after which three specific characteristics of complex systems are explained. Lastly a further elaboration on testing for two of these characteristics is provided. 
 
Dynamical systems can be defined as systems whose behavior evolves or changes over time. Those dynamical systems are considered complex if they entail nonlinear transitions and many interacting components. Those systems often show soft assembly, meaning they reflect a temporary coalition of coordinated entities. Opposed to such systems are non-biological systems that are hard molded. They are externally coordinated, while complex systems are not. Complex systems seem to regulate themselves. 
 
The components of these dynamical systems are fundamentally interdependent and (therefore) hard to assign precise causal roles to. This is also called Interaction Dominant dynamics. Three specific characteristics of dynamic systems are the focus of this module. They are the memory complex systems have, the regime shifts they go through and the sensitive dependence on initial conditions. First those will be explained and thereafter some explanation on testing for them is given. 
 
The first characteristic, memory, relates to complex systems developing over time and their current states depending on previous ones. In other words, future states are dependent on past values. The past values / experiences are the aspects that is referred to as the memory of complex systems.
 
The second one is the regime shifts. This relates to the phase transitions that complex systems exhibit. They entail structural changes in a system. 
 
The third and last one is the sensitive dependence on initial conditions. This one is a bit more difficult and not described in the previous module and will therefore be elaborated on further. Initial conditions in complex systems are the processes / behavior / or anything you measure that are present at the start. Because complex systems have memory, past values influence future states. Consequently, minor differences at the start, can evolve to huge differences in the future. 
This characteristic relates to the concept of chaos. Chaos entails that very simple deterministic, nonlinear systems can produce extremely complex and unpredictable behavior. The cause of this chaos can be found in the sensitive dependence on initial conditions. So, minor differences at the start may be amplified as a system evolves over time, causing the extremely complex behavior (chaos) in nonlinear systems. Important to know, is that this is not the same as randomness. Often, scientists assume randomness once results seem unpredictable. Yet, as augmented above, history does matter in the case of complex systems. Especially because history matters so much, the initial conditions impact later states. In the case of randomness, this history would not matter. So although in one's results chaos and random results may look familiar, they are not the same. 
 
The described characteristic of memory can be tested for using the Bartels rank test and by inspecting autocorrelation functions. The first tests the memory by assessing dependency of past values and the latter by long-range temporal correlations.
 
The data of the young male's heartrate, introduced in the previous blog, is used to show how those tests can be applied.


``` RR <- read.csv("RR.csv")
RR <- subset(RRtest, ibi_s< 3)

ggplot(data = RR, aes(x = X, y = ibi_s))+
  geom_line()+
  scale_x_continuous("Measurement number", limits = c(1, 80000))+
  scale_y_continuous("Time in seconds between heartbeats")+
  ggtitle("Beat to beat interval timeseries")+
  theme(plot.title = element_text(hjust=0.5), panel.background = element_rect(fill = "white", colour = "black"), panel.grid = element_blank())

X = RR$X
time = RR$time
ibi_s = RR$ibi_s 
```
![image](https://user-images.githubusercontent.com/78364132/159040087-c3edb223-5553-4bed-9ef0-93534280f001.png)
 
To test for the complexity of this system, the characteristic of memory is assessed. Memory can be marked by three factors, namely the dependency on past values, long-range temporal correlations and non-stationary temporal correlations. The first can be assessed by the Bartel Rank tests and the latter two via ACF’s. 
 

So, a Bartels Ratio Test is applied in the following way:
 ```
 bartels.rank.test(RR$ibi_s, alternative = "two.sided")
 ```
The test has tested whether the the null hypothesis should be rejected or not, for which the p-value is below 2.2e-16. This means that this hypothesis is rejected, and the alternative hypothesis is assumed. This hypothesis assumes non randomness and thus assumes memory. 
 
Explaining this conclusion in light of the described terms: memory means the results are the way they are, due to previous results. So, although memory is the cause, sometimes the results are considered random. This is due to the complexity / chaotic appearance of the systems. This test has tested for the assumption of randomness. This one was rejected, so memory is assumed. 

 
The example above tested for memory by the marker of dependency of past values, via the Bartels Test. Another way to test for memory is by the long-range temporal correlations, via the Partial Auto-Correlation. 
```
Plotpacf <- pacf(na.exclude(RR$ibi_s),lag.max = 1000)
plot(Plotpacf, main = "Plot partial ACF")
```

The plot below describes the results of this test. The blue lines indicate the thresholds of the auto-correlations. As can be seen, there are several correlations that cross the thresholds. This means the correlations indicate long-range temporal correlations and therefore memory. 
![image](https://user-images.githubusercontent.com/78364132/159040171-8e557c72-ccce-4adb-9fe5-604ec5f1fdbf.png)

To conclude, both tests show the data of seconds between heartbeats have memory. 

The second described characteristic of complex systems is the existence of regime shifts. Those can be tested for by both the Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test and by a change point analysis. A KPSS test will test the null hypothesis that there is stationarity (opposed to phase transitions).
```
kpss.test(na.exclude(RR$ibi_s), lshort=TRUE, 
          null="Level")
```
The results of this test provided a KPSS level = 55.05, Truncation lag parameter = 20, with p-value = 0.01. This p value indicates significance and therefore the assumption of stationarity can be rejected and non-stationarity is assumed. In other words, the data shows signs of nonstationarity. 

The change point analysis will check when the distributional properties change. However, since our time series contains over 70000 data points the change point analysis is computationally very heavy. An alternative way to find a change point is to measure the variance over a fixed interval throughout the time series. Areas that have a high variance then suggest a change in distributional properties and therefore a change point. Calculating the variance over every 1000 values, provides us with the following graph. 
```
variance = c()
interval = 1000

for (i in 1:length(RR$ibi_s - interval)){
  variance[i] <- var(RR$ibi_s[i:(i+interval)])
}
  
variance
plot(c(1:length(variance)), variance, main = "Variance over fixed interval 1000",
     ylab = "Variance", xlab = "Measurement number")
```
![image](https://user-images.githubusercontent.com/78364132/159040222-a99a9bb8-dfd3-411b-b2e1-66fbbc61c001.png)


Two change points are quite easily distinguishable. However, this analysis is very sensitive to the length of the interval that is used to calculate the variance. For example, when using an interval of 5000 the following graph is created. 
```
variance = c()
interval = 5000

for (i in 1:length(RR$ibi_s - interval)){
  variance[i] <- var(RR$ibi_s[i:(i+interval)])
}
  
variance
plot(c(1:length(variance)), variance, main = "Variance over fixed interval 5000",
     ylab = "Variance", xlab = "Measurement number")
```
![image](https://user-images.githubusercontent.com/78364132/159040244-1ebac4db-9d98-4564-9e86-ab351a48c3e3.png)

Still, two points are quite prominent, however, they are less sharp than with the interval of 1000. This does, however, give enough evidence to assume that there are likely two phase transitions. This could, in practice, refer to the change in activity of the male participant. From awake to sleeping and then awake again.

To conclude, this blog has explained three characteristics of complex systems and showed ways on how to assess two of those. Those characteristics will be referred to in future modules (INCLUDE WHICH ONES) and are thus useful to understand. 



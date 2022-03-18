## Blog Module 4 Testing the memory of Dynamical Systems
Up to now, you have read a lot about complex systems and their characteristics. This blog will give you a short recap of some important features, after which three specific characteristics of complex systems are explained. Lastly a further elaboration on testing for one of these characteristics is provided. 
 
Dynamical systems can be defined as systems whose behavior evolves or changes over time. Those dynamical systems are considered complex if they entail nonlinear transitions and many interacting components. Those systems often show soft assembly, meaning they reflect a temporary coalition of coordinated entities. To make this easier to understand: opposed to this are non-biological systems that are hard molded. They are externally coordinated, while complex systems are not. Complex systems seem to regulate themselves. 
 
The components of these dynamical systems are fundamentally interdependent and (therefore) hard to assign precise causal roles to. This is also called Interaction Dominant dynamics. Three specific characteristics of dynamic systems are the focus of this blogpost. They are the memory complex systems have, the regime shifts they go through and the sensitive dependence on initial conditions. First those will be explained and thereafter some explanation on testing for them is given. 
 
To start off with, memory. Complex systems develop over time and their current states depend on previous ones. To put it differently, future states are dependent on past values. The past values / experiences are the aspects that is referred to as memory.
 
The second one is the regime shifts. This relates to the phase transitions that complex systems exhibit. They entail structural changes in a system. 
 
The third and last one is the sensitive dependence on initial conditions. This one is rather new and will therefore be elaborated on further. Initial conditions in complex systems are the processes / behavior / or anything you measure that are present at the start. Because complex systems have memory, past values influence future states. Consequently, minor differences at the start, can evolve to huge differences in the future. 
This characteristic relates to the concept of chaos. To refresh your mind, chaos was the idea that very simple deterministic, nonlinear systems can produce extremely complex and unpredictable behavior. The cause of this chaos can be found in the sensitive dependence on initial conditions. Paraphrasing it one more time: minor differences at the start may be amplified as a system evolves over time, causing the extremely complex behavior (chaos) in nonlinear systems. Important to know, is that this is not the same as randomness. Often, scientists assume randomness once results seem unpredictable. Yet, as augmented above, history does matter in the case of complex systems. Especially because history matters so much, the initial conditions impact later states. In the case of randomness, this history would not matter. So although in one's results, chaos and random results may look familiar, they are not the same. 
 
The described characteristic of memory can be tested for using the Bartels rank test and by inspecting autocorrelation functions. The first tests the memory by assessing dependency of past values and the latter by long-range temporal correlations.
 
The data of the young male beat to beat interval is used to show how you can apply those tests.


``` RR <- read.csv("RR.csv")
RR <- subset(RRtest, ibi_s< 3)

ggplot(data = RRtest, aes(x = X, y = ibi_s))+
  geom_line()+
  scale_x_continuous("Measurement number", limits = c(1, 80000))+
  scale_y_continuous("Time between heartbeats")+
  ggtitle("beat to beat interval timeseries")+
  theme(panel.grid = element_blank())

X = RR$X
time = RR$time
ibi_s = RR$ibi_s 
```

![image](https://user-images.githubusercontent.com/78364132/158975341-b34710a1-af50-4af6-b901-ad9b9c1a0dae.png)

The data is familiar to you, it entails the number of seconds between heartbeats of a healthy, young male measured over the day. 
 
To test for the complexity of this system, the characteristic of memory is assessed. Memory can be marked by three factors, namely the dependency on past values, long-range temporal correlations and non-stationary temporal correlations. The first can be assessed by the Bartel Rank tests and the latter two via ACF’s. 
 

So, a Bartels Ratio Test is applied in the following way:
 ```
 bartels.rank.test(RR$ibi_s, alternative = "two.sided")
 ```
The test has tested for the null hypothesis to be true, for which the p-value is below 2.2e-16. This means that this hypothesis is rejected, and the alternative hypothesis is assumed. This hypothesis assumes non randomness and thus assumes memory. 
 
This conclusion may come a bit too soon if you are unfamiliar with the concept, so let me explain it again: memory means the results are the way they are, due to previous results. So, although memory is the cause, sometimes the results are considered random. This is due to the complexity / chaotic appearance of the systems. This test has tested for the assumption of randomness. This one was rejected, so memory is assumed. 

 
The example above tested for memory by the marker of dependency of past values, via the Bartels Test. Another way to test for memory is by the long-range temporal correlations, via the Partial Auto-Correlation. 
```
pacf(na.exclude(RR$ibi_s),lag.max = 1000)
```

The plot below describes the results of this test. The blue lines indicate the thresholds of the auto-correlations. As can be seen, there are several correlations that cross the thresholds. This means the correlations indicate long-range temporal correlations and therefore memory. 
![image](https://user-images.githubusercontent.com/78364132/158976407-25fc1140-7d16-419a-bc8e-61bc066ed76c.png)
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
plot(c(1:length(variance)), variance)
```
![image](https://user-images.githubusercontent.com/78364132/158976684-22ad6aaf-5c36-4b51-87ed-c3880fb5c72e.png)
Two change points are quite easily distinguishable. However, this analysis is very sensitive to the length of the interval that is used to calculate the variance. For example, when using an interval of 5000 the following graph is created. 
```
variance = c()
interval = 5000

for (i in 1:length(RR$ibi_s - interval)){
  variance[i] <- var(RR$ibi_s[i:(i+interval)])
}
  
variance
plot(c(1:length(variance)), variance)
```
![image](https://user-images.githubusercontent.com/78364132/158976737-c59ddc26-f0d6-472f-88d6-3d8f77ac63c0.png)
Still, two points are quite prominent, however, they are less sharp than with the interval of 1000. This does, however, give us enough evidence to assume that there are likely two phase transitions. This could, in practice, refer to the change in activity of the male participant. From awake to sleeping and then awake again.



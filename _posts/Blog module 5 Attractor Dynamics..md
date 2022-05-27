# Attractor Dynamics

In this module we will explore our activity monitoring dataset by using topology features and testing them as well. 
In the previous module (Properties of Dynamical systems) we saw various phase shifts in the timeline regarding heartrate (HR), which is probably an effect of change in activity. 
We can further investigate these changes through topology in attractor dynamics.

The dataset from Rossi et al. (2020), ‘Multilevel Monitoring of Activity and Sleep in Healthy People’. Where participants heartrate was monitored one full day. Below you can find the heartrate timeseries of this data.

![image](https://user-images.githubusercontent.com/78364132/169966096-dedcb539-49d0-439b-a297-0ced221ff2a7.png)

*Figure 1: heart rate time series*

Topology, in other words, is the graphical representation of differential equations. They are also called phase space or state space. In a later module we will discuss phase space reconstruction and how it can be used to determine the complexity (dimensionality) of a system. For now we will focus vector fields, which is also a topology in attractor dynamics.

### Topology features

Vectors are data objects that have a magnitude and a direction in which they are going and can be pulled or repelled towards data values. In this module we are going to specifically look at how we can make sense of de direction of these vectors. The most basic constructs are attractors and repellors. An attractor pulls vectors towards a setpoint and will be very densely structured. A setpoint is a point of no change and is the place behaviour in the system is measured in relation to this value. A repellor is the opposite of an attractor and will push (repel) vectors away from a setpoint. The last one we would like to highlight, is the saddle. This setpoint acts as both an attractor as well as a repellor, which pulls vectors from one direction while simultaneously pulling vectors from another direction.
Let us first take a look a vector field from our activity monitoring dataset. In order to make this plot we have to make a heartrate vector variable, or change in heartrate compared to a previous datapoint (lag).  We do this by subtracting the lead points by -1 lag points and dividing that by 2.
![vectorfield](https://user-images.githubusercontent.com/106141937/170374256-22e40399-fae1-4412-8f04-03bcb5c58262.png)
*Figure 2: Heartrate vector field*

This figure is a vector field density plot, with heartrate on the Y-axis and time in seconds on the X-axis starting at 10:10 in the morning until 00:46 in the night when the subject is going to sleep. We see various high density areas most of which are either in the 90/100 range or 60/70 range. These areas  could be indicators for attractors. My guess would that there are at least 2 attractors for those areas and a repellor. To check this we will perform a linear regression with a polynomial term (HR^3) with the following code:
```rb
mod3 <- lm(HR_change~poly(HR,3), data=dat)
summary(mod3)
```

This gives the following result:

| Value  | Slope estimate| P-value |
| ------------- | ------------- | ------------- |
| HR | 0.0517182 | 0.97117 |
| HR^2| -4.2395820 | 0.00305 |
| HR^3| -8.8944475 | 5.15e^-10 |

*Table 1 linear regression output

As we can see we have 2 significant negative slopes, which indicates that there are 2 attractors. Though not significant, there is one positive slope and that could mean there is a Repellor. Like our explanation in module 4 about the shifting phases in our dataset, these attractions could be caused by a change in activity due to either rest or workout. The data mainly revolves around those centers i
Right now we have used difference scores to determine our vector variable however, there are other methods to calculate our vectors such as Generalized Orthogonal Local Derivative also known was GOLD. We will use the following function to calculate our derivatives (vectors) with the embedding parameter on 7. The reason for this will be explained in module 6 where we try to find the optimal amount of embedding dimensions.
```rb
gold_vec<-doremi::calculate.gold(dat$HR, time= dat$time1,embedding=7,n=2)
mod <- lm(gold_vec$dsignal[1:42547,2]~poly(gold_vec$dsignal[1:42547,2],3), data=dat)
summary(mod)
```

When we use this variable in the regression format as before we get the same results only our repellor is also significant. This confirms our believe that there are probably 2 attractors and 1 repellor ( see results below).

| Value  | Slope estimate| P-value |
| ------------- | ------------- | ------------- |
| HR | 2.001e^02 | <2e^-16 |
| HR^2| -2.515e^^-12 | <2e^-16|
| HR^3| --3.475e^-12 | <2e^-16 |

*Table 2 linear regression output

In this module we were able to map the heartrate vectors in a density vector field and visualize where the vectors are most densely packed. We explored different topology features and concluded within our dataset there are at least 2 attractors and 1 repellor. Using difference scores but also the GOLD method to determine our vectors gave us confirmation in our findings through linear regression.

## References
Butner, J. E., Gagnon, K. T., Geuss, M. N., Lessard, D. A., & Story, T. N. (2015). Utilizing topology to generate and test theories of change. Psychological Methods, 20(1), 1.

Rossi, A., Da Pozzo, E., Menicagli, D., Tremolanti, C., Priami, C., Sirbu, A., Clifton, D., Martini, C., & Morelli, D. (2020). Multilevel Monitoring of Activity and Sleep in Healthy People (version 1.0.0). PhysioNet. https://doi.org/10.13026/cerq-fc86.


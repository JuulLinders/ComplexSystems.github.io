## This is my first blog post

Blog Module 4 Testing the memory of Dynamical Systems
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
ibi_s = RR$ibi_s ```

![image](https://user-images.githubusercontent.com/78364132/158975341-b34710a1-af50-4af6-b901-ad9b9c1a0dae.png)


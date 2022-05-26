## Blog Module 7 Recurrent Quantification Analysis

In module 6 we learned about techniques in order to reconstruct phase spaces and how to visualize them.However, we ended the module without a satisfying conclusion about the phase space itself.
In this module we will aim to derive quantitative properties based on the phase space reconstruction.
In order to do so, we will use recurrence quantification analysis (RQA) and apply it to the heart rate time series for one day depicted below. 

``` 
data <- read.csv("Actigraph.csv")
plot(data$HR, type = "l", xlab = "Time", ylab = "Heartrate", main = "Plot Heartrate")
```
![image](https://user-images.githubusercontent.com/78364132/169966096-dedcb539-49d0-439b-a297-0ced221ff2a7.png)

*Figure 1: heart rate time series*

RQA is a technique to quanitify the number and duration of recurrences of a system. Several measures can be derived using RQA which will increase one’s understanding of the system.
Remember that we obtained two parameters in the previous module: delay = 3500 and embedding dimension = 7. In order to apply RQA we additionally need to determine a radius parameter. This radius parameter represents a threshold to determine whether two points are recurrent or not. A rule of thumb for this parameter is we choose a radius that gives between 1 to 5 percent recurrence. This percentage may differ based on the stochasticity of the time series. Highly stochastic time series are recommended to use a higher recurrence percentage whereas for more deterministic time series one should aim for a lower recurrence percentage.

Due to the large length of our time series (> 60000 measurements) R cannot process the entire time series at once. Therefore we will split the time series into two subsets deviding the frist 30000 measurement from the final 37936. For the first subset we try different radius settings until we find that for a radius of 20 the recurrence percentage equals 4.76. Next, we will construct the recurrence plot and gather its properties.
```
HR <- data$HR

rqa1<-crqa(ts1 = HR[1:30000], ts2 = HR[1:30000], delay = 3500, embed = 7, rescale = 0, radius = 20 , method = "rqa", datatype = 'continuous')
print(rqa1[1:10])
```
![plotsubset1](https://user-images.githubusercontent.com/78364132/170041415-d9ef457a-489b-40dd-aba9-4088d8b81376.png)

*Figure 2: Recurrence plot for subset 1*

We can observe several features in the obtained recurrence plot. Marwan et al. (2007) states that white areas or bands are related to the occurrence of abrupt changes in the dynamics as well as extreme events in the data. In addition, the vertical and horizontal lines may indicate that some states do not change or change slowly for some time. For Figure 2 we note that a significant part of the plot is white indicating abrupt changes. This may be indicated as the subject of the time series participating in some activity, which may have changed the heart rate. Vertical and horizontal lines are aditionally present. Naturally, a large part of the day humans do the same activity for a extended amount of time e.g working at a desk, wathcing tv. This may have caused the horizontal and vertical lines. Using the properties denoted in Table 1 we are able to make new conclusions regarding the time series.

| Property  | Value for 1st subset|
| ------------- | ------------- |
| The percentage of recurrent points| 4.76 |
| Proportion of recurrent points forming diagonal line structures| 96.60 |
| The length of the longest diagonal line segment in the plot, excluding the main diagonal  | 465555  |
| The average length of line structures  | 8.01  |
| Shannon information entropy of diagonal line lengths longer than the minimum length  | 2.83  |
| Proportion of recurrent points forming vertical line structures  | 98.03  |
| The average length of vertical line structures  | 11.46  |

*Table 1: property values for subset 1*

Interpreting these parameters is not standard. Using literature we aim to understand what these parameters mean for the heart rate time series. The percentage of recurrent points or recurrence rate is rather straight forward. Marwan et al (2007) mention that it is a measure of the density of recurrence points in the recurrent plot. As stated, this rate has been fixed to between 1 and 5 percent when the radius was determined. Using a radius of 20 we obtain a recurrence rate of 4.76. Given that the majority our heart rate measurements lie between 60 and 140 this radius is rather large. The length of the diagonal lines in an recurrent plot can be linked to the predictability of the underlying system (Marwan et al., 2007). For our time series the average length of the line structures is relatively small (8.01) comparing to the length of the longest diagonal line segment. The Shannon information entropy is a measure of the complexity of the dynamics (Letellier, 2006). The proportion of recurrent plots forming vertical line structures, or laminarity, indicates the tendency of a point to repeat the same state. This proportion is high for our recurrence plot, which could mean that the time series tends to return to the same state often.

For the sake of consistency we will use the same radius for the second subset.

```
rqa2 <-crqa(ts1 = HR[30000:60000], ts2 = HR[30000:60000], delay = 3500, embed = 7, rescale = 0, radius = 20 , method = "rqa", datatype = 'continuous')
print(rqa2[1:10])

```

![plotsubset2](https://user-images.githubusercontent.com/78364132/170232935-fd92aa12-e9e6-42b3-954d-770d88d3e0f3.png)

*Figure 3: Recurrence plot for subset 2*


Subset 2 contains the part where the subject of the time series goes to bed. This means that a rather abrupt could also be observed in the recurrence plot. When comparing Figure 2 and 3 one will note that a larger portion of Figure 3 is white. This may indicate the abrupt change from daily activities to sleeping. The resemblance of the two Figures is high, as one might expect since it originates from the same time series. The derived properties are denoted in Table 2.

| Property  | Value for 2nd subset |
| ------------- | ------------- |
| The percentage of recurrent points| 8.70 |
| Proportion of recurrent points forming diagonal line structures| 97.90 |
| The length of the longest diagonal line segment in the plot, excluding the main diagonal  | 563923  |
| The average length of line structures  | 12.243  |
| Shannon information entropy of diagonal line lengths longer than the minimum length  | 3.29  |
| Proportion of recurrent points forming vertical line structures  | 98.71  |
| The average length of vertical line structures  | 17.74  |

*Table 2: property values for subset 2*

For a radius of 20 the recurrence plot of subset 2 has a higher recurrence rate than subset 1. 
The Shannon information entropy is higher for subset 2 than for 1 indiciating more complexity of the dynamics of the time series. However, since the average length of the line structure is higher for subset 2, predictability is higher for subset 2. Therefore, altough subset 2 is more complex it is more predictable than subset 2. 

In this module we were able to obtain quantitative properties of the phase space reconstruction using recurrence plots. We learned how we can interpret the recurren plots and its properties.  



### References
Letellier, C. (2006). Estimating the Shannon entropy: Recurrence plots versus symbolic dynamics. Physical review letters, 96(25), 254102.

Marwan, N., Carmen Romano, M., Thiel, M., and Kurths, J. (2007). Recurrence plots for the analysis of complex systems. Physics Reports, 438(5), 237-329.


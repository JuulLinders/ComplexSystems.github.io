## Blog Module 6 Phase-Space Reconstruction

In module 6 we learned about techniques in order to reconstruct phase spaces and how to visualize them.However, we ended the module without a satisfying conclusion about the phase space itself.
In this module we will aim to derive quantitative properties based on the phase space reconstruction.
In order to do so, we will use recurrence quantification analysis (RQA) and apply it to the heart rate time series depicted below. 

``` 
data <- read.csv("Actigraph.csv")
plot(data$HR, type = "l", xlab = "Time", ylab = "Heartrate", main = "Plot Heartrate")
```
![image](https://user-images.githubusercontent.com/78364132/169966096-dedcb539-49d0-439b-a297-0ced221ff2a7.png)

RQA is a technique to quanitify the number and duration of recurrences of a system. Several measures can be derived using RQA which will increase one’s understanding of the system.
Remember that we obtained two parameters in the previous module: delay = 3500 and embedding dimension = 7. In order to apply RQA we additionally need to determine a radius parameter. This radius parameter represents a threshold to determine whether two points are recurrent or not. A rule of thumb for this parameter is we choose a radius that gives between 1 to 5 percent recurrence. This percentage may differ based on the stochasticity of the time series. Highly stochastic time series are recommended to use a higher recurrence percentage whereas for more deterministic time series one should aim for a lower recurrence percentage.

Due to the large length of our time series (> 60000 measurements) R cannot process the entire time series at once. Therefore we will split the time series into two subsets deviding the frist 30000 measurement from the final 37936. For the first subset we try different radius settings until we find that for a radius of 20 the recurrence percentage equals 4.76. 
![image](https://user-images.githubusercontent.com/78364132/169988376-45ebc4c0-9f23-42a4-84f3-db9eb12309f9.png)

| Property  | Value |
| ------------- | ------------- |
| The percentage of recurrent points| 4.76 |
| Proportion of recurrent points forming diagonal line structures| 96.60 |
| The length of the longest diagonal line segment in the plot, excluding the main
diagonal  | 465555  |
| The average length of line structures  | 8.01  |
| Shannon information entropy of diagonal line lengths longer than the minimum
length
  | 2.83  |
| Proportion of recurrent points forming vertical line structures  | 98.03  |
| The average length of vertical line structures  | 11.46  |


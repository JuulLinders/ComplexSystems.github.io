## Module 10 Fractality

This module focuses on the topic of fractality. Fractality is a figure, object or system that is made up of similar components / patterns. A fractal has the same degree of non-regularity on all scales. It can be considered a never-ending pattern. Fractals thus display self-similarity, because fractal forms consist of subunits that copy the structure of the overall object. The idea of self-similarity is depicted by the underneath. It shows a tree-like branch that is self-similar, since it consists of similar subunits. Those subunits in turn consist of similar subunits again. This is an example of spatial self-similarity, but self-similarity also occurs in temporal scales and can thus checked for in the dataset of the young males which is used in this series of modules. An example of self-similarity in an Heart Rate is depicted by the figure below the tree branches. If self-similarity is present in this dataset, a consistent pattern can be found in different scalings. A more formal way to test this is by means of a Detrended Fluctuation Analysis (DFA), which will be explained further on in this paper.

<img width="158" alt="image" src="https://user-images.githubusercontent.com/105786135/169538973-34b9572b-e674-45c8-9385-ca8d23ff36f4.png"> <img width="164" alt="image" src="https://user-images.githubusercontent.com/105786135/169539002-4ca21a50-029c-4529-a3f9-cfe51f52d89e.png">

Within the concept of fractality, it is important to make the distinction between monofractals and multifractals.  The first are homogeneous, they have one singularity exponent throughout the entire signal. The latter is not, it can theoretically have a continuous number of indices to characterize the scaling properties. Therefore they are also more complex. When a single exponent is not sufficient to describe dynamics of a fractal system, this infinite number of exponents is necessary. 

Another important aspect in fractals is long memory. The fractals seem to have memory because long-range correlations can be found. This means certain values in the complex systems do not relate to just preceded values, but to values that existed further in the past. 

The DFA algorithm is the most reliable method for estimating the scaling component (which is alpha). The DFA involves four steps. The first is to create the profile by the cumulative sum of the mean centred time series. Second, the time series of length N is partitioned into N/1 non-overlapping bins, with each bin containing 1 observation. Third, The root-mean-squared residual is computed across all bins. Step two and three are then repeated for several “””, increasing “”” by a power. The maximum “”” should not exceed N/2 and the result is a fluctuation function, XXXX. The fourth step is a linear regression of LOGFDL on LOGL. 
If fractals are present, the last step is expected to result in a linear slope with alpha above 0.5. The original DFA could not be applied to multifractal systems, but there is a multifractal DFA. This is a generalization of DFA that estimates the scaling components. This also starts off with computing cumulative sums. Secondly it again fits a linear term to nonoverlapping bins. After this, the mean squared error is again calculated of the bins, all of those are averaged and then the square root is calculated. Lastly, both axes are logarithmatically scaled and the estimate linear slope alpha can be computed. This alpha can be used to estimate the scaling component. In R this computation can be executed via premade functions.

``` scale.min = 16
scale.max = length(data)/4
scale.num = length(logScale(scale.min = scale.min, 
                      scale.max = scale.max,
                      scale.ratio = 1.25))
print(scale.num)
dfa.analysis = dfa(time.series = data, npoints = scale.num, window.size.range = c(scale.min, scale.max), do.plot = FALSE)
data.estimation = estimate(dfa.analysis, do.plot=TRUE)
```
<img width="296" alt="image" src="https://user-images.githubusercontent.com/105786135/169539366-382ce985-2048-4007-83f5-ed177ffc7ddc.png">

The DFA was applied to the data of the young males heartbeat and showed an alpha of .49. This is approximately equal to 0.5 and can therefore be considered as white noise. This entails there are no signs of fractality in this timeseries. Multifractality is therefore not assumed either, yet the analysis is performed to show how a plot of this analysis can be used to check whether there is monofractality or multifractality. 

```scale <- logScale(scale.min = scale.min, scale.max = scale.max, scale.ratio = 2)
q <- -10:10 # range of q order exponents
m <- 1 # detrending order 
mfdfa.out <- MFDFA(data, scale = scale, q = q, m = 1)
plot(mfdfa.out$spec$hq, mfdfa.out$spec.Dq, type = "b", pch = 19,
     xlab ="h(q)", ylab = 'D(h)', main = "multifractal singularity spectrum")
lines(mfdfa.out$spec$hq, mfdfa.out$spec$Dq, type = "b", col = "red")

matplot(mfdfa.out$line, type='l', pch=19, add=FALSE, xlab="log Scale", ylab="log Fq", main = "Monofractal")
```
This analysis resulted in the left plot of figure XX. If a timeseries shows multifractality, the slopes would have been more different from each other, as in the right plot of figure XX. This right plot is thus not made up by the data of the young males, but merely a visualization of another, random multifractal timeseries for example purposes. 

<img width="300" alt="image" src="https://user-images.githubusercontent.com/105786135/169539703-5971678b-205b-4495-a0fc-a6fb6925ff1a.png"> <img width="300" alt="image" src="https://user-images.githubusercontent.com/105786135/169539717-75174f43-2135-4403-b4e0-cd2315dd3488.png">

It is unexpected that the timeseries does not show fractality, since the heartbeat of healthy individuals are expected to be fractal. It is namely known that heartbeat failures are related to the break-down of fractal correlations. A break down in this fractality causes a more dominant, simple model to emerge. Put differently, the complexity and adaptability is reduced and replaced by a more simple pattern. In turn this leads to life threatening situation due to this decrease in adaptability. Adaptability creates the ability for human beings to respond to unexpected stimuli and stresses. Because the young males from whom the data is used in this report are all healthy individuals, it was expected that they are still very adaptable and thus that fractal correlations are present. 

Yet, not in all systems fractality is present. Although this does not serve as an explanation for the absence of it in the current timeseries, the absence of control seems a key factor (Likens et al., 2015). Likens et al., indicate previous studies show that fractal properties are indicators of physiological flexibilities and they state there is more and more evidence for fractals to indicate flexible, adaptive behaviour. Yet, control exertion seems a necessary condition for fractals to arise. If a system does not have to exert control, a system cannot be considered fractal. This is the case e.g. when external task constraints dominate performance and thus function as noise, if the goal-relevant behaviour is tightly controlled or when the task itself does not constrain behaviour enough to elicit constant control. Still, a heartbeat is expected to require control exertion. 

To conclude, this module explained the concept of fractality, described how a DFA analysis works, showed how one can be executed and how results can be interpreted. 








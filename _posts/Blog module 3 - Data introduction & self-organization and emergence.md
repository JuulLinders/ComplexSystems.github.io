## Introduction to dataset & self-organization and emergence
In this series of modules, we explore the open dataset ‘Multilevel Monitoring of Activity and Sleep in Healthy people (MMASH) (Rossi et al., 2020). The dataset provides beat-to-beat heart data of 22 healthy young adult males. The data was collected for 24 continuous hours, including the participant’s period of sleep. Furthermore, the dataset contains more features, such as sleep quality, physical activity and psychological characteristics. According to Rossi et al., continuous sleep data can be useful for research after correlations in physical activity, Heart Rate (HR), Heart Rate Variability (HRV) and sleep quality. 

The MMASH dataset consists of seven csv-files for each participant. The files contain information about participant characteristics; their sleep quality and sleep duration; scores for psychological questionnaires; a list of the activities performed throughout the day; clock genes and hormone concentrations and inter-beat intervals (IBI). Furthermore, the file ‘Actigraph.csv’, contains the HR in beats per minute (BPM), registered every time a heartbeat happened. This data allows us to plot day times against the participant’s HR. From the file ‘sleep.csv’, we derive the participant’s bedtime and wake-up time. 

![HR_user1_avg](https://user-images.githubusercontent.com/105788429/170371272-b4929065-a530-4343-918f-aa6ab023436b.png)
_figure 1 - HR + average HR user_1_ 

In this figure, the light blue line represents user_1’s HR when he was awake hours. The dark blue line displays user_1’s HR during the period he was asleep. The red line is the average HR, computed for each hour. User_1 woke up during the night, around 03:15, and went back to sleep shortly after. At first glance, one can see differences between user_1’s heart rate during sleep and his heart rate when he was awake. The HR seems lower, and there is less variety. Only in the last phase of both sleep cycles, there seems to be less consistency in the participant’s HR.

Heart Rate Variability (HRV) is an indicator widely used in clinical settings (Cleveland Clinic, 2021). HRV measures variety  R-R interval; the time between two consecutive heartbeats. More specifically, in an electrocardiogram (ECG) of two heartbeats, the R-R interval is the time between two consecutive ‘R’-peaks. For this measure we use the R-R interval data from the RR.csv file.The heart is driven by the autonomic nervous system. It operates without you thinking about it, and it even operates when the person is asleep. The autonomic nervous system consists of parasympathetic and sympathetic nervous systems. The sympathetic nervous system can control increases in heart rate, for example when a dangerous situation requires so. The parasympathetic nervous system can do the exact opposite; decreasing the heart rate. Usually, a higher HRV is associated with better adaptation of the body. People with a higher HRV experience less stress than people with a lower HRV. Moreover, a low HRV can be an indicator of future health problems. 

Thus, the variation in HR and HRV is controlled by a primitive part of the nervous system called the autonomic nervous system. According to complex systems theory, the nervous system is an example of a complex system. Complex systems are a large network of interdependent components with no central control, in which emergent complex behavior is exhibited (Mitchell, 2006). Emergence, here, means that the system’s behavior is a product from interactions of its components. So to say, a complex system is rather interaction-dominant and non-linear, than component-dominant and linear. The notion that complex systems are typically systems with no central control, refers to the concept of self-organization; the spontaneous emergence of order. 

The Poincaré plot is a recurrence plot, used to visualize and quantify the correlation between two consecutive data points in a time-series (Satti et al., 2019). It is extensively used in HRV analyses, for the detection of fluctuations in HRV. To demonstrate the Poincaré plot, we use the ibi_s (Interbeat Interval) data of RR.csv, along with Python’s toolbox for HRV, ‘pyhrv’. We plot user_1’s 26 minutes between his two periods of sleep. Additionally, we make another plot with 26 minutes of Interbeat Interval data when sleeping. 

![Poincaré_awake](https://user-images.githubusercontent.com/105788429/170713310-987252fa-b1b9-45e2-9b16-f25619ae4d73.png)

_figure 2 - Poincaré plot awake_
![Poincaré_asleep](https://user-images.githubusercontent.com/105788429/170713308-00220606-60da-4468-99cb-23b8fa47ddc0.png)

_figure 3 - Poincaré plot asleep_

The Poincaré plot is a scatter graph, with a datapoint (An) in time on the x-axis, versus it’s consecutive point (An + 1) on the y-axis. The origin (0, 0) is located in the center. The first plot is based on wake data, the second plot is based on sleep data. The Poincaré plot of sleep data seems more centered around the point 0,0, which implies there is less variation in time beween consective beats. In other words, the HRV when sleeping seems lower. On the other hand, the Poincaré plo of wake data is also centered, but also seems more scattered, which would imply a higher HRV.

Finding and understanding patterns in HR and HRV during sleep can say a lot about the person’s health. Complex systems theory is not only the notion of these complex systems, moreover it is an approach to understand how relationships between parts give rise to the collective behaviors of a system, and how the system interacts and forms relationships with its environment (Bar-Yam, 2003). Recognizing the nervous system as a complex system, allows for analyses and research, appropriate for complex systems. In the following modules, we will demonstrate more analyses for this dataset. 


## References
Bar-Yam, Y. (2002). General Features of Complex Systems. Encyclopedia of Life Support Systems. 

Cleveland Clinic (2021). Heart Rate Variability (HRV). 
    https://my.clevelandclinic.org/health/symptoms/21773-heart-rate-variability-          hrv#:~:text=Heart%20rate%20variability%20is%20where,issues%20like%20anxiety%20and%20depression. Retrieved, 25-5-2022

Favela, L. H. (2020). Cognitive science as complexity science. Wiley Interdisciplinary Reviews: 
    Cognitive Science, 11(4), e1525.
Mitchell, M. (2006). Complex systems: Network thinking. Artificial intelligence, 170(18), 1194-1212.

Rossi, A., Da Pozzo, E., Menicagli, D., Tremolanti, C., Priami, C., Sirbu, A., Clifton, D., 
 
Martini, C., & Morelli, D. (2020). Multilevel Monitoring of Activity and Sleep in Healthy People (version 1.0.0). PhysioNet. https://doi.org/10.13026/cerq-fc86.

Satti, R., Abid, N. U. H., Bottaro, M., De Rui, M., Garrido, M., Raoufy, M. R., ... & Mani, A. R. (2019). 
   The application of the extended Poincaré plot in the analysis of physiological variabilities. Frontiers in physiology, 10, 116.


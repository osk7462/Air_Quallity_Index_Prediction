# Air_Quallity_Index_Prediction
a machine learning approach to predict the air quality index of delhi

1.1 About the project
In this minor project, we tackle air quality index forecasting by using
machine learning approaches to predict the Air Quality Index. Machine
learning, as one of the most popular techniques is able to efficiently train
a model on big data by using large-scale optimization algorithms.
However, the relationships between the concentration of Air pollutant
particles and meteorological factors are poorly understood. To shed some
light on these connections, This project attempted to apply some
machine learning techniques to predict Air quality index category based
on a data set consisting of daily meteorological data from May-2015 to
Oct-2018 of Delhi, India

2.1.1 Air Pollutant Data Collection
we downloaded our air pollutant data from Central Pollution Control
Board (http://cpcb.nic.in/) from(may-2015 to Oct-2018) which is a
statutory organization under the Ministry of Environments, Forrest and
Climate Change (MoEFC).we selected the PM 10 , PM 2.5 , NO 2 , O 3 , CO,
SO 2 , NH 3 , and Pb for air quality index calculation.


2.1.2 Meteorological Data Collection
we downloaded our meteorological data from ( https://en.tutiempo.net/
climate ) from(may-2015 to Oct-2018) the features that has been
selected are:
T
Average temperature (c 0 )
0
PP Total rainfall (mm)
TM Maximum Temperature (c )
VV Average visibility(km)
Tm Minimum Temperature(c 0 ) 
V Average wind speed(km/hr)
SLP Atmospheric pressure at sea level 
VM Maximum wind speed(km/hr)
H Average relative humidity


the pollutant data that we have collected from (http://cpcb.nic.in/) doesn’t
contain the air quality index so we have calculated the air quality index
of each day from (may-2015 to Oct- 2018) from the pollutant data. To
calculate the air quality index we used the formula:

I={\frac {I_{high}-I_{low}}{C_{high}-C_{low}}}(C-C_{low})+I_{low}

where:

{\displaystyle I} I = the (Air Quality) index,
{\displaystyle C} C = the pollutant concentration,
{\displaystyle C_{low}} C_{low}= the concentration breakpoint that is ≤ {\displaystyle C} C,
{\displaystyle C_{high}} C_{high}= the concentration breakpoint that is ≥ {\displaystyle C} C,
{\displaystyle I_{low}} I_{low}= the index breakpoint corresponding to {\displaystyle C_{low}} C_{low},
{\displaystyle I_{high}} I_{high}= the index breakpoint corresponding to {\displaystyle C_{high}} C_{high}.

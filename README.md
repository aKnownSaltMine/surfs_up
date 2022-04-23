# surfs_up
## Overview
Weather is a key factor to take into effect when making plans to open up a surf shop. If weather is too unpredictible it could lead to unpredictable tourist/and surfer traffic to the area, endangering consistent revenue. To help prepare for this, We were able to examine weather data taken daily across the island of Oahu from the years 2010 to 2017, previously examining the precipitation on the island, but now examining the temperature on the extremes of the year. 
## Results
**June Temperature Observations**

![June TOBS](https://github.com/aKnownSaltMine/surfs_up/blob/main/Analysis/June_TOBS.PNG)

** December Temperature Observations**

![Dec TOBS](https://github.com/aKnownSaltMine/surfs_up/blob/main/Analysis/Dec_TOBS.PNG)

* The temperature between these two months vary in their average by just under 4 degrees. 
* The standard deviation between these temperature readings are both just over 3 meaning that it would both months' temperatures vary to a similar degree from their mean
* Both months can stay largely within the 70s by looking at their quintiles but December has reached down into the 50s, but both months max temperatures are in the 80s.

## Summary
Overall the temperature remains largely consistent between the months. This overall preditability with the temperature leads to the conclusion that temperature inconsistencies would not be a limiting factor in opening a surf shop on Oahu.

One thing futher factor to examine with the weather from these two months would be the precipitation. Because not many people would attempt let alone enjoy surfing while it is raining, being prepared to see the precepitation trends through these months would be crucial. 
In order to query this from the dataset, the following two queries would filter out the precipitation for all of the June and December months and provide summary statistics of the precipitation for those months:

``` results = []
	results = session.query(Measurement.date, Measurement.prcp).\
	filter(extract('month', Measurement.date) == 6).all()
	
	df = pd.DataFrame(results, columns=['date', 'june_prcp'])
	df.describe()
```

``` results = []
	results = session.query(Measurement.date, Measurement.prcp).\
	filter(extract('month', Measurement.date) == 12).all()
	
	df = pd.DataFrame(results, columns['date', 'dec_prcp'])
	df.describe()
```
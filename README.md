# Exploring weather trends
Udacity's Data Analysis Nanodegree (first project)

### Goal
Explore weather trends on New York city and make a comparision with world data.

### Data
The data (SQL database) was provided by Udacity. I had to extract the data via SQL queries.

### Moving Average
Making use of google sheets I calculated the 10-year moving average to avoid fluctations on visualizations.

### Visualizations
Line charts developed in Python using Matplotlib and Pandas.

### Statistics
I calculated the Pearson coeficient to understand if there is a correlation between the global temperature and the NYC temperature.

### Conclusions
- The average temperature of New York City is higher than the global one in almost all years except in a little
window around 1785.
- The trend in both cases is really similar with some differences around 1785 and 1880 where there is a peak in
the global temperature but a valley in the New York City's temperature.
- The average temperature in both cases is growing since 1850. Before that, the temperature fluctuated a lot
and there is no clear trend.
- Pearson’s correlation coefficient between
the global 10-year moving average and the
one for New York city is p=0.79 indicating
that there is indeed a correlation between
both temperatures.


# Module 2 Final Project

The task is to use data from the King County housing market to make a model that can predict housing prices. In order to determine the most valuable ways to use this model I broke the questions of this project into three groups.

## When To Buy
What factors predict that a house is a good investment?
- Model v. Age grouped by other predictive variables
- Predict age of highest potential (when slope is highest positive, or zero and at the bottom)

- predicted Value over time
- what month should we buy?

## When To Sell 
What factors predict a house is at peak value?
- Model v. Age visual grouped by other predictive variables
- predict age of minimal potential (when slope is 0 and at the top)

## Valuation
After we've made a decision about buying or selling, how should we value the house in the market?

## Hypothesis Testing
Using the model I create I want to test the hypothesis that the largest houses in a neighborhood are less valuable than their peers, holding all else equal. 

# Description of Data
The data contained 21597 entries with 21420 unique houses sold in the King County during 2014 and 2015. Sale prices in the set range from $78,000 to $7,700,000 with a mean of $540,296, median of $450,000 and standard deviation of $367,368. Houses in the sample range from brand new to 115 years old, with a mean age of 43.3 and standard deviation of 29.38 years.  

After data exploration, I chose to drop outliers in these categories: 
 - Price- Houses that sold for more than $1,160,000 (5% of the data, 1458 entries)
 - Bedrooms- Houses with more than 8 bedrooms (8 of the remaining entries)
 - sqft_above- Houses with more than 4750 sqft of space above ground (20 of the remaining entries)
 - sqft_living- Houses with more than 5146 sqft of total living space (20 of the remaining entries)
 - sqft_lot- Houses with more than 19965 sqft lot (2046 of the remaining entries)
 - sqft_lot15- 
 
##### *Note*
There is a large sample of data with very large lot sizes. Potentially, this is farm land or something like it. For future projects this slice of data could be useful for predicting more rural home values. In this analysis, I am focusing on houses with lot sizes closer to the mean.

Ultimately, for this analysis the data contained 18338 entries with 18178 unique houses. Sale prices in the set range from $78,000 to $1,150,000 with a mean of $468,707, median of $427,500 and standard deviation of $206,927.

The data was split into a train test split with a test size of .2. To allow for reproducablity, the random state used for the split was 37.   

# Added Features
Based on the questions posed in the analysis, I chose to add these features to the data:
- age of house at point of sale
- distance from house to each of 6 major cities in the County
- size relative to nearest fifteen neighbors

# Establish a Baseline Model
After standardizing the variables, the baseline model recorded a K-Fold r-squared of (.8125). Against the test set, r-squared was (.8242) and the mean squared error was (.1844). The MSE of the training group was (.1807), meaning a difference of (.0037).  

# Train the Model

# Create Visuals
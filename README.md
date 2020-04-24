
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
The data contained 21597 entries with 21420 unique houses sold in the King County during 2014 and 2015. Sale prices in the set range from $78,000 to $7,700,000 with a mean of $540,296, median of $450,000 and standard deviation of $367,368.  

After data exploration, I chose to drop outliers in these categories: 
 - Price- Houses that sold for more than $1,160,000 (5% of the data, 1458 entries)
 - Bedrooms- Houses with more than 8 bedrooms (8 of the remaining entries)
 - sqft_above- Houses with more than 4750 sqft of space above ground (20 of the remaining entries)
 - sqft_living- Houses with more than 5146 sqft of total living space (20 of the remaining entries)
 - sqft_lot- Houses with more than 19965 sqft lot (2046 of the remaining entries)
 - sqft_lot15- 
 
##### --Note-- There is a large sample of data with very large lot sizes. Potentially, this is farm land or something like it. For future projects this slice of data could be useful for predicting more rural home values. In this analysis, I am focusing on houses with lot sizes closer to the mean.

Ultimately, for this analysis the data contained 18338 entries with 18178 unique houses. Sale prices in the set range from $78,000 to $1,150,000 with a mean of $468,707, median of $427,500 and standard deviation of $206,927.

The data was split into a train test split with a test size of .2. To allow for reproducablity, the random state used for the split was 37.   

# Added Features
Based on the questions posed in the analysis, I chose to add these features to the data:
- age of house at point of sale
- distance from house to each of 6 major cities in the County
- size relative to nearest fifteen neighbors

# Establish a Baseline Model
After standardizing the variables, the baseline model recorded an r-squared of (.8536) against the training set along with a MSE of (.1455). Against the test set, r-squared was (.8458) and the MSE was (.1578). The difference of (.0122) for the MSE of the training and test groups suggests that the model is not overfit.  

Observing this plot:

******

It showed that although the residuals were dispersed fairly evenly, the sudden downward slope at higher prices suggested that the model may be more acurate after training with some added features. 

# Train the Model
In order to train the model I used the following steps:
Find and included interactions.
Find and included polynomial relationships.
Variable Selection.

## Interaction Features
Through an iterative process designed to find the interactions that most highly impacted the MSE of the model I determined 6 interaction features were worthy of inclusion in the final model. 

1. lat and dist_to_Seattle
2. grade and dist_to_Seattle
3. sqft_living and dist_to_Seattle
4. sqft_living15 and dist_to_Seattle
6. long and dist_to_Seattle
6. lat and long


1. sqft_living, sqft_living15, grade and dist_to_Seattle: as distance to Seattle increases, the gap between the price of large homes and small homes decreases. This makes sense, as large homes in higher density areas are likely to cost more relative to similar sized homes in lower density areas. 
2. lat, long and dist_to_Seattle: homes get more valuable as they approach Seattle from any direction, therefore this interaction exists.
3. lat and long: a classic example of a interaction, clearly lattitude and longitude mean more combined then they do apart.   

After including the 6 interaction features, the model(model2) recorded an r-squared of (.8633) against the training set along with a MSE of (.1359). Against the test set, r-squared was (.8551) and the MSE was (.1482). The difference of (.0123) for the MSE of the training and test groups suggests that the model is not overfit, however, it's fit is slightly less generalizable compared to the baseline. Considering substantial improvements in all other metrics, I moved forward with model2. 

## Polynomial Features

# Create Visuals
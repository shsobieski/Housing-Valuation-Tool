
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
The data contained 21597 entries with data on houses sold in King County during 2014 and 2015. Sale prices in the set range from $78,000 to $7,700,000 with a mean of $540,296, median of $450,000 and standard deviation of $367,368.  

During data exploration I found outlier values and tested for linearity of the relationship between the independent variables and the dependent variables.

### Notable Findings:
- A relatively small number of houses with extremely large prices were skewing the sample.
- Lot Square footage does not appear to have a significant relationship with price after accounting for outliers and will be removed from the analysis. 
- Condition has no apparent relationship with price and will be dropped from the analysis.
- Houses East of -121.783 degrees longitude were dropped from this analysis because they accounted for only 1% of the data and were causing skew. All houses are within 32.16 miles of Seattle city center.

*--Note-- There is a very large sample of data with large lot sizes that has a noticably different relationship with price. Potentially, this is farm land or something like it. For future projects this slice of data could be useful for predicting more rural home values. Because these houses are so different I dropped these outliers even though I will  not be using lot size data in this analysis.


### Added Features
Based on the questions posed in the analysis, I chose to add these features to the data:
- age of house at point of sale
- distance from house to Seattle city center
- nearest city data for the 5 largest cities in the county
- sq footage relative to nearest fifteen neighbors

Ultimately, for this analysis the data contained 16565 entries with 16420 unique houses. Sale prices in the set range from $80,000 to $974,350 with a mean of $452,234 median of $420,000 and standard deviation of $186,680.

The data was split into a train test split with a test size of .2. To allow for reproducablity, the random state used for the split was 37.   


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

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
- Month the house was sold
- Age of the house at point of sale
- Number of years since the house has been renovated
- Whether the house had been renovated at all
- Distance from house to Seattle city center
- Nearest city data for the 5 largest cities in the county
- Square footage relative to nearest fifteen neighbors

Ultimately, for this analysis the data contained 16261 entries. Sale prices in the set range from $80,000 to $974,350 with a mean of $451,089 median of $420,000 and standard deviation of $185,546.

The data was split into a train test split with a test size of .2. To allow for reproducablity, the random state used for the split was 37.   


# Establish a Baseline Model
After standardizing the variables, the baseline model recorded an r-squared of (.7500) against the training set along with a MSE of (.2499). In 10-Fold KFold crossvalidation, it recorded an r-squared of (.7487). Against the test set, r-squared was (.7657) and the MSE was (.2348). The difference of (.0151) for the MSE of the training and test groups suggests that the model is not overfit.  

High impact variables included: dist_to_Seattle and WaterFront
Low impact variables included: floors

#### Model 1 Residuals Against Test Data

![](figures/Model1Resids.png)

Based on the KDE plot of residuals, it is clear that the model could be more generalizable, especially for high value homes.

# Train the Model
In order to train the model I used the following steps:
1. Find and included interactions.
2. Find and included polynomial relationships.
3. Selected for statistically significant variables.

## Interaction Features
Through an iterative process designed to find the interactions that most highly impacted the MSE of the model I determined 7 interaction features were worthy of inclusion in the final model. Full details can be found in the model training notebook. The general trend was geographic interactions. (e.g. as dist_to_Seattle and lat, which describes the fact that prices rise when approaching Seattle from the North or the South)  

After including the 7 interaction features, the model(model2)  recorded an r-squared of (.8009) against the training set along with a MSE of (.1990). In 10-Fold KFold crossvalidation, it recorded an r-squared of (.7993). Against the test set, r-squared was (.8147) and the MSE was (.1857). The difference of (.01331) for the MSE of the training and test groups suggests that the model is not overfit.

High impact Variables included: dist_to_Seattle, WaterFront, Federal Way, and long * Seattle
Low impact Variables included: long * dist_to_Seattle

#### Model2 Residuals Against Test Data

![](figures/Model2Resids.png)

Based on the KDE plot of residuals, there is improvement for high values homes, and residuals appear to be reduced. 

## Polynomial Features
Through an iterative process designed to find the polynomial relationships between the independent and dependent variables, I determined polynomial factors to include as features in the model. Full details can be found in the model training notebook. 

After including the new features, the model(model3)  recorded an r-squared of (.8337) against the training set along with a MSE of (.1605). In 10-Fold KFold crossvalidation, it recorded an r-squared of (.8296). Against the test set, r-squared was (.8398) and the MSE was (.1605). The difference of (.0057) for the MSE of the training and test groups suggests that the model is not overfit.

#### Model3 Residuals Against Test Data

![](figures/Model3Resids.png)

Based on the KDE plot of residuals, there is improvement for high values homes, and residuals appear to be reduced. 

## Variable Selection By P-Values
Through stepwise selection, I determined features that had statistically significant relationships at an alpha of .05. 

After excluding insignificant features, the model(model4)  recorded an r-squared of (.8315) against the training set along with a MSE of (.1684). In 10-Fold KFold crossvalidation, it recorded an r-squared of (.8294). Against the test set, r-squared was (.8389) and the MSE was (.1614). The difference of (.0070) for the MSE of the training and test groups suggests that the model is not overfit.

#### Model4 Residuals Against Test Data

![](figures/Model4Resids.png)

Based on the KDE plot of residuals, there is improvement for high values homes, and residuals appear to be reduced. 

# Analysis
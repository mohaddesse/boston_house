### Boston House Pricing Prediction
in this project first we have exploratary data analysis like check linearity, eliminate outliers, check normality,Homoscedasticity ....
then modeling data with these alogorithms:
1. Linear Regression
2. Random Forest Regressor
3. Ridge Regression
4. XGB Regressor
5. Recursive Feature Elimination (RFE) with Random Forest
and finally we compare R2 score rmse and cross validation to choose best model.

check linear regression assumptions:

**1. linearity**

This assumes that there is a linear relationship between the predictors (e.g. independent variables or features) and the response variable (e.g. dependent variable or label). This also assumes that the predictors are additive.

**2. Mean of Residuals**

Residuals as we know are the differences between the true value and the predicted value. One of the assumptions of linear regression is that the mean of the residuals should be zero. So let's find out

**3. Normality of the Error**

More specifically, this assumes that the error terms of the model are normally distributed. Linear regressions other than Ordinary Least Squares (OLS) may also assume normality of the predictors or the label, but that is not the case here.
there are several ways to check normality:

  - normaltest
  - normal_ad
  - qqplot
  - boxplot
  - Shapiro-Wilk Test
  
  **4. multicollinearity**
  
  In regression, multicollinearity refers to the extent to which independent variables are correlated. Multicollinearity affects the coefficients and p-values, but it does not influence the predictions, precision of the predictions, and the goodness-of-fit statistics. If your primary goal is to make predictions, and you don’t need to understand the role of each independent variable, you don’t need to reduce severe multicollinearity.

**5.No Autocorrelation of the Error**

In a time series scenario, there could be information about the past that we aren’t capturing. In a non-time series scenario, our model could be systematically biased by either under or over predicting in certain conditions. Lastly, this could be a result of a violation of the linearity assumption.
  - detected by durbin_watson
  
**6. Homoscedasticity**

This assumes homoscedasticity, which is the same variance within our error terms. Heteroscedasticity, the violation of homoscedasticity, occurs when we don’t have an even variance across the error terms.
  - detected by residual plot
  
  
 ### the result of modeling for various algorithms 
  
![Screenshot from 2022-12-18 00-00-35](https://user-images.githubusercontent.com/36596572/208265204-5687c548-6616-43ba-bdfa-e1c8732ce3a7.png)
![Screenshot from 2022-12-18 00-00-45](https://user-images.githubusercontent.com/36596572/208265207-ab6c07f4-8968-4766-b84c-5224314891c9.png)




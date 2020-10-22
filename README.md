# Kings County Housing Price Predictions

![download.jpg](attachment:download.jpg)

***BUSINESS PROBLEM***  

The business problem is simple: how can we best predict the house prices contained within the holdout data set? 

In order to tackle that problem, we were given access to the following information about just under 18,000 houses in the Kings County area:

* **id** - unique ID for a house
* **date** - Date day house was sold
* **price** - Price is prediction target
* **bedrooms** - Number of bedrooms
* **bathrooms** - Number of bathrooms
* **sqft_living** - square footage of the home
* **sqft_lot** - square footage of the lot
* **floors** - Total floors (levels) in house
* **waterfront** - Whether house has a view to a waterfront
* **view** - Number of times house has been viewed
* **condition** - How good the condition is (overall)
* **grade** - overall grade given to the housing unit, based on King County grading system
* **sqft_above** - square footage of house (apart from basement)
* **sqft_basement** - square footage of the basement
* **yr_built** - Year when house was built
* **yr_renovated** - Year when house was renovated
* **zipcode** - zip code in which house is located
* **lat** - Latitude coordinate
* **long** - Longitude coordinate
* **sqft_living15** - The square footage of interior housing living space for the nearest 15 neighbors
* **sqft_lot15** - The square footage of the land lots of the nearest 15 neighbors

![download.png](attachment:download.png)

**REPOSITORY STRUCTURE**

This repository is structured as follows: 

- archive: contains all the behind-the-scenes work of the final notebook. This is the place where I have placed all of my exloratory data analysis, my cleaning, and my model iterations.

- data: contains the data on Kings Country houses that was used in the making of the final model. It also contains the holdout data set in which the final model is intended to blindly predict prices on as the holdout set does not contain a price column.

- final_notebook: contains the polished and interactive version of my model where you can add features and take away features by commentings and uncommenting them out.

- holdout_set: contains predictions on the holdout data set.

- function.py: where all functions are contained for cleanliness purposes




## Final notebook

Through the modeling process, you will try many different techniques (**feature engineering** and **feature selection**, for example) to try and create your best model. Some will work and some will not lead to a better model. Through your modeling process, you will identify what actions create the best model. After you have finalized your process, you must create a 'cleaned up' and annotated notebook that shows your process.

Your notebook must include the following:

- **Exploratory Data Analysis (EDA):** You must create **at least 4 data visualizations** that help to explain the data. These visualizations should help someone unfamiliar with the data understand the target variable and the features that help explain that target variable.

- **Feature Engineering:** You must create **at least 3 new features** to test in your model. Those features do not have to make it into your final model, as they might be removed during the feature selection process. That is expected, but you still need to explain the features you engineer and your thought process behind why you thought they would explain the selling price of the house.  

- **Statistical Tests:** Your notebook must show **at least 3 statistical tests** that you preformed on your data set. Think of these as being part of your EDA process; for example, if you think houses with a view cost more than those without a view, then perform a two-sample T-test. These can be preliminary evidence that a feature will be important in your model.  

- **Feature Selection:** There are many ways to do feature selection: filter methods, P-values, or recursive feature elimination (RFE). You should try multiple different techniques and combinations of them. For your final model, you will **settle on a process of feature selection**; this process should be **clearly shown in your final notebook**.

- **Model Interpretation:** One of the benefits of a linear regression model is that you can **interpret the coefficients** of the model **to derive insights**. For example, which feature has the biggest impact on the price of the house? Was there a feature that you thought would be significant but was not? Think if you were a real estate agent helping clients price their house: what information would you find most helpful from this model?

## GitHub Repository

A GitHub repo is a good way to keep track of your work, but also to display the work you did to future employers. Your GitHub should contain the following:

- A `README.md` that briefly describes the project and the files within the repo.
- Your cleaned and annotated notebook showing your work.
- A folder with all of your 'working' notebooks where you played around with your data and the modeling process.

## Data Set Information

This data set contains information about houses that were sold in the Seattle area during the last decade. Below is a description of the column names, to help you understand what the data represents. As with most real world data sets, the column names are not perfectly described, so you'll have to do some research or use your best judgment if you have questions relating to what the data means. 

Like every data set, there are some irregularities and quirks. Trust me, there wasn't a house sold with 33 bedrooms, even though the data says there was. *You have to decide how you want to handle that example*. Also, some houses were sold more than once within the time frame of this dataset. Think about how that can be useful information in predicting the selling price.

As you go through this modeling process, think about what determines how much someone will pay for a house.  For example, the larger the house is, the more people will pay for it. If you understand why certain houses cost more than others and represent that in your model, it will be a more accurate model.  

Have fun!

# Column Names and descriptions for Kings County Data Set
* **id** - unique ID for a house
* **date** - Date day house was sold
* **price** - Price is prediction target
* **bedrooms** - Number of bedrooms
* **bathrooms** - Number of bathrooms
* **sqft_living** - square footage of the home
* **sqft_lot** - square footage of the lot
* **floors** - Total floors (levels) in house
* **waterfront** - Whether house has a view to a waterfront
* **view** - Number of times house has been viewed
* **condition** - How good the condition is (overall)
* **grade** - overall grade given to the housing unit, based on King County grading system
* **sqft_above** - square footage of house (apart from basement)
* **sqft_basement** - square footage of the basement
* **yr_built** - Year when house was built
* **yr_renovated** - Year when house was renovated
* **zipcode** - zip code in which house is located
* **lat** - Latitude coordinate
* **long** - Longitude coordinate
* **sqft_living15** - The square footage of interior housing living space for the nearest 15 neighbors
* **sqft_lot15** - The square footage of the land lots of the nearest 15 neighbors

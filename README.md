## Advise
Do not use this with investor purposes, this can be used only with student proposals.

# Price predictor - Main app and API

The main part of the application for predicting cryptocurrency prices.
Here is placed the application API, which contains 3 endpoints (server information, prediction with information whether to buy or sell, prediction with information when to buy, sell and what will be the profit).

## Installation

Command to run: `docker compose up`


### Part of README from price_predictor

The script is responsible for prediction of cryptocurrency price values. When the script is running, a DataFrame object is prepared, of which the price is also a set `X`, and a price column is created as a set `y` which is an offset of the column from the set `X` by the specified number of days (by default 30 days). 

Next, the `X_predict` object is created, containing data on the basis of which the prediction will be made (by default, it is the last 30 days from the set `X`, for which the newly created object `y` has zero values resulting from the shift.
The `SVR (Support Vector Regression)` model is then created from the scikit-learn library and learned.

A prediction based on the variable `X_predict` is performed on the learned model.

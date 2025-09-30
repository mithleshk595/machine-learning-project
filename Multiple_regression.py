# import pandas
# from sklearn import linear_model

# df = pandas.read_csv("data.csv")

# X = df[["Weight", "Volume"]]
# y = df["CO2"]

# regr = linear_model.linearRegression()
# regr.fit(X ,y)

# # predict CO2 emission for a car with weight of 3300lbs and volume of 1300cc
# predictedCO2 = regr.predict([[3300, 1300]])
# print(predictedCO2)


import pandas as pd
from sklearn import linear_model

# Load CSV file
df = pd.read_csv("data.csv")

# Define features and target
X = df[["Weight", "Volume"]]
y = df["CO2"]

# Create linear regression model
regr = linear_model.LinearRegression()
regr.fit(X, y)

# Predict CO2 emission for a car with weight 3300 lbs and volume 1300 cc
predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2)


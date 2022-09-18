import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
Data=pd.read_csv("CatData.csv")
Data=Data.dropna(axis=0,how="any")
# dependant variable: Tail Length (cm)
# independant variable: Mass (kg)
Data=Data[["Tail Length (cm)","Mass (kg)"]]
print(Data.head())
#Taking 80% data for training data:
num=int(len(Data)*0.8)
#training data:
train=Data[:num]
#testing data:
test=Data[num:]
print("Whole Data",len(Data))
print("train Data",len(train))
print("test Data",len(test))
#slope and intercepts:
actual_slope,actual_intercept=(train["Tail Length (cm)"],train["Mass (kg)"])
print("Slope: ",actual_slope)
print("Intercept: ",actual_intercept)
#plotting scatter graph and regression line:
plt.scatter(Data["Tail Length (cm)"],Data["Mass (kg)"])
plt.xlabel("Mass (kg)")
plt.ylabel("Tail Length (cm)")
plt.show()
plt.scatter(Data["Tail Length (cm)"],Data["Mass (kg)"])
plt.plot(train["Tail Length (cm)"],actual_slope*train["Tail Length (cm)"]+actual_intercept,color="red")
plt.xlabel("Mass (kg)")
plt.ylabel("Tail Length (cm)")
plt.show()


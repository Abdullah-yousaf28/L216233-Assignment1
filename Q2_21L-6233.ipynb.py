import pandas as pd
Data=pd.read_csv("StudentMarkSheet.csv")
Data.info()
print("\nNumber of rows BEFORE containing NULL data:\n")
print(Data.iloc[0:47])
print("\nNumber of rows containing NULL data:\n")
print(Data[Data.isna().any(axis=1)])
print("\nNumber of rows AFTER containing NULL data:\n")
print(Data.iloc[189:201])
Data=Data.dropna(axis=0,how="any")
print("\nData of JAMES WALKER:\n")
print(Data.iloc[0])
print(Data.iloc[42])
print(Data.iloc[70])
print(Data.iloc[147])
print(Data.iloc[177])




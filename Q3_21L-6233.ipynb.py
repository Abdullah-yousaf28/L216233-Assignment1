import pandas as pd
import matplotlib.pyplot as plt
Data=pd.read_csv("StudentMarkSheet.csv")
Data=Data.dropna(axis=0,how="any")
print("Average Marks Of Biology Subject\n")
print(Data.iloc[0:38].mean())
print("\nAverage Marks Of Chemistry Subject\n")
print(Data.iloc[38:64].mean())
print("\nAverage Marks Of Mathematics Subject\n")
print(Data.iloc[64:100].mean())
print("\nAverage Marks Of Philosophy Subject\n")
print(Data.iloc[100:137].mean())
print("\nAverage Marks Of Physics Subject\n")
print(Data.iloc[137:158].mean())
print("\nAverage Marks Of Sociology Subject\n")
print(Data.iloc[158:200].mean())
print(Data.plot.bar(x='Exam name',y='Marks',rot=0))


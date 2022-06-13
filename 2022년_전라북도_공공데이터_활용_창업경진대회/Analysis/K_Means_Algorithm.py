import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

df = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/jj.csv", encoding="euc-kr")

print(df)
for i in range(len(df)):
    plt.scatter(df["위도"], df["경도"])

plt.grid(linestyle="--")
plt.show()

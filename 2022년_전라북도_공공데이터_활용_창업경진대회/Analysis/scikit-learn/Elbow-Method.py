from sklearn.cluster import KMeans

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/공공데이터포털/child_house.csv", encoding="euc-kr")
data = {"x" : df["경도"], "y" : df["위도"]}
points = pd.DataFrame(data)

inertia = []
for i in range(1, 50):
    kmeans_plus = KMeans(n_clusters=i, init='k-means++')
    kmeans_plus.fit(points)
    inertia.append(kmeans_plus.inertia_)

plt.plot(range(1, 50), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
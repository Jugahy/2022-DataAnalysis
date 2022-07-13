from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/공공데이터포털/전북_통합.csv", encoding="euc-kr")
data = {"x" : df["경도"], "y" : df["위도"]}
points = pd.DataFrame(data)

silhouette_vals = []
for i in range(2, 200):
    kmeans_plus = KMeans(n_clusters=i, init='k-means++')
    pred = kmeans_plus.fit_predict(points)
    silhouette_vals.append(np.mean(silhouette_samples(points, pred, metric='euclidean')))

plt.plot(range(2, 200), silhouette_vals, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette')
plt.show()
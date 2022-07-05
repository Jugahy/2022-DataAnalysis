from sklearn.cluster import KMeans
import pandas as pd
from sklearn.datasets import make_blobs
import seaborn as sns
import matplotlib.pyplot as plt


# DataFrame 생성
df = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/공공데이터포털/전북_통합.csv", encoding="euc-kr")
data = {"x" : df["경도"], "y" : df["위도"]}
points = pd.DataFrame(data)

# k-means clustering 실행
kmeans = KMeans(n_clusters=3)
kmeans.fit(points)

# 결과 확인
result_by_sklearn = points.copy()
result_by_sklearn["cluster"] = kmeans.labels_
result_by_sklearn.head()

sns.scatterplot(x="x", y="y", hue="cluster", data=result_by_sklearn, palette="Set2")
plt.show()

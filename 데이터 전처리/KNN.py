import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# feature = Iris-Setosa, Iris-Versicolour, Iris-Virginica


# 사용할 데이터 호출
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler

iris = load_iris()

# DataFrame으로 만들기
df = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, dtype="category")
y = y.cat.rename_categories(iris.target_names)
df["species"] = y


# seaborn의 pairplot를 사용하여 각 column별 데이터에 대한 상관관계나 분류적 특성을 확인
# sns.pairplot(df, hue="species")
# plt.show()


# Boxplot를 사용하여 outlier 찾기
# df.boxplot()
# plt.show()


# train과 test data를 0.75 : 0.25 비율로 나눈다
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:-1], df.iloc[:,-1], random_state=3)

ms = MinMaxScaler()
X_train_m = pd.DataFrame(ms.fit_transform(X_train), columns = X_train.columns)
X_test_m = pd.DataFrame(ms.transform(X_test), columns = X_test.columns)

knn_m = KNeighborsClassifier(n_neighbors=4)
knn_m.fit(X_train_m, y_train)

scores = cross_val_score(knn_m, X_train, y_train, cv=10)
print('*** Cross val score *** \n   {}'.format(scores))
print('\n*** Mean Accuracy *** \n   {:.7f}'.format(scores.mean()))
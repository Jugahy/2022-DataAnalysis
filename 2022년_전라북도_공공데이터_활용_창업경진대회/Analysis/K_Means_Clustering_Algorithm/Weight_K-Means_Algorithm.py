import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager, rc

# 한국어
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

data = []

df = pd.read_csv("/Data/공공데이터포털/jj.csv", encoding="euc-kr")

k = [4, 12]
weight = [0.143854161, 0.152846585, 0.015943407, 0.052058502, 0.015189446, 0.013618205, 0.050226951, 0.345446743, 0.063799425, 0.032516483, 0.017644803, 0.046635375, 0.033735954, 0.016483961]

for i, j in zip(df["위도"], df["경도"]):
    data.append([i, j])


def cluster():
    import math

    global remember_group

    distance = []
    group = []
    remember_group = []

    for i in range(len(data)):
        distance.append([])

        for j in k:
            distance[i].append(weight[j] * math.sqrt((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2))

    for i in range(len(data)):
        group.append(k[distance[i].index(min(distance[i]))])

    remember_group = group
    print("asd" ,distance)

    return remember_group


def mid():
    global new_mid
    global remember_group
    try:
        remember_group = group
    except NameError:
        pass
    all_mid = []
    new_mid = []

    all_mid.append([])
    all_mid.append([])

    for i in range(len(k)):
        new_mid.append([])

        for j in [l for l, x in enumerate(remember_group) if x == k[i]]:
            all_mid[0].append(data[j][0])
            all_mid[1].append(data[j][1])

        new_mid[i].append(sum(all_mid[0]) / remember_group.count(k[i]))
        new_mid[i].append(sum(all_mid[1]) / remember_group.count(k[i]))

        all_mid[0] = []
        all_mid[1] = []
    return new_mid

print(cluster())
print(mid())

# 1

import math

reremember_group = []
count = 0


distance = []
group = []


for i in range(len(data)):
    distance.append([])
    kk = [5, 10]
    for kkk, j in zip(kk, new_mid):
        distance[i].append(weight[kkk] * math.sqrt((data[i][0] - j[0]) ** 2 + (data[i][1] - j[1]) ** 2))
print(distance)
for i in range(len(data)):
    group.append(k[distance[i].index(min(distance[i]))])

reremember_group = group
print(mid())




# 2
import math

reremember_group = []
count = 0


distance = []
group = []


for i in range(len(data)):
    distance.append([])
    kk = [5, 11]
    for kkk, j in zip(kk, new_mid):
        distance[i].append(weight[kkk] * math.sqrt((data[i][0] - j[0]) ** 2 + (data[i][1] - j[1]) ** 2))
print(distance)
for i in range(len(data)):
    group.append(k[distance[i].index(min(distance[i]))])

reremember_group = group
print(mid())


# 3

import math

reremember_group = []
count = 0


distance = []
group = []


for i in range(len(data)):
    distance.append([])
    kk = [11, 12]
    for kkk, j in zip(kk, new_mid):
        distance[i].append(weight[kkk] * math.sqrt((data[i][0] - j[0]) ** 2 + (data[i][1] - j[1]) ** 2))
print(distance)
for i in range(len(data)):
    group.append(k[distance[i].index(min(distance[i]))])

reremember_group = group
print(mid())


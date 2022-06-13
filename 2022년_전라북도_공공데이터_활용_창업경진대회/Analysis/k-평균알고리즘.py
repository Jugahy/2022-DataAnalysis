import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

one_distance = []
two_distance = []
group = []
remember_group = []

# 좌표 표현
data = [[1, 2], [3, 5], [3, 2], [2, 1], [4, 2], [2, 3], [4, 4], [4, 5], [5, 5], [5, 1]]

# 군집 수 선택
k = [0, 4]
one_mid = 0
two_mid = 0

new_one_mid = 0
new_two_mid = 0
# 연산
for i in range(100):
    for i in range(len(data)):

        # 군집 나누는 기준
        one_distance.append(math.sqrt((data[i][0] - data[k[0]][0]) ** 2 + (data[i][1] - data[k[0]][1]) ** 2))
        two_distance.append(math.sqrt((data[i][0] - data[k[1]][0]) ** 2 + (data[i][1] - data[k[1]][1]) ** 2))

        # 군집 나누기
        if one_distance[i] > two_distance[i]:
            group.append(2)
        else:
            group.append(1)

    # 군집의 변화가 없다면 멈춤
    if remember_group == group:
        break

    # 현재 군집 기억해주는 군집
    remember_group = group

    # 새로운 평균값 구하기
    for q in range(len(group)):
        if group[q] == 1:
            one_mid.append(data[q][0])
        else:
            two_mid.append(data[q][1])

    new_one_mid = sum(one_mid)/len(one_mid)
    new_two_mid = sum(two_mid)/len(two_mid)

print(new_one_mid)
print(new_two_mid)




# for i in range(len(data)):
#     plt.scatter(data[i][0], data[i][1], color="black")
#
# plt.show()

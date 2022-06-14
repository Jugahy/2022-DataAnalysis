import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from matplotlib import font_manager, rc

# 한국어 사용가능하게 하기
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 전라북도 지역별 위도 경도 읽어오기
df = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/jj.csv", encoding="euc-kr")

# 리스트 생성
one_distance = []
two_distance = []
group = []
remember_group = []
data = []
city = ["군산시", "익산시", "진안군", "완주군", "무주군", "장수군", "김제시", "전주시", "정읍시", "부안군", "임실군", "남원시", "고창군", "순창군"]

# 좌표 표현
for i, j in zip(df["위도"], df["경도"]):
    data.append([i, j])

print(data)

# 군집 선택
k = [4, 5]

# 새로운 평균값
one_mid_x = 0
one_mid_y = 0
two_mid_x = 0
two_mid_y = 0

# 처음 주어진 좌표에서 평균값 구하는 연산
for i in range(len(data)):

    # 군집 나누는 기준
    one_distance.append(math.sqrt((data[i][0] - data[k[0]][0]) ** 2 + (data[i][1] - data[k[0]][1]) ** 2))
    two_distance.append(math.sqrt((data[i][0] - data[k[1]][0]) ** 2 + (data[i][1] - data[k[1]][1]) ** 2))

    # 군집 나누기
    if one_distance[i] > two_distance[i]:
        group.append(2)
    else:
        group.append(1)

# 현재 군집 기억해주는 군집
remember_group = group

# group 뽑았으니 리스트 비워주기
one_distance = []
two_distance = []

# 몇 번 시행하여 군집 나누는지 보기
count = 0

# 계속해서 group 유지하게 만드는 연산
for w in range(100):
    count += 1

    # 새로운 평균값 구하기
    for i in range(len(group)):
        if group[i] == 1:
            one_mid_x += data[i][0]
            one_mid_y += data[i][1]
        else:
            two_mid_x += data[i][0]
            two_mid_y += data[i][1]

    new_one_mid_x = one_mid_x / group.count(1)
    new_one_mid_y = one_mid_y / group.count(1)
    new_two_mid_x = two_mid_x / group.count(2)
    new_two_mid_y = two_mid_y / group.count(2)

    # 중첩되는 것이니 초기화
    one_mid_x = 0
    one_mid_y = 0
    two_mid_x = 0
    two_mid_y = 0
    one_distance = []
    two_distance = []

    # group 다 썻으니 초기화
    group = []

    for i in range(len(data)):
        # 군집 나누는 기준
        one_distance.append(math.sqrt((data[i][0] - new_one_mid_x) ** 2 + (data[i][1] - new_one_mid_y) ** 2))
        two_distance.append(math.sqrt((data[i][0] - new_two_mid_x) ** 2 + (data[i][1] - new_two_mid_y) ** 2))

        # 군집 나누기
        if one_distance[i] > two_distance[i]:
            group.append(2)
        else:
            group.append(1)

    for idx, i in enumerate(city):
        plt.scatter(data[idx][0], data[idx][1], color="black")
        plt.annotate(i, (data[idx][0], data[idx][1]))

    plt.scatter(new_one_mid_x, new_one_mid_y, color="red")
    plt.scatter(new_two_mid_x, new_two_mid_y, color="red")
    plt.show()

    # 군집의 변화가 없다면 멈춤
    if remember_group == group:
        print("전 그룹과 현재 그룹이 같으므로 프로그램 종료")
        break

    # 현재 군집 기억해주는 군집
    else:
        remember_group = group


print("군집 1과의 거리 :", one_distance)
print("군집 2와의 거리 :", two_distance)
print("소속될 군집 :", group)
print("군집1의 x좌표 : %.2f, 군집1의 y좌표 : %.2f" % (new_one_mid_x, new_one_mid_y))
print("군집2의 x좌표 : %.2f, 군집2의 y좌표 : %.2f" % (new_two_mid_x, new_two_mid_y))
print(count)

# for i in range(len(data)):
#     plt.scatter(data[i][0], data[i][1], color="black")

# for idx, i in enumerate(city):
#     plt.scatter(data[idx][0], data[idx][1], color="black")
#     plt.annotate(i, (data[idx][0], data[idx][1]))
#
# plt.scatter(new_one_mid_x, new_one_mid_y, color="red")
# plt.scatter(new_two_mid_x, new_two_mid_y, color="red")
# plt.show()

def korean():
    from matplotlib import font_manager, rc

    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)


data = [[1, 2], [3, 5], [3, 2], [2, 1], [4, 2], [2, 3], [4, 4], [4, 5], [5, 5], [5, 1]]
k = [0, 4]



# 데이터 형식 : [[위도1,경도1], [위도2,경도2], ...[위도n,경도n]]
# k 형식 : data의 값 중 원하는 좌표의 인덱스 [0,8]
def put(data, k):
    # 새로운 평균값을 저장해 놓는 리스트 인덱스 0,1이 data
    mid_list = []
    for i in range(len(k) * 2):
        mid_list.append([0, 0])
    print(mid_list)


# data의 좌표를 이용할 때 군집 나누는 함수
def cluster():
    import math

    global remember_group

    distance = []
    group = []
    remember_group = []

    for i in range(len(data)):
        distance.append([])

        for j in k:
            distance[i].append(math.sqrt((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2))

    for i in range(len(data)):
        group.append(k[distance[i].index(min(distance[i]))])

    remember_group = group

    return remember_group


# 새로운 평균값 만드는 함수
def mid():
    global new_mid
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


# 새로운 평균값의 좌표를 이용할 때 군집 나누는 함수
def k_cluster():
    import math
    global group
    reremember_group = []
    while True:
        distance = []
        group = []


        for i in range(len(data)):
            distance.append([])

            for j in new_mid:
                distance[i].append(math.sqrt((data[i][0] - j[0]) ** 2 + (data[i][1] - j[1]) ** 2))
        print("distance :",distance)
        for i in range(len(data)):
            group.append(k[distance[i].index(min(distance[i]))])
        print(1, group, reremember_group)
        if remember_group == group:
            print(new_mid)
            break
        elif reremember_group == group:
            print(new_mid)
            break
        else:
            reremember_group = group
            print("mid :", mid())

    return group

print(cluster())
print(mid())
print(k_cluster())
# def main():
#     cluster()
#     mid()
#     k_cluster()
#     if remember_group == group:
#         print(new_mid)
#         print()
#         break

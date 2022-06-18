def korean():
    from matplotlib import font_manager, rc

    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)


data = [[1, 2], [3, 5], [3, 2], [2, 1], [4, 2], [2, 3], [4, 4], [4, 5], [5, 5], [5, 1]]
k = [0, 4, 6]


# 데이터 형식 : [[위도1,경도1], [위도2,경도2], ...[위도n,경도n]]
# k 형식 : data의 값 중 원하는 좌표의 인덱스 [0,8]
def put(data, k):
    # 새로운 평균값을 저장해 놓는 리스트 인덱스 0,1이 data
    mid_list = []
    for i in range(len(k) * 2):
        mid_list.append([0, 0])
    print(mid_list)


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


def mid():
    for i in range(len(data)):
        for j in range(len(k)):
            if remember_group[i] ==

cluster()

"""
이상값 : 중앙값에서 스케일링된 3 중앙값 절대 편차를 초과하여 떨어져 있는 값입니다.

    - 예시로 평균을 구할때 이상값이 존재하면 평균이 정확하지 않을 수 있습니다.
    - 이것을 방지하기 위해 이상값을 찾고 제거하는 작업을 합니다.
    - 작업으로는 이상치 검출 IQR (사 분위 범위) 방법이 있습니다.

IQR Method : 박스플롯 그래프는 사 분위 수(데이터를 동일한 사이즈의 4개 그룹으로 나누는 기준 점)를 사용하여 데이터의 모양을 표시합니다.

    - 박스는 25번째와 75번째 백분위 수와 같은 1사 분위수와 3사 분위수를 나타냅니다. 박스 중간에 있는 선은 중앙값인 2사 분위수를 나타냅니다.
"""


def outlier_iqr(data, column):
    # lower, upper 글로벌 변수 선언하기
    global lower, upper

    # 4분위수 기준 지정하기
    q25, q75 = np.quantile(data[column], 0.25), np.quantile(data[column], 0.75)

    # IQR 계산하기
    iqr = q75 - q25

    # outlier cutoff 계산하기
    cut_off = iqr * 1.5

    # lower와 upper bound 값 구하기
    lower, upper = q25 - cut_off, q75 + cut_off

    print('IQR은', iqr, '이다.')
    print('lower bound 값은', lower, '이다.')
    print('upper bound 값은', upper, '이다.')

    # 1사 분위와 4사 분위에 속해있는 데이터 각각 저장하기
    data1 = data[data[column] > upper]
    data2 = data[data[column] < lower]

    # 이상치 총 개수 구하기
    return print('총 이상치 개수는', data1.shape[0] + data2.shape[0], '이다.')

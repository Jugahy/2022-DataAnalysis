"""
# 모든 결측값 확인
data.isnull()


# 결측값 개수 세기
data.isnull().sum()


# 결측값 특정 문자로 채우기
data.fillna("*")


# 결측값 평균값으로 채우기
data.fillna(data.mean())


# 결측값 중간값으로 채우기
data.fillna(data.median())


# 결측값 그룹별 평균값으로 채우기
lambda g: g.fillna(g.mean())data.groupby("grp").apply(fill_mean_func)


# 결측값 특정 열에서 가장 많은 값으로 치환
most_value = data["embarked"].value_counts(dropna=True).idxmax()  # 빈도 수 높은 값 찾기
data["embarked"].fillna(most_value, inplace=True)  # 결측값에 채우기


# 결측값 행 또는 열 삭제
data.dropna(axis=0)
data.dropna(axis=1)


# 셀 값 전체가 결측값인 행 삭제
data.dropna(how="all")


# 결측값이 500개 이상이면 모두 삭제 (cabin, boat, body 삭제됨)
data.dropna(axis=1, thresh=500)


# 특정 칼럼 안에서만 삭제
data.dropna(subset=["body"])


# age열에 나이 데이터가 없는 모든 행을 삭제
data.dropna(subset=["age"], how="any", axis=0)
"""

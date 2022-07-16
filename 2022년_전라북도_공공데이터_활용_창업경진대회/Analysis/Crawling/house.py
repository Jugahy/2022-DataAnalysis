import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/공공데이터포털/pnu.csv", encoding="euc-kr")


# for i in range(len(df)):
#     num = df["읍면동코드"][i]
#     URL = "http://api.vworld.kr/req/data?key=8979E835-98C6-33B1-957D-BB6DEF17E8AD&domain=http://dev.vworld.kr/dev/v4dv_2ddataguide2_s002.do?svcIde=mgprtfa&service=data&version=2.0&request=getfeature&data=LT_P_MGPRTFA&attrfilter=emdcd:=:"+str(num)
#     result = requests.get(URL)
#     soup = BeautifulSoup(result.text, "html.parser")
#     print(soup)


num = df["읍면동코드"][2]
URL = "http://api.vworld.kr/req/data?key=8979E835-98C6-33B1-957D-BB6DEF17E8AD&domain=http://dev.vworld.kr/dev/v4dv_2ddataguide2_s002.do?svcIde=mgprtfa&service=data&version=2.0&request=getfeature&data=LT_P_MGPRTFA&attrfilter=emdcd:=:"+str(num)
result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
# print(soup)
idx = str(soup).find("fac_n_add")

r = str(soup)[idx:]
print(r)
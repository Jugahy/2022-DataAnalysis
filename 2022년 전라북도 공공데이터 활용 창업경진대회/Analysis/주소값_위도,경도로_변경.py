import pandas as pd
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')

data = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/전라북도_어린이집.csv", encoding="cp949")
pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)

address = data["소재지도로명주소"][1351]

# for i in range(len(address)):
#     a = address[i].split(' ')
#     address[i] = " ".join(a[0:5])
# print(address.head())

# 데이터 다듬기

# for i in [1383, 1354, 1339]:
#     split_data = address[i].split(" ")
#     del split_data[5:]
#     address[i] = " ".join(split_data)
#
# address[320] = "전라북도 전주시 덕진구 송천중앙로 100-3"
# address[1115] = "전라북도 남원시 수철길 4-14"

print(address)

# 주소를 위도, 경도로 변환
def geocoding(address):
    geo = geo_local.geocode(address)
    x_y = [geo.latitude, geo.longitude]
    return x_y




latitude = []
longitude = []

for i in address:
    latitude.append(geocoding(i)[0])
    longitude.append(geocoding(i)[1])

print(latitude, longitude)


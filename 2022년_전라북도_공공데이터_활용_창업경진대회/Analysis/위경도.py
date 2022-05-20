import pandas as pd

# 데이터 불러오기
data = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/전라북도_어린이집.csv", encoding="cp949")

# 모든 행, 열 보기
pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)


# 소재지도로명주소 잘못된 데이터 수정(copy 하지 않으면 기존의 데이터는 변하지 않는다고 애러 뜸
addr = data["소재지도로명주소"].copy()

for i in [1382, 1353, 1338]:
    split_data = addr[i].split(" ")
    del split_data[5:]
    addr[i] = " ".join(split_data)

addr[319] = "전라북도 전주시 덕진구 송천중앙로 100-3"
addr[1114] = "전라북도 남원시 수철길 4-14"

# ~길 ~-~ 만 출력 시키되 각 문자의 길이에 따라 다르게 해줌
for i in range(len(addr)):
    split_data = addr[i].split(" ")
    if len(split_data) == 4:
        addr[i] = " ".join(split_data[2:])
    elif len(split_data) == 5:
        addr[i] = " ".join(split_data[3:])
    else:
        addr[i] = " ".join(split_data[4:])

# 주소를 위도, 경도로 변경하기 위한 모듈
from Geopy_Module.geocoders import Nominatim

geolocator = Nominatim(user_agent='South Korea')

# 주소를 위도, 경도로 변경
# def geocoding(addr):
#     geo = geolocator.geocode(addr)
#     x_y = [geo.latitude, geo.longitude]
#     return x_y
#
#
# latitude = []
# longitude = []
#
# for i in addr:
#     latitude.append(geocoding(i)[0])
#     longitude.append(geocoding(i)[1])
#
# address_df = pd.DataFrame({'위도': latitude, '경도': longitude})
# print(address_df)
#
# geocoding(addr)
# try:
#     def geocoding(addr):
#         geo = geolocator.geocode(addr)
#         x_y = [geo.latitude, geo.longitude]
#
#         return x_y
#
#     latitude = []
#     longitude = []
#
#     for i in addr:
#         latitude.append(geocoding(i)[0])
#         longitude.append(geocoding(i)[1])
#
#
#     address_df = pd.DataFrame({'위도': latitude, '경도': longitude})
#     print(address_df)
#
# except AttributeError:
#     print(i)
#     pass


# 주소 하나만 예시로 해볼 때

# for i in addr:
#     try:
#         location = geolocator.geocode(i)
#         print(i, (location.latitude, location.longitude))
#     except AttributeError:
#         print(i)
#         pass


location = geolocator.geocode("척동1길 18-5")
print((location.latitude, location.longitude))

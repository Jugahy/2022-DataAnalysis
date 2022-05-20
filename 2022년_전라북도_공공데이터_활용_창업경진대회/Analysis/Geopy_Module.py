import pandas as pd
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent="South Korea")

data = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/전라북도_어린이집.csv", encoding="cp949")
pd.set_option("display.max_rows", None)

addr = data["소재지도로명주소"].copy()


# 데이터 다듬기

for i in [1383, 1354, 1339]:
    split_data = addr[i].split(" ")
    del split_data[5:]
    addr[i] = " ".join(split_data)

addr[320] = "전라북도 전주시 덕진구 송천중앙로 100-3"
addr[1115] = "전라북도 남원시 수철길 4-14"

for i in range(len(addr)):
    split_data = addr[i].split(" ")
    if len(split_data) == 4:
        addr[i] = " ".join(split_data[2:])
    elif len(split_data) == 5:
        addr[i] = " ".join(split_data[3:])
    elif len(split_data) == 6:
        addr[i] = " ".join(split_data[4:])
    elif len(split_data) == 7:
        addr[i] = " ".join(split_data[5:])

num = []
latitudes = []
longitudes = []

f = open("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/어린이집.csv", "w")
#
# for i in range(len(addr)):
#     try:
#         num.append(i)
#         location = geo_local.geocode(addr[i])
#         latitudes.append(str(location.latitude))
#         longitudes.append(str(location.longitude))
#     except AttributeError:
#         num.append(i)
#         latitudes.append(None)
#         longitudes.append(None)
for i in range(5):
    try:
        num.append(i)
        location = geo_local.geocode(addr[i])
        latitudes.append(str(location.latitude))
        longitudes.append(str(location.longitude))
    except AttributeError:
        num.append(i)
        latitudes.append(None)
        longitudes.append(None)


for i in range(len(latitudes)):
    f.write(latitudes[i] + ',' + longitudes[i] + '\n')

f.close()
# def geocoding(addr):
#     try:
#         geo = geo_local.geocode(addr)
#         x_y = [geo.latitude, geo.longitude]
#         return x_y
#     except AttributeError:
#         pass
#
# latitude = []
# longitude = []
# num = []
# try:
#     for i in addr:
#         num.append(i)
#         latitude.append(geocoding(i)[0])
#         longitude.append(geocoding(i)[1])
# except TypeError:
#     pass
#
# address_df = pd.DataFrame({'위도': latitude, '경도': longitude})
# print(address_df)
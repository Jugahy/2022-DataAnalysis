import requests, json, pandas as pd
from geopy.geocoders import Nominatim

geo_local = Nominatim(user_agent="South Korea")

pd.set_option('display.max_rows', None)
# Kakao 지오코드
def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    headers = {"Authorization": "KakaoAK b0fb3729d2fb8c9d30c1d622f364130d"}
    api_json = json.loads(str(requests.get(url, headers=headers).text))
    address = api_json['documents'][0]['address']
    crd = [str(address['y']), str(address['x'])]
    address_name = address['address_name']

    return crd


FileName = "C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/jjpark.csv"
data = pd.read_csv(FileName, encoding="euc-kr")
addr = data["주 소"].copy()


# for i in range(81):
#     try:
#         print(i+2,addr[i], get_location(addr[i]))
#     except IndexError:
#         print(i+2, addr[i])
#         pass


latitudes = []
longitudes = []
er = []
for i in range(len(addr)):
    try:
        crd = get_location(addr[i])
        latitudes.append(crd[0])
        longitudes.append(crd[1])
        print(i, addr[i], crd)
    except IndexError:
        try:
            location = geo_local.geocode(addr[i])
            latitudes.append(str(location.latitude))
            longitudes.append(str(location.longitude))
            print(i, addr[i], str(location.latitude))
        except AttributeError:
            latitudes.append(0)
            longitudes.append(0)
            print(i+2, addr[i])
            er.append(i+2)
            pass

data["위도"] = latitudes
data["경도"] = longitudes

print(data)
data.to_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/jjpark.csv", encoding="euc-kr")

print(er)
# print(latitudes)
# print(longitudes)
# for i in range(len(addr)):
#     split_data = addr[i].split(" ")
#     if len(split_data) == 2:
#         addr[i] = " ".join(split_data[0:])
#     elif len(split_data) == 3:
#         addr[i] = " ".join(split_data[1:])
#     elif len(split_data) == 4:
#         addr[i] = " ".join(split_data[2:])
#     elif len(split_data) == 5:
#         addr[i] = " ".join(split_data[3:])
#     elif len(split_data) == 6:
#         addr[i] = " ".join(split_data[4:])


# # 데이터 전처리
# def GetData(FileName):
#     global addr, data
#
#     data = pd.read_csv(FileName, encoding="euc-kr")
#     addr = data["주 소"].copy()
#
#     # for i in [1383, 1354, 1339]:
#     #     split_data = addr[i].split(" ")
#     #     del split_data[5:]
#     #     addr[i] = " ".join(split_data)
#
#     # addr[320] = "전라북도 전주시 덕진구 송천중앙로 100-3"
#     # addr[1115] = "전라북도 남원시 수철길 4-14"
#
#     for i in range(len(addr)):
#         split_data = addr[i].split(" ")
#         if len(split_data) == 3:
#             addr[i] = " ".join(split_data[1:])
#         elif len(split_data) == 4:
#             addr[i] = " ".join(split_data[2:])
#         elif len(split_data) == 5:
#             addr[i] = " ".join(split_data[3:])
#         elif len(split_data) == 6:
#             addr[i] = " ".join(split_data[4:])
#         elif len(split_data) == 7:
#             addr[i] = " ".join(split_data[5:])
#
#     return addr
#
#
# latitudes = []
# longitudes = []
#
# for i in range(len(addr)):
#     try:
#         crd = get_location(addr[i])
#         latitudes.append(crd[0])
#         longitudes.append(crd[1])
#     except IndexError:
#         location = geo_local.geocode(addr[i])
#         latitudes.append(str(location.latitude))
#         longitudes.append(str(location.longitude))
#
#
# print(latitudes)
# data["위도"] = latitudes
# data["경도"] = longitudes
#
# data.to_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/jjpark.csv", encoding="euc-kr")

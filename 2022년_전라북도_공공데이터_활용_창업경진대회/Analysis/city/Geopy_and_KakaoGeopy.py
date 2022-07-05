import requests, json, pandas as pd
from geopy.geocoders import Nominatim

geo_local = Nominatim(user_agent="South Korea")

pd.set_option('display.max_rows', None)


def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    headers = {"Authorization": "KakaoAK b0fb3729d2fb8c9d30c1d622f364130d"}
    api_json = json.loads(str(requests.get(url, headers=headers).text))
    address = api_json['documents'][0]['address']
    crd = [str(address['y']), str(address['x'])]
    address_name = address['address_name']

    return crd


# FileName = "C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/공공데이터포털/아동보호전문기관 정보.csv"
# data = pd.read_csv(FileName, encoding="euc-kr")
# addr = data["주소"].copy()
addr = ["전라북도 군산시 백토로 202","전라북도 전주시 완산구 팔달로 77","전라북도 전주시 덕진구 송천로 35-15","전라북도 익산시 인북로 112"]

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
            print(i + 2, addr[i])
            er.append(i + 2)
            pass

data["위도"] = latitudes
data["경도"] = longitudes

data.to_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/공공데이터포털/아동보호전문기관 정보.csv", encoding="euc-kr")

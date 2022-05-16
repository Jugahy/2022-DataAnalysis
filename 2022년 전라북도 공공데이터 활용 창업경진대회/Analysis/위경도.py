import pandas as pd

data = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/전라북도_어린이집.csv", encoding="cp949")
pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)


# for i in [1383, 1354, 1339]:
#     split_data = address[i].split(" ")
#     del split_data[5:]
#     address[i] = " ".join(split_data)
#
# address[320] = "전라북도 전주시 덕진구 송천중앙로 100-3"
# address[1115] = "전라북도 남원시 수철길 4-14"


# addr = data["소재지도로명주소"]
# addr.remove(0)
# print(addr)


for i in range(len(addr)):
    addr = addr.drop(26, axis=0)
    split_data = addr[i].split(" ")
    if len(split_data) == 4:
        addr[i] = " ".join(split_data[2:])
    else:
        addr[i] = " ".join(split_data[3:])

print(addr)
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='South Korea')

try:
    def geocoding(addr):
        geo = geolocator.geocode(addr)
        x_y = [geo.latitude, geo.longitude]
        return x_y

    latitude = []
    longitude = []

    for i in addr:
        latitude.append(geocoding(i)[0])
        longitude.append(geocoding(i)[1])

    address_df = pd.DataFrame({'위도': latitude, '경도': longitude})
    print(address_df)
except AttributeError:
    print(addr[i])
    pass
location = geolocator.geocode("내원당길 70-15")
print((location.latitude, location.longitude))
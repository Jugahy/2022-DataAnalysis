import pandas as pd


csv = pd.read_csv('C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/인천광역시 중구_카페 및 커피숍 현황_20210805.csv',
                  encoding='cp949')
print(csv.head())


address = csv['소재지도로명주소']
print(address.head())


for i in range(len(address)):
    a = address[i].split(' ')
    address[i] = " ".join(a[0:4])
print(address)


from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')


# 위도, 경도 반환하는 함수
def geocoding(address):
    geo = geo_local.geocode(address)
    x_y = [geo.latitude, geo.longitude]
    return x_y


latitude = []
longitude = []

for i in address:
    latitude.append(geocoding(i)[0])
    longitude.append(geocoding(i)[1])

address_df = pd.DataFrame({'위도': latitude, '경도': longitude})
print(address_df)

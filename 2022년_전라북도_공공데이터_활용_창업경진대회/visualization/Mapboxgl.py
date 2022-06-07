import mapboxgl
import json

geo_data = "C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/seoul_dong.geojson"

with open(geo_data, encoding="UTF8") as f:
    data = json.loads(f.read())
print(data)
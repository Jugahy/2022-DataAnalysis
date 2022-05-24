import pandas as pd
import mapboxgl
import json
from mapboxgl.viz import *
import os
from mapboxgl.utils import df_to_geojson

df = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/toilet_seoul.csv", encoding="utf-8-sig")
# print(df)

geo_data = df_to_geojson(
    df=df,
    lat='위도',
    lon='경도',
    # filename = "data/toilet_seoul.geojson"
)
print(geo_data)
# token = "pk.eyJ1IjoiZ2FuMTIwNSIsImEiOiJjbDNqbjUzeHUwOTRtM2JvNDNxcG1yNGdxIn0.4WjLZBjrgSaw3MgSur6wQw"
# center = [126.986, 37.565]
#
# viz = CircleViz(
#     geo_data,
#     access_token=token,
#     center=center,
#     zoom=10
# )
#
# viz.show()

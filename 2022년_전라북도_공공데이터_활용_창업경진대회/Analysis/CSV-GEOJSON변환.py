import pandas as pd
import mapboxgl
import json
from mapboxgl.viz import *
from mapboxgl.utils import df_to_geojson

df = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/인천광역시 중구_카페 및 커피숍 현황_20210805.csv", encoding="utf-8-sig")
print(df)

geo_data = df_to_geojson(
    df=df,
    lat='위도',
    lon='경도',
    # filename = "data/toilet_seoul.geojson"
)

type(geo_data)
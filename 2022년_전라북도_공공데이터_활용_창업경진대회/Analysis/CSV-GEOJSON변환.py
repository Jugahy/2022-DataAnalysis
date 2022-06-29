import pandas as pd
import mapboxgl
import json
from mapboxgl.viz import *
import os
from mapboxgl.utils import df_to_geojson
import folium
from folium.plugins import MarkerCluster

df = pd.read_csv("/Data/공공데이터포털/전라북도_유치원.csv", encoding="euc_kr")

m = folium.Map([35.716705, 127.144185],
               zoom_start=17,
               width=750,
               height=500
               )

coord = df[["위도", "경도"]]

marker_cluster = MarkerCluster().add_to(m)

for lat, long in zip(coord["위도"], coord["경도"]):
    folium.Marker([lat, long], icon=folium.Icon(color="green")).add_to(marker_cluster)

m
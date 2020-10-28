import os
import pandas
from geopy.geocoders import ArcGIS

arc = ArcGIS()

def get_coords(row):
    return arc.geocode(row["Address"])[1]

df = pandas.read_csv("addresses.csv")

df[["latitude", "longitude"]] = df.apply(get_coords, axis=1).tolist()
print(df)

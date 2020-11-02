import pandas
from geopy.geocoders import ArcGIS

def geocode_addresses(df, header):
    arc = ArcGIS()
    def get_coords(row):
        return arc.geocode(row[header])[1]

    df[["Latitude", "Longitude"]] = df.apply(get_coords, axis=1).tolist()
    df["Latitude"] = df["Latitude"].round(decimals=6)
    df["Longitude"] = df["Longitude"].round(decimals=6)
    return df

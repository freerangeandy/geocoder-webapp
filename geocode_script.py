import pandas
from geopy.geocoders import ArcGIS

def geocode_addresses(df, header):
    arc = ArcGIS()
    def get_coords(row):
        return arc.geocode(row[header])[1]

    df[["latitude", "longitude"]] = df.apply(get_coords, axis=1).tolist()
    return df

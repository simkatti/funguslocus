import pandas as pd
import numpy as np
import geopandas as gpd
import fiona

def get_forest_data():
    # gdf = gpd.read_file('MV_Uusimaa.gpkg', layer='stand')
    # print(gdf.columns)
    # print(gdf)
    layers = fiona.listlayers('datasets/MV_Uusimaa.gpkg')
    print(layers)

    for layer in layers:
        gdf = gpd.read_file('datasets/MV_Uusimaa.gpkg', layer=layer, rows=1)  # just read 1 row to see columns fast
        print(f"\n--- {layer} ---")
        print(gdf.columns.tolist())

if __name__ == "__main__":
    get_forest_data()
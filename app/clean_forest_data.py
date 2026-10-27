import pandas as pd
import numpy as np
import geopandas as gpd
import fiona

def get_forest_data():    
    stand = gpd.read_file('datasets/MV_Uusimaa.gpkg', layer='stand')
    treestand = gpd.read_file('datasets/MV_Uusimaa.gpkg', layer='treestand')
    growthplacedata = gpd.read_file('datasets/MV_Uusimaa.gpkg', layer='growthplacedata')
    
    habitat = stand[['standid', 'geometry']].merge(treestand[['standid', 'maintreespecies', 'developmentclass']], on='standid', how='left').merge(growthplacedata[['standid', 'fertilityclass', 'soiltype', 'drainagestate', 'maingroup']], on='standid', how='left')

    # print(habitat.isna().sum())
    # print(habitat['soiltype'].unique())

def map_codes():
    df = pd.read_csv('datasets/codes.txt', sep='\t', names=['class', 'code', 'meaning'], header=None)
    print(df)

def open_data():
    paths = ['datasets/MV_Varsinais-Suomi.gpkg',
    'datasets/MV_Uusimaa.gpkg',
    'datasets/MV_Satakunta.gpkg',
    'datasets/MV_Pohjois-Savo.gpkg',
    'datasets/MV_Pohjois-Pohjanmaa.gpkg',
    'datasets/MV_Pohjois-Karjala.gpkg',
    'datasets/MV_Pohjanmaa.gpkg',
    'datasets/MV_Pirkanmaa.gpkg',
    'datasets/MV_Päijät-Häme.gpkg',
    'datasets/MV_Lappi_P.gpkg',
    'datasets/MV_Lappi_E.gpkg',
    'datasets/MV_Kymenlaakso.gpkg',
    'datasets/MV_Keski-Suomi.gpkg',
    'datasets/MV_Keski-Pohjanmaa.gpkg',
    'datasets/MV_Kanta-Häme.gpkg',
    'datasets/MV_Kainuu.gpkg',
    'datasets/MV_Etelä-Savo.gpkg',
    'datasets/MV_Etelä-Pohjanmaa.gpkg',
    'datasets/MV_Etelä-Karjala.gpkg']

if __name__ == "__main__":
    get_forest_data()
    # map_codes()
    
    


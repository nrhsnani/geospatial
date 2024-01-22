import geopandas as gpd

def read_shapefile(file_path):
    df = gpd.read_file(file_path)
    return df

# Example usage:
shapefile_path = 'CEN_FDP_BND_SHAPEFILE/CEN_FDP_BND.shp'
result_df = read_shapefile(shapefile_path)
print(result_df.head())

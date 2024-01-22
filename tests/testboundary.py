import geopandas as gpd

def read_shapefile(file_path):
    df = gpd.read_file(file_path)
    return df

def point_inside_polygon(point, polygon_gdf):
    point_geom = Point(point)
    inside_polygon = False

    for _, polygon in polygon_gdf.iterrows():
        if point_geom.within(polygon['geometry']):
            inside_polygon = True
            break

import geopandas as gpd
from shapely.geometry import Point

def point_inside_polygon(point, polygon_gdf):
    point_geom = Point(point)
    inside_polygon = False

    for _, polygon in polygon_gdf.iterrows():
        if point_geom.within(polygon['geometry']):
            inside_polygon = True
            break

    return inside_polygon

# Example usage:
shpfile_path = 'CEN_FDP_BND.shp'
polygon_gdf = gpd.read_file(shpfile_path)

#point_to_check = point_row['longitude'], point_row['latitude'])
point_to_check = Point(101.740213979999993, 3.075299640000000)
point_gdf = gpd.GeoDataFrame(geometry=[point_to_check])

# Add a new column 'BND_ID' indicating whether the point is inside the boundary
point_gdf['inside_bnd'] = point_gdf.apply(lambda row: row['geometry'].within(polygon_gdf['geometry']).any(), axis=1)

print(point_gdf)

def main():
    if __name__ == 'geospatial.main':
        print('Hello this is testing')


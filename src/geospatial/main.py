import geopandas as gpd
from shapely.geometry import Point

def read_shapefile(file_path):
    df = gpd.read_file(file_path)
    return df
    
def find_boundary(point, polygon_gdf):
    point_geom = Point(point)

    for index, row in polygon_gdf.iterrows():
        if point_geom.within(row['geometry']):
            return row['BND_ID']
    # If the point is not inside any polygon, return None or any other appropriate value
    return 'N/A'

# Example usage:
cust_input = pd.read_csv('dataCust.csv')

shpfile_path = 'dataSHP.shp'
polygon_gdf = read_shapefile(shpfile_path)

result = []

for index, row in cust_input.iterrows():
    x_longitude = row['Longitude']
    y_latitude = row['Latitude']
    point = Point(x_longitude, y_latitude)
    
    # Find the boundary_id for the point
    bnd_id = find_boundary(point, polygon_gdf)
    result.append(bnd_id)

cust_input['Boundary_Overlap'] = result
# cust_input

def main():
    if __name__ == 'geospatial.main':
        print('Hello this is testing')


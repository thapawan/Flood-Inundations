import ee
import geemap
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import contextily as ctx
import numpy as np
from matplotlib_scalebar.scalebar import ScaleBar

# Get River Geometries from GEE
FrenchBroadRiver = ee.FeatureCollection('projects/skilful-boulder-440618-e7/assets/FrenchBoardRiver')
SwannanoaRiver = ee.FeatureCollection('projects/skilful-boulder-440618-e7/assets/SwannanoaRiver')
NolichuckyRiver = ee.FeatureCollection('projects/skilful-boulder-440618-e7/assets/NolichuckyRiver')
PigeonRiver = ee.FeatureCollection('projects/skilful-boulder-440618-e7/assets/PigeonRiver')
rivers = FrenchBroadRiver.merge(SwannanoaRiver).merge(NolichuckyRiver).merge(PigeonRiver)


# Function to convert GEE geometry to GeoPandas DataFrame
def ee_geom_to_gdf(geometry):
    features = geometry.getInfo()['features']
    geometries = []
    for feature in features:
        geom_type = feature['geometry']['type']
        coordinates = feature['geometry']['coordinates']

        if geom_type == 'Polygon':
            geometries.append(Polygon(coordinates[0]))  # Assuming exterior ring is at index 0
        elif geom_type == 'LineString':
            geometries.append(LineString(coordinates))
        elif geom_type == 'Point':
            geometries.append(Point(coordinates))
        else:
            print(f"Skipping geometry type: {geom_type}")
            continue # Skip geometry if not Polygon, LineString or Point

    gdf = gpd.GeoDataFrame(geometry=geometries)
    return gdf

# Convert river geometries to GeoPandas GeoDataFrames
gdf_rivers = ee_geom_to_gdf(rivers)

# Set CRS for gdf_rivers
gdf_rivers.crs = 'EPSG:4326'  # Assuming WGS 84 (latitude/longitude)

# 2. Create Square Validation Polygons
square_size = 0.5  # Adjust as needed (in degrees)

# Representative points for each river (adjust as needed)
river_points = {
    'French Broad': (-82.5, 35.5),
    'Swannanoa': (-82.4, 35.6),
    'Nolichucky': (-82.8, 36.1),
    'Pigeon': (-83.0, 35.7)
}

# Create square polygons
squares = []
for river, (lon, lat) in river_points.items():
    min_lon, max_lon = lon - square_size / 2, lon + square_size / 2
    min_lat, max_lat = lat - square_size / 2, lat + square_size / 2
    square = Polygon([(min_lon, min_lat), (max_lon, min_lat), (max_lon, max_lat), (min_lon, max_lat)])
    squares.append(square)

gdf_squares = gpd.GeoDataFrame(geometry=squares)
gdf_squares.crs = 'EPSG:4326'

# 3. Plot the Map
fig, ax = plt.subplots(figsize=(10, 8))

# Plot rivers
gdf_rivers.plot(ax=ax, color='blue', linewidth=1)

# Plot validation squares
gdf_squares.plot(ax=ax, color='red', linewidth=1, hatch='///')

# Add basemap to main map
ctx.add_basemap(ax, crs=gdf_rivers.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)


# Add labels and title
#ax.set_title('Four Rivers with Validation Squares and Basemap')
#ax.set_xlabel('Longitude')
#ax.set_ylabel('Latitude')

# Add scale bar
scalebar = ScaleBar(1, "km", location="lower right")  # 1 pixel = 1 km
ax.add_artist(scalebar)

plt.show()

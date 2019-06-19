# Script to combine .svx files into a combined cave silloute gis layer
import argparse
import os
import geopandas as gpd
import shapely as sp
import pandas as pd

# Path to folder containing survex folders
svx_path = "20190616_jenolan"

def process_svx_kml(kml_path):
    """
    Convert the KML into a single dissolved geometry. Describing the silloette of
    the cave.
    """
    cave_kml = gpd.read_file(kml_path)
    cave_geom = cave_kml.geometry.unary_union()

    return cave_geom, cave_kml.crs

caves=[]
# Find all the survex files in the folder
for root,dirs,files in os.walk(svx_path):
    # print(root)
    # print(dirs)
    for file in files:
        if file.endswith('.svx'):
            # Name of different files
            file_3d = file.replace('.svx','.3d')
            cave_name = file.replace('.svx','')
            file_kml = file.replace('.svx','.kml')
            os.system('cavern {}'.format(os.path.join(root,file)))
            os.system('survexport -passages -kml {}'.format(os.path.join(root,file_3d)))

            cave_geom, crs = process_svx_kml(file_kml)
            cave_dict = {'name':cave_name, 'geometry':cave_geom}
            caves.append(cave_dict)
    # Convert it back to a data frame.`
    caves_df =pd.DataFrame(caves)
    # Comnvert it to a geodataframe
    geometry = caves_df['geometry']
    caves_gdf = gpd.GeoDataFrame(caves_df[['name']],
    geometry=geometry,crs=crs)
    caves_df.to_file('test.csv')

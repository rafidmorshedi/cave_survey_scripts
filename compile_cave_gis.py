# Script to combine .svx files into a combined cave silloute gis layer
import argparse
import os
import geopandas as gpd
import shapely as sp

# Path to folder containing survex folders
svx_path = "./jenolan"

def process_svx_kml(kml_path):
    """
    Convert the KML into a single dissolved geometry. Describing the silloette of
    the cave.
    """
    cave_kml = gpd.read_file(kml_path,layer_name = "")
    cave_geom = cave_kml.geometry.unary_union()

    return cave_geom, cave_kml.crs

caves=[]
# Find all the survex files in the folder
for root,dirs,files in os.walk(svx_path):
    # print(root)
    # print(dirs)
    for file in files:
        if file.endswith('.svx'):
            print('cavern {}'.format(os.path.join(root,file)))
            # Name of .3d file
            file_3d = file.replace('.svx','.3d')
            cave_name = file.replace('.svx','')
            os.system()
            print('survexport -passages -kml {}'.format(os.path.join(root,file_3d)))

            cave_geom, crs = process_svx_kml()
            cave_dict = {'name':cave_name, 'geometry':}
    # print(os.path.join(root,files))

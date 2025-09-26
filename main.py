""" scripts to view and reproject spatial vector data """

#import the necessary libraries

import geopandas as gpd  #gpd is an alias for GeoPandas and will be used to shorten the code and make it more efficeient to use the library.

"""""Global Perameters"""

FILE_PATH = r"C:\Programming\Spatial_data_original\Fire_and_Rescue.shp"  #Define input shapefile path

OUTPUT_PATH = r"C:\Programming\Output" #Defined output folder 



"""Function: Read shapefile from a specified path and returns a geodata frame object"""

def read_return_gdf(FILE_PATH):
    
     #  Parameters:FILE_PATH (str): The full file path to the input shapefile.

    gdf = gpd.read_file(FILE_PATH) 

     #  Returns:gpd.GeoDataFrame: A GeoDataFrame containing the spatial and attribute data from the shapefile

    return gdf  

gdf = read_return_gdf(FILE_PATH) # Call the function with the defined file path

print(gdf) #validation of dataframe



"""This function is to show spatial data and attriutes row by row"""


"""Reads a shapefile from the specified file path and prints each row
    of the resulting GeoDataFrame along with a separator line.

Parameters:
        FILE_PATH (str): The full path to the shapefile to be read.

Returns:
        None: This function does not return a value. It prints each row
              (both geometry and attributes) of the GeoDataFrame to the console."""


def print_all_rows(FILE_PATH):
    try:
        gdf = gpd.read_file(FILE_PATH)
        print(f"File loaded successfully.")
      
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if gdf.empty:
        print("GeoDataFrame is empty — no rows to print.")
        return

    for row in gdf.iterrows():
        
        print(row)
        print("-" * 60)


print_all_rows(FILE_PATH)

"""Reads a shapefile, transforms its CRS to the specified EPSG code,
    and prints the CRS and the first few rows of the transformed GeoDataFrame.

Parameters:
        FILE_PATH (str): The path to the shapefile to read.
        EPSG (int, optional): The target EPSG code for CRS transformation. Default is 7856.

Returns: None"""

gdf = gpd.read_file(FILE_PATH)

gdf = gdf.to_crs(epsg=7856)

print(gdf.crs)
print(gdf.head())

def transform_From_Projected_To_Geographic(FILE_PATH,EPSG=7856):

    """this function reads a shapefile from a selected file path to a geodata frame, then convert coordinate system to an EPSG of choice, then save tranformed gdf as a shapefile to output folder"""

    try:
        gdf = gpd.read_file(FILE_PATH)
        gdf = gdf.to_crs(epsg=EPSG)  #transormed from projected crs to geographic
    except Exception as e:
        print("Error",e)

    return gdf #returns geodata frame object

  

"""export gdf to GeoJson"""

def export_to_GeoJson(gdf,OUTPUT_PATH):

    """this function take a geodataframe as a perameter gdf
    it takes output folder as string perameter
    returns none"""


    full_output_path_with_filename = OUTPUT_PATH + "\\" + "output.geojson"
    print(full_output_path_with_filename) #validate correct file name and path 

    gdf.to_file(full_output_path_with_filename, driver="GeoJSON")

    return None

# # print(Transformgdf)  #validate transformation
# # print(Transformgdf.crs)  #validate transformation
Transformgdf = transform_From_Projected_To_Geographic(FILE_PATH,EPSG=7844) #by adding ,ESPG= after FILE_PATH we can overwrite the default value, carrying out a new crs tranformation, making the script easily reusable.
export_to_GeoJson(Transformgdf,OUTPUT_PATH)





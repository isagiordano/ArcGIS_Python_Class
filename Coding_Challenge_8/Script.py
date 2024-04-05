###### CODING CHALLENGE 8


# Convert some of your earlier code into a function. The only rules are:
# 1) You must do more than one thing to your input to the function, and
# 2) the function must take two arguments or more. You must also,
# 3) provide a zip file of example data within your repo.
# Plan the task to take an hour or two, so use one of the simpler examples from our past classes.


# Import system modules, overwrite ensures if I rerun this code, i am not met with
# error that file already exists.
import arcpy
arcpy.env.overwriteOutput = True
base_path_directory="C:\ArcGIS_python\class_4\Coding_chall_4_data\data_chall_4"
arcpy.env.workspace = base_path_directory

### STEP 1: Using describe as a function to describe the HYDRO rivers and streams shapefile
# Describing the shape type and spatial reference type.

def describe_shp(input_shapefile):
    if arcpy.Exists(input_shapefile):
        desc = arcpy.Describe(input_shapefile)
        if arcpy.Exists(input_shapefile):
            if desc.dataType == "ShapeFile":
                print("Describing: " + str(input_shapefile))
                print("Feature Type:  " + desc.shapeType)
                print("Coordinate System Type:  " + desc.spatialReference.type)
            else:
                print("Input data not ShapeFile..")
    else:
        print("Dataset not found, please check the file path..")

input_shapefile = r"HYDRO_Rivers_and_Streams_24K.shp"
describe_shp(input_shapefile)



### STEP 2: Using select tool as a function to select only streams with stream order 1.
# Defined the Select tool as a function called "select features"

def select_features(in_features, out_feature_class, where_clause):
    arcpy.analysis.Select(in_features, out_feature_class, where_clause)
    print("Selecting first order streams in " + str(in_features))
in_features = r"HYDRO_Rivers_and_Streams_24K.shp"
out_feature_class = r"stream_order_1.0.shp"
where_clause = '"Strm_Ordr" = 1'

select_features(in_features, out_feature_class, where_clause)

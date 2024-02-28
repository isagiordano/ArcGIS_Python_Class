# For this coding challenge, I want you to find a particular tool that you like in arcpy.
# It could be a tool that you have used in GIS before or something new. Try browsing the full tool list to get
# some insight here (click Tool Reference on the menu list to the left).
# #
# Set up the tool to run in Python, add some useful comments, and importantly, provide some example
# data in your repository (try to make it open source, such as Open Streetmap, or RI GIS.
# You can add it as a zip file to your repository.
#
# My only requirements are:
#
# Comment your code well.
# Ensure that the code will run on my machine with only a single change
# to a single variable (i.e. a base folder location).

# # Coding Challenge 4
# Using the RIGIS Rivers and Streams data, this script will use the select tool
# to select only the 1st Order Streams.


# Import system modules, overwrite ensures if I rerun this code, i am not met with
# error that file already exists.
import arcpy
arcpy.env.overwriteOutput = True

arcpy.env.workspace = r"C:\ArcGIS_python\class_4\Coding_chall_4_data\data_chall_4"
# creates a workspace to save all my data so only one variable needs to be changed.

in_features = r"HYDRO_Rivers_and_Streams_24K.shp"
# location of input features- in this case I used the RIGIS Rivers and Streams shapefile

out_feature_class = r"stream_order_1.shp"
# Specifies output location for the shapefile i create/have named

where_clause = '"Strm_Ordr" = 1'
# selects features in the rivers and streams shapefile that have a stream order value of 1

arcpy.analysis.Select(in_features, out_feature_class, where_clause)
# uses the select output tool, executes the clause i chose, saves output to shapefile

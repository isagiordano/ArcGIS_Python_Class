# # CODING CHALLENGE 5
# Creating a heatmap of two species.
# for this challenge, I chose data from GBIS. I chose sea turtles and pinnipeds spotted around the Azores.

# 1. Set up and combining my csv. I used pandas and followed a source example.
# if this is not okay, I am totally fine with redoing it without pandas.
import arcpy
arcpy.env.workspace = r"C:\ArcGIS_python\class_5"
arcpy.env.overwriteOutput = True

import pandas as pd
import os

# List all CSV files to be combined
csv_files = ['pinnipeds.csv', 'Sea_turtles.csv']

# Read and combine the CSV files
combined_df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

# Save to a new CSV file
combined_df.to_csv('azores.csv', index=False)

# send message to confirm the file was created. this is also why I imported os.
if os.path.exists('azores.csv'):
    print("Created combined file successfully!")

# Here is the source: https://johnvastola.medium.com/how-to-combine-multiple-csv-files-using-python-to-analyze-797fc825c541


# 2. Creating the shp layer.

# assign values from csv, and save output.
# for some reason, latitude and longitude was saved under genus and family, but I did confirm
# the rows corresponded to the actual extent values from the other two csvs.
# If there is a way to fix this let me know. I attempted but was unsuccessful.

in_Table = r"azores.csv"
x_coords = "genus"
y_coords = "family"
z_coords = ""
out_Layer = "azores"
saved_Layer = r"Step_1_azores_Output.shp"

# Set the spatial reference
spRef = arcpy.SpatialReference(4326)

# saving actual output to lyr
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

# Print the total rows
print('There are ' + str(arcpy.GetCount_management(out_Layer)) + ' rows of data')

# Save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

# send message to confirm the file was created
if arcpy.Exists(saved_Layer):
    print("Created file successfully!")



# # 2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated Cepphus_grylle shapefile.

desc = arcpy.Describe(saved_Layer)
Xmin = desc.extent.XMin
Xmax = desc.extent.XMax
Ymin = desc.extent.YMin
Ymax = desc.extent.YMax

# send message to confirm the values were calculated, and send output values.
if Xmin is not None and Xmax is not None and Ymin is not None and Ymax is not None:
    print('Spatial extents calculated successfully!\n'
          + 'Xmin = ' + str(Xmin) + ' Xmax = ' + str(Xmax) +
          ' Ymin = ' + str(Ymin) + ' Ymax = ' + str(Ymax))


# 3. Generate a fishnet

outFeatureClass = "Azores_fishnet.shp"
# Name of output fishnet

# Set the origin of the fishnet

originCoordinate = str(Xmin) + ' ' + str(Ymin)
# origin coordinate = xmin + ' ' + y min

yAxisCoordinate = str(Xmin) + ' ' + str(Ymin + 1)
cellSizeWidth = "0.25"
cellSizeHeight = "0.25"
numRows = ""
numColumns = ""
oppositeCorner = str(Xmax) + ' ' + str(Ymax)
# max x and max y coordinate

labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

# sends message to confirm file was successfully created
if arcpy.Exists(outFeatureClass):
    print("Created fishnet successfully!")


# 4. Undertake a Spatial Join to join the fishnet to the observed points.

# setting all variables
target_features = "Azores_fishnet.shp"
join_features = "Step_1_azores_Output.shp"
out_feature_class = "Azores_HeatMap.shp"
join_operation = "JOIN_ONE_TO_ONE"
join_type = "KEEP_ALL"
field_mapping = ""
match_option = "INTERSECT"
search_radius = ""
distance_field_name = ""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)


# 5. Check that the heatmap is created and delete the intermediate files

if arcpy.Exists(out_feature_class):
    print("File successfully created! Slay!")
    print("Deleting intermediate files... without deleting my entire hard drive")
    arcpy.Delete_management(join_features)
    arcpy.Delete_management(target_features)


# Sources:
# # GBIF.org (29 February 2024) GBIF Occurrence Download https://doi.org/10.15468/dl.upfp6x
# # GBIF.org (29 February 2024) GBIF Occurrence Download https://doi.org/10.15468/dl.e5e9ug

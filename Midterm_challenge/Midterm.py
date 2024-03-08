# MIDTERM CODING CHALLENGE
# I chose to redo a past project in which large water bodies (higher order streams and lakes)
# are buffered 200 feet, and smaller water bodies (wetlands and first order streams)
# are buffered 100 feet.
# For the same of visualization in this project, I chose to also clip the features and only create
# buffer zones for Narragansett.
# Therefore, this project will visualize buffer zones of large and small water bodies in the
# town of Narragansett.

# I used buffer, select, clip, and intersect tools to complete this analysis.
# I used 4 datasets: Towns, Lakes, Streams, and Rivers.


import arcpy, os

# Setting base path directory so only one variable needs to be changed.
# doing this instead of just arcpy.env allows the code to be seen not just in arcpy.
# Setting environment overwrite to true allows me to run this a few times over without
# receiving an error message that the files already exist.
base_path_directory = "C:\ArcGIS_python\midterm_data"
arcpy.env.workspace = base_path_directory
arcpy.env.overwriteOutput = True

# Locating my data within my base directory, and setting the path as a variable
Lakes = os.path.join(base_path_directory,"Lakes.shp")
Wetlands = os.path.join(base_path_directory,"wetlands.shp")
Rivers = os.path.join(base_path_directory,"Rivers.shp")
Towns = os.path.join(base_path_directory,"towns.shp")

# Creates temporary files folder
# If not is used oftentimes in this code to allow it to run faster and skip over
# commands that have already been carried out and saved as shp files
if not os.path.exists(os.path.join(base_path_directory,"temporary_files")):
    os.mkdir(os.path.join(base_path_directory,"temporary_files"))

print("Hold tight- arcpy is running...")


# STEP 1:
# Selecting only Narragansett within towns.shp

print("Clipping towns layer to Narragansett...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "Narragansett.shp")):
    arcpy.analysis.Select(in_features=Towns,
                          out_feature_class=os.path.join(base_path_directory, "temporary_files", "Narragansett.shp"),
                          where_clause="NAME = 'NARRAGANSETT'")
    # uses the select output tool, executes the clause i chose, saves output to shapefile
    print("Narragansett File Successfully Created!")
else:
    print("Narragansett File  Already There")

# Saving Narragansett as a variable to be referenced later.
Gansett = os.path.join(base_path_directory, "temporary_files", "Narragansett.shp")


# STEP 2:
# Selecting ONLY first order streams within Rivers.shp

print("Selecting first order streams...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "first_streams.shp")):
    arcpy.analysis.Select(in_features=Rivers,
                          out_feature_class=os.path.join(base_path_directory,"temporary_files", "first_streams.shp"),
                                                         where_clause='"StrmOrder" = 1')
    # uses the select output tool, executes the clause I chose, saves output to shapefile
    # figured out the syntax of the where_clause via ModelBuilder, as I know
    # it is pretty finicky.
    print("First Order Streams Successfully Created!")
else:
    print("First Order Streams Already There")


# STEP 3: Selecting higher order streams (from 2-6)

print("Selecting higher order streams...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "higher_streams.shp")):
    arcpy.analysis.Select(in_features=Rivers,
                          out_feature_class=os.path.join(base_path_directory,"temporary_files", "higher_streams.shp"),
                                                         where_clause="StrmOrder >= 2")
    # uses the select output tool, executes the clause i chose, saves output to shapefile
    print("Higher Order Streams Successfully Created!")
else:
    print("Higher Order Streams Already There")


# STEP 4: Creating an intersection between higher order streams and lakes
# This intersection will create one shapefile for Large Water Bodies.
# Saving the output type gave me a bit of trouble. The default on ModelBUilder
# was "same as input" but that did not visualize very well.
# In playing around with it I found that setting output_type = POINT
# created a better dataset both in visualization and later creation of the buffer.

print("Creating an intersection between higher order streams and lakes...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "large_water_bodies.shp")):
    Higher_Streams = os.path.join(base_path_directory,"temporary_files", "higher_streams.shp")
    arcpy.analysis.Intersect(in_features=[[Lakes, ""], [Higher_Streams, ""]],
                         out_feature_class=os.path.join(base_path_directory,"temporary_files", "large_water_bodies.shp"),
                         join_attributes = "ALL", output_type="POINT")
    print("Large Water Body Intersection Successfully Created!")
else:
    print("Large Water Body Intersection already there")


# STEP 5: Clipping the large water bodies to Narragansett.
#  Clip_features = Gansett will use the border of the Narragansett
# dataset I created in step 1 as the area extent for the water bodies.

print("Clipping large water bodies to Narragansett...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "Large_Water_Gansett.shp")):
    arcpy.analysis.Clip(in_features=os.path.join(base_path_directory,"temporary_files", "large_water_bodies.shp"),
                        clip_features=Gansett, out_feature_class=os.path.join(base_path_directory,"temporary_files", "Large_Water_Gansett.shp"))
    print("Clipping Large Water Bodies to Narragansett Successful!")
else:
    print("Clip already created")


# STEP 6: Buffering the large water bodies 200 feet.
# I found that using method= GEODESIC provided me with clearer buffers
# when visualized in ArcPro.

print("Buffering large water bodies 200 feet...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "Large_water_buffer.shp")):
    Large_water = os.path.join(base_path_directory,"temporary_files", "Large_Water_Gansett.shp")
    arcpy.analysis.Buffer(in_features= Large_water,
                          out_feature_class=os.path.join(base_path_directory,"temporary_files", "Large_water_buffer.shp"),
                          buffer_distance_or_field="200 feet",
                          dissolve_option="ALL", method="GEODESIC")
    print("Large Water Body Buffer Successfully Created!")
else:
    print("Large Water Body Buffer  already there")


# STEP 7: Creating an intersection between first order streams and wetlands
# This will be the small water body group. I used a point output type for
# this as well.

print("Creating an intersection between first order streams and wetlands...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "small_water_bodies.shp")):
    First_Streams = os.path.join(base_path_directory,"temporary_files", "first_streams.shp")
    arcpy.analysis.Intersect(in_features=[[Lakes, ""], [First_Streams, ""]],
                         out_feature_class=os.path.join(base_path_directory,"temporary_files", "small_water_bodies.shp"),
                         join_attributes = "ALL", output_type="POINT")
    print("Small Water Body Intersection Successfully Created!")
else:
    print("Small Water Body Intersection already there")


# STEP 8: Clipping the small water body shapefile to Narragansett.

print("Clipping small water bodies to Narragansett...")
if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "Small_Water_Gansett.shp")):
    arcpy.analysis.Clip(in_features=os.path.join(base_path_directory,"temporary_files", "small_water_bodies.shp"),
                        clip_features=Gansett, out_feature_class=os.path.join(base_path_directory,"temporary_files", "Small_Water_Gansett.shp"))
    print("Clipping Small Water Bodies to Narragansett Successful!")
else:
    print("Clip already created")


# STEP 9: Buffering small water bodies 100 ft. I also
# used a geodesic method for this dataset, like I did with
# The large water bodies.

print("Buffering small water bodies 100 ft...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "Small_water_buffer.shp")):
    Small_water = os.path.join(base_path_directory,"temporary_files", "Small_Water_Gansett.shp")
    arcpy.analysis.Buffer(in_features= Small_water,
                          out_feature_class=os.path.join(base_path_directory,"temporary_files", "Small_water_buffer.shp"),
                          buffer_distance_or_field="100 feet",
                          dissolve_option="ALL",method="GEODESIC")
    print("Small Water Body Buffer Successfully Created!")
else:
    print("Small Water Body Buffer already there")

# Awesome! we did it! (hopefully!)

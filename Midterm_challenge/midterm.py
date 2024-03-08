import arcpy, os

base_path_directory = "C:\ArcGIS_python\midterm_data"
arcpy.env.workspace = base_path_directory
arcpy.env.overwriteOutput = True


Lakes = os.path.join(base_path_directory,"Lakes.shp")
Wetlands = os.path.join(base_path_directory,"wetlands.shp")
Rivers = os.path.join(base_path_directory,"Rivers.shp")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files")):
    os.mkdir(os.path.join(base_path_directory,"temporary_files"))

print("Hold tight- arcpy is running...")

print("Selecting first order streams...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "first_streams.shp")):
    arcpy.analysis.Select(in_features=Rivers,
                          out_feature_class=os.path.join(base_path_directory,"temporary_files", "first_streams.shp"),
                                                         where_clause='"StrmOrder" = 1')
    # uses the select output tool, executes the clause i chose, saves output to shapefile
    print("First Order Streams Successfully Created!")
  else:
    print("First Order Streams Already There")

print("Selecting higher order streams...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "higher_streams.shp")):
    arcpy.analysis.Select(in_features=Rivers,
                          out_feature_class=os.path.join(base_path_directory,"temporary_files", "higher_streams.shp"),
                                                         where_clause='"StrmOrder" = 2'+'"StrmOrder" = 3'+ '"StrmOrder" = 4'+
                                                                      '"StrmOrder" = 5'+'"StrmOrder" = 6')
    # uses the select output tool, executes the clause i chose, saves output to shapefile
    print("Higher Order Streams Successfully Created!")
else:
    print("Higher Order Streams Already There")

print("Creating an intersection between higher order streams and lakes...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "large_water_bodies.shp")):
    Higher_Streams = os.path.join(base_path_directory,"temporary_files", "higher_streams.shp")
    arcpy.analysis.Intersect(in_features=[[Lakes, ""], [Higher_Streams, ""]],
                         out_feature_class=os.path.join(base_path_directory,"temporary_files", "large_water_bodies.shp"),
                         join_attributes = "ALL")
    print("Large Water Body Intersection Successfully Created!")
else:
   print("Large Water Body Intersection already there")

print("Creating an intersection between first order streams and wetlands...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "small_water_bodies.shp")):
    First_Streams = os.path.join(base_path_directory,"temporary_files", "first_streams.shp")
    arcpy.analysis.Intersect(in_features=[[Lakes, ""], [First_Streams, ""]],
                         out_feature_class=os.path.join(base_path_directory,"temporary_files", "small_water_bodies.shp"),
                         join_attributes = "ALL")
    print("Small Water Body Intersection Successfully Created!")
else:
    print("Small Water Body Intersection already there")

print("Buffering large water bodies 200 ft...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "Large_water_buffer.shp")):
    Large_water = os.path.join(base_path_directory,"temporary_files", "large_water_bodies.shp")
    arcpy.analysis.Buffer(in_features= Large_water,
                          out_feature_class=os.path.join(base_path_directory,"temporary_files", "Large_water_buffer.shp.shp"),
                          buffer_distance_or_field="200 feet",
                          dissolve_option="ALL")
    print("Large Water Body Buffer Successfully Created!")
else:
    print("Large Water Body Buffer  already there")
  
print("Buffering small water bodies 100 ft...")

if not os.path.exists(os.path.join(base_path_directory,"temporary_files", "Small_water_buffer.shp")):
    Small_water = os.path.join(base_path_directory,"temporary_files", "small_water_bodies.shp")
    arcpy.analysis.Buffer(in_features= Small_water,
                          out_feature_class=os.path.join(base_path_directory,"temporary_files", "Small_water_buffer.shp.shp"),
                          buffer_distance_or_field="100 feet",
                          dissolve_option="ALL")
    print("Small Water Body Buffer Successfully Created!")
else:
    print("Small Water Body Buffer  already there")

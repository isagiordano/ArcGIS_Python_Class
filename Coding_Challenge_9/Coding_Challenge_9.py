##### CODING CHALLENGE  9


# As always, starting with importing arcpy, os, and setting my workspace

import arcpy, os
base_path_directory = r"C:\ArcGIS_python\class_9"
arcpy.env.workspace = base_path_directory
arcpy.env.overwriteOutput = True


# STEP 1: setting variables that I will use later to create my shapefiles.

spatial_ref = 4326
input_shp = os.path.join(base_path_directory, 'RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp')
out_path = arcpy.env.workspace
out_name_photo = "records_w_photo.shp"
out_name_no_photo = "records_w_no_photo.shp"
geometry_type = "POINT"
template = "#"
has_m = "DISABLED"
has_z = "DISABLED"

# not entirely sure if I needed to set template, has_m, or has_z, but it was
# in Step 4, and better safe than sorry!


# STEP 2
# First, I will use arcpy.da.SearchCursor to find/count each record that has a photo
# I noticed on ArcGIS, the PHOTO description was within the Other field, so I used that.
# There were multiple other fields labelled "PhotoN," "PhotoS," etc., but the PHOTO option
# within the Other field most closely matched the assignment description.
# I also felt no need to print every row that had a PHOTO as it printed too many results
# and felt unnecessary when the goal is simply to count the records

field = ['Other']
expression = arcpy.AddFieldDelimiters(input_shp, "Other") + " = 'PHOTO'"
count_photo = 0
with arcpy.da.SearchCursor(input_shp, field, expression) as cursor:
    for row in cursor:
        count_photo = count_photo + 1
print("There are " + str(count_photo) + " records that have a photo.")


# STEP 3
# Repeating the above process but only selecting records with no photo.
# I had initially used != to mean "does not equal" but it was not working.
# After a little digging, I found that <> is another option, and it seems to
# be working just fine!

field = ['Other']
expression = arcpy.AddFieldDelimiters(input_shp, "Other") + " <> 'PHOTO'"
count_no_photo = 0
with arcpy.da.SearchCursor(input_shp, field, expression) as cursor:
    for row in cursor:
        count_no_photo = count_no_photo + 1
print("There are " + str(count_no_photo) + " records that DO NOT have a photo.")


# STEP 4
# Counting unique species names
# I created an empty species list and used append to add each species name
# so I would not have any duplicates, and then used len to count them.

field = ['Species']
species_list = []

with arcpy.da.SearchCursor(input_shp, field) as cursor:
    for row in cursor:
        species_name = row[0]
        if species_name not in species_list:
            species_list.append(species_name)

print("There are " + str(len(species_list)) + " unique species.")


# STEP 5
# I used the select tool to create two shapefiles- one with photos, one without.
# The input features were my input_shp, the output shapefile is located in the base
# directory with the name I specified earlier, and the where clause is either
# Other=Photo or Other<> Photo.I had to use <> again.
# I double checked this process worked by ensuring that it had the same point count in ArcGIS.

print("Creating a shapefile including records with photos...")
arcpy.analysis.Select(input_shp, os.path.join(out_path, out_name_photo), "Other = 'PHOTO'")

print("Creating a shapefile including records without photos...")
arcpy.analysis.Select(input_shp, os.path.join(out_path, out_name_no_photo), "Other <> 'PHOTO'")


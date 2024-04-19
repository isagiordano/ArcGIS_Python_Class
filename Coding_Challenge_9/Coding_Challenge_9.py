# I noticed on ArcGIS, the PHOTO description was within the Other field, so I used that.
# There were multiple other fields labelled "PhotoN," "PhotoS," etc., but the "photo" option
# with a value of u most closely matched the assignment description.
# I also felt no need to print every row that had a PHOTO as it printed too many results
# and felt unnecessary when the goal is simply to count the records

field = ['photo']
expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " = 'y'"
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

field = ['photo']
expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " <> 'y'"
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
# photo=y or photo<> y.I had to use <> again.
# I double checked this process worked by ensuring that it had the same point count in ArcGIS.

print("Creating a shapefile including records with photos...")
arcpy.analysis.Select(input_shp, os.path.join(out_path, out_name_photo), "photo = 'y'")

print("Creating a shapefile including records without photos...")
arcpy.analysis.Select(input_shp, os.path.join(out_path, out_name_no_photo), "photo <> 'y'")



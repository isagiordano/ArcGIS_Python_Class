#### CODING CHALLENGE 10

# this challenge creates tif files showing the ndvi from
# landsat data and rasters containing bands 4 and 5.


#  Setting workspaces, checking extnsions, the basics.
import os, arcpy
arcpy.env.overwriteOutput = True
input_Directory = r"C:\ArcGIS_python\class_10\LANDSAT"
arcpy.env.workspace = input_Directory

arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")\


# Defining a function to calculate NDVI
# The function is called BandsCalc. I used ModelBuilder and exported the code
# as a first step for creating this function.
# The function calculates (band5-band4)/(band5+band4)

def BandsCalc(input_raster_b4, input_raster_b5, outputDirectory, output_raster):
    # Check out any necessary licenses.

    raster_b4 = arcpy.Raster(input_raster_b4)
    raster_b5 = arcpy.Raster(input_raster_b5)
    output_raster_path = os.path.join(outputDirectory, output_raster)

    # NDVI equation
    ndvi =  ((raster_b5)-(raster_b4))/((raster_b5)+(raster_b4))
    ndvi.save(output_raster_path)
    return(output_raster_path)


# Listing directories within the input directory and then iterating over the 
# different files in the Landsat directory to find only rasters containing B4 and B5.
# Then, usinf Bandscalc to calculate NDVI and saves the raster as a tif file including the month it was taken from.

listMonth = os.listdir(input_Directory)

for month in listMonth:

    arcpy.env.workspace = os.path.join(input_Directory, month)

    b4_file = arcpy.ListRasters("*b4*")[0]
    b5_file = arcpy.ListRasters("*b5*")[0]
    output_raster_name = "NVDI_" + month + ".tif"
    BandsCalc(b4_file, b5_file, input_Directory, output_raster_name)
 

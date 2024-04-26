 # Our coding challenge this week that improves our practice with rasters from Week 10.
#
# Task 1 - Use what you have learned to process the Landsat files provided, this time,
# you know you are interested in the NVDI index which will use Bands 4 (red, aka vis) and
# 5 (near-infrared, aka nir) from the Landsat 8 imagery, see here for more info about the
# bands: https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites. Data
# provided are monthly (a couple are missing due to cloud coverage) during the year 2015
# for the State of RI, and stored in the file Landsat_data_lfs.zip.
#
# Before you start, here is a suggested workflow:
#
# Extract the Landsat_data_lfs.zip file into a known location.
# For each month provided, you want to calculate the NVDI, using the equation:
# nvdi = (nir - vis) / (nir + vis) https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index.
# Consider using the Raster Calculator Tool in ArcMap and using "Copy as Python Snippet" for the first
# calculation.
# The only rule is, you should run your script once, and generate the NVDI for ALL
# MONTHS provided. As part of your code submission, you should also provide a visualization
# document (e.g. an ArcMap layout in PDF format), showing the patterns for an area of RI that
# you find interesting.


import os, arcpy
arcpy.env.overwriteOutput = True
outputDirectory = r"C:\ArcGIS_python\class_10\LANDSAT_DATA"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

import arcpy

def BandsCalc(input_raster_b4, input_raster_b5, output_raster):
 
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
 
# definining the variables i am going to use for my ndvi function
 # doing arcpy.raster because thats what my model did 
 
    raster_b4 = arcpy.Raster(input_raster_b4))
    raster_b5 = arcpy.Raster(input_raster_b5))
    output_raster_path = os.path.join(outputDirectory, output_raster)

 # the equation
    ndvi =  ((raster_b5)-(raster_b4))/((raster_b5)+(raster_b4))
    ndvi.save(output_raster_path)


input_raster_b4 = ["LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif", "LC08_L1TP_012031_20150422_20170301_01_T1_B4.tif",
                       "LC08_L1TP_012031_20150508_20170227_01_T1_B4.tif","LC08_L1TP_012031_20150711_20170226_01_T1_B4.tif",
                       "LC08_L1TP_012031_20151015_20170225_01_T1_B4.tif","LC08_L1TP_012031_20151116_20170225_01_T1_B4.tif"]

input_raster_b5 = ["LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif", "LC08_L1TP_012031_20150422_20170301_01_T1_B5.tif",
                        "LC08_L1TP_012031_20150508_20170227_01_T1_B5.tif", "LC08_L1TP_012031_20150711_20170226_01_T1_B5.tif",
                        "LC08_L1TP_012031_20151015_20170225_01_T1_B5.tif",
                        "LC08_L1TP_012031_20151116_20170225_01_T1_B5.tif"]

output_raster = ["NVDI_2.tif", "NVDI_4.tif", "NVDI_5.tif","NVDI_7.tif", "NVDI_10.tif", "NVDI_11.tif"]

# so i was getting an error that LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif did not exist or was not supported
# it does in fact exist, i triple checked that arcpro wasnt open, and i redownloaded the zip file in case it was corrupted
# then i was concerned that maybe it was because the files were within folders inside my workspace/output directory
# so i tried something new 


# then, i was playing around with this..

listMonth = ["02","04","05","07","10","11"]
for month in listMonth:
    month_directory = os.path.join(outputDirectory, "2015" + month)

    if os.path.exists(month_directory):

        files = os.listdir(month_directory)

        b4_files = [file for file in files if "B4.tif" in file]
        b5_files = [file for file in files if "B5.tif" in file]

        files_NDVI= [b4_files, b5_files]
        for b4_file, b5_file in files_NDVI:

            output_raster_name = "NVDI_" + month + ".tif"

            BandsCalc(b4_file, b5_file, output_raster_name)


# but i was getting an error for line 74: ValueError: too many values to unpack (expected 2)
# currently trying to figure out how to fix. lol

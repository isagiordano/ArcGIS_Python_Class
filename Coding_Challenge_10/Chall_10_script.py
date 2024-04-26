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
listMonth = ["02","04","05","07","10","11"]
outputDirectory = r"C:\ArcGIS_python\class_10\LANDSAT_DATA"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

import arcpy

def BandsCalc(input_raster_b4, input_raster_b5, output_raster):
    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")

    raster_b4 = arcpy.Raster(input_raster_b4))
    raster_b5 = arcpy.Raster(input_raster_b5))
    output_raster_path = os.path.join(outputDirectory, output_raster)

    ndvi =  ((raster_b5)-(raster_b4))/((raster_b5)+(raster_b4))
    ndvi.save(output_raster_path)


input_raster_b4 = ["LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif", "LC08_L1TP_012031_20150422_20170301_01_T1_B4.tif",
                       "LC08_L1TP_012031_20150508_20170227_01_T1_B4.tif","LC08_L1TP_012031_20150711_20170226_01_T1_B4.tif",
                       "LC08_L1TP_012031_20151015_20170225_01_T1_B4.tif","LC08_L1TP_012031_20151116_20170225_01_T1_B4.tif"]

input_raster_b5 = ["LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif", "LC08_L1TP_012031_20150422_20170301_01_T1_B5.tif",
                        "LC08_L1TP_012031_20150508_20170227_01_T1_B5.tif", "LC08_L1TP_012031_20150711_20170226_01_T1_B5.tif",
                        "LC08_L1TP_012031_20151015_20170225_01_T1_B5.tif",
                        "LC08_L1TP_012031_20151116_20170225_01_T1_B5.tif"]

output_raster = ["NVDS_2.tif", "NVDS_4.tif", "NVDS_5.tif","NVDS_7.tif", "NVDS_10.tif", "NVDS_11.tif"]




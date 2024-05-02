# Coding Challenge 10

In this challenge, I calculated the NDVI (normalized difference
vegetation index) from Landsat files. 
NDVI is calculated from Bands 4 and 5. 
The formula is (band 5- band 4) / (band 5 + band 4)

I defined a function called BandsCalc to calculate the NDVI.
I iterated over a list of directories corresponding
to different months to select raster files containing b4 and b5.
My output was a tif file for each month showing the NDVI.


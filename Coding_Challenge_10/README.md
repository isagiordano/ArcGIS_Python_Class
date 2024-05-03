# Coding Challenge 10

In this challenge, I calculated the NDVI (normalized difference
vegetation index) from Landsat files. 
NDVI is calculated from Bands 4 and 5. 
The formula is (band 5- band 4) / (band 5 + band 4)

I defined a function called BandsCalc to calculate the NDVI.
I iterated over a list of directories corresponding
to different months to select raster files containing b4 and b5.
My output was a tif file for each month showing the NDVI.

I chose to visualize the area around Narragansett and South Kingston, as this is where I have spent my time here in Rhode Island and I wanted to see what the NDVI looked like around the coast. I chose the April NDVI honestly because that's when my birthday is and it's my favorite month.


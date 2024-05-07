# Final Toolbox

This toolbox (Bella's Final Toolbox) contains 4 tools- Select, Clip, Buffer, and AddMessage tools.
They are all part of one workflow (save for the last tool) in which lakes in the county of the user's choosing are buffered to the extent of their choosing. 

## Tool 1: Select

### Summary
The user will add a "Towns" shapefile which countains the feature "COUNTY." The tool will then ask the user to input a county of their choosing. The tool will select the county they chose from the Towns shapefile, and generate an output shapefile using arcpy.Select.

### Parameters
This tool requires 2 inputs and 1 output. 

**Input 1:** This should be the Towns shapefile containing a COUNTY feature. The dataset type is Feature class.  
**Input 2:** This is the name of the county chosen. The dataset type is String. 

**Output:** The output is a shapefile containing the towns in the selected county. The dataset type is Feature class.

### Messages

Upon successful completion, a message will be displayed confirming the selection was successful. Otherwise, a message will be displayed saying the tool was unable to run. 


## Tool 2: Clip

### Summary
The user will use the previously generated County shapefile, along with an added Lakes file. The tool will clip the lakes to the extent of the county using arcpy.Clip. The tool will only include lakes that are larger than 1 acre, using arcpy.MakeFeatureLayer. The tool will check coordinate systems using arcpy.Describe and provide a message to confrim or deny if the two datasets have matching coordinate systems. The tool will run if the coordinate systems do not match, but it is recommended that they match. This message will allow the user to check the coordinate systems and decide which dataset to reproject, or to use other datasets entirely. The Clip tool will then be executed, creating an output shapefile containing the lakes larger than 1 acre within the selected county. Finally, arcpy.GetCount will be used to count the number of lakes in the new shapefile.

### Parameters
This tool requires 2 inputs and 1 output. It is important to use the correct shapefile for each input.

**Input 1:** This should be the Lakes shapefile. The dataset type is Feature class. 
**Input 2:** This is the shapefile of the county generated with the last tool. The dataset type is Feature class. 

**Output:** The output is a shapefile containing the lakes larger than 1 acre in the selected county. The dataset type is Feature class.

### Messages

Upon completion, the following messages will be provided:

- a message stating if the coordinate systems of the two datasets match
- a message stating that lakes > 1 acre have been selected, or were unable to be selected
- a message stating if the clip was successfully executed
- a message stating how many lakes are in the new shapefile.
  
These messages are useful to the user if they are running into problems. They can see if tools were or were not executed correctly to track the issue.

## Tool 3: Buffer

### Summary
The user will use the Lakes in County shapefile generated previously. They will them be asked to input a buffer distance in feet. The tool will use arcpy.Buffer to buffer the lakes to the desired distance and generate a shapefile showing the buffers. Then, arcpy.Describe is used to describe a few features of the new buffer dataset- name, shapetype, and spatial extent.

### Parameters
This tool requires 2 inputs and 1 output. It is important to use the correct shapefile for each input.

**Input 1:** This should be the Lakes in the county shapefile. The dataset type is Feature class. 
**Input 2:** This is the number of feet you want to buffer. The recommended buffer distance for large water bodies like lakes is 100 feet. The dataset type is Long. 

**Output:** The output is a shapefile containing the buffer at a distance of the user's choosing. The dataset type is Feature Class.

### Messages

Upon completion, if successful, ArcGIS will display a message saying the buffer was created. It will also display the description of the new shapefile- the shapefile name, shape type, and coordinate system. 

## Tool 4: AddMessage

### Summary
This tool is just silly. It is an arcpy.AddMessage tool that asks the user "Did I slay?" and requires an answer as the input.

### Parameters
This tool requires 1 input. 

**Input 1:** Takes a string that answers the question posed to the user (yes or no).

### Messages
ArcGIS will then display the question I asked and the user's answer. 

## Thanks again for a great semester. I hope now I have slayed. 

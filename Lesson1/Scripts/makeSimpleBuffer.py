# -*- coding: utf-8 -*-
# This script runs the Buffer tool. The user supplies the input and output paths, and the buffer distance.
# Import arcpy module
import arcpy
arcpy.env.overwriteOutput = True


# Script arguments
try:
    inPath = arcpy.GetParameterAsText(0)
    outPath = arcpy.GetParameterAsText(1)
    bufferDistance = arcpy.GetParameterAsText(2)

    # Run the Buffer tool
    arcpy.Buffer_analysis(inPath, outPath, bufferDistance)

    # Report a success message    
    arcpy.AddMessage("All done!")
except:
    # Report an error messages
    arcpy.AddError("Could not complete the buffer")

    # Report any error messages that the Buffer tool might have generated    
    arcpy.AddMessage(arcpy.GetMessages())

# This script takes a DEM, a minimum elevation, and a maximum elevation. It outputs a new raster showing only areas that fall between the min and the max
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
env.workspace = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson4'
# Get parameters of min and max elevations
#inMin = arcpy.GetParameterAsText(0)
#inMax = arcpy.GetParameterAsText(1)
inMin = 2900
inMax = 3200
# Perform the map algebra and make a temporary raster
inDem = Raster("foxlake")
tempRaster = (inDem > int(inMin)) & (inDem < int(inMax))
# Set up remap table and call Reclassify, leaving all values not 1 as NODATA
remap = RemapValue([[1,1]])
remappedRaster = Reclassify(tempRaster, "Value", remap, "NODATA")
# Save the reclassified raster to disk
remappedRaster.save("foxlake_recl")
arcpy.CheckInExtension("Spatial")
print "All done!"

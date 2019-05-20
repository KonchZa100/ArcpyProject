import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
env.workspace = r"C:\Users\Sheol\Desktop\2013-14\2015-2016\ProgramGIS\ArcPy\Lesson4"

# Get parameters of min and max elevations
inMin = 3000
inMax = 3100
 
# Perform the map algebra and make a temporary raster
inDem = Raster("foxlake")
tempRaster = (inDem > int(inMin)) & (inDem < int(inMax))
# Set up remap table and call Reclassify, leaving all values not 1 as NODATA
remap = RemapValue([[1,1]])
remappedRaster = Reclassify(tempRaster, "Value", remap, "NODATA")
# Save the reclassified raster to disk
remappedRaster.save("foxlake_recl1.tif")
arcpy.CheckInExtension("Spatial")

featureClassList = arcpy.ListFeatureClasses() 
featureClass = "Temp1.shp"
if featureClass not in featureClassList:    
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, featureClass, "POINT", "", "DISABLED", "DISABLED", "foxlake")
    print "Temp1 was created"

fieldName = "Value"

arcpy.RasterToPoint_conversion("foxlake_recl1.tif", featureClass, fieldName)

print "All done!"


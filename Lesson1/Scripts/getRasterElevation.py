# This script uses map algebra to find values in an
# elevation raster greater than 3500 (meters).
import arcpy
from arcpy.sa import *

arcpy.env.overwriteOutput = True
# Specify the input raster
inRaster = "F:/Demidov/PythEveryone/PyCharmProject/Lesson1/foxlake"
cutoffElevation = 3500

# Check out the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

# Make a map algebra expression and save the resulting raster
outRaster = Raster(inRaster) > cutoffElevation
outRaster.save("F:/Demidov/PythEveryone/PyCharmProject/Lesson1/foxlake_hi_20")

# Check in the Spatial Analyst extension now that you're done
arcpy.CheckInExtension("Spatial")

print 'All done'

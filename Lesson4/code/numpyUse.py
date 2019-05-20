import arcpy
import numpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
env.workspace = r"C:\Users\Sheol\Desktop\2013-14\2015-2016\ProgramGIS\ArcPy\Lesson4"

# Get input Raster properties
inRas = arcpy.Raster('foxlake')
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

# Convert Raster to numpy array
arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=0)

# Calculate percentage of the row for each cell value
arrSum = arr.sum(1)
arrSum.shape = (arr.shape[0],1)
arrPerc = (arr)/arrSum

#Convert Array to raster (keep the origin and cellsize the same as the input)
newRaster = arcpy.NumPyArrayToRaster(arrPerc,lowerLeft,cellSize,
                                     value_to_nodata=0)
newRaster.save("foxlake_per")
arcpy.CheckInExtension("Spatial")
print "All done!"

import arcpy
from arcpy import env
env.workspace = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson4'
raster = "landcover.tif"
desc = arcpy.Describe(raster)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print "-------Raster block-------"
print "Raster base name is: " + desc.basename
print "Raster data type is: " + desc.dataType
print "Raster file extension is: " + desc.extension
print "Raster spatial reference is: " + spatialref.name
print "Raster format is: " + desc.format
print "Raster compression type is: " + desc.compressionType
print "Raster number of bands is: " + str(desc.bandCount)
print "The raster resolution is " + str(x) + " by " + str(y) + " " + units + "."

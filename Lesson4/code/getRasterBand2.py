import arcpy
from arcpy import env
env.workspace = r"C:\Users\Sheol\Desktop\2013-14\2015-2016\ProgramGIS\ArcPy\Lesson4"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print"-------Raster block-------"
print "Raster base name is: " + desc.basename
print "Raster data type is: " + desc.dataType
print "Raster file extension is: " + desc.extension

print "Raster spatial reference is: " + spatialref.name
print "Raster format is: " + desc.format
print "Raster compression type is: " + desc.compressionType
print "Raster number of bands is: " + str(desc.bandCount)
print "The raster resolution is " + str(x) + " by " + str(y) + " " + units + "."

rasterband = "tm.img/Layer_1"
desc = arcpy.Describe(rasterband)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.spatialReference
units = spatialref.angularUnitName
pixeltype = desc.pixelType
print"\n-------Rasterband block-------"

print "TThe raster resolution of Band 1 is " + str(x) + " by " + str(y) + " " + units + " in " + pixeltype + " type of pixel."


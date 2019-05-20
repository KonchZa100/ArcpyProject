import arcpy
from arcpy import env
env.workspace = r"C:\Users\Sheol\Desktop\2013-14\2015-2016\ProgramGIS\ArcPy\Lesson4"
rasterband = "landcover.tif"
desc = arcpy.Describe(rasterband)
print desc.meanCellHeight
print desc.meanCellWidth
print desc.pixelType

spatialref = desc.spatialReference
print spatialref.name
print spatialref.linearUnitName

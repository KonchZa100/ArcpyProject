import arcpy
from arcpy import env
env.workspace = r"C:\Users\Sheol\Desktop\2013-14\2015-2016\ProgramGIS\ArcPy\Lesson4"
rasterlist = arcpy.ListRasters( )
for raster in rasterlist:
    desc = arcpy.Describe(raster)
    print raster + " is <<<" + desc.dataType + ">>> raster type"

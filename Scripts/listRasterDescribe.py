import arcpy
from arcpy import env
env.workspace = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson4'
rasterlist = arcpy.ListRasters( )
for raster in rasterlist:
    desc = arcpy.Describe(raster)
    print raster + " is <<<" + desc.dataType + ">>> raster type"
    print raster + " has <<<" + desc.format + ">>> raster format"

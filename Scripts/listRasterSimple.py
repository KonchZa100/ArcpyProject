import arcpy
from arcpy import env
env.workspace = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson4'
rasterlist = arcpy.ListRasters( )
for raster in rasterlist:
    print raster

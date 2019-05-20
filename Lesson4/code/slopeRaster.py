import arcpy
from arcpy import env
env.workspace = r"C:\Users\Sheol\Desktop\2013-14\2015-2016\ProgramGIS\ArcPy\Lesson4"
arcpy.CheckOutExtension("Spatial")
outraster = arcpy.sa.Slope("elevation")
outraster.save("Slope")
print "All done!"

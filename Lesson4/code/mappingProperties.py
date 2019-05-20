'''
mapdoc = arcpy.mapping.MapDocument("CURRENT")
mapdoc.title = "Housing vacancy rates for counties in the State of Georgia, 2000"
mapdoc.save()
del mapdoc
'''

'''
import arcpy
mxd = r"C:/Users/Sheol/Desktop/arcGis/Lesson4/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
listdf = arcpy.mapping.ListDataFrames(mapdoc)
for df in listdf:
	print df.name
del mapdoc
del listdf
'''

import arcpy
mxd = r"C:/Users/Sheol/Desktop/arcGis/Lesson44/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
dataset = r"C:/Users/Sheol/Desktop/arcGis/Lesson44/Austin/base.shp"
spatialref = arcpy.Describe(dataset).spatialReference
extent = arcpy.Describe(dataset).extent
for df in arcpy.mapping.ListDataFrames(mapdoc):
        df.spatialReference = spatialref
        df.panToExtent(extent)
        df.scale = 15000
mapdoc.save()
del mapdoc


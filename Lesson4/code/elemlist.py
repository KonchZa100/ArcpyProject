import arcpy
mxd = r"C:/Users/Sheol/Desktop/arcGis/Lesson44/Georgia.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
for elem in elemlist:
    print elem.name + " " + elem.type
del mapdoc
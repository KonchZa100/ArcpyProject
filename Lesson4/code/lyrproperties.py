import arcpy
mxd = r"C:/Users/Sheol/Desktop/arcGis/Lesson44/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
lyrlist = arcpy.mapping.ListLayers(mapdoc)
for lyr in lyrlist:
    if lyr.name == "parks":
        print lyr.name
        lyr.visible = True
        lyr.showLabels = True
mapdoc.save()
del mapdoc
del lyrlist

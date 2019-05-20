import arcpy
mxd = r"C:/Users/Sheol/Desktop/arcGis/Lesson4/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
for df in arcpy.mapping.ListDataFrames(mapdoc):
    print "Data frame " + df.name + " contains the following layers:"
    lyrlist = arcpy.mapping.ListLayers(mapdoc, "", df)
    for lyr in lyrlist:
        print "\t"+lyr.name
del mapdoc

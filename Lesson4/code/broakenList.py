import arcpy

mapdoc = arcpy.mapping.MapDocument(r"C:\Users\Sheol\Desktop\arcGis\Lesson44\Austin_TX.mxd")
brokenlist = arcpy.mapping.ListBrokenDataSources(mapdoc)
if (brokenlist):
    for lyr in brokenlist:
        print lyr.name    
    mapdoc.findAndReplaceWorkspacePaths(r"C:\Users\Sheol\Desktop\arcGis\Lesson44", r"C:\Users\Sheol\Desktop\arcGis")
    mapdoc.save()
    print "\n +++ Successed execution +++"
del mapdoc

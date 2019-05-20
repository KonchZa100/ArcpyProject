import arcpy
mxd = r"C:/Users/Sheol/Desktop/arcGis/Lesson44//Georgia.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
title = elemlist[0]
title.text = "Housing Vacancy for Georgia Counties (2016)"
mapdoc.save()
del mapdoc

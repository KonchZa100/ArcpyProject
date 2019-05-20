import arcpy
 
try:
    arcpy.env.workspace =  r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2\PractiseData\\'
 
    template = "Precip2008Readings.shp"
 
    for year in range(2009,2013):
        newfile = "Precip" + str(year) + "Readings.shp"
        arcpy.CreateFeatureclass_management(arcpy.env.workspace, newfile, "POINT", template,
                                            "DISABLED", "DISABLED", template)
        print newfile + " was created"
    print ('All doe')
except:
    print arcpy.GetMessages()

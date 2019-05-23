import arcpy

arcpy.env.overwriteOutput = True
Countries =r'F:\Demidov\PythEveryone\PyCharmProject\s12\CentralAmerica.shp'
OSMpoints =r'F:\Demidov\PythEveryone\PyCharmProject\s12\OSMpoints.shp'
amenity = ['school','hospital','place_of_worship']
country = 'El Salvador'
workspace= r'F:\Demidov\PythEveryone\PyCharmProject\s12'
out_name = r'F:\Demidov\PythEveryone\PyCharmProject\s12\Geodatabase.gdb'

arcpy.env.workspace = workspace

arcpy.MakeFeatureLayer_management(OSMpoints,'osm')
arcpy.MakeFeatureLayer_management(Countries,'country', '"NAME" =' + "'" + country + "'")

arcpy.SelectLayerByLocation_management('osm', 'WITHIN', 'country')
for shel in amenity:
    arcpy.MakeFeatureLayer_management('osm',shel+'1','"amenity"='+"' "+shel+"'")
    #arcpy.FeatureClassToShapefile_conversion(str(shel), workspace)
    arcpy.CopyFeatures_management(shel+'1', out_name + '\\' + str(shel)+'elSalvador')
    arcpy.AddField_management(out_name + '\\' + str(shel),'source','TEXT')
    arcpy.AddMessage('Amenities in'+str(country)+' ' +str(shel) +' type are found')
'''
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    cursor=arcpy.InsertCursor(fc)
    for row in cursor:
        row.setValue('source','OpenStreetMap')
        cursor.updateRow(row)'''
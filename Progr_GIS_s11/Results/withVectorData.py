import arcpy
arcpy.env.overwriteOutput = True
facilitshp = arcpy.GetParameterAsText(0)
zipshp = arcpy.GetParameterAsText(1)
resultsWorkspace = arcpy.GetParameterAsText(2)

distancelow = arcpy.GetParameterAsText(3) #1000
distanceup = arcpy.GetParameterAsText(4) #3000
fieldName = arcpy.GetParameterAsText(5) #FACILITY
fieldvalue = arcpy.GetParameterAsText(6) #COLLEGE
arcpy.env.workspace = resultsWorkspace


arcpy.MakeFeatureLayer_management(facilitshp, 'facilit')
arcpy.MakeFeatureLayer_management(zipshp, 'zip')
arcpy.AddMessage('Making feature layers')
arcpy.SelectLayerByLocation_management('facilit', 'WITHIN_A_DISTANCE', 'zip', distanceup + ' meters ', 'NEW_SELECTION')
arcpy.SelectLayerByLocation_management('facilit', 'WITHIN_A_DISTANCE', 'zip', distancelow + ' meters ', "REMOVE_FROM_SELECTION")
arcpy.SelectLayerByAttribute_management("facilit", "SUBSET_SELECTION", '"' + str(fieldName) + '" =' + "'" + str(fieldvalue) + "'")
arcpy.AddMessage('Selecting objects within ' + distanceup + " meters with '{}' values in the field '{}'".format(fieldvalue, fieldName))



res_shp = "facilities_Distance_"+distanceup+'.shp'
arcpy.CreateFeatureclass_management(arcpy.env.workspace, res_shp, "POINT", spatial_reference="facilit")

#create new fields
insertfields = ['ADDRESS', 'NAME', 'FACILITY']
for f in insertfields:
    arcpy.AddField_management(res_shp, f, "TEXT")

searchFields = ('SHAPE@XY', 'ADDRESS', 'NAME', 'FACILITY')
with arcpy.da.InsertCursor(res_shp, searchFields) as cursorInsert, arcpy.da.SearchCursor("facilit", searchFields) as cursorSearch:
    for row in cursorSearch:
        cursorInsert.insertRow(row)
arcpy.AddMessage("Updated fields: ".format(str(searchFields)))



newfield = fieldvalue[:5] + '_NAME'
arcpy.AddField_management(res_shp, newfield, "Float")

searchvalues = []
with arcpy.da.SearchCursor("facilit", ('FAC_ID',)) as cursors, arcpy.da.UpdateCursor(res_shp, (newfield)) as cursori:
    for row in cursors:
        searchvalues.append(row)
    i = 0
    for row in cursori:
        row = searchvalues[i]
        cursori.updateRow(row)
        i += 1



mxd = arcpy.mapping.MapDocument("CURRENT")
dataframe = arcpy.mapping.ListDataFrames(mxd, "*")[0]
addLayer = arcpy.mapping.Layer(res_shp)
arcpy.mapping.AddLayer(dataframe, addLayer, "AUTO_ARRANGE")
del addLayer, mxd, dataframe

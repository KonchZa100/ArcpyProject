'''
import arcpy
inTable = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2\CityBoundaries.shp'
inField = "NAME"
 
rows = arcpy.SearchCursor(inTable)
 
#This loop goes through each row in the table
#  and gets a requested field value
 
for row in rows:
    currentCity = row.getValue(inField)
    print currentCity

# Prints the name of each city in a feature class

import arcpy

featureClass = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2PracticeExercise\USA.gdb\Cities'

rows = arcpy.SearchCursor(featureClass)
row = rows.next()

while row:
    print row.NAME
    row = rows.next()
'''
import arcpy
inTable = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2\CityBoundaries.shp'

rows = arcpy.SearchCursor(inTable)
 
#This loop goes through each row in the table
#  and gets a requested field value
field_names = [f.name for f in arcpy.ListFields(inTable)]

#print field_names
 
for row in rows:
    #currentCity = row.getValue(inField) #print currentCity
    print "++++++++++++++++++++"
    for col in field_names:
        currentCity = row.getValue(col)
        print str(col)+" -> "+str(currentCity)

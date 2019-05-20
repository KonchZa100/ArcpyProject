# Finds the average population in a counties dataset

import arcpy

featureClass = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2PracticeExercise\Pennsylvania\Pennsylvania.gdb\counties'
populationField = 'NAME'
where_clause = '"NAME"='+"'Krim'"

rows = arcpy.SearchCursor(featureClass, where_clause, fields=populationField)
row = rows.next()

while row:
    print row.getValue("NAME")
    row = rows.next()

# Finds the average population in a counties dataset

import arcpy

featureClass = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2PracticeExercise\Pennsylvania\Pennsylvania.gdb\counties'
populationField = "POP1990"

with arcpy.da.SearchCursor(featureClass, (populationField,) , '"POP1990" > 100000') as cursor:
    for row in cursor:
        print str(row[0])

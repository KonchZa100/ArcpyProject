# Reads the fields in a feature class

import arcpy

featureClass = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2PracticeExercise\USA.gdb\Cities'
fieldList = arcpy.ListFields(featureClass)

# Loop through each field in the list and print the name
for field in fieldList:
    print field.name

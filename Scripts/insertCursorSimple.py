#add new field in feature class
import arcpy

fc = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson3\USA.gdb\CitiesCopy2'
newField = ["NAME","CAPITAL"]

with arcpy.da.InsertCursor(fc, newField) as cursor:       
        cursor.insertRow(["Kiev",3])
        del cursor
print "All done!"

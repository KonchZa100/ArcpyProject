#Simple search and replace script
import arcpy
# Retrieve input parameters: the feature class, the field affected by
# the search and replace, the search term, and the replace term.
fc = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson3\Alabama.gdb\StateBoundary'
#newField = "POPULATION"
affectedField = "BOUND_P_"
oldValue = 1421
newValue = 1422
 
# Create the SQL expression for the update cursor. Here this is
#  done on a separate line for readability.
queryString = '"BOUND_P_" = '+ str(oldValue)
 # Create the update cursor and update each row returned by the SQL expression
with arcpy.da.UpdateCursor(fc, (affectedField,), queryString) as cursor:
    for row in cursor:
        row[0] = newValue
        cursor.updateRow(row)
print "All done!"


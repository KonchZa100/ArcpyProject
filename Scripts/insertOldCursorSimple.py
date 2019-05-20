#add new field in feature class
import arcpy

# Create insert cursor for table
fc = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson3\USA.gdb\CitiesCopy2'
rows = arcpy.InsertCursor(fc)

# Create 25 new rows. Set the initial row ID and distance values
for x in xrange(1, 26):
    row = rows.newRow()
    row.setValue("UIDENT", x)
    row.setValue("POPCLASS", 1)
    rows.insertRow(row)

# Delete cursor and row objects to remove locks on the data
del row
del rows

print "All done!"

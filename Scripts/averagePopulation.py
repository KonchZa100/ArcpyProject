# Finds the average population in a counties dataset
import arcpy

#featureClass = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2PracticeExercise\Pennsylvania\counties.shp'
featureClass = arcpy.GetParameterAsText(0)
populationField = arcpy.GetParameterAsText(1)

rows = arcpy.SearchCursor(featureClass)
row = rows.next()

average = 0
totalPopulation = 0
recordsCounted = 0

# Loop through each row and keep running total of population
# and records counted.
while row:
    totalPopulation += row.POP1990 ###totalPopulation += row.getValue(populationField)
    recordsCounted += 1
    row = rows.next()
average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)
##############################
for row in rows:
    totalPopulation += row.getValue(populationField)
    recordsCounted += 1
average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)

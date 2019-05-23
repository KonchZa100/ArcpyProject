import arcpy
import os

arcpy.env.overwriteOutput = True

targetFC=r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2\CountyLines.shp'
folderToExamine=r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2\PractiseData\Result'

targetSR=arcpy.Describe(targetFC).spatialReference
#targetSRName=targetSR.SpatialReference.Name
print targetSR
'''
arcpy.env.workspace = folderToExamine
listOfFCs = arcpy.ListFeatureClasses()

for currentFC in listOfFCs:
    currentFCSRName = arcpy.Describe(currentFC).SpatialReference.Name
    if currentFCSRName != targetSRName:
        outCS = arcpy.SpatialReference('NAD 1983 UTM Zone 10N')
        rootName = currentFC[:-4] + "_projected.shp"
        arcpy.Project_management(currentFC, rootName, outCS)
        arcpy.AddMessage(rootName)'''
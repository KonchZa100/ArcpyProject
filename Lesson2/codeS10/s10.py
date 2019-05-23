import arcpy
import os

arcpy.env.overwriteOutput = True

targetFC=arcpy.GetParameterAsText(0)
folderToExamine=arcpy.GetParameterAsText(1)

targetSR=arcpy.Describe(targetFC).spatialReference.name
#targetSRName=targetSR.SpatialReference.Name
print targetSR

arcpy.env.workspace = folderToExamine
listOfFCs = arcpy.ListFeatureClasses()

for currentFC in listOfFCs:
    currentFCSRName = arcpy.Describe(currentFC).SpatialReference.Name
    if currentFCSRName != targetSR:
        outCS = arcpy.SpatialReference('NAD 1983 UTM Zone 10N')
        rootName = currentFC[:-4] + "_projected.shp"
        arcpy.Project_management(currentFC, rootName, outCS)
        arcpy.AddMessage(rootName)
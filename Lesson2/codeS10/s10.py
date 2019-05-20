import arcpy

arcpy.env.overwriteOutput = True

targetFC=
folderToExamine=

targetSRName=arcpy.Describe(targetFC).SpatialReference.Name
arcpy.env.workspace = folderToExamine
listOfFCs = arcpy.ListFeatureClasses()

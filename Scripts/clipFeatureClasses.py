# This script clips all datasets in a folder
import arcpy

inFolder = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2\PractiseData\\'
resultsFolder = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2\PractiseData\Result\\'
clipFeature = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2\PractiseData\Result\Nebraska.shp'
 
# List feature classes
arcpy.env.workspace = inFolder
featureClassList = arcpy.ListFeatureClasses()
 
# Loop through each feature class and clip
for featureClass in featureClassList:
     
    # Make the output path by concatenating strings
    outputPath = resultsFolder + featureClass
    print 'New FC is ' + outputPath
    # Clip the feature class
    arcpy.Clip_analysis(featureClass, clipFeature, outputPath)
print 'All done!'

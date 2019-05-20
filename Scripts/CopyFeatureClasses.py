# Copies all feature classes from one folder to another
import arcpy

try:
    arcpy.env.workspace = r"F:\Demidov\PythEveryone\PyCharmProject\Lesson1\Precip2008\\"

    # List the feature classes in the Lesson 1 folder
    fcList = arcpy.ListFeatureClasses()
    print (fcList)
    
    # Loop through the list and copy the feature classes to the Lesson 2 PracticeData folder
    for featureClass in fcList:
        arcpy.CopyFeatures_management(featureClass, r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2\PractiseData'+'\\' + featureClass)
        print 'New ' + featureClass + ' was created'
    print 'All done!'
except:
    print "Script failed to complete"
    print arcpy.GetMessages(2)

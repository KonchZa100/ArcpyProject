# Opens a feature class from a geodatabase and prints the spatial reference
 
import arcpy
 
featureClass = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson1\StateBoundaries.lyr'
 
# Describe the feature class and get its spatial reference   
desc = arcpy.Describe(featureClass)

print ('Describe object was created')

spatialRef = desc.spatialReference
 
# Print the spatial reference name
print (spatialRef.Name)
print (desc.lengthFieldName) #GDB Feature Class
print (desc.shapeType) # Feature Class

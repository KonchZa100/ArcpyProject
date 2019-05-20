import arcpy
import sys
# Get the layer as a parameter and describe it.
## The layer could be a layer in ArcMap (like "some_layer")
# Or, it could be a .lyr file (like "C:/data/some.lyr")

layerString = arcpy.GetParameterAsText(0)
#layerString = sys.argv[1]
#layerString = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson1\StateBoundaries.lyr'
desc = arcpy.Describe(layerString)

# Print selected layer and describe object properties
'''
print("Name: {}".format(desc.name))
if hasattr(desc, "layer"):
    print("Layer name: {}".format(desc.layer.name))
    print("Layer data source: {}".format(desc.layer.catalogPath))
    print(".lyr file: {}".format(desc.catalogPath))
else:
    print("Layer name: {}".format(desc.name))
    print("Layer data source: {}".format(desc.catalogPath))

if desc.FIDSet != '':
    print("Number of selected features: {}".format(len(desc.FIDSet.split(";"))))
'''
arcpy.AddMessage("Name: {}".format(desc.name))
if hasattr(desc, "layer"):
    arcpy.AddMessage("Layer name: {}".format(desc.layer.name))
    arcpy.AddMessage("Layer data source: {}".format(desc.layer.catalogPath))
    arcpy.AddMessage(".lyr file: {}".format(desc.catalogPath))
else:
    arcpy.AddMessage("Layer name: {}".format(desc.name))
    arcpy.AddMessage("Layer data source: {}".format(desc.catalogPath))

if desc.FIDSet != '':
    arcpy.AddMessage("Number of selected features: {}".format(len(desc.FIDSet.split(";"))))
arcpy.AddMessage("All done")

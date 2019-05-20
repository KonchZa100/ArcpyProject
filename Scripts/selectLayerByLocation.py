# Selects all states whose boundaries touch a user-supplied state
import arcpy
# Get the US States layer, state, and state name field
usaLayer = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2PracticeExercise\USA.gdb\StateBoundaries'
state = "Wyoming"
nameField = "NAME"
try:
    # Make a feature layer with all the US States
    arcpy.MakeFeatureLayer_management(usaLayer, "AllStatesLayer")
    # Make a feature layer containing only the state of interest
    arcpy.MakeFeatureLayer_management(usaLayer, "SelectionStateLayer", '"' + str(nameField) + '" =' + "'" + str(state) + "'")
    # Apply a selection to the US States layer
    arcpy.SelectLayerByLocation_management("AllStatesLayer","BOUNDARY_TOUCHES","SelectionStateLayer")
    # Open a search cursor on the US States layer
    with arcpy.da.SearchCursor("AllStatesLayer", (nameField,)) as cursor:
        for row in cursor:
            # Print the name of all the states in the selection
            print row[0]
except:
    print arcpy.GetMessages()
# Clean up feature layers
arcpy.Delete_management("AllStatesLayer")
arcpy.Delete_management("SelectionStateLayer")

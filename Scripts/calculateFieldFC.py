import arcpy

fc = r'F:\Demidov\PythEveryone\PyCharmProject\Lesson2PracticeExercise\USA.gdb\CitiesCopy'

# Get a list of field objects
#
fields = arcpy.ListFields(fc)

for field in fields:
    # Check the field name, perform a calculation when finding the field 'Flag'
    #
    print field.name
    if field.name == 'CAPITAL':
        # Set the NEW value for the field and exit loop
        #
        arcpy.CalculateField_management(fc, 'CAPITAL', '1')
        break

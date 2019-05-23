import arcpy

arcpy.env.overwriteOutput = True
poligon =r'F:\Demidov\PythEveryone\PyCharmProject\s12\CentralAmerica.shp'
points =r'F:\Demidov\PythEveryone\PyCharmProject\s12\OSMpoints.shp'
amenities = ('school','hospital','place_of_worship')
country = 'El Salvador'
workspace= r'F:\Demidov\PythEveryone\PyCharmProject\s12'
out_name = r'F:\Demidov\PythEveryone\PyCharmProject\s12\Geodatabase.gdb'
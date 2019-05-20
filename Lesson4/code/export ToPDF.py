import arcpy

# Create a MapDocument object referencing the MXD you want to update
mxd = arcpy.mapping.MapDocument(r"C:\Users\Sheol\Desktop\arcGis\Lesson44\Austin_TX.mxd")
 
# Loop through each text element in the map document
for textElement in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
     
    # Check if the text element contains the out of date text
    if textElement.text == "GIS Services Division 2015":
         
    # If out of date text is found, replace it with the new text
        textElement.text = "GIS Services Division 2016"
         
# Export the updated map to a PDF
arcpy.mapping.ExportToPDF(mxd, r"C:\Users\Sheol\Desktop\arcGis\Lesson44\Austin_TX.pdf")
 
# Clean up the MapDocument object by deleting it
del mxd

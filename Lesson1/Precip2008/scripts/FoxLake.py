import arcpy

# ---------------------------------------------------------------------------
arcpy.env.overwriteOutput = True

try:
    # Local variables:
    rastr = arcpy.GetParameterAsText(0)
    VectorModel = arcpy.GetParameterAsText(1)
    arcpy.AddMessage("All done!")

except:
    # Report an error messages
    arcpy.AddError("Could not complete the vector model")

    # Report any error messages that the Buffer tool might have generated
    arcpy.AddMessage(arcpy.GetMessages())

arcpy.gp.Contour_sa(rastr, VectorModel, "25", "0", "1")

# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# MODELPRECIp.py
# Created on: 2019-05-20 22:27:04.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
Precip2008Readings = "F:\\Demidov\\PythEveryone\\PyCharmProject\\Lesson1\\Precip2008\\Precip2008.gdb\\Precip2008Readings"
IdwRaster = "F:\\Demidov\\PythEveryone\\PyCharmProject\\Lesson1\\Precip2008\\IdwRaster"
ReclassIdw = "F:\\Demidov\\PythEveryone\\PyCharmProject\\Lesson1\\Precip2008\\Precip2008.gdb\\ReclassIdw"
RasterT_Reclass1 = "F:\\Demidov\\PythEveryone\\PyCharmProject\\Lesson1\\Precip2008\\Precip2008.gdb\\RasterT_Reclass1"
Nebraska__2_ = "F:\\Demidov\\PythEveryone\\PyCharmProject\\Lesson1\\Precip2008\\Precip2008.gdb\\Nebraska"
RasterT_Reclass1_Clip = "F:\\Demidov\\PythEveryone\\PyCharmProject\\Lesson1\\Precip2008\\Precip2008.gdb\\RasterT_Reclass1_Clip"

# Process: IDW
arcpy.gp.Idw_sa(Precip2008Readings, "RASTERVALU", IdwRaster, "1850,46467", "2", "VARIABLE 12", "")

# Process: Reclassify
arcpy.gp.Reclassify_sa(IdwRaster, "VALUE", "27715,960938 57484,319210 1;57484,319210 80383,056342 2;80383,056342 111132,789063 3", ReclassIdw, "DATA")

# Process: Raster to Polygon
arcpy.RasterToPolygon_conversion(ReclassIdw, RasterT_Reclass1, "SIMPLIFY", "VALUE")

# Process: Clip
arcpy.Clip_analysis(RasterT_Reclass1, Nebraska__2_, RasterT_Reclass1_Clip, "")


# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2021-04-09 13:22:11
"""
import arcpy

def Model11():  # HSM_Model_YE

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("3D")

    CSEO_YE_logbook = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\CSEO_YE_logbook"
    CSEO_YE_logbook_2_ = "CSEO_YE_logbook"
    CSEORugosity = arcpy.Raster("CSEORugosity")
    CSEO_YE_logbook_3_ = "CSEO_YE_logbook"
    Band_1 = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\SEAK_bathy\\Band_1"
    CSEO_YE = "CSEO_YE"
    CSEORugosity_2_ = arcpy.Raster("Rugosity - CSEO\\CSEORugosity")
    Band_1_3_ = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\CSEORugosity\\Band_1"
    CSEO_YE_logbook_4_ = "CSEO_YE_logbook"
    CSEO_YE_2_ = "CSEO_YE"
    Band_1_4_ = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\ALFA_bathy_DSR\\Band_1"
    CSEO_YE_3_ = "CSEO_YE"
    CSEO_YE_logbook_5_ = "CSEO_YE_logbook"
    ALFA_Slope_CSEO_3_ = arcpy.Raster("ALFA_Slope_CSEO")
    ALFA_Slope_CSEO_2_ = arcpy.Raster("ALFA_Slope_CSEO")

    # Process: Extract Values to Points (Extract Values to Points) (sa)
    YE_CSEO_Rugosity = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\YE_CSEO_Rugosity"
    arcpy.sa.ExtractValuesToPoints(in_point_features=CSEO_YE_logbook_2_, in_raster=CSEORugosity, out_point_features=YE_CSEO_Rugosity, interpolate_values="NONE", add_attributes="VALUE_ONLY")

    # Process: Extract by Mask (Extract by Mask) (sa)
    SEAK_Bath_CSEO = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\SEAK_Bath_CSEO"
    Extract_by_Mask = SEAK_Bath_CSEO
    SEAK_Bath_CSEO = arcpy.sa.ExtractByMask(in_raster=Band_1, in_mask_data=CSEO_YE)
    SEAK_Bath_CSEO.save(Extract_by_Mask)


    # Process: Extract Values to Points (3) (Extract Values to Points) (sa)
    YE_CSEO_Depth = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\YE_CSEO_Depth"
    arcpy.sa.ExtractValuesToPoints(in_point_features=CSEO_YE_logbook_3_, in_raster=SEAK_Bath_CSEO, out_point_features=YE_CSEO_Depth, interpolate_values="NONE", add_attributes="VALUE_ONLY")

    # Process: Reclassify (Reclassify) (3d)
    CSEO_RC_Depth = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\CSEO_RC_Depth"
    arcpy.ddd.Reclassify(in_raster=SEAK_Bath_CSEO, reclass_field="VALUE", remap="-3449 -1555 1;-1555 -835 2;-835 -715 3;-715 -115 4;-115 0 3;0 23 1", out_raster=CSEO_RC_Depth, missing_values="DATA")
    CSEO_RC_Depth = arcpy.Raster(CSEO_RC_Depth)

    # Process: Extract by Attributes (Extract by Attributes) (sa)
    High_Elev_Rug_C = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\High_Elev_Rug_C"
    Extract_by_Attributes = High_Elev_Rug_C
    High_Elev_Rug_C = arcpy.sa.ExtractByAttributes(in_raster=Band_1_3_, where_clause="VALUE >= 0.01")
    High_Elev_Rug_C.save(Extract_by_Attributes)


    # Process: Euclidean Distance (Euclidean Distance) (sa)
    CSEO_ED = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\CSEO_ED"
    Euclidean_Distance = CSEO_ED
    Output_direction_raster = ""
    Out_back_direction_raster = ""
    CSEO_ED = arcpy.sa.EucDistance(in_source_data=High_Elev_Rug_C, maximum_distance=None, cell_size="7.01354840000005E-04", out_direction_raster=Output_direction_raster, distance_method="PLANAR", in_barrier_data="", out_back_direction_raster=Out_back_direction_raster)
    CSEO_ED.save(Euclidean_Distance)


    # Process: Extract by Mask (2) (Extract by Mask) (sa)
    ED_CSEO_mask = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\ED_CSEO_mask"
    Extract_by_Mask_2_ = ED_CSEO_mask
    ED_CSEO_mask = arcpy.sa.ExtractByMask(in_raster=CSEO_ED, in_mask_data=CSEO_YE_2_)
    ED_CSEO_mask.save(Extract_by_Mask_2_)


    # Process: Extract Values to Points (2) (Extract Values to Points) (sa)
    YE_CSEO_ED = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\YE_CSEO_ED"
    arcpy.sa.ExtractValuesToPoints(in_point_features=CSEO_YE_logbook_4_, in_raster=ED_CSEO_mask, out_point_features=YE_CSEO_ED, interpolate_values="NONE", add_attributes="VALUE_ONLY")

    # Process: Reclassify (2) (Reclassify) (3d)
    CSEO_RC_ED = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\CSEO_RC_ED"
    arcpy.ddd.Reclassify(in_raster=ED_CSEO_mask, reclass_field="VALUE", remap="0 0.053600 4;0.053600 0.073700 3;0.073700 0.107200 2;0.107200 0.217023 1", out_raster=CSEO_RC_ED, missing_values="DATA")
    CSEO_RC_ED = arcpy.Raster(CSEO_RC_ED)

    # Process: Extract by Mask (3) (Extract by Mask) (sa)
    ALFA_Bathy_CSEO = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\ALFA_Bathy_CSEO"
    Extract_by_Mask_3_ = ALFA_Bathy_CSEO
    ALFA_Bathy_CSEO = arcpy.sa.ExtractByMask(in_raster=Band_1_4_, in_mask_data=CSEO_YE_3_)
    ALFA_Bathy_CSEO.save(Extract_by_Mask_3_)


    # Process: Slope (Slope) (3d)
    ALFA_Slope_CSEO = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\ALFA_Slope_CSEO"
    arcpy.ddd.Slope(in_raster=ALFA_Bathy_CSEO, out_raster=ALFA_Slope_CSEO, output_measurement="DEGREE", z_factor=0.008, method="PLANAR", z_unit="METER")
    ALFA_Slope_CSEO = arcpy.Raster(ALFA_Slope_CSEO)

    # Process: Extract Values to Points (4) (Extract Values to Points) (sa)
    YE_CSEO_Slope = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\YE_CSEO_Slope"
    arcpy.sa.ExtractValuesToPoints(in_point_features=CSEO_YE_logbook_5_, in_raster=ALFA_Slope_CSEO_3_, out_point_features=YE_CSEO_Slope, interpolate_values="NONE", add_attributes="VALUE_ONLY")

    # Process: Reclassify (3) (Reclassify) (3d)
    CSEO_RC_Slope = "E:\\Yelloweye HSM Outside Federal\\YE_HSM_Federal.gdb\\CSEO_RC_Slope"
    arcpy.ddd.Reclassify(in_raster=ALFA_Slope_CSEO_2_, reclass_field="VALUE", remap="0 50 1;50 70 2;70 80 3;80 89.947891 4", out_raster=CSEO_RC_Slope, missing_values="DATA")
    CSEO_RC_Slope = arcpy.Raster(CSEO_RC_Slope)

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\klwood\Documents\ArcGIS\Projects\MyProject3\MyProject3.gdb", workspace=r"C:\Users\klwood\Documents\ArcGIS\Projects\MyProject3\MyProject3.gdb"):
        Model11()

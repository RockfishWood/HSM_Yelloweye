# HSM_Yelloweye
## Python code from ModelBuilder for yelloweye rockfish habitat suitability modeling in Southeast Alaska.

### **KEY DATA USED:**

- Yelloweye rockfish logbook data: Dates, Latitude, Longitude, Number of Fish Per Coordinate. Used to determine suitability classes when extracting raster cell values to yelloweye rockfish points.

- SEAK Management Areas (vector polygon shapefile): Used to create mask of raster data to shorten processing time and create model in smaller defined area.

- Bathymetric Raster (bath_stp): Foot_US, Cell Size 164, NAD 1927, StatePlane Alaska 1 FIPS 5001. Used for depth variable, to create a slope raster, and to obtain a rugosity layer from the Benthic Terrain Modeler (https://coast.noaa.gov/digitalcoast/tools/btm.html).


### **KEY GIS TOOLS USED (Most utilized in ArcGIS Pro):**

- Extract by Mask (Spatial Analyst Tools)

- Extract Values to Points (Spatial Analyst Tools)

- Slope (degrees) (Spatial Analyst Tools)

- Hillshade (Spatial Analyst Tools)

- Benthic Terrain Modeler (https://coast.noaa.gov/digitalcoast/tools/btm.html) to obtain rugosity (VRM) - Requires ArcGIS 10.x and the Spatial Analyst extension

- Summarize (in attribute table - summed number of fish per raster value)

- Reclassify (Spatial Analyst Tools)

- Euclidean Distance (Spatial Analyst Tools)

- Weighted Overlay (to multiply reclassified rasters to create final HSM)

### GENERAL STEPS USED

- Clip bathymetry raster down to a workable size for your species/study area.
- 
- Create environmental variables (rasters) by extracting environmental variable raster cell values to species presence data.
- 
- Summarize number of species per raster values to determine appropriate classes (i.e., 1 - not suitable, 2 - low suitability, 3 - moderate suitability, 4 - high suitability). Exporting data into Excel or R to run frequency bins is best way to determine appropriate classes.

- Reclassify base raster files to match predetermined classes.
- 
- Multiply reclassified variable rasters with weighted overlay tool. Start with equal weights and compare to species presence data, and then adjust weights as necessary.




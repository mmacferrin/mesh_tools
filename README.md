#mesh_tools

# Prepare fault for meshing
#Step 1: Convert fault rupture KML to SHP
#ogr2ogr outputShapefile.shp input.kml

ogr2ogr Ridgecrest_Surface_Ruptures.shp Ridgecrest_Surface_Ruptures.kml

#Step 2: Smooth fault rupture SHP
ogr2ogr outputShapefile_smoothed.shp outputShapefile.shp -simplify 0.05

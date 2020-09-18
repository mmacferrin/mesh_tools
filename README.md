#mesh_tools

# Prepare fault for meshing
## Step 1: Convert fault rupture KML to SHP
```
ogr2ogr Ridgecrest_Surface_Ruptures.shp Ridgecrest_Surface_Ruptures.kml
```
## Step 2: Smooth fault rupture SHP
```
ogr2ogr Ridgecrest_Surface_Ruptures_smoothed.shp Ridgecrest_Surface_Ruptures.shp -simplify 0.002
```
## Step 3: Convert to kml again for viewing
ogr2ogr Ridgecrest_Surface_Ruptures_smoothed.kml Ridgecrest_Surface_Ruptures_smoothed.shp

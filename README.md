# Prepare fault for meshing
## Step 1: Convert fault rupture KML to SHP
```
ogr2ogr Ridgecrest_Surface_Ruptures.shp Ridgecrest_Surface_Ruptures.kml
```
## Step 2: Smooth fault rupture SHP
```
ogr2ogr Ridgecrest_Surface_Ruptures_0.002.shp Ridgecrest_Surface_Ruptures.shp -simplify 0.002
```
## Step 3: Run ./faultrace_shp2jou.py
```
faulttrace_shp2jou.py -i RidgecrestSurfaceRuptures_downloaded.shp -lat 35.7665 -lon -117.6048
```

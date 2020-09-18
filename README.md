## Prepare fault for meshing

#### Step 0: Download fault rupture kmz file from [Ridgecrest SCEC Response](https://response.scec.org/sites/default/files/Ridgecrest%20Surface%20Ruptures_0.kmz). Open it in GoogleEarth/GoogleEarthPro. Remove smaller rupture traces. Resave as kml file.

#### Step 1: Convert fault rupture filetype from kml to shp
##### Input: RidgecrestSurfaceRuptures_4faults.kml
##### Output: RidgecrestSurfaceRuptures_4faults.shp
```
ogr2ogr RidgecrestSurfaceRuptures_4faults.shp RidgecrestSurfaceRuptures_4faults.kml
```
#### Step 2: Smooth fault rupture shp file
##### Input: RidgecrestSurfaceRuptures_4faults.shp
##### Output: RidgecrestSurfaceRuptures_4faults_0.003.shp 

```
ogr2ogr RidgecrestSurfaceRuptures_4faults_0.003.shp RidgecrestSurfaceRuptures_4faults.shp -simplify 0.003
```
#### Step 3: Create journal file for CUBIT
##### Input: RidgecrestSurfaceRuptures_4faults_0.003.shp
##### Output: RidgecrestSurfaceRuptures_4_faults_0.003.jou
```
faulttrace_shp2jou.py -i RidgecrestSurfaceRuptures_4faults_0.003.shp -lat 35.7665 -lon -117.6048
```
#### Step 4: Load and run journal file in CUBIT's Journal Editor
![alt text](https//github.com/magalibarbasevilla/mesh_tools/)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import utm

def latlon2EQdist(eq_lat,eq_lon,lat,lon):
	dx=[]
	dy=[]
	eq = utm.from_latlon(eq_lat,eq_lon)
	eq_x,eq_y=eq[0],eq[1]

	#print "UTM ZONE INFO: ", eq
	for p in range(len(lat)):
		xy = utm.from_latlon(lat[p],lon[p])
		x,y = xy[0],xy[1]
		dx_in = x - eq_x
		dy_in = y - eq_y #in m!!
		dx=np.append(dx,dx_in)
		dy=np.append(dy,dy_in)

	return dx,dy


def EQdist2latlon(lat,lon,zone_num,zone_let):
	dx=[]
	dy=[]
	for p in range(len(lat)):
		xy = utm.to_latlon(lat[p],lon[p],zone_num,zone_let)
		x,y = xy[0],xy[1]
		dx_in = x 
		dy_in = y
		dx=np.append(dx,dx_in)
		dy=np.append(dy,dy_in)

	return x,y


def eq_dist_2latlon(eq_lat,eq_lon,north_offset,east_offset):
	eq = utm.from_latlon(eq_lat,eq_lon)
	eq_x,eq_y,zone_num,zone_let=eq[0],eq[1],eq[2],eq[3]

	print zone_num, zone_let
	new_x, new_y= eq[0]+east_offset, eq[1]+north_offset
	print "original x & y (km)", eq_x, eq_y
	print "new x & y",new_x,new_y
	new_lat,new_lon = utm.to_latlon(new_x,new_y,zone_num,zone_let)
	print "new lat and lon:", new_lat,new_lon
	return new_lat,new_lon






#dx_max,dy_max= latlon2EQdist(eq_lat_usgs,eq_lon_usgs,[eq_m5_lat],[eq_m5_lon])

#print dx_max,dy_max
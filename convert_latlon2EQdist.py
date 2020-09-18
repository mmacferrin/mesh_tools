#!/usr/bin/env python3

import numpy as np
import utm

def latlon2EQdist(eq_lat,eq_lon,lat,lon):
	dx=[]
	dy=[]
	eq = utm.from_latlon(eq_lat,eq_lon)
	eq_x,eq_y=eq[0],eq[1]

	for p in range(len(lat)):
		xy = utm.from_latlon(lat[p],lon[p])
		x,y = xy[0],xy[1]
		dx_in = x - eq_x
		dy_in = y - eq_y #in m!!
		dx=np.append(dx,dx_in)
		dy=np.append(dy,dy_in)

	return dx,dy
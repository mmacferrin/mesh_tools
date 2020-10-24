#!/usr/bin/env python3

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyvista as pv
import matplotlib

#matplotlib.rcParams['font.sans-serif'] = "Comic Sans MS"
matplotlib.rc('font', serif='Arial')


#pv.set_plot_theme("default")
pv.set_plot_theme("document")
#pv.set_plot_theme("ParaView")

################################################################
# Load fault nodes for slip plot
################################################################
node_fname = 'fault2loc.txt'
node_data = pd.read_table(node_fname,header=0,sep='\s+')
inode = np.array(node_data['inode']).astype(int)

node_fname = 'plotNodes.dat'
node_data = pd.read_table(node_fname,sep='\s+',header=None)
node_data = node_data.T
node_data.columns = ['node']
node_id = node_data['node']

blocks = pv.read_exodus('mesh_4plots.exo')

print(blocks.keys())

args_grid = dict(label_font_size=50,title_font_size=50)


meshes = blocks['Element Blocks'] 

mantle_block = meshes[0]
crust_block = meshes[1]
fault_block = meshes[2]

faults = blocks['Side Sets'][2]


##################################################
# Plot simple rheology structure
################################################## 

p = pv.Plotter(window_size=[1400,1400])
#p.set_background("31092D")
#p.add_mesh(meshes,show_edges=True,lighting=False,color='lightgoldenrodyellow') #, point_size=8.0, render_points_as_spheres=True)
p.add_mesh(mantle_block,show_edges=False,lighting=False,color='97bfc7',line_width=0.1) 
p.add_mesh(crust_block,show_edges=False,lighting=False,color='b9b9b7',line_width=0.1) 
p.add_mesh(fault_block,show_edges=False,lighting=False,color='e5b397',line_width=0.1) 

p.add_mesh(faults,lighting=False,color='white',edge_color='red',show_edges=True,line_width=4)

#p.add_mesh(faults,show_edges=True,lighting=False,color='452142',line_width=1) #edge_color

p.show_bounds(grid='front', location='outer', all_edges=True,font_size=50,font_family='arial')
p.remove_scalar_bar()
p.enable_terrain_style()
p.show_axes()

side_cpos = [(-534.3440717049617, -1034.4191150136714, 952.1763261588785),
 (6.874786376953125, -4.4228363037109375, -249.99999999999545),
 (0.0, 0.0, 1.0)]

test = p.show(cpos=side_cpos,screenshot="model.png")
print(test)


##################################################
# Plot simple rheology structure with edges (aka wire frame)!
################################################## 

p = pv.Plotter(window_size=[1400,1400])
#p.set_background("31092D")
#p.add_mesh(meshes,show_edges=True,lighting=False,color='lightgoldenrodyellow') #, point_size=8.0, render_points_as_spheres=True)
p.add_mesh(mantle_block,show_edges=True,lighting=False,color='97bfc7',line_width=0.1) 
p.add_mesh(crust_block,show_edges=True,lighting=False,color='b9b9b7',line_width=0.1) 
p.add_mesh(fault_block,show_edges=True,lighting=False,color='e5b397',line_width=0.1) 

p.add_mesh(faults,lighting=False,color='white',edge_color='red',show_edges=True,line_width=4)

#p.add_mesh(faults,show_edges=True,lighting=False,color='452142',line_width=1) #edge_color

p.show_bounds(grid='front', location='outer', all_edges=True,font_size=50,font_family='arial')
p.remove_scalar_bar()
p.enable_terrain_style()
p.show_axes()

test = p.show(cpos=side_cpos,screenshot="model_mesh.png")
print(test)


##################################################
# Make fake legend
################################################## 
plt.figure()
plt.plot([],[],'-',color='#97bfc7',linewidth=10,label='mantle block')
plt.plot([],[],'-',color='#b9b9b7',linewidth=10,label='crust block')
plt.plot([],[],'-',color='#e5b397',linewidth=10,label='fault block')
plt.plot([],[],'-',color='red',label='fault trace')

legend = plt.legend(frameon=False,ncol=4)
plt.gca().set_axis_off()

#fig.savefig("legend.png")

plt.savefig("model_legend.png", dpi=200)



os.system('convert model.png -trim model.png')
os.system('convert model_mesh.png -trim model_mesh.png')
os.system('convert model_legend.png -trim model_legend.png')
os.system('convert -border 70 -bordercolor white model_legend.png model_legend.png')



# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:31:45 2023

@author: ry22aas
"""
"""
robs_get_colour.py:
    Routine to return a particular shade of the inputted colour.
"""

#Local packages:
import sys
sys.path.append('/vol/ph/astro_data2/rmyates/python/python_libraries/Robs_Routines/')
from robs_truncate_colormap import *
from robs_get_colour_map import robs_get_colour_map

def robs_get_colour(colour, shade=0.5, colTrunc=[0.2,0.8]):
    if type(colour) == str :
        new_cmap = robs_get_colour_map(colour, colTrunc=[colTrunc[0],colTrunc[1]])
    
        if (colour == 'black') : 
            avecol = new_cmap(1.0)
        else : 
            avecol = new_cmap(shade) #To match average colour from robs_plot_average.py, use new_cmap(0.5)
    elif type(colour) == list :
        avecol = []
        for i in range(len(colour)) :
            new_cmap = robs_get_colour_map(colour[i], colTrunc=[colTrunc[0],colTrunc[1]])
        
            if (colour[i] == 'black') : 
                avecol_ind = new_cmap(1.0)
            else : 
                avecol_ind = new_cmap(shade) #To match average colour from robs_plot_average.py, use new_cmap(0.5)
            avecol.append(avecol_ind)
    else :
        print("***** WARNING: robs_get_colour.py: Type of attribute 'colour' is not a string or a list. *****")
    
    return avecol
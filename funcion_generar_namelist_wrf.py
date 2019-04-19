#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:19:39 2018
Creador de namelist.wps
@author: edwin
"""

def namelist_input_2(n_dom=3, longi=[1100000, (88*3666.667), (76*1222.222)], resol=11000):
    d = {}    
    for en , uu in enumerate(range(0,n_dom)):
        print(en, uu)
        d[uu] = longi[en]
        e_we_1 = (d[0]//(resol))+1 # Se le adicionó 1 para que se amplíe 
    if (n_dom >1):
        e_we_2 = (d[1]//(resol/3))
        while (e_we_2 % 3 )!= 0:
            e_we_2 += 1
        e_we_2 += 1
        i_parent_2 = ((d[0]-(e_we_2 * (resol/3))) /2)//(resol)
    else:
        e_we_2 = 'vacio'
        i_parent_2 = 'vacio'
        
    if (n_dom >2):
        e_we_3 = (d[2]//(resol/9))
        while (e_we_3 % 3) != 0:
            e_we_3 += 1
        e_we_3 += 1
        i_parent_3 = (((e_we_2 * (resol/3))-(e_we_3 * (resol/9))) /2)//(resol/3)
    else:
        e_we_3 = 'vacio'
        i_parent_3 = 'vacio'
            
    
    return('e_we_1', e_we_1,'e_we_2',  e_we_2,'e_we_3',  e_we_3,'i_paren2',  i_parent_2,'i_paren3', i_parent_3)


namelist_input_2(n_dom=3, longi=[(99*10000), (148*(10000/3)), (190*(10000/9))], resol=10000) #Eje x
namelist_input_2(n_dom=3, longi=[(99*10000), (148*(10000/3)), (190*(10000/9))], resol=10000) #Eje x


###Antigüos
namelist_input_2(n_dom=2, longi=[835124, 444870, 129308], resol=12000) #Eje x
namelist_input_2(n_dom=2, longi=[832750, 465011, 122190], resol=12000) #Eje y


namelist_input_2(n_dom=2, longi=[835124, 444870, 129308], resol=15000) #Eje x
namelist_input_2(n_dom=2, longi=[832750, 465011, 122190], resol=15000) #Eje y

namelist_input_2(n_dom=2, longi=[835124, 444870, 129308], resol=18000) #Eje x
namelist_input_2(n_dom=2, longi=[832750, 465011, 122190], resol=18000) #Eje y



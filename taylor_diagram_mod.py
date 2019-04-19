#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 08:56:51 2018

@author: edwin
"""
##############################################
##############################################
########### FUNCIóN###########################



"""
Taylor diagram (Taylor, 2001) implementation.
"""

__version__ = "Time-stamp: <2017-11-24 18:01:03 ycopin>"
__author__ = "Yannick Copin <yannick.copin@laposte.net>"

import numpy as NP
import matplotlib.pyplot as PLT
from matplotlib import pylab
from matplotlib.font_manager import FontProperties
from matplotlib.pyplot import figure


class TaylorDiagram(object):
    """
    Taylor diagram.

    Plot model standard deviation and correlation to reference (data)
    sample in a single-quadrant polar plot, with r=stddev and
    theta=arccos(correlation).
    """

    def __init__(self, refstd, fig=None, rect=111, label='_', srange=(0, 1.5)):
        """
        Set up Taylor diagram axes, i.e. single quadrant polar
        plot, using `mpl_toolkits.axisartist.floating_axes`.

        Parameters:

        * refstd: reference standard deviation to be compared to
        * fig: input Figure or None
        * rect: subplot definition
        * label: reference label
        * srange: stddev axis extension, in units of *refstd*
        """

        from matplotlib.projections import PolarAxes
        import mpl_toolkits.axisartist.floating_axes as FA
        import mpl_toolkits.axisartist.grid_finder as GF

        self.refstd = refstd            # Reference standard deviation

        tr = PolarAxes.PolarTransform()

        # Correlation labels
        rlocs = NP.concatenate((NP.arange(10)/10., [0.95, 0.99]))
        tlocs = NP.arccos(rlocs)        # Conversion to polar angles
        gl1 = GF.FixedLocator(tlocs)    # Positions
        tf1 = GF.DictFormatter(dict(zip(tlocs, map(str, rlocs))))

        # Standard deviation axis extent (in units of reference stddev)
        self.smin = srange[0]*self.refstd
        #self.smax = srange[1]*self.refstd
        self.smax = srange[1] * 1.1
        

        ghelper = FA.GridHelperCurveLinear(tr,
                                           extremes=(0, NP.pi/2,  # 1st quadrant
                                                     self.smin, self.smax),
                                           grid_locator1=gl1,
                                           tick_formatter1=tf1)

        if fig is None:
            fig = PLT.figure()

        ax = FA.FloatingSubplot(fig, rect, grid_helper=ghelper)
        fig.add_subplot(ax)

        # Adjust axes
        ax.axis["top"].set_axis_direction("bottom")  # "Angle axis"
        ax.axis["top"].toggle(ticklabels=True, label=True)
        ax.axis["top"].major_ticklabels.set_axis_direction("top")
        ax.axis["top"].label.set_axis_direction("top")
        ax.axis["top"].label.set_text("Correlación")

        ax.axis["left"].set_axis_direction("bottom")  # "X axis"
        ax.axis["left"].label.set_text("Desviación estándar")

        ax.axis["right"].set_axis_direction("top")   # "Y axis"
        ax.axis["right"].toggle(ticklabels=True)
        ax.axis["right"].major_ticklabels.set_axis_direction("left")

        ax.axis["bottom"].set_visible(False)         # Useless

        self._ax = ax                   # Graphical axes
        self.ax = ax.get_aux_axes(tr)   # Polar coordinates

        # Add reference point and stddev contour
        l, = self.ax.plot([0], self.refstd, 'k*',
                          ls='', ms=10, label=label)
        t = NP.linspace(0, NP.pi/2)
        r = NP.zeros_like(t) + self.refstd
        self.ax.plot(t, r, 'k--', label='_')

        # Collect sample points for latter use (e.g. legend)
        self.samplePoints = [l]

    def add_sample(self, stddev, corrcoef, *args, **kwargs):
        """
        Add sample (*stddev*, *corrcoeff*) to the Taylor
        diagram. *args* and *kwargs* are directly propagated to the
        `Figure.plot` command.
        """
        

        l, = self.ax.plot(NP.arccos(corrcoef), stddev,
                          *args, **kwargs)  # (theta,radius)
        self.samplePoints.append(l)

        return l

    def add_grid(self, *args, **kwargs):
        """Add a grid."""

        self.ax.grid(*args, **kwargs)

    def add_contours(self, levels=5, **kwargs):
        """
        Add constant centered RMS difference contours, defined by *levels*.
        """

        rs, ts = NP.meshgrid(NP.linspace(self.smin, self.smax),
                             NP.linspace(0, NP.pi/2))
        # Compute centered RMS difference
        rms = NP.sqrt(self.refstd**2 + rs**2 - 2*self.refstd*rs*NP.cos(ts))

        contours = self.ax.contour(ts, rs, rms, levels, **kwargs)

        return contours

    
####################
import pandas as pd
import numpy as np


tabla_1 = pd.DataFrame({'std':np.random.randint(1.8,5, 10),
                        'r2':np.random.rand(10),
                        'names':['a','b','c','d','e',
                                 'a','b','c','d','e']})
    

tabla_1 = pd.DataFrame({'std':np.random.randint(1.8,5, 5),
                        'r2':np.random.rand(5),
                        'names':['a','b','c','d','e'
                                 ]})


    
tabla_1 = tabla_1[['std','r2','names']] # OJO primero debe ir la desviación estándar, luego el coeficiente de Pearson y al final los nombres




stdref = 48.491

def diagrama_taylor(tabla_1, stdref, nombre_1, rango=(0, 1.5)):
    """
    Climatology-oriented example (after iteration w/ Michael A. Rawlins).
    """
    if stdref*1.1 > rango[1]:
        rango = (rango[0], stdref*1.5)
        
    # Reference std# De la muestra solo es necesario la desviación estándar
    
    # Samples std,rho,name# Acá están los valores que van a ser usados para realizar el diagrama de taylor


    fig = PLT.figure()

    dia = TaylorDiagram(stdref, fig=fig, label='Referencia', srange = rango)
    dia.samplePoints[0].set_color('r')  # Mark reference point as a red star

    # Add models to Taylor diagram
    for i in tabla_1.index:
        print(tabla_1.iloc[i,0], tabla_1.iloc[i,1], tabla_1.iloc[i,2])
        dia.add_sample(tabla_1.iloc[i,0], tabla_1.iloc[i,1],
                       marker='$%d$' % (i+1), ms=10, ls='',
                       mfc='k', mec='k',
                       label=tabla_1.iloc[i,2])

    # Add RMS contours, and label them
    contours = dia.add_contours(levels=6, colors='0.5')  # 5 levels in grey
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.0f')

    # Add a figure legend and title
    pylab.legend(dia.samplePoints,
               [ p.get_label() for p in dia.samplePoints ],
               numpoints=1, prop=dict(size='small'), loc='upper right', bbox_to_anchor=(1.5, 1.1)) # bbox_to_anchor es útil para mover fuera de la imágen el label
    #pylab.legend(loc=9, bbox_to_anchor=(1,1.1))
    fig.suptitle(nombre_1, size='x-large')  # Figure title
    

    return fig


#diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        


"""
Script creado para probar que el proceso está bien, realizado para la profe
"""
import pandas as pd
import numpy as np
import os

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series')
base = pd.read_csv('21195160.csv')
base.tmp_2m.std()

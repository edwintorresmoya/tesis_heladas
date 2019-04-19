import pandas as pd
import pdb

pdb.set_trace()

base_tmp = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/resumen_dias_con_heladas_20190129.csv')
base_tmp['var_1'] = 'tmp_2m'
base_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/resumen_todas_var_con_heladas_20190129.csv')
resumen = base_1.groupby('var_1').mean()

base_resumen = pd.concat([base_tmp, base_1])

base_resumen.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/sumatoria_datos_heladas.csv')

recoleccion_minim_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/simulacion_200702.csv')                                    
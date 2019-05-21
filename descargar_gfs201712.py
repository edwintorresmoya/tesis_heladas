#author: edwin
## Script de descarga de los datos del 2016 feb 19 20160219
import urllib.request
import datetime
from datetime import timedelta
import pdb

#ftp://nomads.ncdc.noaa.gov/GFS/analysis_only/200612/20061201/gfsanl_3_20061201_0000_000.grb


start_date = datetime.datetime(2017, 12,18)
end_date = datetime.datetime(2017, 12, 21)
#pdb.set_trace()
for a in range(0, int((end_date - start_date) / timedelta(seconds = 21600)) + 1):
        b = start_date + (timedelta(seconds = 21600) * a)
        url = ('ftp://nomads.ncdc.noaa.gov/GFS/analysis_only/'+
           b.strftime("%Y%m")+'/'+b.strftime("%Y%m%d")+
           '/gfsanl_3_'+b.strftime("%Y%m%d")+'_'+b.strftime("%H")+'00_000.grb2')
        try:
            print(url)
            urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
            print('Paila')
            continue


        print(url)
        print('______________________________________________________________________________________________________________________________________')
        urllib.request.urlretrieve(url, '/media/edwin/disco2/gfs/201712/'+b.strftime("%Y%m%d%H")+'.grb2')

#import os
#os.system('python3.6 ~/Downloads/mail.py')

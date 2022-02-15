# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:11:40 2021

@author: Tanveer
"""

from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt
import os


os.chdir("C:/Users/Tanveer/Desktop/NO2")

# Import the netCDF data
ncd_file = Dataset('posCovidChina.nc', 'r')

# Saving the data to lat, long, and no2_data variables 
lat = ncd_file.groups['PRODUCT'].variables['latitude'][0, :, :]
lon = ncd_file.groups['PRODUCT'].variables['longitude'][0, :, :]
no2_data = ncd_file.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'][0, :, :]

# Extracting the fill value 
fill_value = ncd_file.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column']._FillValue
fill_val = fill_value*1000000

# Replacing the fill values/ missing values by 'nan'
no2_em = np.array(no2_data)*1000000
no2_em[no2_em == fill_val] = np.nan
no2_data = no2_em

# Creating the basemap

m = Basemap(projection = 'cyl', resolution = 'i', 
            llcrnrlat = -90, 
            urcrnrlat = 90,
            llcrnrlon = -180,
            urcrnrlon = 180)  

m.drawcoastlines(linewidth = 1)
m.drawcountries(linewidth = 1)


cmap = plt.cm.get_cmap('jet')
cmap.set_under('w')

m.pcolormesh(lon, lat, no2_data, latlon = True, vmin =0 , vmax = 500, cmap = cmap)
color_bar = m.colorbar()
color_bar.set_label('μ.mol / Sq.meter')
plt.autoscale()

axes = plt.gca()
axes.set_xlim([80, 135])
axes.set_ylim([15, 50])

plt.title('Nitrogen Dioxide Emissions over China on 16 March, 2020')

fig = plt.gcf()
fig.savefig('NO2_20200316.jpg')

plt.show()
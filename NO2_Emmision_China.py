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


os.chdir("F:/SEM 8/FYP 2/NO2")

# Import the netCDF data
ncd_file = Dataset('PreCovidMalaysia_01122019.nc', 'r')

# Saving the data to lat, long, and no2_data variables 
lat = ncd_file.groups['PRODUCT'].variables['latitude'][0, :, :]
lon = ncd_file.groups['PRODUCT'].variables['longitude'][0, :, :]
no2_data = ncd_file.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'][0, :, :]

# Extracting the fill value 
fill_value = ncd_file.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column']._FillValue
fill_val = fill_value*1000000

# Replacing the fill values/ missing values by 'nan'
no2_em = np.array(no2_data)*1000000



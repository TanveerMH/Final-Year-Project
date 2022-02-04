# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:09:28 2021

@author: Tanveer
"""

from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import BaseMap
import matplotlib.pyplot as plt

ncd_file = Dataset('preCovid.nc', 'r')



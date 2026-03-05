# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:30:35 2026

@author: mmebe
"""


import numpy as np
from uncertainties import ufloat
from fit_background import *
from uncertainties import unumpy
from HS1_code import skalierung_lon_left_sun, skalierung_lon_rigth_sun


# lon background left

lon_b_left_scal = unumpy.uarray(lon_b_left, sigma_y_b) * skalierung_lon_left_sun

lblpopt, lblpcov = curve_fit(f, np.asarray(lon_az_b), unumpy.nominal_values(lon_b_left_scal), initial, unumpy.std_devs(lon_b_left_scal))
lblmodel_plot = f(lonleftb_model,lblpopt[0],lblpopt[1])

plt.errorbar(lon_az_b,  unumpy.nominal_values(lon_b_left_scal), unumpy.std_devs(lon_b_left_scal), marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(lonleftb_model, lblmodel_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lon left background scal')
plt.xlabel('Azimuth')
plt.ylabel('Temperature')
plt.show()

# lon background right

lon_b_right_scal = unumpy.uarray(lon_b_right, sigma_y_b) * skalierung_lon_rigth_sun

lbrpopt, lbrpcov = curve_fit(f, np.asarray(lon_az_b), unumpy.nominal_values(lon_b_right_scal), initial, unumpy.std_devs(lon_b_right_scal))
lbrmodel_plot = f(lonrightb_model,lbrpopt[0],lbrpopt[1])

plt.errorbar(lon_az_b,  unumpy.nominal_values(lon_b_right_scal), unumpy.std_devs(lon_b_right_scal), marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(lonrightb_model, lbrmodel_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lon right background scal')
plt.xlabel('Azimuth')
plt.ylabel('Temperature')
plt.show()


# lat background left

lat_b_left_scal = unumpy.uarray(lat_b_left, sigma_y_b) * skalierung_lon_left_sun

latblpopt, latblpcov = curve_fit(f, np.asarray(lon_az_b), unumpy.nominal_values(lat_b_left_scal), initial, unumpy.std_devs(lat_b_left_scal))
latblmodel_plot = f(latleftb_model,latblpopt[0],latblpopt[1])

plt.errorbar(lat_az_b,  unumpy.nominal_values(lat_b_left_scal), unumpy.std_devs(lat_b_left_scal), marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(latleftb_model, latblmodel_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lat left background scal')
plt.xlabel('Elevation')
plt.ylabel('Temperature')
plt.show()


# lat background right

lat_b_right_scal = unumpy.uarray(lat_b_right, sigma_y_b) * skalierung_lon_rigth_sun

latbrpopt, latbrpcov = curve_fit(f, np.asarray(lat_az_b), unumpy.nominal_values(lat_b_right_scal), initial, unumpy.std_devs(lat_b_right_scal))
latbrmodel_plot = f(latrightb_model,latbrpopt[0],latbrpopt[1])

plt.errorbar(lat_az_b,  unumpy.nominal_values(lat_b_right_scal), unumpy.std_devs(lat_b_right_scal), marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(latrightb_model, latbrmodel_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lat right background scal')
plt.xlabel('ELevation')
plt.ylabel('Temperature')
plt.show()


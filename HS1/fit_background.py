import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

lon_az_b=[]
lon_b_left=[]
lon_b_right=[]
sigma_y_b = []
filename = "20260302-122659_TPI-CSCAN_LON-3C147_02#_01#_t1.txt"

with open(filename) as inf:
    for line in inf:
        if not line.startswith('#'):
            parts= line.split()
            lon_az_b.append(float(parts[0]))
            lon_b_left.append(float(parts[1]))
            lon_b_right.append(float(parts[2]))
            sigma_y_b.append(float(142))


def f(x, a, b):
    return a*x + b

# fehler berechnen

error = np.std(lon_b_left)

# Initial guess.
initial    = np.array([1., 1.])

# lon left background

lonleftbpopt, lonleftbpcov = curve_fit(f, np.asarray(lon_az_b), np.asarray(lon_b_left), initial, np.asarray(sigma_y_b))

print('=====Best-fitting results======================================')
print('a =', lonleftbpopt[0], '+/-', lonleftbpcov[0,0]**0.5, 'cm')
print('b =', lonleftbpopt[1], '+/-', lonleftbpcov[1,1]**0.5, 'cm')
lonleftbmodel = f(np.asarray(lon_az_b),lonleftbpopt[0],lonleftbpopt[1])
lonleftbr = np.asarray(lon_b_left) - lonleftbmodel
lonleftbchisq = np.sum((lonleftbr/np.asarray(sigma_y_b))**2)
lonleftbdf = len(lon_b_left) - 2.0
print('Reduced chisq lonleftb = ',lonleftbchisq/lonleftbdf)
print('Degrees of freedom lonleftb = ', lonleftbdf)
print('===============================================================')

lonleftb_model = np.arange(np.amin(lon_az_b),np.amax(lon_az_b), (np.amax(lon_az_b)-np.amin(lon_az_b)) / 100.)
lonleftb_model_plot = f(lonleftb_model,lonleftbpopt[0],lonleftbpopt[1])

plt.errorbar(lon_az_b, lon_b_left, sigma_y_b, marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(lonleftb_model, lonleftb_model_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lon left background')
plt.xlabel('Azimuth')
plt.ylabel('Temperature')
plt.show()


# lon right background

# lon left background

lonrightbpopt, lonrightbpcov = curve_fit(f, np.asarray(lon_az_b), np.asarray(lon_b_right), initial, np.asarray(sigma_y_b))

print('=====Best-fitting results======================================')
print('a =', lonrightbpopt[0], '+/-', lonrightbpcov[0,0]**0.5, 'cm')
print('b =', lonrightbpopt[1], '+/-', lonrightbpcov[1,1]**0.5, 'cm')
lonrightbmodel = f(np.asarray(lon_az_b),lonrightbpopt[0],lonrightbpopt[1])
lonrightbr = np.asarray(lon_b_right) - lonrightbmodel
lonrightbchisq = np.sum((lonrightbr/np.asarray(sigma_y_b))**2)
lonrightbdf = len(lon_b_right) - 2.0
print('Reduced chisq lonrightb = ',lonrightbchisq/lonrightbdf)
print('Degrees of freedom lonrightb = ', lonrightbdf)
print('===============================================================')

lonrightb_model = np.arange(np.amin(lon_az_b),np.amax(lon_az_b), (np.amax(lon_az_b)-np.amin(lon_az_b)) / 100.)
lonrightb_model_plot = f(lonrightb_model,lonrightbpopt[0],lonrightbpopt[1])

plt.errorbar(lon_az_b, lon_b_right, sigma_y_b, marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(lonrightb_model, lonrightb_model_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lon right background')
plt.xlabel('Azimuth')
plt.ylabel('Temperature')
plt.show()



# lat left background

lat_az_b=[]
lat_b_left=[]
lat_b_right=[]
sigma_y_b = []
filename = "20260302-123126_TPI-CSCAN_LAT-3C147_02#_02#_t1.txt"

with open(filename) as inf:
    for line in inf:
        if not line.startswith('#'):
            parts= line.split()
            lat_az_b.append(float(parts[0]))
            lat_b_left.append(float(parts[1]))
            lat_b_right.append(float(parts[2]))
            sigma_y_b.append(float(142))


def f(x, a, b):
    return a*x + b

latleftbpopt, latleftbpcov = curve_fit(f, np.asarray(lat_az_b), np.asarray(lat_b_left), initial, np.asarray(sigma_y_b))

print('=====Best-fitting results======================================')
print('a =', latleftbpopt[0], '+/-', latleftbpcov[0,0]**0.5, 'cm')
print('b =', latleftbpopt[1], '+/-', latleftbpcov[1,1]**0.5, 'cm')
latleftbmodel = f(np.asarray(lat_az_b),latleftbpopt[0],latleftbpopt[1])
latleftbr = np.asarray(lat_b_left) - latleftbmodel
latleftbchisq = np.sum((latleftbr/np.asarray(sigma_y_b))**2)
latleftbdf = len(lat_b_left) - 2.0
print('Reduced chisq latleftb = ',latleftbchisq/latleftbdf)
print('Degrees of freedom latleftb = ', latleftbdf)
print('===============================================================')

latleftb_model = np.arange(np.amin(lat_az_b),np.amax(lat_az_b), (np.amax(lat_az_b)-np.amin(lat_az_b)) / 100.)
latleftb_model_plot = f(latleftb_model,latleftbpopt[0],latleftbpopt[1])

plt.errorbar(lat_az_b, lat_b_left, sigma_y_b, marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(latleftb_model, latleftb_model_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lat left background')
plt.xlabel('Elevation')
plt.ylabel('Temperature')
plt.show()


# lat right background



latrightbpopt, latrightbpcov = curve_fit(f, np.asarray(lat_az_b), np.asarray(lat_b_right), initial, np.asarray(sigma_y_b))

print('=====Best-fitting results======================================')
print('a =', latrightbpopt[0], '+/-', latrightbpcov[0,0]**0.5, 'cm')
print('b =', latrightbpopt[1], '+/-', latrightbpcov[1,1]**0.5, 'cm')
latrightbmodel = f(np.asarray(lat_az_b),latrightbpopt[0],latrightbpopt[1])
latrightbr = np.asarray(lat_b_right) - latrightbmodel
latrightbchisq = np.sum((latrightbr/np.asarray(sigma_y_b))**2)
latrightbdf = len(lat_b_right) - 2.0
print('Reduced chisq latrightb = ',latrightbchisq/latrightbdf)
print('Degrees of freedom latrightb = ', latrightbdf)
print('===============================================================')

latrightb_model = np.arange(np.amin(lat_az_b),np.amax(lat_az_b), (np.amax(lat_az_b)-np.amin(lat_az_b)) / 100.)
latrightb_model_plot = f(latrightb_model,latrightbpopt[0],latrightbpopt[1])

plt.errorbar(lat_az_b, lat_b_right, sigma_y_b, marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(latrightb_model, latrightb_model_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lat right background')
plt.xlabel('Elevation')
plt.ylabel('Temperature')
plt.show()
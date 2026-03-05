import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

lon_az_sun=[]
lon_sun_left=[]
lon_sun_right=[]
sigma_y = []
filename = "20260302-113046_TPI-CSCAN_LON-SUN.txt"

with open(filename) as inf:
    for line in inf:
        if not line.startswith('#'):
            parts= line.split()
            lon_az_sun.append(float(parts[0]))
            lon_sun_left.append(float(parts[1]))
            lon_sun_right.append(float(parts[2]))
            sigma_y.append(float(400))  #geratener error


def f(x, a, b, c, d):
    return a * np.exp(-(x-b)**2 / (2*c**2)) + d


# Initial guess.
initial    = np.array([1., 0., 1., 0.])


# lon left sun

lonleftsunpopt, lonleftsunpcov = curve_fit(f, np.asarray(lon_az_sun), np.asarray(lon_sun_left), initial, np.asarray(sigma_y))

print('=====Best-fitting results======================================')
print('a =', lonleftsunpopt[0], '+/-', lonleftsunpcov[0,0]**0.5, 'cm')
print('b =', lonleftsunpopt[1], '+/-', lonleftsunpcov[1,1]**0.5, 'cm')
print('c =', lonleftsunpopt[2], '+/-', lonleftsunpcov[2,2]**0.5, 'cm')
print('b =', lonleftsunpopt[3], '+/-', lonleftsunpcov[3,3]**0.5, 'cm')
print("cov",lonleftsunpcov)
lonleftsunmodel = f(np.asarray(lon_az_sun),lonleftsunpopt[0],lonleftsunpopt[1],lonleftsunpopt[2],lonleftsunpopt[3])
lonleftsunr = np.asarray(lon_sun_left) - lonleftsunmodel
lonleftsunchisq = np.sum((lonleftsunr/np.asarray(sigma_y))**2)
lonleftsundf = len(lon_sun_left) - 2.0
print('Reduced chisq lonleftsun = ',lonleftsunchisq/lonleftsundf)
print('Degrees of freedom lonleftsun= ', lonleftsundf)
print('===============================================================')

lonleftsun_model = np.arange(np.amin(lon_az_sun),np.amax(lon_az_sun), (np.amax(lon_az_sun)-np.amin(lon_az_sun)) / 100.)
lonleftsun_model_plot = f(lonleftsun_model,lonleftsunpopt[0],lonleftsunpopt[1],lonleftsunpopt[2],lonleftsunpopt[3])

plt.errorbar(lon_az_sun, lon_sun_left, sigma_y, marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(lonleftsun_model, lonleftsun_model_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lon sun left ')
plt.xlabel('Azimuth')
plt.ylabel('Temperature')
plt.show()


a_lon_left_sun = ufloat(lonleftsunpopt[0], lonleftsunpcov[0,0]**0.5)

# lon right sun

lonrightsunpopt, lonrightsunpcov = curve_fit(f, np.asarray(lon_az_sun), np.asarray(lon_sun_right), initial, np.asarray(sigma_y))

print('=====Best-fitting results======================================')
print('a =', lonrightsunpopt[0], '+/-', lonrightsunpcov[0,0]**0.5, 'cm')
print('b =', lonrightsunpopt[1], '+/-', lonrightsunpcov[1,1]**0.5, 'cm')
print('c =', lonrightsunpopt[2], '+/-', lonrightsunpcov[2,2]**0.5, 'cm')
print('b =', lonrightsunpopt[3], '+/-', lonrightsunpcov[3,3]**0.5, 'cm')
print("cov",lonrightsunpcov)
lonrightsunmodel = f(np.asarray(lon_az_sun),lonrightsunpopt[0],lonrightsunpopt[1],lonrightsunpopt[2],lonrightsunpopt[3])
lonrightsunr = np.asarray(lon_sun_right) - lonrightsunmodel
lonrightsunchisq = np.sum((lonrightsunr/np.asarray(sigma_y))**2)
lonrightsundf = len(lon_sun_right) - 2.0
print('Reduced chisq lonrightsun = ',lonrightsunchisq/lonrightsundf)
print('Degrees of freedom lonrightsun = ', lonrightsundf)
print('===============================================================')

lonrightsun_model = np.arange(np.amin(lon_az_sun),np.amax(lon_az_sun), (np.amax(lon_az_sun)-np.amin(lon_az_sun)) / 100.)
lonrightsun_model_plot = f(lonrightsun_model,lonrightsunpopt[0],lonrightsunpopt[1],lonrightsunpopt[2],lonrightsunpopt[3])

plt.errorbar(lon_az_sun, lon_sun_right, sigma_y, marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(lonrightsun_model, lonrightsun_model_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lon sun right ')
plt.xlabel('Azimuth')
plt.ylabel('Temperature')
plt.show()


a_lon_right_sun = ufloat(lonrightsunpopt[0], lonrightsunpcov[0,0]**0.5)




# latidude sun

lat_az_sun=[]
lat_sun_left=[]
lat_sun_right=[]
sigma_y = []
filename = "20260302-113503_TPI-CSCAN_LAT-SUN_01#_02#_t1.txt"

with open(filename) as inf:
    for line in inf:
        if not line.startswith('#'):
            parts= line.split()
            lat_az_sun.append(float(parts[0]))
            lat_sun_left.append(float(parts[1]))
            lat_sun_right.append(float(parts[2]))
            sigma_y.append(float(400))  #geratener error


def f(x, a, b, c, d):
    return a * np.exp(-(x-b)**2 / (2*c**2)) + d


# Initial guess.
initial    = np.array([1., 0., 1., 0.])


# lat left sun

latleftsunpopt, latleftsunpcov = curve_fit(f, np.asarray(lat_az_sun), np.asarray(lat_sun_left), initial, np.asarray(sigma_y))

print('=====Best-fitting results======================================')
print('a =', latleftsunpopt[0], '+/-', latleftsunpcov[0,0]**0.5, 'cm')
print('b =', latleftsunpopt[1], '+/-', latleftsunpcov[1,1]**0.5, 'cm')
print('c =', latleftsunpopt[2], '+/-', latleftsunpcov[2,2]**0.5, 'cm')
print('b =', latleftsunpopt[3], '+/-', latleftsunpcov[3,3]**0.5, 'cm')
print("cov",latleftsunpcov)
latleftsunmodel = f(np.asarray(lat_az_sun),latleftsunpopt[0],latleftsunpopt[1],latleftsunpopt[2],latleftsunpopt[3])
latleftsunr = np.asarray(lat_sun_left) - latleftsunmodel
latleftsunchisq = np.sum((latleftsunr/np.asarray(sigma_y))**2)
latleftsundf = len(lat_sun_left) - 2.0
print('Reduced chisq latleftsun = ',latleftsunchisq/latleftsundf)
print('Degrees of freedom latleftsun = ', latleftsundf)
print('===============================================================')

latleftsun_model = np.arange(np.amin(lat_az_sun),np.amax(lat_az_sun), (np.amax(lat_az_sun)-np.amin(lat_az_sun)) / 100.)
latleftsun_model_plot = f(latleftsun_model,latleftsunpopt[0],latleftsunpopt[1],latleftsunpopt[2],latleftsunpopt[3])

plt.errorbar(lat_az_sun, lat_sun_left, sigma_y, marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(latleftsun_model, latleftsun_model_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lat sun left ')
plt.xlabel('Elevation')
plt.ylabel('Temperature')
plt.show()


a_lat_left_sun = ufloat(latleftsunpopt[0], latleftsunpcov[0,0]**0.5)




# lat right sun

#latrightsunpopt, latrightsunpcov = curve_fit(f, np.asarray(lat_az_sun), np.asarray(lat_sun_right), initial, np.asarray(sigma_y))

# ignoring first 2 values for fit
latrightsunpopt, latrightsunpcov = curve_fit(f, np.asarray(lat_az_sun)[2:], np.asarray(lat_sun_right)[2:], initial, np.asarray(sigma_y)[2:])

print('=====Best-fitting results======================================')
print('a =', latrightsunpopt[0], '+/-', latrightsunpcov[0,0]**0.5, 'cm')
print('b =', latrightsunpopt[1], '+/-', latrightsunpcov[1,1]**0.5, 'cm')
print('c =', latrightsunpopt[2], '+/-', latrightsunpcov[2,2]**0.5, 'cm')
print('b =', latrightsunpopt[3], '+/-', latrightsunpcov[3,3]**0.5, 'cm')
print("cov",latrightsunpcov)
#model = f(np.asarray(lat_az_sun),latrightsunpopt[0],latrightsunpopt[1],latrightsunpopt[2],latrightsunpopt[3])
#r = np.asarray(lat_sun_right) - model
#chisq = np.sum((r/np.asarray(sigma_y))**2)
#df = len(lat_sun_right) - 2.0

# ignoring first 2 values for fit
latrightsunmodel = f(np.asarray(lat_az_sun)[2:], latrightsunpopt[0], latrightsunpopt[1], latrightsunpopt[2], latrightsunpopt[3])
latrightsunr = np.asarray(lat_sun_right)[2:] - latrightsunmodel
latrightsunchisq = np.sum((latrightsunr/np.asarray(sigma_y)[2:])**2)
latrightsundf = len(lat_sun_right[2:]) - 4.0  
print('Reduced chisq latrightsun = ',latrightsunchisq/latrightsundf)
print('Degrees of freedom latrightsun = ', latrightsundf)
print('===============================================================')

latrightsun_model = np.arange(np.amin(lat_az_sun),np.amax(lat_az_sun), (np.amax(lat_az_sun)-np.amin(lat_az_sun)) / 100.)
latrightsun_model_plot = f(latrightsun_model,latrightsunpopt[0],latrightsunpopt[1],latrightsunpopt[2],latrightsunpopt[3])

plt.errorbar(lat_az_sun, lat_sun_right, sigma_y, marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(latrightsun_model, latrightsun_model_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lat sun right ')
plt.xlabel('Elevation')
plt.ylabel('Temperature')
plt.show()


a_lat_right_sun = ufloat(lonrightsunpopt[0], lonrightsunpcov[0,0]**0.5)
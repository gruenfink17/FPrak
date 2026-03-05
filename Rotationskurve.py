# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:16:44 2026

@author: mmebe
"""
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy
from scipy.optimize import curve_fit

# 5.4

longitude = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
max_rad_velocity = np.array([51, 126, 117, 95, 80, 55, 38, 32, 18])  # km/s
sigma_rad_velocity = np.array([4, 4.5, 7, 2, 3.5, 2.5, 9, 4.5, 2 ])
sigma_longitude = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2])


# dstance R with uncertainty 
distance_R = 8.5 * unumpy.sin(unumpy.uarray(longitude, sigma_longitude) / 180 * np.pi)  # kpc


w_0 = 220/8.5  # km/s /kpc 

orbital_velocity = unumpy.uarray(max_rad_velocity, sigma_rad_velocity) + w_0 * distance_R

orbital_vel_bar = 452 * unumpy.sqrt(1/distance_R * (1 - (distance_R / 2 + 1) * unumpy.exp(-distance_R / 2)))

plt.errorbar(
    unumpy.nominal_values(distance_R),
    unumpy.nominal_values(orbital_velocity),
    yerr=unumpy.std_devs(orbital_velocity),
    xerr=unumpy.std_devs(distance_R),       # optional, für Fehler in R
    fmt='o',
    color='r',
    markersize=5,
    capsize=2.5,
    label='measured'
)
plt.errorbar(
    unumpy.nominal_values(distance_R),
    unumpy.nominal_values(orbital_vel_bar),
       
    fmt='o',
    color='b',
    markersize=5,
    capsize=2.5,
    label='baryonic'
)
plt.title("Rotational curve milky way")
plt.xlabel("R (kpc)")
plt.ylabel("orbital velocity 8 km/s)")
plt.legend()
plt.show()


# enclosed mass of milky way  
# ALS FKT DER SONNENMASSE PLOTTEN

m_mw = 0.234e10 * (orbital_velocity)**2 * distance_R* 1.98e30

m_bar = 0.234e10 * (orbital_vel_bar)**2 * distance_R* 1.98e30

m_mw_sunmass = m_mw / 1.98e30
m_bar_sunmass = m_bar / 1.98e30

m_dm_sunmass = m_mw_sunmass - m_bar_sunmass

plt.errorbar(unumpy.nominal_values(distance_R) , unumpy.nominal_values(m_mw_sunmass), yerr= unumpy.std_devs(m_mw_sunmass), xerr=unumpy.std_devs(distance_R), marker='o', color='r', fmt='o', markersize = 5, capsize = 2.5, label='measured')
plt.errorbar(unumpy.nominal_values(distance_R) , unumpy.nominal_values(m_bar_sunmass), marker='.', color='b', fmt='o', markersize = 5, capsize = 2.5, label='baryionic')
plt.title("Enclosed mass milky way")
plt.xlabel("R (kpc)")
plt.ylabel("enclosed mass / sun mass")
plt.legend()
plt.show()





# Modellfunktion
def lin_func(x, m, b):
    return m*x + b

# Beispiel-Daten
x = unumpy.uarray(unumpy.nominal_values(distance_R), unumpy.std_devs(distance_R))
y = unumpy.uarray(unumpy.nominal_values(m_dm_sunmass), unumpy.std_devs(m_dm_sunmass))

# Fit
params, cov = curve_fit(lin_func, unumpy.nominal_values(x), unumpy.nominal_values(y), p0=[1e14,-1e14],sigma = unumpy.std_devs(m_dm_sunmass), absolute_sigma=True)
m, b = params
m_err, b_err = np.sqrt(np.diag(cov))

print("m =", m, "+/-", m_err)
print("b =", b, "+/-", b_err)

x_rand = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8,9])

#plt.errorbar(unumpy.nominal_values(distance_R),unumpy.nominal_values(m_dm_sunmass), yerr= unumpy.std_devs(m_dm_sunmass), marker='o', color='g', fmt='o', markersize = 5, capsize = 2.5, label='measured')
#plt.plot(x_rand,lin_func(x_rand,m,b))
#plt.title("dark matter mass")
#plt.xlabel("R (kpc)")
#plt.ylabel("mass / sun mass")
#plt.show()
plt.errorbar(
    unumpy.nominal_values(distance_R),         # x-Werte
    unumpy.nominal_values(m_dm_sunmass),      # y-Werte
    xerr=unumpy.std_devs(distance_R),         # Fehler in x
    yerr=unumpy.std_devs(m_dm_sunmass),       # Fehler in y
    marker='o',
    color='g',
    fmt='o',
    markersize=5,
    capsize=2.5,
    label='measured'
)
plt.plot(x_rand,lin_func(x_rand,m,b))
plt.title("dark matter mass")
plt.xlabel("R (kpc)")
plt.ylabel("mass / sun mass")
plt.show()
print(f"M(R_0) = {lin_func(8.5, m, b):.3e}")
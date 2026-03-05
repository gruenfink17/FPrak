# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:32:35 2026

@author: mmebe
"""

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

R_nom = unumpy.nominal_values(distance_R)

# generating 100 x values to plot the baryonic curve
R_smooth = np.linspace(np.min(R_nom), np.max(R_nom), 100)


w_0 = 220/8.5  # km/s /kpc 

orbital_velocity = unumpy.uarray(max_rad_velocity, sigma_rad_velocity) + w_0 * distance_R

orbital_vel_bar = 452 * unumpy.sqrt(1/distance_R * (1 - (distance_R / 2 + 1) * unumpy.exp(-distance_R / 2)))

orbital_vel_bar_smooth = 452 * np.sqrt(1/R_smooth * (1 - (R_smooth / 2 + 1) * np.exp(-R_smooth / 2)))

plt.errorbar(
    unumpy.nominal_values(distance_R),
    unumpy.nominal_values(orbital_velocity),
    yerr=unumpy.std_devs(orbital_velocity),
    xerr=unumpy.std_devs(distance_R),      
    fmt='o',
    color='r',
    markersize=5,
    capsize=2.5,
    label='measured'
)
plt.plot(
    R_smooth,
    orbital_vel_bar_smooth,
    color='b',
    linewidth=2,
    label='baryonic'
)
plt.title("Rotational curve milky way")
plt.xlabel("R (kpc)")
plt.ylabel("orbital velocity 8 km/s)")
plt.legend()
plt.show()


# enclosed mass of milky way  
# ALS FKT DER SONNENMASSE PLOTTEN

m_mw = 0.234e10 * (orbital_velocity / 100)**2 * distance_R* 1.98e30

m_bar = 0.234e10 * (orbital_vel_bar / 100)**2 * distance_R* 1.98e30

m_bar_smooth = 0.234e10 * (orbital_vel_bar_smooth / 100)**2 * R_smooth* 1.98e30

m_mw_sunmass = m_mw / 1.98e30
m_bar_sunmass = m_bar / 1.98e30
m_bar_sunmass_smooth = m_bar_smooth /  1.98e30

m_dm_sunmass = m_mw_sunmass - m_bar_sunmass

plt.errorbar(unumpy.nominal_values(distance_R) , unumpy.nominal_values(m_mw_sunmass), yerr= unumpy.std_devs(m_mw_sunmass), xerr=unumpy.std_devs(distance_R), marker='o', color='r', fmt='o', markersize = 5, capsize = 2.5, label='measured')
plt.plot(R_smooth , m_bar_sunmass_smooth, color='b', linewidth = 2, label='baryionic')
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

# data without first value to avoid negative mass values later 
x_fit = unumpy.nominal_values(x)[1:]
y_fit = unumpy.nominal_values(y)[1:]
y_err_fit = unumpy.std_devs(y)[1:]

# Fit
params, cov = curve_fit(
    lin_func,
    x_fit,
    y_fit,
    p0=[1e14,-1e14],
    sigma=y_err_fit,
    absolute_sigma=True
)
m, b = params
m_err, b_err = np.sqrt(np.diag(cov))

print("m =", m, "+/-", m_err)
print("b =", b, "+/-", b_err)

x_rand = np.linspace(1.5, 9, 200)


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


plt.errorbar(unumpy.nominal_values(distance_R) , unumpy.nominal_values(m_mw_sunmass), yerr= unumpy.std_devs(m_mw_sunmass), xerr=unumpy.std_devs(distance_R), marker='o', color='r', fmt='o', markersize = 5, capsize = 2.5, label='measured')
plt.plot(
    R_smooth,
    m_bar_sunmass_smooth,
    color='b',
    markersize=5,
    label='baryonic'
)
plt.errorbar(
    unumpy.nominal_values(distance_R),         
    unumpy.nominal_values(m_dm_sunmass),      
    xerr=unumpy.std_devs(distance_R),
    yerr=unumpy.std_devs(m_dm_sunmass),       
    marker='o',
    color='g',
    fmt='o',
    markersize=5,
    capsize=2.5,
    label='dark matter'
)
plt.plot(x_rand,lin_func(x_rand,m,b))
plt.title("Enclosed mass milky way")
plt.xlabel("R (kpc)")
plt.ylabel("enclosed mass / sun mass")
plt.legend()
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:04:58 2026

@author: mmebe
"""

import numpy as np
from uncertainties import ufloat
from fit_sonne import *
from uncertainties import unumpy
#from fit_background import f as f_bg
#from fit_background import lon_az_b, lon_b_left, lon_b_right, sigma_y_b, bx_model, lonleftbpcov, lonleftbpopt

# 5.1.1 Calibation 

T_cal = 170 #K

onTPI = np.array([21421.66, 26588.14, 24394.16, 20447.94, 15493.96, 20791.28, 27503.18, 25648.44, 19559.58, 12946.34])

offTPI = np.array([1498.28, 1865.08, 1733.34, 1537.46, 1299.92, 3495.68, 2649.10, 1652.62, 1241.02, 965.52])

calTPI = np.array([3345.70, 4447.34, 4037.48, 3410.48, 2642.64, 4978.04, 5319.28, 4444.60, 3207.46, 2104.94])

T_sys = T_cal * (offTPI/(calTPI - offTPI))

T_sys_left = T_sys[0:5]

T_sys_right = T_sys[5:10]

T_sys_mean_left = ufloat(np.mean(T_sys_left), np.std(T_sys_left, ddof = 1) / np.sqrt(len(T_sys_left)))

T_sys_mean_right = ufloat(np.mean(T_sys_right), np.std(T_sys_right, ddof = 1) / np.sqrt(len(T_sys_left)))

print("T_sys_left (mean) = ", T_sys_mean_left)
print("T_sys_right (mean) = ", T_sys_mean_right)

# T_sys mean of all values: 
    
T_sys_mean = ufloat(np.mean(T_sys), np.std(T_sys, ddof = 1) / np.sqrt(len(T_sys)))

print("T_sys mean = ", T_sys_mean)
    


T_sun = T_sys * (onTPI - offTPI) / offTPI


T_sun_mean = ufloat(np.mean(T_sun), np.std(T_sun, ddof = 1) / np.sqrt(len(T_sun)))

print("T_sun (mean) = ", T_sun_mean)

# T sun mean left and right separately 

T_sun_left = T_sun[0:5]

T_sun_right = T_sun[5:10]

T_sun_left_mean = ufloat(np.mean(T_sun_left), np.std(T_sun_left, ddof = 1) / np.sqrt(len(T_sun_left)))

T_sun_right_mean = ufloat(np.mean(T_sun_right), np.std(T_sun_right, ddof = 1) / np.sqrt(len(T_sun_right)))

# solar flux density
A_e = 3.534

S = 2 * 1.381e-23 * T_sun_mean / A_e

print("SFU_our_data =", S)



# from website: 
sfu_10_7 = 147e-22

sfu_21 = np.sqrt(10.7/21) * sfu_10_7

print("SFU_theo = ", sfu_21)



# Theoretical T sun
T_sun_theo = sfu_21 * A_e / (2 * 1.381e-23)

print("T_sun_theo", T_sun_theo)

 


# 5.2 

# long left sun

skalierung_lon_left_sun = T_sun_left_mean / a_lon_left_sun


print("Skalierung lon left sun = ", skalierung_lon_left_sun)

lon_sun_left_scal = unumpy.uarray(np.array(lon_sun_left) * skalierung_lon_left_sun.nominal_value, np.array(sigma_y) * skalierung_lon_left_sun.nominal_value) 


lslpopt, lslpcov = curve_fit(f, np.asarray(lon_az_sun), unumpy.nominal_values(lon_sun_left_scal), initial, unumpy.std_devs(lon_sun_left_scal))
lslmodel_plot = f(lonleftsun_model,lslpopt[0],lslpopt[1],lslpopt[2],lslpopt[3])
print("a = ",lslpopt[0],"+-",lslpcov[0,0])
lsl_c = ufloat(lslpopt[2],lslpcov[2,2])

plt.errorbar(lon_az_sun, unumpy.nominal_values(lon_sun_left_scal), unumpy.std_devs(lon_sun_left_scal), marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(lonleftsun_model, lslmodel_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lon sun left scal')
plt.xlabel('Azimuth')
plt.ylabel('Temperature')
plt.grid()
plt.show()


# FWHM

fwhm_meas_lsl = 2 * np.sqrt(2* np.log(2)) * lsl_c

print("FWHM lsl (measured) = ", fwhm_meas_lsl)

# correcting FWHM with elevation = 29

fwhm_corr_lsl = fwhm_meas_lsl * np.cos(29/180 * np.pi)


print("FWHM lsl (corrected with el=29) = ", fwhm_corr_lsl)



#lon right sun 

skalierung_lon_rigth_sun = T_sun_right_mean / a_lon_right_sun


print("Skalierung lon right sun= ", skalierung_lon_rigth_sun)

lon_sun_right_scal = unumpy.uarray(np.array(lon_sun_right) * skalierung_lon_rigth_sun.nominal_value, np.array(sigma_y)* skalierung_lon_rigth_sun.nominal_value) 


lsrpopt, lsrpcov = curve_fit(f, np.asarray(lon_az_sun), unumpy.nominal_values(lon_sun_right_scal), initial, unumpy.std_devs(lon_sun_right_scal))
lsrmodel_plot = f(lonrightsun_model,lsrpopt[0],lsrpopt[1],lsrpopt[2],lsrpopt[3])
print("a lsr= ",lsrpopt[0],"+-",lsrpcov[0,0])
lsr_c = ufloat(lsrpopt[2],lsrpcov[2,2])

plt.errorbar(lon_az_sun, unumpy.nominal_values(lon_sun_right_scal), unumpy.std_devs(lon_sun_right_scal), marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(lonrightsun_model, lsrmodel_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lon sun right scal')
plt.xlabel('Azimuth')
plt.ylabel('Temperature')
plt.grid()
plt.show()


# FWHM

fwhm_meas_lsr = 2 * np.sqrt(2* np.log(2)) * lsr_c

print("FWHM lsr (measured) = ", fwhm_meas_lsr)

# correcting FWHM with elevation = 29

fwhm_corr_lsr = fwhm_meas_lsr * abs(np.cos(29))

print("FWHM  lsr (corrected with el=29) = ", fwhm_corr_lsr)



# lat left sun

lat_sun_left_scal = unumpy.uarray(np.array(lat_sun_left)  * skalierung_lon_left_sun.nominal_value, np.array(sigma_y)  * skalierung_lon_left_sun.nominal_value) 


latslpopt, latslpcov = curve_fit(f, np.asarray(lat_az_sun), unumpy.nominal_values(lat_sun_left_scal), initial, unumpy.std_devs(lat_sun_left_scal))
latslmodel_plot = f(latleftsun_model,latslpopt[0],latslpopt[1],latslpopt[2],latslpopt[3])
print("a = ",latslpopt[0],"+-",latslpcov[0,0])
latsl_c = ufloat(latslpopt[2],latslpcov[2,2])

plt.errorbar(lat_az_sun, unumpy.nominal_values(lat_sun_left_scal), unumpy.std_devs(lat_sun_left_scal), marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(latleftsun_model, latslmodel_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lat sun left scal ')
plt.xlabel('Elevation')
plt.ylabel('Temperature')
plt.grid()
plt.show()


# FWHM

fwhm_meas_latsl = 2 * np.sqrt(2* np.log(2)) * latsl_c

print("FWHM latsl (measured) = ", fwhm_meas_latsl)

# correcting FWHM with elevation = 29

fwhm_corr_latsl = fwhm_meas_latsl * abs(np.cos(29))

print("FWHM latsl (corrected with el=29) = ", fwhm_corr_latsl)



#lat right sun 


lat_sun_right_scal = unumpy.uarray(np.array(lat_sun_right) * skalierung_lon_rigth_sun.nominal_value, np.array(sigma_y) * skalierung_lon_rigth_sun.nominal_value) 


latsrpopt, latsrpcov = curve_fit(f, np.asarray(lat_az_sun), unumpy.nominal_values(lat_sun_right_scal), initial, unumpy.std_devs(lat_sun_right_scal))
latsrmodel_plot = f(latrightsun_model,latsrpopt[0],latsrpopt[1],latsrpopt[2],latsrpopt[3])
print("a latsr= ",latsrpopt[0],"+-",latsrpcov[0,0])
latsr_c = ufloat(latsrpopt[2],latsrpcov[2,2])

plt.errorbar(lat_az_sun, unumpy.nominal_values(lat_sun_right_scal), unumpy.std_devs(lat_sun_right_scal), marker='_', color='r', fmt='o', markersize = 5, capsize = 2.5, label='Messwerte')
plt.plot(latrightsun_model, latsrmodel_plot, label='Fit')
plt.legend(loc='lower right')
plt.title('lat sun right scal ')
plt.xlabel('Elevation')
plt.ylabel('Temperature')
plt.grid()
plt.show()


# FWHM

fwhm_meas_latsr = 2 * np.sqrt(2* np.log(2)) * latsr_c

print("FWHM latsr (measured) = ", fwhm_meas_latsr)

# correcting FWHM with elevation = 29

fwhm_corr_latsr = fwhm_meas_latsr * abs(np.cos(29))

print("FWHM  latsr (corrected with el=29) = ", fwhm_corr_latsr)






# 5.3.1 

d_nu = 61e3 # Hz
C_s = 2
tau = 1

sensitivity_lim = 2 * 1.381e-23 * C_s * T_sys_mean / (A_e * np.sqrt(d_nu * tau))

print("limited sensitivity (61kHz) = ", sensitivity_lim)


# Cyg A, finding tau

S_cyga = ufloat(1.42e-23, 7e-25)  # Watts per sqaure meter per Hertz

tau_cyga = 1 / d_nu * ((20 * 1.381e-23 * T_sys_mean) / (S_cyga * A_e))**2  

print("Tau CYGA = ", tau_cyga)  

# 5.3.2

# map noise in units of Kelvin

mean_map = 1832.3 
sigma_map = 55.4377

map_noise = sigma_map / mean_map * T_sys_mean


print("map noise (K) = ", map_noise)



# 5.4

longitude = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
max_rad_velocity = np.array([51, 126, 117, 95, 80, 55, 38, 32, 18 ])

# 10: 51 pm 4
# 40: 95 pm 2
# bsk 10:10, 40:0 





    



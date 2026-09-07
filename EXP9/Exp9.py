# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:02:13 2026

@author: mmebe
"""

# z_Dipol = 123 pm1cm
# z_Schirm = 176,5 pm1cm

import numpy as np
import matplotlib.pyplot as plt

# Energiemessung 

I_E = np.array([-0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
y_E = np.array([-17.15270, -16.10596, -14.00309, -12.92428, -11.09183, -9.692310, -8.314764, -6.449249, -5.235687, -3.914095, -2.249105])

plt.scatter(I_E, y_E)
plt.title("Dipolstrom vs y-Position")
plt.xlabel("I in A")
plt.ylabel("y-Positioin in mm")
plt.grid(True)
plt.show()


p1 = 15.0286*10**(-3) # m/A
k = 7.64*10**(-6) # Tm/A
L = (176.5-123) *10**(-2) #m
e = 1.602*10**(-19) # C
m_e = 9.109 * 10**(-31) #kg
c = 2.99 * 10**8 #m/s

beta_gamma = e*k*L / (m_e *c*p1) # Js^2/(kgm^2)
print("beta_gamma=", beta_gamma)

gamma = np.sqrt(1+(beta_gamma)**2)
print("gamma = ", gamma)

E_0 = m_e * c**2
E_kin = E_0 * (gamma - 1)
print("E_kin = ", E_kin / e *10**(-3), "keV" )

# -> elektronen bewegen sich mit ~ 15% der Lichtgeschwindigkeit 
# -> eigentlich klassische Rechnung, aber wir machen trotzdem relativistisch 
# E_kin = mittlere Strahlenergie; Energie unseres Referenzteilchens, Bezugssystem für die Transfermatrix kommt von diesem Referenzteilchen

# Emittanz



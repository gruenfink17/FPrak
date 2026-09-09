# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:57:43 2026

@author: mmebe
"""

import numpy as np
import matplotlib.pyplot as plt

z_schirm = np.array([176, 232.5, 288.5, 344.5])
x_RMS = np.array([2.872729, 4.045438, 3.033364, 2.569578])
y_RMS = np.array([2.473640, 3.788590, 3.564704, 1.235016])
RMSerr = 0.2/np.sqrt(15) #Fehler auf Strahlbreiten in mm

farben = ['red', 'blue', 'green', 'orange']

fig, ax = plt.subplots()

for i in range(4):
    ax.errorbar(x_RMS[i], y_RMS[i], xerr=RMSerr, yerr=RMSerr, capsize=5, color=farben[i], label=f"Schirm {i+3}")

ax.set_xlabel(r"$\sigma_\mathrm{x}$ [mm]")
ax.set_ylabel(r"$\sigma_\mathrm{y}$ [mm]")
ax.grid(True)
ax.set_title("Strahlbreiten an Schirmen 3-6")
ax.legend()

plt.show()

# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:57:43 2026

@author: mmebe
"""

import numpy as np
import matplotlib.pyplot as plt

# Fehler?? 


z_schirm = np.array([176, 232.5, 288.5, 344.5])
x_RMS = np.array([2.872729, 4.045438, 3.033364, 2.569578])
y_RMS = np.array([2.473640, 3.788590, 3.564704, 1.235016])

farben = ['red', 'blue', 'green', 'orange']

fig, ax = plt.subplots()

for i in range(4):
    ax.scatter(x_RMS[i], y_RMS[i], color=farben[i], label=f"Schirm {i+3}")

ax.set_xlabel(r"$x_\mathrm{RMS}$ [mm]")
ax.set_ylabel(r"$y_\mathrm{RMS}$ [mm]")
ax.grid(True)
ax.set_title("Strahlbreiten an Schirmen 3-6")
ax.legend()

plt.show()

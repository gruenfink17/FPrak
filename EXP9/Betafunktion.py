# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:57:43 2026

@author: mmebe
"""

import numpy as np
import matplotlib.pyplot as plt
from Quadrupolscan import emit_h, emit_v

z_schirm = np.array([176, 232.5, 288.5, 344.5]) *10**(-2) # m
x_RMS = np.array([2.872729, 4.045438, 3.033364, 2.569578]) *10**(-3)  # m
y_RMS = np.array([2.473640, 3.788590, 3.564704, 1.235016]) *10**(-3) # m

beta_x = x_RMS **2 / emit_h.nominal_value
beta_y = y_RMS**2 / emit_v.nominal_value

z_qp = np.array([208.5]) *10**(-2) # m
beta_x_qp = np.array([1.36]) # m
beta_y_qp = np.array([0.99]) # m

RMSerr = 0.2 / np.sqrt(15)  # Fehler auf Strahlbreiten in mm

farben = ['red', 'blue', 'green', 'orange']


fig, ax = plt.subplots()

for i in range(4):
    ax.errorbar(z_schirm[i], beta_x[i], fmt='o', capsize=5, color=farben[i], label=f"Schirm {i+3}")
ax.errorbar(z_qp, beta_x_qp, fmt='o', capsize=5, color= 'purple', label='Quadrupol')
ax.set_xlabel(r"$z$ [m]")
ax.set_ylabel(r"$\beta_\mathrm{x}$ [m]")
ax.set_title(r"$\beta_\mathrm{x}$ als Funktion von $z$")
ax.grid(True)
ax.legend()

plt.show()


fig, ax = plt.subplots()

for i in range(4):
    ax.errorbar(z_schirm[i], beta_y[i], fmt='o', capsize=5, color=farben[i], label=f"Schirm {i+3}")
ax.errorbar(z_qp, beta_y_qp, fmt='o', capsize=5, color= 'purple', label='Quadrupol')
ax.set_xlabel(r"$z$ [m]")
ax.set_ylabel(r"$\beta_\mathrm{y}$ [m]")
ax.set_title(r"$\beta_\mathrm{y}$ als Funktion von $z$")
ax.grid(True)
ax.legend()

plt.show()

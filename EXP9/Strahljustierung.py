import numpy as np
from uncertainties import unumpy as unp

from functions import *

# todo: Legende verschieben (überdeckt teilweise den Plot)

# Strahlbasierte Justage
#linearer fit
def linreg(x, a, b):
    return a * x + b

#Fehler auf Position
yerr = 0.2/np.sqrt(15) #mm

# Fehler Strom
Ierr = 0.003

# horizontal
# I_qp = -2.8A
I_Dp1h = np.array([-2.9, -2.7, -2.5, -2.3, -2.1, -1.9, -1.8, -1.7, -1.5, -1.3, -1.1, -0.9])
x_1h = np.array([1.512200, 1.004406, 0.442551, 0.086023, -0.691112, -1.317591, -1.645250, -1.984885, -2.643876, -3.29885, -3.962618, -4.677156])


a1h,b1h = optimal_params(linreg,I_Dp1h,x_1h,yerr) #a in mm/A, b in mm
print("a1h", a1h, "b1h", b1h)

# I_qp = -1.8A
I_Dp2h = np.array([-2.3, -2.2, -2.1, -2.0 , -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7])
x_2h = np.array([-0.656189, -1.261055, -1.913192, -2.387855, -2.972455, -3.552116, -4.096201, -4.647038, -5.23464, -5.814752, -6.409733, -6.944705, -7.503301, -8.051078, -8.594271, -9.159939, -9.760734])

a2h,b2h = optimal_params(linreg,I_Dp2h,x_2h,yerr) #a in mm/A, b in mm
print("a2h", a2h, "b2h", b2h)

x_lin = np.linspace(-3, 0, 50)

plt.errorbar(I_Dp1h, x_1h, xerr=Ierr, yerr=yerr, fmt='.', capsize=5, label=f"I_QP=-2.8A", color='tab:blue')
plt.errorbar(I_Dp2h, x_2h, xerr=Ierr, yerr=yerr, fmt='.', capsize=5,label=f"I_QP=-1.8A", color='tab:orange')
plt.plot(x_lin, linreg(x_lin, a1h.n, b1h.n), color='tab:blue', label=f"Fit: y=({a1h})mm/A $\cdot$ I+({b1h})mm ")
plt.plot(x_lin, linreg(x_lin, a2h.n, b2h.n), color='tab:orange', label=f"Fit: y=({a2h})mm/A $\cdot$ I+({b2h})mm")
plt.title("Dipolstrom vs x-Position")
plt.xlabel("$I_D$ in A")
plt.ylabel("x-Position in mm")
plt.grid(True)
plt.legend()
plt.show()

# vertikal
# I_qp = 1.4A

I_Dp1v = np.array([-0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8])
y_1v = np.array([-5.491102, -4.053651, -2.430504, -0.935522, 0.620073, 2.188491, 3.807588, 5.304055, 6.977924, 8.610670, 10.188083, 11.609190])

a1v,b1v = optimal_params(linreg,I_Dp1v,y_1v,yerr) #a in mm/A, b in mm
print("a1v", a1v, "b1v", b1v)

# I_qp = 2.4A

I_Dp2v = np.array([-0.3, -0.1, 0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1])
y_2v = np.array([0.851899, 1.791788, 2.739709, 3.676269, 4.556785, 5.511437, 6.446761, 7.337466, 8.263653, 9.092880, 9.987592, 10.852653, 11.503083])

a2v,b2v = optimal_params(linreg,I_Dp2v,y_2v,yerr) #a in mm/A, b in mm
print("a2v", a2v, "b2v", b2v)

x_lin = np.linspace(-1, 2.5)
plt.errorbar(I_Dp1v, y_1v,  xerr=Ierr, yerr=yerr, fmt='.', capsize=5,label=f"I_QP=1.4A", color='tab:blue')
plt.errorbar(I_Dp2v, y_2v, xerr=Ierr, yerr=yerr, fmt='.', capsize=5, label=f"I_QP=2.4A", color='tab:orange')
plt.plot(x_lin, linreg(x_lin, a1v.n, b1v.n), color='tab:blue', label=f"Fit: y=({a1v})mm/A $\cdot$ I+({b1v})mm" )
plt.plot(x_lin, linreg(x_lin, a2v.n, b2v.n), color='tab:orange', label=f"Fit: y=({a2v})mm/A $\cdot$ I+({b2v})mm")
plt.title("Dipolstrom vs y-Position")
plt.xlabel("$I_D$ in A")
plt.ylabel("y-Position in mm")
plt.grid(True)
plt.legend()
plt.show()


# testen: Quadrupolstrom ändern bei Dipolstrom der Schnittstelle

# horizontal (sieht linear aus, aber different ist 2pixel und wir messen auf 1pixel genau, also passt schon)
I_Qph = np.array([-1.8, -1.9, -2.0, -2.1, -2.2, -2.3, -2.4, -2.5, -2.6, -2.7, -2.8])
x_3h = np.array([0.689216, 0.6775189, 0.636440, 0.593137, 0.527598, 0.500795, 0.433892, 0.323571, 0.259655, 0.177970, 0.089828 ])

plt.errorbar(I_Qph, x_3h, xerr=Ierr, yerr=yerr, fmt='.', capsize=5)
plt.title("Quadrupolstrom vs x-Position")
plt.xlabel("Quadrupolstrom in A")
plt.ylabel("x-Position in mm")
plt.grid(True)
plt.show()

# vertikal (Ungenauigkeiten zB dadurch dass wir die Schraube getroffen haben)
I_Qpv = np.array([1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4])
y_3v = np.array([8.880867, 8.864568, 8.861105, 8.834509, 8.842101, 8.855623, 8.825236, 8.828870, 8.869526, 8.894355, 8.888450])

plt.errorbar(I_Qpv, y_3v, xerr=Ierr, yerr=yerr, fmt='.', capsize=5)
plt.title("Quadrupolstrom vs y-Position")
plt.xlabel("Quadrupolstrom in A")
plt.ylabel("y-Position in mm")
plt.grid(True)
plt.show()






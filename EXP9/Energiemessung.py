import matplotlib.pyplot as plt

from functions import *

#gemessene Positionen des Dipols und des Schirms
z_Dipol = uc.ufloat(123e-2, 1e-2) #m
z_Schirm = uc.ufloat(176.5e-2, 1e-2) #m


# Energiemessung
I_E = np.array([-0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]) #Dipolstrom in A
y_E = np.array([-17.15270, -16.10596, -14.00309, -12.92428, -11.09183, -9.692310, -8.314764, -6.449249, -5.235687, -3.914095, -2.249105]) #y-Position in mm
Ierr = 0.003 #A
yerr = 0.2/np.sqrt(15) #mm

#linearer fit
def linreg(x, a, b):
    return a * x + b
a,b = optimal_params(linreg,I_E,y_E,yerr) #a in mm/A, b in mm
print("a=", a, "mm/A")
print("b=", b, "mm")
ypred = linreg(I_E,a.n,b.n)
r2 = skm.r2_score(y_E, ypred)
r = np.corrcoef(I_E, y_E)[0,1]
print("r=", r)
print("r2=", r2)


#plotten
plt.scatter(I_E, y_E)
#plt.errorbar(I_E, y_E, xerr=Ierr, yerr=yerr,  marker="none", linestyle="none", capsize=2)
x = np.linspace(-0.4,0.8,50)
plt.plot(x, linreg(x, a.n, b.n), label="Lineare Regression")
a_str = str(a).replace("+/-", r"\pm")
b_str = str(b).replace("+/-", r"\pm")
plt.plot([],[],linestyle="none", label = (rf"$y = ({a_str})\,\text{{mm/A}}\cdot I_D +  ({b_str})\,\text{{mm}}$" "\n" 
        rf"$r = {r:.3f}, \quad R^2 = {r2:.3f}$"))
plt.legend()
plt.title("y-Position vs. Dipolstrom")
plt.xlabel(r"$I_D$ in A")
plt.ylabel("y-Position in mm")
plt.xlim(-0.4,0.8)
plt.ylim(-17.5,0)
plt.grid(True)
#plt.show()


#p1 = 15.0286*10**(-3) # m/A
k = 7.64*10**(-6) # Tm/A
L = z_Schirm-z_Dipol #m
e = 1.602*10**(-19) # C
m_e = 9.109 * 10**(-31) #kg
c = 2.99 * 10**8 #m/s


beta_gamma = e*k*L / (m_e*c*a*1e-3) #hat in fact keine einheit, beta und gamma sind beide einheitenlos
print("beta_gamma=", beta_gamma)

gamma = unp.sqrt(1+(beta_gamma)**2)
print("gamma = ", gamma)

beta = beta_gamma/gamma
print("beta = ", beta)

E_0 = m_e * c**2
E_kin = E_0 * (gamma - 1)
print("E_kin = ", E_kin / e *10**(-3), "keV" )

#Impuls berechnen
p = E_0*unp.sqrt(gamma**2-1)/e *10**(-3)
print("relativistischer Impuls p = ", p, "keV/c")

plt.show()

# -> elektronen bewegen sich mit ~ 15% der Lichtgeschwindigkeit 
# -> eigentlich klassische Rechnung, aber wir machen trotzdem relativistisch 
# E_kin = mittlere Strahlenergie; Energie unseres Referenzteilchens, Bezugssystem für die Transfermatrix kommt von diesem Referenzteilchen



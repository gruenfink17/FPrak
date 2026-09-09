from functions import *
from Energiemessung import beta_gamma
RMSerr = 0.2/np.sqrt(15) #Fehler auf Strahlbreiten in mm

#Messergebnisse einlesen
horizontal = np.loadtxt("Quadrupolscan_horizontal.txt", unpack=True)
I_h = horizontal[0] #Quadrupolstrom in A
xRMS = horizontal[1] #horizontale Strahlbreite in mm
xRMS = unp.uarray(xRMS, RMSerr) #als uarray mit Fehler

vertikal = np.loadtxt("Quadrupolscan_vertikal.txt", unpack=True)
I_v = vertikal[0] #Quadrupolstrom in A
yRMS = vertikal[1] #vertikale Strahlbreite in mm
yRMS = unp.uarray(yRMS, RMSerr) #als uarray mit Fehler

#graphische Darstellung

#horizontal
fig, ax = plt.subplots()
ax.errorbar(I_h, unp.nominal_values(xRMS), yerr=RMSerr, marker="o", linestyle="none", capsize=5)
ax.set_xlim(-2.9, -1.7)
ax.set_ylim(0.4, 1.5)
ax.set_title("Horizontaler Quadrupolscan")
ax.grid(True)
ax.set_xlabel(r"$I_Q$ [A]")
ax.set_ylabel(r"$\sigma_x$ [mm]")

#vertikal
fig, ax = plt.subplots()
ax.errorbar(I_v, unp.nominal_values(yRMS), yerr=RMSerr, marker="o", linestyle="none", capsize=5)
ax.set_xlim(1.3, 2.5)
ax.set_ylim(0.2, 0.8)
ax.set_title("Vertikaler Quadrupolscan")
ax.grid(True)
ax.set_xlabel(r"$I_Q$ [A]")
ax.set_ylabel(r"$\sigma_y$ [mm]")


#Mit dem Skript berechnete Emittanz und Fehler und T-Vektoren (siehe Gl. 62):
T_h = 1.0e-03 * np.array([0.0142, 0.0398, 0.1188])
T_v = 1.0e-05 * np.array([0.2834, 0.3159, 0.6386])

print("T_x:", T_h)
print("T_y:", T_v)


emit_h =   1.0468e-05 #m
rel_error_h = 4.5251 #%
emit_h_err = rel_error_h/100 * emit_h #absoluter Fehler
emit_h = uc.ufloat(emit_h, emit_h_err)

emit_v =    2.8487e-06 #m
rel_error_v = 6.7828 #%
emit_v_err = rel_error_v/100 * emit_v
emit_v = uc.ufloat(emit_v, emit_v_err)

#Twiss-Parameter (Nach Gl. 51 bzw. Gl. 64 in der Versuchsmappe)

beta_h = T_h[0]/emit_h #m
alpha_h = -T_h[1]/emit_h
gamma_h = T_h[2]/emit_h #1/m

print("horizontal:")
print("Emittanz", emit_h, "m")
print("alpha", alpha_h)
print("beta", beta_h, "m")
print("gamma", gamma_h, "1/m")


beta_v = T_v[0]/emit_v #m
alpha_v = -T_v[1]/emit_v
gamma_v = T_v[2]/emit_v #1/m

print("vertikal:")
print("Emittanz", emit_v, "m")
print("alpha", alpha_v)
print("beta", beta_v, " m")
print("gamma", gamma_v, " 1/m")

#normierte Emittanz berechnen
emit_n_h = emit_h * beta_gamma
emit_n_v = emit_v * beta_gamma

print("normierte Emittanz x:", emit_n_h, "m")
print("normierte Emittanz y:", emit_n_v, "m")

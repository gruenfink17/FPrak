from functions import *
Ierr = 0.003 #Fehler auf Strom in A #ToDo: nehmen oder weglassen?
RMSerr = 0.2/np.sqrt(15) #Fehler auf Strahlbreiten in mm

#Messergebnisse einlesen
horizontal = np.loadtxt("Quadrupolscan_horizontal.txt", unpack=True)
I_h = horizontal[0] #Quadrupolstrom in A
xRMS = horizontal[1] #horizontale Strahlbreite in mm
xRMS = unp.uarray(xRMS, RMSerr) #als uarray mit Fehler

vertikal = np.loadtxt("Quadrupolscan_vertikal.txt")
I_v = vertikal[0] #Quadrupolstrom in A
yRMS = horizontal[1] #vertikale Strahlbreite in mm
yRMS = unp.uarray(yRMS, RMSerr) #als uarray mit Fehler

#graphische Darstellung
#ToDo

#Mit dem Skript berechnete Emittanz und Fehler und T-Vektoren (siehe Gl. 62):
T_h = 1.0e-03 * np.array([0.0142, 0.0398, 0.1188])
T_v = 1.0e-05 * np.array([0.2834, 0.3159, 0.6386])

emit_h =   1.0468e-05
rel_error_h = 4.5251 #%
emit_h_err = rel_error_h/100 * emit_h #absoluter Fehler
emit_h = uc.ufloat(emit_h, emit_h_err)

emit_v =    2.8487e-06
rel_error_v = 6.7828 #%
emit_v_err = rel_error_v/100 * emit_v
emit_v = uc.ufloat(emit_v, emit_v_err)

#Twiss-Parameter (Nach Gl. 64 in der Versuchsmappe)
#ToDo: darf ich das damit rechnen oder muss ich Gl. 51 nehmen?
#ToDo: Einheiten!

beta_h = T_h[0]/emit_h
alpha_h = -T_h[1]/emit_h
gamma_h = T_h[2]/emit_h

print("horizontal:")
print("Emittanz", emit_h)
print("alpha", alpha_h)
print("beta", beta_h)
print("gamma", gamma_h)


beta_v = T_v[0]/emit_v
alpha_v = -T_v[1]/emit_v
gamma_v = T_v[2]/emit_v

print("vertikal:")
print("Emittanz", emit_v)
print("alpha", alpha_v)
print("beta", beta_v)
print("gamma", gamma_v)

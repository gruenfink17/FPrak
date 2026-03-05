import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat 

### measurement data

# voltage
V = np.array([1000, 900, 800, 700, 675, 650, 625, 600, 575, 550, 525, 500, 475, 450, 400, 300])

# fails channel 2 and 4 
f_2 = np.array([7, 5, 13, 8, 12, 38, 165, 664, 1287, 1952, 2265, 2412, 2465, 2486, 2489, 2492])
uf_2 = unp.uarray(f_2,np.sqrt(f_2))

f_4 = np.array([212, 210, 266, 217, 246, 267, 312, 493, 914, 1555, 2003, 2347, 2437, 2473, 2484, 2492])
uf_4 = unp.uarray(f_4,np.sqrt(f_4))

triggers = ([2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500])

# successes channel 2 and 4
suc_2 = triggers - uf_2

suc_4 = triggers - uf_4

# efficiencies channel 2 and 4 
eff_2 = suc_2 / triggers

eff_4 = suc_4 / triggers



### Monte Carlo Simulations

# length and width of detectors:
xmax = 40
xerr = 0.1
xmax_e = 40 + xerr  # with error, to calculate absolute error in the end
xerr = 0.1
ymax = 100
yerr = 0.1
ymax_e = 100 + yerr #cm
yerr = 0.1

# thickness of plates:
h = 1.3
herr = 0.1 #cm
h_e = 1.3 + herr#cm

# distance between detector plates:
d3 = 2.5
derr = 0.1 #cm
d3_e = 2.5 + derr #cm (distance between 3 and 4)
d2 = 2.2
d2_e = 2.2 + derr#cm
d1 = 2.3
d1_e = 2.3 + derr#cm

# number of muons to generate:
Nmu = 10**6

# generate Nmu random x and y coordinates on the first detector plate:
x1 = np.random.uniform(0,xmax,Nmu) #m
y1 = np.random.uniform(0,ymax,Nmu) #m

# generate Nmu random phi coordinates on the first detector plate:
phi = np.random.uniform(0,2*np.pi,Nmu) #rad

# generate theta coordinates
unif = np.random.uniform(0,1,Nmu)
theta = np.arccos(np.cbrt(unif))

# coordinates on 2nd, 3rd, 4th plate:
x2 = x1+np.tan(theta)*np.cos(phi)*(h+d1)
y2 = y1+np.tan(theta)*np.sin(phi)*(h+d1)

x3 = x1+np.tan(theta)*np.cos(phi)*(2*h+d1+d2)
y3 = y1+np.tan(theta)*np.sin(phi)*(2*h+d1+d2)

x4 = x1+np.tan(theta)*np.cos(phi)*(3*h+d1+d2+d3)
y4 = y1+np.tan(theta)*np.sin(phi)*(3*h+d1+d2+d3)

# with error: 
x2_e = x1+np.tan(theta)*np.cos(phi)*(h_e+d1_e)
y2_e = y1+np.tan(theta)*np.sin(phi)*(h_e+d1_e)

x3_e = x1+np.tan(theta)*np.cos(phi)*(2*h_e+d1_e+d2_e)
y3_e = y1+np.tan(theta)*np.sin(phi)*(2*h_e+d1_e+d2_e)

x4_e = x1+np.tan(theta)*np.cos(phi)*(3*h_e+d1_e+d2_e+d3_e)
y4_e = y1+np.tan(theta)*np.sin(phi)*(3*h_e+d1_e+d2_e+d3_e)


# does muon hit plate 3?
def trigger (x3,y3):
    hitcounter = []
    for i, n in zip(x3, y3):
        if i <= xmax and n <= ymax:
            hitcounter.append(True)
        else:
            hitcounter.append(False)
    return hitcounter

def trigger_e (x3,y3):
    hitcounter = []
    for i, n in zip(x3, y3):
        if i <= xmax_e and n <= ymax_e:
            hitcounter.append(True)
        else:
            hitcounter.append(False)
    return hitcounter

maske = np.array (trigger(x3,y3))
maske_e = np.array (trigger_e(x3_e,y3_e))

# muons that hit plate 3:
x2_hit = x2[maske]
y2_hit = y2[maske]
x4_hit = x4[maske]
y4_hit = y4[maske]

x2_hit_e = x2_e[maske_e]
y2_hit_e = y2_e[maske_e]
x4_hit_e = x4_e[maske_e]
y4_hit_e = y4_e[maske_e]
        


# does muon hit the plate?
def hit (x,y):
    hitcounter= 0
    for i, n in zip(x,y):
        if i<= xmax and n<= ymax:
            hitcounter+= 1
        else:
            pass
    return hitcounter

def hit_e (x,y):
    hitcounter= 0
    for i, n in zip(x,y):
        if i<= xmax_e and n<= ymax_e:
            hitcounter+= 1
        else:
            pass
    return hitcounter

# printing number of hits on plate 2 and 4 
print("len plate 2 hit = ", len(x2_hit))
print("len plat e4 hit = ", len(x4_hit))

# geometric efficiency
effgeom_2 = hit(x2_hit, y2_hit)/len(x2_hit)

effgeom_4 = hit(x4_hit, y4_hit)/len(x4_hit)


print("geometric efficiency_2 = ", effgeom_2)
print("geometric cefficiency_4 = ", effgeom_4)


print("hits plate two e = ", len(x2_hit_e))
print("hits plate 4 e = ", len(x4_hit_e))

# geometric efficiency with error 
effgeom_2_e = hit_e(x2_hit_e, y2_hit_e)/len(x2_hit_e)

effgeom_4_e = hit_e(x4_hit_e, y4_hit_e)/len(x4_hit_e)


print("geometric efficiency_2 e = ", effgeom_2_e)
print("geometric efficiency_4 e= ", effgeom_4_e)

# absolute error of geometric efficiency plate 4
print("correction factor plate 4 = ", effgeom_4 - effgeom_4_e)

# detector efficiency 
effdec_2 = eff_2 / ufloat(effgeom_2, effgeom_2 - effgeom_2_e) 

effdec_4 = eff_4 / ufloat(effgeom_4, effgeom_4 - effgeom_4_e)

# plotting results 
plt.errorbar(V, unp.nominal_values(eff_2), yerr=unp.std_devs(eff_2), fmt='.', label="measured efficiency")
plt.errorbar(V, unp.nominal_values(effdec_2), yerr=unp.std_devs(effdec_2), fmt='.', label="detector efficiency")
plt.title("Efficiency Channel 2")
plt.xlabel("Voltage (V)")
plt.ylabel("Efficiency")
plt.legend(loc = 'lower right')
plt.grid()
plt.show()

plt.errorbar(V, unp.nominal_values(eff_4), yerr=unp.std_devs(eff_4), fmt='.', label="measured efficiency")
plt.errorbar(V, unp.nominal_values(effdec_4), yerr=unp.std_devs(effdec_4), fmt='.', label="detector efficiency")
plt.title("Efficiency Channel 4")
plt.xlabel("Voltage (V)")
plt.ylabel("Efficiency")
plt.grid()
plt.legend(loc = 'lower right')
plt.show()
efficiency_4_e)

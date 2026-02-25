import numpy as np



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
efficiency_2 = hit(x2_hit, y2_hit)/len(x2_hit)

efficiency_4 = hit(x4_hit, y4_hit)/len(x4_hit)


print("efficiency_2 = ", efficiency_2)
print("efficiency_4 = ", efficiency_4)


print("len plate 2 hit e = ", len(x2_hit_e))
print("len plate 4 hit e = ", len(x4_hit_e))

# efficiency with error 
efficiency_2_e = hit_e(x2_hit_e, y2_hit_e)/len(x2_hit_e)

efficiency_4_e = hit_e(x4_hit_e, y4_hit_e)/len(x4_hit_e)


print("efficiency_2 e = ", efficiency_2_e)
print("efficiency_4 e= ", efficiency_4_e)

# absolute error of geometric efficiency 
print("absolute error", efficiency_4 - efficiency_4_e)

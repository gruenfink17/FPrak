import numpy as np

from functions import *


###Monte Carlo Simulations
#length and width of detectors:
xmax = 40 #cm
xerr = 0.1
uxmax=uc.ufloat(xmax,xerr)
ymax = 100 #cm
yerr= 0.1
uymax=uc.ufloat(ymax,yerr)
#thickness of plates:


h = 1.3 #cm
herr = 0.1 #cm
uh = uc.ufloat(h,herr)

#distance between detector plates:


d3= 2.5 #cm (distance between 3 and 4)
d2= 2.2 #cm
d1=2.3 #cm
derr = 0.1 #cm
ud1 = uc.ufloat(d1,derr)
ud2 = uc.ufloat(d2,derr)
ud3 = uc.ufloat(d3,derr)


#Todo: errors

#number of muons to generate:
Nmu= 10
# generate Nmu random x and y coordinates on the first detector plate:
x1 = np.random.uniform(0,xmax,Nmu) #m
y1 = np.random.uniform(0,ymax,Nmu) #m

#generate Nmu random phi coordinates on the first detector plate:
phi = np.random.uniform(0,2*np.pi,Nmu) #rad


unif = np.random.uniform(0,1,Nmu)
theta = np.arccos(np.cbrt(unif))



#coordinates on 2nd, 3rd, 4th plate:
x2 = x1+np.tan(theta)*np.cos(phi)*(uh+ud1)
y2 = y1+np.tan(theta)*np.sin(phi)*(uh+ud1)

x3 = x1+np.tan(theta)*np.cos(phi)*(2*uh+ud1+ud2)
y3 = y1+np.tan(theta)*np.sin(phi)*(2*uh+ud1+ud2)

x4 = x1+np.tan(theta)*np.cos(phi)*(3*uh+ud1+ud2+ud3)
y4 = y1+np.tan(theta)*np.sin(phi)*(3*uh+ud1+ud2+ud3)

# does muon hit plate 3?
def trigger (x3,y3):
    hitcounter = []
    for i, n in zip(x3, y3):
        if i <= uxmax and n <= uymax:
            hitcounter.append(True)
        else:
            hitcounter.append(False)
    return hitcounter

maske= np.array (trigger(x3,y3))
# muons that hit plate 3:
x2_hit=x2[maske]
y2_hit=y2[maske]
x4_hit=x4[maske]
y4_hit=y4[maske]

print(x2)
print(x2_hit)


print(uxmax)

#does muon hit the plate?
def hit (x,y):
    hitcounter= 0
    for i, n in zip(x,y):
        if i<= uxmax and n<= uymax:
            hitcounter+= 1
        else:
            pass
    return hitcounter


efficiency2 = hit(x2_hit,y2_hit)/len(x2_hit)
efficiency4 = hit(x4_hit,y4_hit)/len(x2_hit)


print(efficiency2,efficiency4)




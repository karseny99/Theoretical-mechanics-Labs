import matplotlib.pyplot as p
from matplotlib.animation import FuncAnimation
import numpy as n
from scipy.integrate import odeint


def SystDiffEq(y, t, m1, R, m2, a, g, l, c):
    # y = [phi, psi, phi', psi'] -> dy = [phi', psi', phi'', psi'']
    dy = n.zeros_like(y)
    dy[0] = y[2]
    dy[1] = y[3]

    # a11 * phi'' + a12 * psi'' = b1
    # a21 * phi'' + a22 * psi'' = b2

    a11 = (m1 * R**2 + 2 * m2 * a**2)
    a12 = 2 * m2 * a * l * n.cos(y[0] + y[1]) 

    b1 = 2 * m2 * g * a * n.sin(y[0]) - 2 * c * (y[0] + y[1]) + 2 * m2 * a * l * y[3]**2 * n.sin(y[0] + y[1])

    a21 = m2 * l * a * n.cos(y[0] + y[1])
    a22 = m2 * l**2
    b2  = y[2]**2 * n.sin(y[0] + y[1]) * m2 * l * a - m2 * g * l * n.sin(y[1]) - c*(y[0] + y[1])

    dy[2] = (b1 * a22 - b2 * a12)/ (a11 * a22 - a12 * a21)
    dy[3] = (a11 * b2 - a21 * b1)/ (a11 * a22 - a12 * a21)
    
    return dy


T = n.linspace(0, 10, 200)

# Габаритные характеристики берутся из задания #12

m1 = 1
m2 = 1 
a = 0.5 
g = 9.81
R = 1 
l = 1
c = 1

y0 = [n.pi / 6, 0, 0, 0]

Y = odeint(SystDiffEq, y0, T, (m1, R, m2, a, g, l, c))

Phi = Y[:,0]
Ksi = Y[:,1]
Phit = Y[:,2]
Psit = Y[:,3]

# tmp = Phi
# Phi = Ksi
# Ksi = tmp


fgrp = p.figure()
plPhi = fgrp.add_subplot(4,1,1)
plPhi.plot(T, Phi)

plPsi = fgrp.add_subplot(4,1,2)
plPsi.plot(T, Ksi)


Phitt = n.zeros_like(T)
Psitt = n.zeros_like(T)
for i in range(len(T)):
    Phitt[i] = SystDiffEq(Y[i], T[i], m1, R, m2, a, g, l, c)[2]
    Psitt[i] = SystDiffEq(Y[i], T[i], m1, R, m2, a, g, l, c)[3]

Nox = (m1 + m2) * g - m2 * (a * (Phitt * n.sin(Phi) + Phit**2 * n.cos(Phi)) - l * (Psitt * n.sin(Ksi) + (Psit)**2 * n.cos(Ksi)))

plN = fgrp.add_subplot(4,1,3)
plN.plot(T, Nox)


fgrp.show()


#======= анимация системы =========
r = R
fgr = p.figure()
plt = fgr.add_subplot(1, 1, 1)
plt.axis("equal")

# Шаблон диска
Alp = n.linspace(0, 2 * n.pi, 100)
Xc = r * n.cos(Alp)
Yc = r * n.sin(Alp)
Disk = plt.plot(Xc, Yc)[0]



Xa = l * 0.3 * n.cos(Phi[0]  )
Ya = l * 0.3 * n.sin(Phi[0]  )    # Координаты точки A

Yb = l * n.sin(Ksi[0]) * 0.4 + Ya 
Xb = l * n.cos(Ksi[0]) * 0.4 + Xa
AB = plt.plot([Xa, Xb], [Ya, Yb])[0]

# Шарик, закрепленный на палке

Xcircle = r * n.cos(Alp) * 0.04 + Xb
Ycircle = r * n.sin(Alp) * 0.04 + Yb
Circle = plt.plot(Xcircle, Ycircle)[0]

# Шаблон спиральной пружины
Ns = 4
r1 = 0
r2 = l * 0.1


numpoints = n.linspace(0, 1, 50 * Ns + 1)
Betas = numpoints * (2 * n.pi * Ns + Ksi[0])
Xs = n.cos(Betas) * (r1 + (r2 - r1) * numpoints)
Ys = n.sin(Betas) * (r1 + (r2 - r1) * numpoints)

SpPruzh = plt.plot(Xs + Xa, Ys + Ya)[0]

# Disk.set_data(Xc + Xb, Yc + Yb) # Изменение положения диска
def run(i):
    # Xb = l * n.sin(Psi[i])

    Xa = l * 0.3 * n.cos(Phi[i] )
    Ya = l * 0.3 * n.sin(Phi[i] )    # Координаты точки A


    Yb = l * n.sin(Ksi[i] ) * 0.4 + Ya 
    Xb = l * n.cos(Ksi[i] ) * 0.4 + Xa

    AB.set_data([Xa, Xb], [Ya, Yb]) # Изменение положения палки

    Betas = numpoints * (2 * n.pi * Ns + Ksi[i])
    Xs = n.cos(Betas) * (r1 + (r2 - r1) * numpoints) 
    Ys = n.sin(Betas) * (r1 + (r2 - r1) * numpoints) # Изменение положения пружины
    SpPruzh.set_data(Xs + Xa, Ys + Ya)

    
    Xcircle = r * n.cos(Alp) * 0.04 + Xb
    Ycircle = r * n.sin(Alp) * 0.04 + Yb
    Circle.set_data(Xcircle, Ycircle)




anim = FuncAnimation(fgr, run, frames = len(T), interval = 1)

fgr.show()
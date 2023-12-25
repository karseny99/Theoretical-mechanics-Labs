import matplotlib.pyplot as p
from matplotlib.animation import FuncAnimation
import numpy as n

T = n.linspace(0, 10, 100)

# Взять phi(t) из предыдущей лабы
Psi = n.linspace(0, 2 * n.pi,  100) # первоначальное отклонение от вертикальной оси
Ksi = n.linspace(0, - n.pi,  50)
Ksi1 = n.linspace(-n.pi, 0, 50)
Ksi = n.append(Ksi, Ksi1)
fgr = p.figure()
plt = fgr.add_subplot(1, 1, 1)
plt.axis('equal')

# Габаритные характеристики берутся из задания #12

l = 1
r = l
a = 3

h = 0.5
b = 2

# plt.plot([0, 0], [0, 3])
# plt.plot([0, a, a, 0], [h, h, h + b, h + b])


# Шаблон диска
Alp = n.linspace(0, 2 * n.pi, 100)
Xc = r * n.cos(Alp)
Yc = r * n.sin(Alp)
Disk = plt.plot(Xc, Yc)[0]



Xa = l * 0.3 * n.cos(Psi[0]  )
Ya = l * 0.3 * n.sin(Psi[0]  )    # Координаты точки A

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

    Xa = l * 0.3 * n.cos(Psi[i] )
    Ya = l * 0.3 * n.sin(Psi[i] )    # Координаты точки A


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
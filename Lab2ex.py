import matplotlib.pyplot as p
from matplotlib.animation import FuncAnimation
import numpy as n

T = n.linspace(0, 10, 100)
# Взять phi(t) из предыдущей лабы
Psi = n.sin(0.5 * T) + 1.1 # 1.1 - первоначальное отклонение от вертикальной оси

fgr = p.figure()
plt = fgr.add_subplot(1, 1, 1)
plt.axis('equal')

# Габаритные характеристики берутся из задания #12

l = 1
r = 0.1
a = 3

h = 0.5
b = 2

plt.plot([0, 0], [0, 3])
plt.plot([0, a, a, 0], [h, h, h + b, h + b])


# Шаблон диска
Alp = n.linspace(0, 2 * n.pi, 10)
Xc = r * n.cos(Alp)
Yc = r * n.sin(Alp)

Xb = l * n.sin(Psi[0])  # Координаты точки B
Yb = h + r

Disk = plt.plot(Xc + Xb, Yc + Yb)[0]

Xa = 0 
Ya = h + r + l * n.cos(Psi[0])  # Координаты точки A

AB = plt.plot([Xa, Xb], [Ya, Yb])[0]

# Шаблон пружины
# /\  /\  /\
#   \/  \/  \/

Np = 30  # количество сегментов
Xp = n.linspace(0, 1, 2 * Np + 1)
Yp = 0.05 * n.sin(n.pi / 2 * n.arange(2 * Np + 1))

Pruzh = plt.plot(Xb + (a - Xb) * Xp, Yp + Yb)[0]

# Шаблон спиральной пружины
Ns = 3
r1 = 0.06
r2 = 0.1

numpoints = n.linspace(0, 1, 50 * Ns + 1)
Betas = numpoints * (2 * n.pi * Ns - Psi[0])
Xs = n.sin(Betas) * (r1 + (r2 - r1) * numpoints)
Ys = n.cos(Betas) * (r1 + (r2 - r1) * numpoints)

SpPruzh = plt.plot(Xs + Xb, Ys + Yb)[0]

def run(i):
    Xb = l * n.sin(Psi[i])
    Disk.set_data(Xc + Xb, Yc + Yb) # Изменение положения диска

    Ya = h + r + l * n.cos(Psi[i])
    AB.set_data([Xa, Xb], [Ya, Yb]) # Изменение положения палки

    Pruzh.set_data(Xb + (a - Xb) * Xp, Yp + Yb)

    Betas = numpoints * (2 * n.pi * Ns - Psi[i])
    Xs = n.sin(Betas) * (r1 + (r2 - r1) * numpoints) 
    Ys = n.cos(Betas) * (r1 + (r2 - r1) * numpoints) # Изменение положения пружины
    SpPruzh.set_data(Xs + Xb, Ys + Yb)



anim = FuncAnimation(fgr, run, frames = len(T), interval = 100)

fgr.show()
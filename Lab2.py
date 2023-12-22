import matplotlib.pyplot as p
from matplotlib.animation import FuncAnimation
import numpy as n

T = n.linspace(0, 10, 100)
# Взять phi(t) из предыдущей лабы
Psi = n.linspace(3 * n.pi / 2,  n.pi / 2,  100) # первоначальное отклонение от вертикальной оси
Ksi = n.linspace(n.pi / 2, 3 * n.pi / 2,  100) 
Ksi = Psi
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

Xa = l * 0.3 * n.cos(Psi[0] - 3 * n.pi / 4 )
Ya = l * 0.3 * n.sin(Psi[0] - 3 * n.pi / 4 )    # Координаты точки A

Yb = l * n.cos(Ksi[0]) * 0.4 + Ya 
Xb = l * n.sin(Ksi[0]) * 0.4 + Xa
AB = plt.plot([Xa, Xb], [Ya, Yb])[0]

# # Шаблон пружины
# # /\  /\  /\
# #   \/  \/  \/

# Np = 30  # количество сегментов
# Xp = n.linspace(0, 1, 2 * Np + 1)
# Yp = 0.05 * n.sin(n.pi / 2 * n.arange(2 * Np + 1))

# Pruzh = plt.plot(Xb + (a - Xb) * Xp, Yp + Yb)[0]

# Шаблон спиральной пружины
Ns = 2
r1 = 0
r2 = l * 0.1

# Радиус r1 сделать нулем, а r2 поставить в точку B

numpoints = n.linspace(0, 1, 50 * Ns + 1)
Betas = numpoints * (2 * n.pi * Ns + Ksi[0])
Xs = n.sin(Betas) * (r1 + (r2 - r1) * numpoints)
Ys = n.cos(Betas) * (r1 + (r2 - r1) * numpoints)

SpPruzh = plt.plot(Xs + Xa, Ys + Ya)[0]

# Disk.set_data(Xc + Xb, Yc + Yb) # Изменение положения диска
def run(i):
    # Xb = l * n.sin(Psi[i])

    Xa = l * 0.3 * n.cos(Psi[i] - 3 * n.pi / 4)
    Ya = l * 0.3 * n.sin(Psi[i] - 3 * n.pi / 4)    # Координаты точки A


    Yb = l * n.cos(Ksi[i]) * 0.4 + Ya 
    Xb = l * n.sin(Ksi[i]) * 0.4 + Xa

    AB.set_data([Xa, Xb], [Ya, Yb]) # Изменение положения палки

    Betas = numpoints * (2 * n.pi * Ns + Ksi[i])
    Xs = n.sin(Betas) * (r1 + (r2 - r1) * numpoints) 
    Ys = n.cos(Betas) * (r1 + (r2 - r1) * numpoints) # Изменение положения пружины
    SpPruzh.set_data(Xs + Xa, Ys + Ya)



anim = FuncAnimation(fgr, run, frames = len(T), interval = 1)

fgr.show()
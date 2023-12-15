import math
import sympy as s
import matplotlib.pyplot as plt
import numpy as n
from matplotlib.animation import FuncAnimation

t = s.Symbol('t')

# x = s.sin(t)
# y = s.sin(2 * t)

phi = 7 * t + 1.2 * s.cos(6 * t)
r = (2 + s.cos(6 * t))
x = r * s.cos(phi)
y = r * s.sin(phi)


Vx = s.diff(x)
Vy = s.diff(y)
V = s.sqrt(Vx ** 2 + Vy ** 2)

Ax = s.diff(Vx)
Ay = s.diff(Vy)
A = s.sqrt(Ax ** 2 + Ay ** 2)

At = s.diff(V, t)

R = V ** 2 / s.sqrt(A ** 2 - At ** 2)


step = 1001
T = n.linspace(0, 10, step) # Time
X = n.zeros_like(T)
Y = n.zeros_like(T)
VX = n.zeros_like(T)
VY = n.zeros_like(T)
AX = n.zeros_like(T)
AY = n.zeros_like(T)
Rarr = n.zeros_like(T)


for i in range(len(T)):
    X[i] = s.Subs(x, t, T[i])
    Y[i] = s.Subs(y, t, T[i])
    VX[i] = s.Subs(Vx, t, T[i])
    VY[i] = s.Subs(Vy, t, T[i])
    AX[i] = s.Subs(Ax, t, T[i])
    AY[i] = s.Subs(Ay, t, T[i])
    Rarr[i] = s.Subs(R, t, T[i])

fig = plt.figure()

axis = fig.add_subplot(1, 1, 1)
axis.axis('equal')
axis.set(xlim=[-7, 7], ylim=[-7, 7])
axis.plot(X, Y)

Rx = X[0] + VY[0] * Rarr[0]/math.sqrt(VX[0]**2 + VY[0]**2)
Ry = Y[0] - VX[0] * Rarr[0]/math.sqrt(VX[0]**2 + VY[0]**2)

Pnt = axis.plot(X[0], Y[0], marker='o')[0]
Vp = axis.plot([X[0], X[0] + VX[0]], [Y[0], Y[0] + VY[0]], 'r')[0]
Acc = axis.plot([X[0], X[0] + AX[0]], [Y[0], AY[0] + Y[0]], 'purple')[0]
Rp = axis.plot([X[0], Rx], [Y[0], Ry], 'black')[0]


def Vect_arrow(X, Y, ValX, ValY):
    a = 0.2
    b = 0.3
    Arx = n.array([-b, 0, -b])
    Ary = n.array([a, 0, -a])
    alp = math.atan2(ValY, ValX)
    RotArx = Arx * n.cos(alp) - Ary * n.sin(alp)
    RotAry = Arx * n.sin(alp) + Ary * n.cos(alp)

    Arx = X + ValX + RotArx
    Ary = Y + ValY + RotAry
    return Arx, Ary


RAx, RAy = Vect_arrow(X[0], Y[0], VX[0], VY[0])
RAccx, RAccy = Vect_arrow(X[0], Y[0], AX[0], AY[0])
Rrx, Rry = Vect_arrow(X[0], Y[0], Rx, Ry)

Varrow = axis.plot(RAx, RAy, 'red')[0]
Accarrow = axis.plot(RAccx, RAccy, 'purple')[0]
Rarrow = axis.plot(Rrx, Rry, 'black')[0]

def anim(i):
    Rx = X[i] + VY[i] * Rarr[i]/math.sqrt(VX[i]**2 + VY[i]**2)
    Ry = Y[i] - VX[i] * Rarr[i]/math.sqrt(VX[i]**2 + VY[i]**2)
    Rrx, Rry = Vect_arrow(X[i], Y[i], Rx - X[i], Ry - Y[i])
    Rarrow.set_data(Rrx, Rry)

    Rp.set_data([X[i], Rx], [Y[i], Ry])

    Pnt.set_data(X[i], Y[i])

    Acc.set_data([X[i], X[i] + AX[i]], [Y[i], Y[i] + AY[i]])
    RAccx, RAccy = Vect_arrow(X[i], Y[i], AX[i], AY[i])
    Accarrow.set_data(RAccx, RAccy)

    Vp.set_data([X[i], X[i] + VX[i]], [Y[i], Y[i] + VY[i]])
    RAx, RAy = Vect_arrow(X[i], Y[i], VX[i], VY[i])
    Varrow.set_data(RAx, RAy)


an = FuncAnimation(fig, anim, frames=step, interval=12)
fig.show()

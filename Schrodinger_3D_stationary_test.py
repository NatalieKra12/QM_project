#simulation in 3D
from math import sin, pi,cos
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.cm as cm
from matplotlib.widgets import Slider
from matplotlib.widgets import CheckButtons
from colorspacious import cspace_converter
from tkinter import *
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
#constants------------------------
#a = 1 #nm
#b = 1
hc = 1240
hbc = 197
m = 511000
pi = np.pi
#calculations_unstationary_states----------------------------------
time  = 0
nx = 3
ny = 3
L = 1**-10
x = np.linspace(0, L, 100)
y = np.linspace(0, L, 100)
X, Y = np.meshgrid(x, y)

Ex = nx**2*hbc**2*np.pi**2/(2*m*L**2)
Ey = ny**2*hbc**2*np.pi**2/(2*m*L**2)
E = Ex + Ey
	
psi = np.real((2/np.sqrt(L*L))*np.sin(nx*pi*x/L)*np.sin(ny*pi*y/L)*np.exp(-1j*E*time/(hbc**2)))

def Psi_3d(a, b, t):
    psi_3d = np.real((2/np.sqrt(L*L))*np.sin(nx*pi*a/L)*np.sin(ny*pi*b/L)*np.exp(-1j*E*t/(hbc**2)))  
    return psi_3d	
	
psi = np.array([Psi_3d(x,y,time) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = Psi_3d(X,Y,time)
PSI = psi.reshape(X.shape)
#plot = none
def animate(i, Z, line):
    global time
    #psi = np.array([Psi_3d(x,y,time) for x,y in zip(np.ravel(X), np.ravel(Y))])
    #PSI = psi.reshape(X.shape)
    ax.clear();
    Z = Psi_3d(X,Y,time)
    line = ax.plot_surface(X,Y,Z, cmap = cm.twilight, linewidth =0.5)
    time = time+300
    print("Tu")
    return line,
if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    line = ax.plot_surface(X,Y,Z,cmap = cm.twilight, linewidth = 0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    ax.set_zlim(-2, 2)
    ax.set_zlabel('Z')
    Z = Psi_3d(X,Y,time)
    plt.title('Probability density n=1', color='magenta')
    
    ani = animation.FuncAnimation(fig, animate, fargs = (Z, line),  interval=100, blit = FALSE)
    plt.show()
	
	
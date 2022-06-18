#Energy States
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
#constants------------------------
a = 1 #nm
b = 1
hc = 1240
hbc = 197
m = 511000
pi = np.pi
#calculations_unstationary_states----------------------------------
time  = 0
i = 0
nx = 3
ny = 3

x = np.arange(0, a, 0.01)
y = np.arange(0, b, 0.01)
xp, yp = np.meshgrid(x, y)

Ex = nx**2*hbc**2*np.pi**2/(2*m*a**2)
Ey = ny**2*hbc**2*np.pi**2/(2*m*b**2)
E = Ex + Ey

Earray = []
Xarray = []
Yarray = []

psi = np.real((2/np.sqrt(a*b))*np.sin(nx*pi*xp/a)*np.sin(ny*pi*yp/b)*np.exp(-1j*E*time/(hbc**2)))
def addStages(nxx, nyy):
    for x in range(nxx):
	    for y in range(nyy):
		    Ex = x**2*hbc**2*np.pi**2/(2*m*a**2)
		    Ey = y**2*hbc**2*np.pi**2/(2*m*b**2)
		    E = Ex + Ey
		    Earray.append(E)
		    Xarray.append(x)
		    Yarray.append(y)
		    #xcoor = [0, 20]
		   # ycoor = [E, E]
		    #plt.plot(xcoor, ycoor, label = "Stan i")
		    print(E)
            			

#simualtion--------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(111)
    ax.set_title('Energy Stages')
    #ax.set_xlabel('x [nm]')
    ax.set_ylabel('E = Enx+Eny')
    addStages(nx, ny)
    for i in range(len(Earray)):
	    xcoor = [0, 20]
	    ycoor = [Earray[i], Earray[i]]
	    if Xarray[i]==Yarray[i]:
		    plt.text(0,Earray[i], str(Xarray[i])+', '+str(Yarray[i]))
	    if Xarray[i]>Yarray[i]:
		    plt.text(10,Earray[i], str(Xarray[i])+', '+str(Yarray[i]))
	    if Xarray[i]<Yarray[i]:
		    plt.text(15,Earray[i], str(Xarray[i])+', '+str(Yarray[i]))
	    plt.plot(xcoor, ycoor, label = "Stan i")
    plt.show()

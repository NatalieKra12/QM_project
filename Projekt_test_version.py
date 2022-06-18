# test version

from math import sin, pi,cos
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.cm as cm
from matplotlib.widgets import Slider
from matplotlib.widgets import CheckButtons
from colorspacious import cspace_converter
from qmsolve import Hamiltonian, SingleParticle, init_visualization
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#Window--------------------------------------------------------------------------------

#End_Window----------------------------------------------------------------------------
fig = plt.figure()
phase_plot  = fig.add_subplot(111)
psi_plot = fig.add_subplot(212)

a = 1 #nm
b = 1
hc = 1240
hbc = 197
m = 511000
pi = np.pi

nx = 1
ny = 1

    x = np.arange(0, a, 0.01)
    y = np.arange(0, b, 0.01)
    xp, yp = np.meshgrid(x, y)

    psi = (2/np.sqrt(a*b))*np.sin(nx*pi*xp/a)*np.sin(ny*pi*yp/b)
    fig, ax = plt.subplots()
    cs = ax.contourf(xp, yp, psi, levels = 50, cmap = cm.hsv)
	
plt.show();
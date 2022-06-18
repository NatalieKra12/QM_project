"""
A programming project created as a part of completing
the Quantum Physics course at the Warsaw University of Technology

Authors: Viktoriia Vlasenko, Natalia Kramarz
"""

# import sys
# import csv
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

from math import sin, pi,cos
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.cm as cm
from matplotlib.widgets import Slider
from matplotlib.widgets import CheckButtons
from colorspacious import cspace_converter
from qmsolve import Hamiltonian, SingleParticle, init_visualization

# --------------CONSTANS--------------
a = 1 #nm
b = 1
hc = 1240
hbc = 197
m = 511000
pi = np.pi



if __name__ == "__main__":
    nx = 1
    ny = 1

    x = np.arange(0, a, 0.01)
    y = np.arange(0, b, 0.01)
    xp, yp = np.meshgrid(x, y)

    psi = (2/np.sqrt(a*b))*np.sin(nx*pi*xp/a)*np.sin(ny*pi*yp/b)
    fig, ax = plt.subplots()
    cs = ax.contourf(xp, yp, psi, levels = 50, colors='red')
	

    cbar = fig.colorbar(cs, label = 'psi')
    ax.set_title('Particle in an Infinite 2D Square Well')
    ax.set_xlabel('x [nm]')
    ax.set_ylabel('y [nm]')

    plt.subplots_adjust(left=0.12, bottom=0.35)
	
    ax_a = plt.axes([0.1, 0.15, 0.8, 0.03])
    a_slider = Slider(ax_a, '$n_{x}$', 1, 5, valinit=1, valfmt='%0.0f')
    a_slider.label.set_size(20)
    #
    ax_b = plt.axes([0.1, 0.05, 0.8, 0.03])
    b_slider = Slider(ax_b, '$n_{y}$', 1, 5, valinit=1, valfmt='%0.0f')
    b_slider.label.set_size(20)

    def update_n(val_):
        ax.clear()
        nx = a_slider.val
        ny = b_slider.val
        Ex = nx*hc**2/(8*m*a**2)
        Ey = ny*hc**2/(8*m*b**2)
        E = Ex + Ey
        psi = (2/np.sqrt(a*b))*np.sin(nx*pi*xp/a)*np.sin(ny*pi*yp/b)
        t = 1 #s
        phase = np.exp(E*t/hbc)
        cs = ax.contourf(xp, yp, phase, levels = 50, cmap = cm.hsv)
        # cbar = fig.colorbar(cs, label = 'psi')


    a_slider.on_changed(update_n)
    b_slider.on_changed(update_n)

    # check.on_clicked(on_check)
    plt.show()
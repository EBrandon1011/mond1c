# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:25:55 2017

@author: brandon

CÓDIGO PARA EL AJUSTE DE UNA ELIPSE OBTENIDO DE:
https://scipython.com/book/chapter-8-scipy/examples/non-linear-fitting-to-an-ellipse/
"""

import numpy as np
from scipy import optimize
import pylab

class Elipse():
    nombre = 'Algo'

def f(theta, p):
    a, e = p
    return a * (1 - e**2)/(1 - e*np.cos(theta))


def residuals(p, r, theta):
    """ Return the observed - calculated residuals using f(theta, p). """
    return r - f(theta, p)

def jac(p, r, theta):
    """ Calculate and return the Jacobian of residuals. """
    a, e = p
    da = (1 - e**2)/(1 - e*np.cos(theta))
    de = (-2*a*e*(1-e*np.cos(theta)) + a*(1-e**2)*np.cos(theta))/(1 -
                                                        e*np.cos(theta))**2                                    
    return -da,  -de
    return np.array((-da, -de)).T

# Initial guesses for a, e
#p0 = (1, 0.5)
#plsq = optimize.leastsq(residuals, p0, Dfun=jac, args=(r, theta), col_deriv=True)

def iteraciones(planetas):
    
    for astro in planetas:           
        astro.data = pylab.loadtxt('RT{}Error.dat'.format(astro.nombre))  
        astro.r = astro.data[:,0]
        astro.theta = astro.data[:,1]
        if astro.nombre == "Hale":
            pylab.polar(astro.theta, astro.r, 'r-', label='HaleBopp', linewidth=1)
        else:
            pylab.polar(astro.theta, astro.r, 'b-', label='HaleBopp', linewidth=1)
        # Initial guesses for a, e
        p0 = (200, 0.8)
        plsq = optimize.leastsq(residuals, p0, Dfun=jac, args=(astro.r, astro.theta), col_deriv=True)
        print('Ecc.{} = {}'.format(astro.nombre, plsq[0]))

def main():
    hale=Elipse()
    hale.nombre ='Hale'
    
    haleP=Elipse() #PLUS r+dr
    haleP.nombre ='HaleP'

    haleM=Elipse() #MINUS r-dr
    haleM.nombre ='HaleM'    
    
    iteraciones([hale, haleP, haleM])

if __name__ == '__main__':
    main()

#theta_grid = np.linspace(0, 2*np.pi, 100)
#pylab.polar(theta_grid, f(theta_grid, plsq[0]), lw=2)
#pylab.polar(theta_grid, f(theta_grid, plsq[0]), lw=2)
pylab.savefig('HBErrorv0.pdf')
pylab.show()

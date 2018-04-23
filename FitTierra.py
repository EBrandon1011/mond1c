import numpy as np
from scipy import optimize
import pylab
import matplotlib.pyplot as plt

def f(theta, p):
    a, e = p
    return a * (1 - e**2)/(1 - e*np.cos(theta))

# The data to fit
data = pylab.loadtxt('NewtonTierra.dat', dtype=float)  
r = data[:,0]
theta = data[:,1]


def residuals(p, r, theta):
    """ Return the observed - calculated residuals using f(theta, p). """
    return r - f(theta, p)

def jac(p, r, theta):
    """ Calculate and return the Jacobian of residuals. """
    a, e = p
    da = (1 - e**2)/(1 - e*np.cos(theta))
    de = (-2*a*e*(1-e*np.cos(theta)) + a*(1-e**2)*np.cos(theta))/(1 -e*np.cos(theta))**2
    return -da,  -de
    return np.array((-da, -de)).T

# Initial guesses for a, e
p0 = (1, 0.1)
plsq = optimize.leastsq(residuals, p0, Dfun=jac, args=(r, theta), col_deriv=True)
print(plsq)

pylab.polar(theta, r, 'b-')
theta_grid = np.linspace(0, 2*np.pi, 200)
pylab.polar(theta_grid, f(theta_grid, plsq[0]), lw=2)
plt.rgrids((0.5, 1))
pylab.savefig('FitTierra.pdf')
pylab.show()

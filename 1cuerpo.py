# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:17:28 2018

@author: brandon
"""

import numpy as np
from scipy.constants import G

AU = (149597870700)     # Definiendo una ua
ao=1.2*10**(-10)         #Constante a_o

class Mond():
    nombre='ninguno'    #será dado después
    masa=0.0
    x=y=0.0
    vx=vy=0.0
    r=0.0
    
    def lmi(self):     #Longitud característica
        Mo=1.989*10**30     #Masa solar
        lm=np.sqrt(G*Mo/ao)
        return lm
        
    def f(self):        #Función f(\chi)
        x=self.x
        y=self.y
        r=np.sqrt(x**2+y**2)
        X=self.lmi()/r
        #funcion=X**2    #Newton
        funcion=X*(1+X+X**2+X**3)/(1+X+X**2)    #MOND
        ax=-ao*funcion*x/r
        ay=-ao*funcion*y/r
        ang=np.arctan2(y,x)
        return ax, ay, r, ang
        
    def iteraciones(self):
        counter=0
        NIter=400	#Número de iteraciones
        arch = open("1c{}.dat".format(self.nombre), "w")
        while counter<NIter:
            counter+=1
            dt=24*3600  #1 día
            ax, ay, rad, ang=self.f()
            self.vx+=ax*dt      #Algoritmo v(n+1)=v(n)+a*dt
            self.vy+=ay*dt
            self.x+=self.vx*dt
            self.y+=self.vy*dt
      #      print('x= {:>6.2f}; y= {:>6.2f}'.format(self.x/AU, self.y/AU))     #Datos X,Y en UA
            imp='{:>6.8f} {:>6.8f}'.format(rad/AU, ang)       #Radio y ángulo
            arch.write(str(imp)+"\n")
        arch.close()
                        
def main():
#    hale=Mond()
#    hale.nombre ='Hale'
#    hale.x=-136759097051.827
#    hale.vy=-44001.0945139
#    
#    haleP=Mond() #PLUS r+dr
#    haleP.nombre ='HaleP'
#    haleP.x=-137250656596.667
#    haleP.vy=-43922.4701946
#    
#    haleM=Mond() #MINUS r-dr
#    haleM.nombre ='HaleM'
#    haleM.x=-136267537506.986
#    haleM.vy=-44079.7188331

    tierra = Mond()
    tierra.nombre = 'Tierra'
    tierra.masa = 5.9742 * 10**24
    tierra.x = -147.09 *10**9
    tierra.vy = 30.29 * 1000 
        
#    hale.iteraciones()
#    haleP.iteraciones()
#    haleM.iteraciones()
    tierra.iteraciones()
    
if __name__ == '__main__':
    main()
    
    
    

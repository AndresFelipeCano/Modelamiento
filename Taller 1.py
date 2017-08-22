# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:43:59 2017

@author: Cano
"""

# -- coding: utf-8 --
import numpy as np
import matplotlib.pyplot as plt
figureNumber = 1 #Se llevará el conteo de las gráficas
######################################################
#Problema #1, clase 15/08/2017
t = 0 #Tiempo inicial
dt = 0.001 #El intervalo de tiempo
ti = [t] #Arreglo para guardar cada instante de tiempo
x = 0 #posición en x inicial
y = 200 #posición en y inicial
xi = [x] #Arreglo donde se guarda cada posición en x
yi = [y] #Arreglo donde se guarda cada posición en y
while(y >= 0 ):
    t = t + dt
    x = 2598*(1-np.exp(-0.01*t))
    y = 99700 - 99500*np.exp(-0.01*t) - 980*t
    ti.append(t)
    xi.append(x)
    yi.append(y)
plt.figure(figureNumber)
plt.plot(xi, yi, '-b')
figureNumber = figureNumber + 1
print("Punto 4")
#Fin ejercicio 1
######################################################


#########################
#########################

#Rosa de 8 petalos.
angle = 0
r = 2*(np.cos(np.radians(angle))**4 - 6*np.cos(np.radians(angle))**2 * np.sin(np.radians(angle))**2 + np.sin(np.radians(angle))**4)
vali = [r + 0.5]
anglei = [np.radians(angle)]
while( angle <= 360):
    angle += 0.02
    r = 2*(np.cos(np.radians(angle))**4 - 6*np.cos(np.radians(angle))**2 * np.sin(np.radians(angle))**2 + np.sin(np.radians(angle))**4)
    
    if( r <= 0):
        r = -2*(np.cos(np.radians(angle))**4 - 6*np.cos(np.radians(angle))**2 * np.sin(np.radians(angle))**2 + np.sin(np.radians(angle))**4)
        
    vali.append(r + 0.5)
    anglei.append(np.radians(angle))
plt.figure(figureNumber)
figureNumber += 1
plt.polar(anglei, vali)
#########################
#circulo rectangular
angle = 0
r = 1
vali = [r]
anglei = [np.radians(angle)]
cont = 0
while( angle <= 360):
    angle += 2.5 
    if(cont <= 5):
        r = 1.5
        cont += 1
    elif(cont <= 10):
        r = 1
        cont += 1
    else:
        cont = 0
    vali.append(r)
    anglei.append(np.radians(angle))
plt.figure(figureNumber)
figureNumber += 1        
plt.polar(anglei, vali)
#######################
######################
#Función Seno
periodo = 0.5

x = np.linspace(0, 2, 1000)*2

y = np.sin((2*np.pi*x/periodo)+1.5)-1

plt.figure(figureNumber)
figureNumber += 1

plt.plot(-x, -y, 'k', linewidth = 1, label = 'y1')

plt.show()
#################################
###############################
#Punto 1

#Lista de coeficientes de fricción:
t = 0
dt = 0.0001
ti = [t]
h0 = 100
y = h0
yi = [y]
#Aquí se puede cambiar el valor actual de la masa y la friccion
#masa = int(input("Ingrese la masa:\n"))
#friccion = float(input("Ingrese la friccion:\n"))
masa = 100
friccion = 5
gravedad = 9.8
while( y >= 0 ):
    t = t + dt
    y = h0 + ((masa**2)/friccion**2) * gravedad - ((masa**2)/friccion**2) * gravedad * np.exp((-friccion/masa)* t) - ((masa*gravedad)/friccion) * t
    ti.append(t)
    yi.append(y)
print("Punto 1 con fricción:")   
plt.figure(figureNumber)
figureNumber += 1
plt.plot(ti, yi, '-b')
#Sin fricción.
print("Punto 1 sin fricción:")
t = 0
dt = 0.001
h0 = 100
y = h0
ti = [t]
yi = [y]
masa = 100
gravedad = 9.8
while( y >= 0):
    t = t + dt
    y = h0 - (masa*gravedad)*t/2
    yi.append(y)
    ti.append(t)

plt.figure(figureNumber)
figureNumber += 1
plt.plot(ti, yi, '-b')




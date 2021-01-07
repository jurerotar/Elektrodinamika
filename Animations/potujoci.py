#!/usr/bin/python3
print('*** Animacija pretoka moči - S53MV 12.12.2020 ***')

Gama=0      #Odbojnost bremena pri z=0
ab=0        #Slabljenje voda alpha/beta
zk=1.5      #razmerje napetost/tok ali E/H

import numpy as np                  #Uporaba učinkovitih funkcij numpy
import matplotlib.pyplot as plt     #Risanje rezultata z matplotlib

def u(az,wt,bz,Gama):   #u(t,z) na prenosnem vodu
    return np.real(np.exp(-az+1j*(wt-bz))+Gama*np.exp(az+1j*(wt+bz)))

def i(az,wt,bz,Gama):   #i(t,z) na prenosnem vodu
    return np.real(np.exp(-az+1j*(wt-bz))-Gama*np.exp(az+1j*(wt+bz)))

bz=np.linspace(-6*np.pi,0,3333)  #Faza beta*z negativna proti izvoru
az=ab*bz                    #Slabljenje alpha*z
wt=0                        #Začetni omega*t

fig,ax=plt.subplots()       #Prvo risanje z normalizacijo matplotlib
line1,=ax.plot(bz,u(az,wt,bz,Gama),'-b')        #Začetni u(t,z)
line2,=ax.plot(bz,i(az,wt,bz,Gama)/zk,'-g')     #Začetni i(t,z)
line3,=ax.plot(bz,u(az,wt,bz,Gama)*i(az,wt,bz,Gama),'-r')   #Začetni p(t,z)
plt.title(r'Breme $\Gamma=$'+str(Gama)+r'     Slabljenje $\alpha/\beta=$'+str(ab))
plt.xlabel(r'Razdalja do bremena $\beta z$')
plt.ylabel(r'Modra$\equiv E=u/h$   Zelena$\equiv H=i/w$   Rdeča$\equiv S=p/hw$')

while plt.waitforbuttonpress(0.01)==None:           #Zanka animacije
    wt+=0.03                #Časovni korak omega*t
    line1.set_ydata(u(az,wt,bz,Gama))       #Animacija u(t,z)
    line2.set_ydata(i(az,wt,bz,Gama)/zk)    #Animacija i(t,z)
    line3.set_ydata(u(az,wt,bz,Gama)*i(az,wt,bz,Gama))  #Animacija p(t,z)
    fig.canvas.draw()       #Ponovno risanje

print('*** Konec ***')      #Izhod=pritisk tipke/miške

# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#t = np.arange(0.,5.,0.2)
#
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#plt.show()

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
    
t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.figure(1) #first figure
plt.subplot(211) #first subplot in the first figure
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212) #second subplot in first figure
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:22:18 2020

@author: Kuntal
"""
from scipy import signal
import matplotlib.pyplot as plt

s1 = signal.lti([15], [5,17])


w, mag1, phase1 = signal.bode(s1)



plt.figure()
plt.semilogx(w, mag1)    # Bode magnitude plot

plt.title('Magnitude')
plt.grid()
plt.figure()
plt.semilogx(w, phase1)  # Bode phase plot

plt.title('Phase')
plt.grid()
plt.show()

A = [[1,2],
     [3,4],
     [5,6]]
#A += 1
print(np.array(A)+1)
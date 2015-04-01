# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

x=[]
y=[]

readfile = open('numbers.txt', 'r')
sepfile = readfile.read().split('\n')
readfile.close()

for plotpair in sepfile:
    xandy = plotpair.split(',')
    x.append(int(xandy[0]))
    y.append(int(xandy[1]))
    
plt.plot(x,y)
plt.title('Graph')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()
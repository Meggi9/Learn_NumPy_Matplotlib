import math as mh
import numpy as np
import matplotlib.pyplot as plt

def Task_5():
    x0=-10
    x1=10
    h=0.1
    a=2
    b=3

    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []

    for i in np.arange(x0, x1+1, h):
        x.append(round(i,1))
        y1.append(mh.fabs(a*i))
        y2.append(a*mh.fabs(i))
        y3.append(mh.fabs(a+i))
        y4.append(-1*(i**3))
        y5.append(a*(i**2)-(i**3))
        y6.append(b-(i**3))

    print(x)
    print(y1)
    print(y2)
    print(y3)
    print(y4)
    print(y5)
    print(y6)

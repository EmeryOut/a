# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:55:34 2019

@author: cheng
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('data.xls')
data.columns = ['t', 'd']

d = data['d'].get_values()

def mean(n, array):
    length = len(array)
    end = (length//n)
    return np.mean(array[:n*end].reshape(n,end), axis=1)


def _allan_deviation(series):
    length = len(series)
    return 0.5*np.mean([(series[i] - series[i+1])*(series[i] - series[i+1]) for i in range(length-1)])/(len(series)-1)

def allan_deviation(n):
    series = mean(n, d)
    return _allan_deviation(series)

f = 299792458.0 / 730e-9 
ad = [allan_deviation(i)/f for i in range(2,len(d)//2)]


fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)

line, = ax.plot(np.linspace(2,3690,3688)*11.2, ad, color='blue', lw=0.5)
ax.set_title(r'Allan variance of the fractional frequency deviation ($\delta f/f$)')
ax.set_xlabel('Time interval/$s$')
ax.set_ylabel('Allan variance')

ax.set_xscale('log')
ax.set_yscale('log')

plt.savefig("data.pdf")




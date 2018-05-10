# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 500);
y = np.sin(x)
plt.style.use('ggplot')
fig = plt.figure()
plt.plot(x, y)
plt.show()
fig.savefig('sin.pdf', format='pdf')
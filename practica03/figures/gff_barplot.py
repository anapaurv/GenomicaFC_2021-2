#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/Users/solouli/opt/anaconda3/bin/python

import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

open('/Users/anapau/Desktop/GenomicaComputacional/aprubio_p03/figures/barplot_data.txt', 'r')
frecuencias = [3, 12, 5, 18, 45]
categorias = ['Categoría A', 'Categoría B', 'Categoría C', 'Categoría D', 'Categoría E']
categorias = [ '\n'.join(wrap(l, 11)) for l in categorias]

y_pos = np.arange(len(categorias))

# Gráfico de barras
plt.bar(y_pos, frecuencias)

# Nombres en el eje-x
plt.xticks(y_pos, categorias)

# Mostrar la gráfica
plt.show()


# In[ ]:





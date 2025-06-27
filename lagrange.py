import numpy as np
from scipy.interpolate import lagrange
x = np.array([-2, -1, 3, 4.3, 7.7])
y = x
poly = lagrange(x, y)

print(poly)

#PAGINA 126 LIBRO METODOS NUMERICOS

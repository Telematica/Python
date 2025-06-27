from numpy.random import default_rng as rng
import matplotlib.pyplot as plt
import pandas as pd


rng = rng(12345)

uniform = rng.uniform(1, 5, size=100)
# uniform
#plt.plot(uniform)
# plt.show()

normal = rng.normal(1, 2.5, size=100)
# normal
# plt.plot(normal)
#plt.hist(normal)
# plt.show()

# Distribución uniforme
# - Los resultados son muy similares

# Distribución normal
# - Los resultados en forma de campana de Gauss
print(type(uniform))

# @todo homework

df = pd.DataFrame([uniform, normal],
   # index=['u', 'n',],
   # columns=['uniform', 'normal']
)

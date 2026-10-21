import numpy as np

print(" ---- LLenar matriz de ceros ----- ")
matriz=np.zeros([3,5]) # 3 filas x 5 culumnas 
print(matriz)
print(" ---- LLenar matriz de unos ----- ")
matriz=np.ones([3,5])
print(matriz)
print(" ---- LLenar matriz de vacios ----- ")
matriz=np.empty([3,5])
print(matriz)
print(" ---- LLenar lista con rango ----- ")
# el primer parametro es el valor inicial
# el segundo parametro es el valor final
# el tercer parametro es el incremento
lista=np.arange(0,10,2)
print(lista)
print(" ---- LLenar lista con rango No2 ----- ")
lista=np.arange(0,10,1)
print(lista)
import numpy as np

califas=np.array([60,70,90])
print(" ---------- ej 1  imprimir califas -------")
print(califas) # imprime la lista de califas 
print(type(califas)) # muestra el tipo de arreglo 
print(" ---------- ej 0 dimensiones de un array -------")
califas=np.array(60)
print(califas)
print("Dimension :", califas.ndim)
print(" ---------- ej 1 dimensiones de un array -------")
califas=np.array([60,70,90])
print(califas)
print("Dimension :", califas.ndim)
print(" ---------- ej 2 dimensiones de un array -------")
califas=np.array([
    [60,70,90],
    [50,80,98]
    ]) # un arreglo de 2 dimenciones es como unaq tablas em excel 
print(califas)
print("Dimension :", califas.ndim)
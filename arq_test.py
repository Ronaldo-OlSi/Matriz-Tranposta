from apre__matriz import ler_matriz, exibir_matriz
from operac import *

A = ler_matriz("matriz1.txt")
B = ler_matriz("matriz2.txt")
"""
if (eh_igual(A, A)):
    exibir_matriz(A)
    print('Matriz A igual a M A')
else:
    print("Erro")
"""

Tr = transposta(A)
print("\n")
print("***** Transposição de Matriz ****\n")
exibir_matriz(A)
print("Original")
print("\n")
print("***********")
exibir_matriz(Tr)
print("Resultado transposto")

print("#######################")
print("\n")
print("*** Prova real ****")
P = transposta(Tr)
exibir_matriz(Tr)
print("Transposta Obtida")
print("\n")
print("***********")
exibir_matriz(P)
if (eh_igual(A, P)):
    print("Prova real. A transposta da transposta é igual a matriz original")
else:
    print("Erro na transposta de transposta")

arquivo = open('Result_01.txt', 'w')
t = str(Tr)
arquivo.write(t)
arquivo.close()
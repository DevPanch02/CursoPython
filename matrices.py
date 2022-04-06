#   LISTAS ANIDADAS o MATRICES
#   CONJUNTO DE LISTAS

#   MATRIZ[FILA][COLUMNA]

# fila=[1,2,3]
# fila1=[4,5.5,6]
# fila2=[7,8,9]

# matriz=[fila, fila1, fila2]

# suma = matriz[1][1] + matriz[2][1]
# print(f"{matriz[1][1]} + {matriz[2][1]} = {suma} ")


#   PRIMERA MATRIZ
fila=[1,2,3]
fila1=[4,5.5,6]
fila2=[7,8,9]


#   SEGUNDA MATRIZ
fila3=[10,20,30]
fila4=[41,51.5,61]
fila5=[32,83,93]

matriz=[fila, fila1, fila2]
matriz1=[fila3,fila4,fila5]
print(f"PRIMERA MATRIZ {matriz}\nSEGUNDA MATRIZ {matriz1} ")


print("-----------ADICION DE MATRICES----------------")
sumaMatrices=matriz + matriz1
print(f"La suma de las matrices es: {sumaMatrices} ")






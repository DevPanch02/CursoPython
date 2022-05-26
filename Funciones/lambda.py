#   LAMBDA
#   FUNCIONES PEQUENIAS QUE SON DECLARAS DE MANERA 
#   CONCISA LO CUAL AYUDA A REDUCIR LINEAS DE CODIGO

#   EJEMPLO lambda : map(duplicar valores), filter(filtrar)

def suma(a,b): return a+b

print(suma(4,5))


valor = lambda a1,b1: a1+b1
print(valor(3,2))

#   EJERCICIO map
mi_lista=[1,2,3,4,6,7,8]
valor=map(lambda x: x*2, mi_lista)
print(list(valor))

#   EJERCICIO filter
mi_lista1=[1,2,3,4,6,7,8]
valor1=filter(lambda x1: x1%2==0, mi_lista1)
print(tuple(valor1))



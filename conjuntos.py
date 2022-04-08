#   CONJUNTOS
#   SON COLECCIONES DE DATOS NO ORDENADOS, 

conjunto={1,2,3,'holaDev'}
# print(type(conjunto))


lista=[1,5,3,4]
lista1=[10,50,30,1,3]
a1=set(lista)
a2=set(lista1)
# print(f" Lista a conjunto: {a1} ")

# prueba=list(a1)
# print(f" Conjunto a lista: {prueba} ")

#   METODOS
#   AGREGAR VALORES

print(a1)
a1.add(34)
print(f"Agregar: {a1} ")

print(5 in a1)

#   BORRAR ELEMENTO DE CONJUNTO
a1.discard(5)
print(f"Elemento borrado: {a1}")

#   CONTAR NUMERO DE VALORES
print("El numero de elementos es: ",len(a1))

#   COMPARAR VALORES
print(5 in a1)


#   OPERACIONES
print(a1 | a2)
print(a1 & a2)
print(a1 - a2)
print(a2 - a1)



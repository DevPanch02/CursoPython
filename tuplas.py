#   SIMILAR A LAS LISTAS CON LA DIFERENCIA
#   QUE ESTA NO PUEDE SER MODIFICADA

#   UNA TUPLA ES INMUTABLE
#   SE ESCRIBE CON PARENTESIS EN LUGAR DE CORCHETES

tupla=('Enero','Febrero','Marzo')

unionTupla=([1,2,3],'dev',tupla)

# tupla[1]=4 #   NOS DARA ERROR

# print(tupla)

lista = list(tupla)
print(lista)
lista[1]=3
print(f"Modificacion: {lista} ")

unionTupla1=([1,2,3],'dev',lista)
print(unionTupla1)
listaMulti=list(unionTupla1)

print(listaMulti[2])
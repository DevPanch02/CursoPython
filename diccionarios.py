#   DICCIONARIOS

#   ALMACENA DIVERSOS TIPOS DE DATOS
#   

valor1={1:'hola', 2:'Dev',3:None}
valor2={'Diccionarios':2.3, 'listas':4, 'tuplas':5}
print(type(valor1))


#   METODOS DENTRO DE DICCIONARIOS
#   ASIGNAR VALORES
valor1[3]=5.4
print(valor1)

#   BUSQUEDA DE VALORES EN DICCIONARIO
print(3 in valor1)

#   COPIAR DICCIONARIO
copiaValor=valor1.copy()
print(f'copia {copiaValor} ')

#   BUSQUEDA EN UN DICCIONARIO
print(valor1.get(1))
print(valor2.get('Diccionarios'))


#   DEVUELVE UNA LISTA DE DICCIONARIOS
print(valor1.items())

#   AGREGAR UN NUEVO ELEMENTO EN DICCIONARIO
valor1[4]='Nuevo valor'
print(valor1)

#   ELIMINAR ELEMENTOS DE UN DICCIONARIO
print(f'Segundo diccionario: {valor2} ')
print(valor2.pop('Diccionarios'))
print(valor2)


#   BORRAR DICCIONARIO
valor1.clear()
print(valor1)



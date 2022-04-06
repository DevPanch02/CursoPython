#   LISTAS -> ESTRUCTURA DE DATOS

#   PERMITE ALMACENAR CUALQUIER TIPO DE
#   VALOR YA SEA ENTERO, FLOTANTE Y CADENAS
# lista1=[]

lista = [1, 2.5, 'DevPanch',4, True]
print(lista)
print(" METODOS DE LISTAS ")

#  METODO PARA AGREGAR ELEMENTOS EN LISTA append()
print("-----AGREGAR------")
lista.append("Hola de nuevo")
print(lista)

#   ELIMINAR ULTIMO VALOR -> pop()
print("-----BORRAR UTIMO VALOR------")
lista.pop()
print(lista)

#   METODO PARA BORRAR UN ELEMENTO -> remove()
print("-----BORRAR------")
lista.remove(4)
print(lista)

#   INVERTIR ELEMENTO DE UNA LISTA -> reverse()
print("-----REVERTIR------")
lista.reverse()
print(lista)

#   ACTUALIZAR
print("-----ACTUALIZAR------")
lista[3:]=[4.5,3,5]
print(lista)

#   OPERACIONES CON VALORES DE UNA LISTA?
suma = lista[2]+lista[3]
print(f"La suma es: {suma} ")
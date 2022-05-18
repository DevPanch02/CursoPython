#   FUNCIONES
#   PODEMOS CREAR NUESTRAS PROPIAS FUNCIONES len(), range(),
#   random(), print(), etc.
#   REDUCE EL NUMERO TOTAL DE LINEAS DE CODIGO
#   PALABRA CLAVE 'def'
#   FUNCIONES CON PARAMETROS / SIN PARAMENTROS

#   FUNCIONES SIN PARAMENTROS
#   ESTRUCTURA
# def mensaje():
#     for i in range(10):
#         print(f" {i} * {5} = {i*5} ")

# mensaje()


#   FUNCIONES CON RETORNOS
#   SE USA LA FUNCION return

def mensaje1():
    return "Hola Dev",[1,2,3,4],2022

mensaje,lista,anio=mensaje1()
print(mensaje)
print(lista)
print(anio)
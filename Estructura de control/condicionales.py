#   IF  / ELSE
#   NOS PERMITE DEFINIR UN CAMINO 
#   PARA SU CORRECTA EJECUCION

valor= int(input('Ingrese valor: '))
# print(valor%2)
# if valor%2==0:
#     print(f'El valor {str(valor)}, se encuentra en rango ')
# else:
#     print(f'El valor {valor}, no esta en rango ')
         
if (valor>0) and (valor<10):
    if valor%2==0:
        print(f'El valor {valor}, es par ')
    else:
        print(f'El valor {valor}, es impar ')

    print(f'El valor {valor}, se encuentra en rango ')

else:
    print(f'El valor {valor}, no esta en rango ')
    
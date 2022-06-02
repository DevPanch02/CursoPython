#   LAS EXCEPCIONES SON BLOQUES DE CODIGO
#   QUE NOS PERMITE CONTINUAR CON LA
#   EJECUCION DE UN PROGRAMA PESE A QUE 
#   OCURRA UN ERROR.

#   EJEMPLO ERROR COMUN
# n=float(input("Ingrese valor: "))
# print(f"El numero {n} es igual: {n/n} ")

#   SOLUCION

while True:
    try:
        n=float(input("Ingrese valor: "))
        print(f"El numero {n} es igual: {n/n} ") 
        
    except TypeError:
        print("Error\nIngrese nuevamente..!")

    else:
        print("Ah culminado..!")
        break

    finally:
        print("Ah terminado la excepcion..!")
    

#   TypeError
#   ValueError
#   ZeroDivisionError
#   Exception
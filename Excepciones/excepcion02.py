#   TypeError => tipo de error
#   ValueError => error de valores
#   ZeroDivisionError => error de division
#   Exception => algun error restante   

try:
    n=float(input("Ingrese valor: "))
    print(f"La operacion es: {5/n} ")
    
except TypeError:
    print("NO se puede realizar operacion con str")

except ValueError as e:
    print(f"Debe ingresar numeros: {e} ")

except ZeroDivisionError as e:
    print(f"No se puede realizar operacion: {e} ")

except Exception as e:
    print(f"Error no previsto: {e} ")
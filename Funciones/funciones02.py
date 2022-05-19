#   FUNCIONES CON PARAMETOS Y ARGUMENTOS

# def suma(a,b):
#     suma=a+b
#     return suma

# valor = int(input("Ingrese valor 1: "))
# valor1 = int(input("Ingrese valor 2: "))

# print(suma(valor,valor1))

def valores(a=None, b=None):
    if a==None or b==None:
        
        return "Llene los campos"
    else:
        return a+b

valor = int(input("Ingrese valor 1: "))
valor1 = int(input("Ingrese valor 2: "))

print(valores(valor,valor1))   
import math
#   FUNCION DE LA OPERACION 1
def area_circulo(radio):
    area=math.pi*(radio*radio)
    return area

#   FUNCION DE LA OPERACION 2
def opcion_2():
    while True:
        operacion=input("1.SUMA\n2.RESTA\n3.MULTIPLICACION\n4.DIVISION\n5.FACTORIAL\nIngrese tipo de operacion: ")
        if operacion == '1':
            print("\tSUMA")
            a=int(input("Ingrese primer valor: "))
            b=int(input("Ingrese segundo valor: "))

            c=a+b

            return f'EL valor de la suma es: {c} '
        elif operacion =='2':
            print("\tRESTA")
            a=int(input("Ingrese primer valor: "))
            b=int(input("Ingrese segundo valor: "))

            c=a-b

            return f'EL valor de la resta es: {c} '
        elif operacion == '3':
            print("\tMULTIPLICACION")
            a=int(input("Ingrese primer valor: "))
            b=int(input("Ingrese segundo valor: "))

            c=a*b

            return f'EL valor de la multiplicacion es: {c} '
        elif operacion == '4':
            print("\tDIVISION")
            a=int(input("Ingrese primer valor: "))
            b=int(input("Ingrese segundo valor: "))

            c=a/b

            return f'EL valor de la division es: {c} '

        elif operacion == '5':
            print("\tFACTORIAL")

            def factorial(num):
                if num>1:
                    num=num*factorial(num-1)
                return num

            return f"Nuestra factorial de 5 es: {factorial(5)} "
        else: 
            print("Error.!!\n\tIngrese nuevamente..!!")

#   FUNCION DE LA OPERACION 3
def opcion_3():

    frutas=['mango', 'apple', 'melon', 'pineapple']
    frutas_upper=[]
    print(f"LISTA ORIGINAL: {list(frutas)} ")
    for fruta in frutas:
        x=lambda fruta: fruta.upper()
        frutas_upper.append(x(fruta))
    

    return frutas_upper

#   FUNCION DE LA OPERACION 4
def opcion_4(x):
    prod=1
    for i in range(1,x+1):
        prod=prod*i
    return prod

while True:
    opcion=input("1.AREA DE UN CIRCULO\n2.OPERACIONES BASICAS\n3.LAMBDA\n4.OTRA FACTORIAL\nIngrese opcion: ")
    if opcion == '1':
        print("AREA DE UN CIRCULO")
        radio=float(input('Ingrgese valor de radio: '))

        print(f"El area de un circulo es: {area_circulo(radio)} ")

        break
    elif opcion == '2':
        print("\tOPERACIONES BASICAS")

        print(opcion_2())#Llamada a la funcion

        break
    elif opcion == '3':
        print("LAMBDA")
        print(opcion_3())
        break
    elif opcion == '4':
        print("OTRA FACTORIAL")

        factorial=int(input("Ingrese valor de factorial: "))
        print(f"La factorial de {factorial} es: {opcion_4(factorial)} ")

        break
    else:
        print("Error..!!\n\tIngrese nueuvamente!!")

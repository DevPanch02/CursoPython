import random

while True:
    print("1.SUMA\n2.GRAFICAR TABLAS\n3.LANZAMIENTO DE MONEDA")
    opcion=(input("Ingrese opciones:"))

    if opcion == "1":
        print("SUMA")
        m=int(input("Ingrese primer valor: "))
        m1=int(input("Ingrese segundo valor: "))
        suma=m+m1
        print(f"la suma de {m} + {m1} = {suma} ")
        break

    elif opcion == "2":
        print("GRAFICAR TABLAS")
        m=int(input("Ingrese primer valor: "))
        for i in range(m):
            print(f" {i} * {m} = {i*m} ")
        break

    elif opcion == "3":
        print("LANZAMIENTO DE MONEDA")
        lista=["cara","sello"]
        opcion=random.choices(lista)
        if opcion == "cara":
            print(f"Ah salido {opcion} ")
        else:
            print(f"Ah salido {opcion} ")
        break

    else:
        print("Error al ingreso de datos\n\tINGRESE NUEVAMENTE..!!")
        
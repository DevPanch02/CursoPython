#   EJERCICIOS CON FUNCIONES INDETERMINADAS
def ejercicio(*args,**kwargs):
    for data in kwargs:
        print(data,"=>",kwargs[data])
    
    cont=0
    for elementos in args:
        cont+=elementos
    promedio=cont/len(args)

    if promedio>7:
        print(f"Sumatoria: {cont} ")
        print(f"Promedio: {promedio} ")
        print("Aprovado")
    else:
        print(f"Sumatoria: {cont} ")
        print(f"Promedio: {promedio} ")
        print("Reprovado")

ejercicio(0,9,8,8, nombre="Dev",edad=24)
#   WHILE
#   SE EJECUTA EN REITERADAS OCACIONES
#   UNA ACCION HASTA QUE SE CUMPLA LA CONDICION LOGICA
#   

# valor = float(input("Ingrese valor: "))
# contador=0
# while contador < 10:
#     print(f" {contador} * {valor} = {contador*valor} ")
#     contador+=1

# else:
#     print(f"Los saltos fueron: {contador} ")
#---------------------------------------------------------------------------
#   BREAK 
#   SIRVE PARA EL CONTROL DE BUCLES

# contador=0
# while contador<=10:
#     contador=contador+1
#     if contador == 6:
#         print(f"Se rompe el bucle en el valor: {contador} ")
#         break
#     print(f"Valor: {contador} ")


#   CONTINUE
#   IDENTIFICAR VALOR Y SEGUIR
# print("-----------------------------------------------------------------")
# contador=0
# while contador<=10:
#     contador=contador+1
#     if contador == 6:
#         print(f"Se identifica valor y se sigue: {contador} ")
#         continue
#     print(f"Valor: {contador} ")
# else:
#     print(f"Las iteraciones: {contador} ")

# while True:
#     numeros=int(input("Ingrese valor: "))
#     if numeros % 2 == 0:
#         print(f"El numero {numeros}, es par ")
#         break
#     else:
#         print("Ingrese nuevamente..!!")

lista=[1,2,3,4,8,6,7]
indice=0
print(len(lista))
print("----------------")

while (indice < len(lista)):
    print(lista[indice])
    indice+=1

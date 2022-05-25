#   FUNCIONES RECURSIVAS
#   SE LLAMAN A SI MISMAS DURANTE LA EJECUCION

#   SIN RETORNO
#   CUENTA REGRESIVA
#   5,4,3,2,1 boom
def cuenta(num):
    num-=1
    if num>0:
        print(f"Valores iniciales: {num} ")
        cuenta(num)
    else:
        print("Boom!!")

cuenta(5)

#   CON RETORNO
#   FACTORIAL DE UN NUMERO
#   5!=1*2*3*4*5= 120

def factorial(num):
    if num>1:
        num=num*factorial(num-1)
    print(f"Valores finales: {num} ")
    return num

print(f"NUestra factorial es: {factorial(5)} ")

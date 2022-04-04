
mensaje=input("Ingrese mensaje: ")

print("------------------------------------------")
#   upper()  -> PARA MAYUSCULAS
print(f"En mayusculas es: {mensaje.upper()} ")

#   lower() -> PARA MINUSCULAS
print(f"En minusculas es: {mensaje.lower()} ")

#   capitalize()  -> PRIMERA EN MAYUSCULA   
print(f"Primera en mayuscula es: {mensaje.capitalize()} ")

#   title()  -> CADA INICIO DE PALABRA EN MAYUSCULA
print(f"Titulo es: {mensaje.title()} ")

#   swapcase()  -> INVIRTE CADA PALABRA
print(f"Palabras invertidas: {mensaje.swapcase()} ")

print("------------------------------------------")

mensaje2=input("Ingrese segundo mensaje: ")
numeroVeces = mensaje.count(mensaje2)
print(f"El numero de veces que se repite la palabra {mensaje2} es: {numeroVeces} ")
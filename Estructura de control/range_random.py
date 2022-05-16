import random

#   FUNCION RANDOM
#   GENERA VALORES ALEATORIOS
b=random.randint(1,10)
b1=random.randrange(10, 110)
# print(b1)

#   EJMPLO RANDOM
#   LANZAMIENTO DE MONEDA

# lista=["cara","sello"]
# opcion=random.choices(lista)

# if opcion == "cara":
#     print(f"Ah salido {opcion} ")
# elif opcion == "sello":
#     print(f"Ah salido {opcion} ")




#   FUNCION RANGE
#   PERMITE GENERAR LISTAS O TUPLAS

print(range(4))

a=list(range(0,20,2))
print(type(a))

a1="Hola Dev"
valor=tuple(range(len(a1)))
print(type(valor))


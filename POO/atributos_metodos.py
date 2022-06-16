#   ATRIBUTOS
#   CARACTERISTICAS DE UN OBJETO

#   ATRIBUTOS DINAMICOS
class Perro:
    pass

perro=Perro()
perro.nombre="Pepe"
perro.edad=3
print(f"Nombre: {perro.nombre}\nEdad: {perro.edad} ")
#   ATRIBUTOS DE CLASE
class Perro1:
    macho=False

perro1=Perro1()
if perro1.macho:
    print("Es macho")
else:
    print("No es macho")

#   METODOS
#   ACCIONES DE LOS OBJETOS
class Gato:

    def comer():
        print("El gato esta comiendo")
    
    def dormir():
        print("El gato esta durmiedo")

Gato.comer()
Gato.dormir()


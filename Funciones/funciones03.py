#   FUNCIONES INDETERMINADAS *args y **kwargs

#   *args

def argumentos(*args):
    return args

print(argumentos(4,'hola Dev',[1,2,3,4],11.1))

print("----------------------------")

def argumentos1(*args):
    for elemento in args:
        print(elemento)

argumentos1(4,'hola Dev',[1,2,3,4],11.1)

#   **kwargs

print("----------------------------")

def indetermindas(**kwargs):
    return kwargs
print(indetermindas(a=1,b=1.3,c='Hola Dev',d=[1,2,3,4]))

print("----------------------------")
def indetermindas1(**kwargs):
    for elementos in kwargs:
        print(kwargs[elementos])

indetermindas1(a=1,b=1.3,c='Hola Dev',d=[1,2,3,4])



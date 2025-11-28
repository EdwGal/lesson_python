#formateo de cadenas
name, surname, alias, age = "John", "Doe", "jdoe", 30
print(f"Nombre: {name}\nApellido: {surname}\nAlias: {alias}\nAge: {age}")
print("====================================")
print("hola" > "miercoles")
print('mi nombre es {} {} y mi edad es {}' .format(name, surname, age))
print('mi nombre es %s %s y mi edad es %d' % (name, surname, age))
#desempaquetado de caracteres
lista = ['Python', 'es', 'genial']
lista.insert(2, 145)
print(lista)
print(type(lista))
print('hello' == 'hello')

value = 2
for i in range(1,4):
    value += (i +value)
    print(value)

print(value)
for i in range(0,5):
    print(i)   

lista1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
rango = lista1.__len__()
print(rango)
for i in range(rango):
    print(lista1[i])
#genera un triangulo de asteriscos    
rows = 15
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
 
 #generar un rombo
rows = 9
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)

#generar n cuadrado
rows = 8
cols = 8
for i in range(rows):
    for j in range(cols):
        if ( i + j ) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

#trabajos con una tupla
my_tuple = tuple()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
#trabajos con set
my_set = set()
print(type(my_set))
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

########3
name = "Alice"
age = 28
print(f"my names is {name} and I am {age} years old.")

#######3
def is_even(n):
    return n % 2 == 0
print(is_even(4))  # True

lst = [10, 20, 30, 40, 50]
lst.reverse()
print(lst)  # [50, 40, 30, 20, 10

text= "python is fun"
print(text.capitalize())  # Python is fun
print(text.title())       # Python Is Fun

d= {"a":1}
print(d.get("b", 0))
print(d)# Not Found

lst =[1,2,3]
x = lst.pop(1)
print(x,lst)
print(lst)  # [1, 3]

x = 1_000
print(x)  # 1010
x = 1_000 + 10
print(x)  # 1
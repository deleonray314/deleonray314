#Estructuras de datos
#Litas
#Operaciones con listas
#Crear una lista
mi_lista = ['Rojo','Azul','Amarillo','Naranja','Violeta','Verde'] #Almacena un conjunto de datos de forma ordenada en lista
type(mi_lista) #Muestra el tipo de dato 
print(mi_lista) #Muestra el el contenido de la lista 
print(mi_lista[0]) #Se puede acceder a elemntos de la lista con un INDICE
print(mi_lista[0:2]) #El INDICE se puede delimitar a través de un rango 
print(mi_lista[:2]) #Al no incluir el primer valor se asume que inicia con el primer elemnto de la lista 
print(mi_lista[0:]) #Al no poner el segundo valor se asume que se trata de los elementos a partir del primero 
print(mi_lista.count('Rojo'))
mi_lista.append('Blanco') #Agrega un elemento al final de la lista
print(mi_lista)
mi_lista.insert(3,'Negro')#Agrega in elemento especificando el infice 
print(mi_lista)
mi_lista.extend(['Marron','Gris']) #Concatena una nueva lista a la lista original
print(mi_lista)
print(mi_lista.index('Azul')) #Encontrar el indice de un valor especifico
mi_lista.remove('Blanco')
print(mi_lista)
ultimo = mi_lista.pop() #mi_lista.pop() muestra el último elemento de la lista
print(ultimo) #Se declaró la variable "ultimo" y esta se definió mi_lista.pop()
#
#Ordenar una lista de Menor a Mayor 
lista = [1,4,3,6,8,2]
lista.sort() #Ordenó los datos de la lista de Menor a Mayor 
mi_lista.sort
print(mi_lista) #Esta funcion no tiene  efecto en datos típo str
#Ordenar una lista de mayor a menor 
lista = [1,4,3,6,8,2]
lista.reverse() #La funcion reverse nos muestra la lista en el orden opuesto al entregado
print(lista)
lista.sort(reverse=True) #lista.sort(reverse=True) esta sintaxis de código te permite organizar las listas de mayor a menor 
print(lista) #la expresión print(lista.sort(Reverse =True)) devolverá None
####
#Tuplas
# Convertir listas en tuplas
mi_tupla = tuple(mi_lista) #'Tuple' permite convertir una lista en una tupla
print(mi_tupla)
list(mi_tupla) #Mientras que la funcion list convierte una tupla en una lista 
print(mi_tupla[1]) #Para extraer un dato de la tupa se puede usar la misma sintaxis de las listas 
print('Rojo' in mi_tupla) # 'Rojo' in mi_tupla evalua si el elemento rojo se encuentra en la tupla 
print(mi_tupla.count('Rojo')) #mi_tupla.count('Rojo') Evalua cuantas veces está contenido el elemento dentro de la tupla
mi_tupla = 'Gaspar', 5, 8, 1999 # Empaquetado de una tupla
print(mi_tupla)
#El empaquetado consiste en la utilización de variables como elementos de una tupla.
#Ejemplo de empaquetado de tupla 
x=11
y=22
z= 'Henry'
mi_tupla=x,y,z
print(type(mi_tupla))
print(mi_tupla)
#El desempaquetado es asignar variables a cada uno de los elementos de la tupla 
#Ejempplo de desempaquetado de tupla 
Date = (22,'agosto',1999)
print(type(Date))
print(Date)
Uno, dos, tres = Date
print(Uno)
print(dos)
print(tres)
#Desempaquetado con guión bajo. Se usa guió bajo para reemplazar las posiciones de los elementos de la tupla que se desean ignorar 
#Y se asignan variables a los elementos que se quieren traer
Tuple_even = (1,3,5,7,9)
_,_,_, Cuarto, Quinto = Tuple_even
print(Cuarto)
print(Quinto)
####
#Diccionarios
#Es una estructura de datos que permite almacenar cualquier tipo de dato:
# Candenas de texto 'str' 
# Números enteros 'int'
# Decimales 'floats'
# Listas
# otros diccionarios
##
#Un dicionario tiene una organización de "clave" y "valor"
mi_diccionario = {  'Colores primarios' : ['rojo', 'Azul', 'Amarillo'], #Se crea un diccionario al abrir {}.
                    'Colores secundarios': ['Naranja','Violeta','Verde'], #Entre las {} se definen las claves y se declaran los valores separados por : así ---> 'Colores secundarios': ['Naranja','Violeta','Verde']
                    'Cavle3':10, #Las claves se separan una de las otras con , 
                    'Clave4':False}  
print(mi_diccionario['Colores secundarios']) # mi_diccionario['Colores secundarios'] imprime los datos contenidos en esa clave
mi_diccionario['Calave5'] = 'Otro ejemplo'
print(mi_diccionario) 
# del mi_diccionario['Clave4'] ---> Borrar una clave del diccionario
print(mi_diccionario) #Queremos el diccionario completo para seguir realizando validaciones 
# mi_diccionario['Clave3']=2  ---> Este punto se supone debe modificar el contenido de la clave pero, simplemente esta agregando una clave 3 adicional
print(mi_diccionario)
tupla_2 = ('Argentina', 'italia', 'Inglaterra') #Utilizar el indice de una tupla como clave de un diccionario
diccionario_2 = {
    tupla_2[0]:'Buenos Aires',
    tupla_2[1]:'Roma',
    tupla_2[2]:'Londres'
}
print(diccionario_2) # Poner un tupla dentro de un diccionario 
diccionario_3 = {
    'Clave1': 'Valor1', 'Clave2':(1,2,3,4,5)
}
print(diccionario_3)
print(diccionario_3.keys()) #Esta funcion muestra en pantalla las claves del diccionario 
print(mi_diccionario.keys())
print(mi_diccionario.values()) #Mestras los valores del diccionarios
print(len(mi_diccionario)) #Muestra la longitud del diccionario, es descir el número de claves que este tiene. 



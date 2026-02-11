#variables recordar la nomenclatura cammel case en este caso no se aplica y se usa la snake case
#en vez de separar con mayusculas, se usa el guion bajo 
myVariable = "Mi variable"
print(myVariable)
#esto está mal
my_variable = "Mi variable"
print(my_variable)
#esta nomenclatura es la mas comun para variables en python
my_bool_variable = True
print(my_bool_variable)
#Los argumentos varios que puedo pasarle a print se separan con una coma
print(myVariable, my_bool_variable, my_variable)
#Hay funciones que pueden cambiar el tipo de variables que les pasamos, así como print toma las
#variables y a bajo nivel las convierte en cadenas para mostrarlas, podemos hacer eso mismo pero con
#funciones
my_str_variable = str(my_bool_variable)
print(my_bool_variable)
print(my_bool_variable)
print(type(my_str_variable))
#intentar sacar el type a un print es encontrarse con un "NonType" aunque uno piense que transforma
#a string
print(len(my_str_variable))
my_variable_de_input = input()
print("La cantida de caracteres que posee la variable es: ", len(my_variable_de_input))
#cuenta la cantidad de caracteres de la variable que recibe
#Variables en una sola linea
nombre, apellido, alias, edad = "Matias", "Hita", "elperrohita", 35
print("me llamo:",nombre,"mi apellido es:", apellido,"me dicen:", alias,"y mi edad es:", edad)
#Inputs
nombre = input("como te llamas: ")
edad = input("que edad tenes: ")
print(nombre, edad)
#¿forzamos el tipo a la variable?
adress: str = "Mi dirección"
adress = 32
print(adress, type(adress))
name = "Matias Alfredo"
list_name = list(name)
print(list_name)
"""
#Algunas funciones para no perderlas con su descripción
# =====================================================
# PYTHON BUILT-IN FUNCTIONS — referencia rápida clara
# =====================================================

abs(x)            # devuelve el valor absoluto (sin signo)
all(iterable)     # True si TODOS los elementos son verdaderos
any(iterable)     # True si AL MENOS uno es verdadero
ascii(obj)        # representación texto escapando caracteres raros
bin(x)            # convierte entero a binario ('0b...')
bool(x)           # convierte a True o False según su valor
breakpoint()      # pausa el programa para depurar
bytearray()       # secuencia mutable de bytes
bytes()           # secuencia inmutable de bytes
callable(obj)     # True si el objeto se puede llamar como función
chr(i)            # número Unicode → carácter
classmethod()     # método que recibe la clase (cls) en vez de instancia
compile()         # compila código string a bytecode ejecutable
complex(a,b)      # crea número complejo (a + bi)

delattr(obj, a)   # elimina un atributo del objeto
dict()            # crea diccionario (clave → valor)
dir(obj)          # lista nombres de atributos y métodos
divmod(a, b)      # devuelve (cociente, resto)
enumerate(it)     # itera dando (índice, valor)
eval(code)        # evalúa expresión string y devuelve resultado
exec(code)        # ejecuta bloque de código dinámico
filter(f, it)     # deja solo elementos donde f(elem) es True
float(x)          # convierte a número decimal
format(x, fmt)    # formatea texto (decimales, alineación, etc.)
frozenset()       # conjunto inmutable (no se puede modificar)
getattr(obj, a)   # obtiene valor de un atributo por nombre
globals()         # diccionario con variables globales
hasattr(obj, a)   # True si el atributo existe

hash(obj)         # número hash (para sets/dicts)
help(obj)         # muestra documentación/ayuda
hex(x)            # entero → hexadecimal ('0x...')
id(obj)           # identificador único en memoria
input(msg)        # lee texto del usuario
int(x)            # convierte a entero
isinstance(x, t)  # True si x es instancia del tipo t
issubclass(a, b)  # True si clase a hereda de b
iter(obj)         # obtiene un iterador del objeto
len(obj)          # cantidad de elementos

list()            # crea lista mutable
locals()          # diccionario con variables locales
map(f, it)        # aplica función a cada elemento
max(it)           # mayor elemento
min(it)           # menor elemento

memoryview(obj)   # vista eficiente de datos binarios sin copiarlos
next(it)          # obtiene siguiente elemento del iterador
object()          # clase base de todos los objetos
oct(x)            # entero → octal ('0o...')
open(ruta)        # abre archivo para leer/escribir
ord(c)            # carácter → código Unicode
pow(a, b)         # potencia (a**b), también con módulo opcional
print()           # muestra texto en consola
property()        # crea atributos con getters/setters
range()           # secuencia de números para bucles
repr(obj)         # representación técnica del objeto (debug)
reversed(seq)     # iterador con orden invertido
round(x)          # redondea número
set()             # conjunto sin duplicados
setattr(obj,a,v)  # asigna valor a un atributo
slice()           # objeto para cortes (slicing avanzado)
sorted(it)        # devuelve iterable ordenado nuevo
staticmethod()    # método sin acceso a self ni cls
str(x)            # convierte a texto
sum(it)           # suma todos los elementos numéricos
super()           # acceso a métodos de la clase padre
tuple()           # crea tupla inmutable
type(obj)         # devuelve el tipo/clase del objeto
vars(obj)         # atributos del objeto como diccionario
zip(a,b,...)      # agrupa iterables por posición
__import__()      # importa módulos dinámicamente (uso interno)
"""
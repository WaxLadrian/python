#strings
my_string = "\\Se permiten variables \n con saltos de linea\n \t a ver la tabulacion"
print(my_string)
my_multi_line_string = """En teoría se pueden hacer
variables de tipo string con saltos de linea de esta forma
con tres comillas dobles
jeje"""
print(my_multi_line_string)
"""
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
Esas ultimas tres son para escribir esos caracteres y que no haga interferencia
con la syntaxis del idioma
"""
lista_a_imprimir = ["la", "gorda", "trola", "de","mi","jermu",5]
my_contatenation_by_format = "Quien se la come? %s" %(lista_a_imprimir) 
print(my_contatenation_by_format)
#los procentajes junto al tipo de variable me sirven para controlar que imprimimos por pantalla
#cosas con sentido
name, last_name, age = "matias", "hita", 24
my_format_string = "me llamo {} mi apellido es {} y mi edad es {} ".format(name,last_name,age)
print(my_format_string)
#Es mejor format para la ejecucion, velocidad y recursos
#inferencia de datos, es mejor poner la f de format delante y los nombres dentro de las llaves
my_format_string = f"me llamo {name} mi apellido es {last_name} y mi edad es {age} "
print(my_format_string)
#desempaquetado de caracteres
""" esto da error para que sea correcto debemos crear tantas variables como caracteres tenga nuestra
variable madre "lenguaje"
lenguaje = "python"
a,b = lenguaje
print(a)
print(b)
"""
lenguaje = "python"
a,b,c,d,e,f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
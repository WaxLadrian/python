"""
# =========================================
# OPERADORES DE ASIGNACIÓN EN PYTHON
# =========================================
# Asignación básica
x = 5          # Asigna 5 a x
# Suma y asigna
x += 3         # x = x + 3
# Resta y asigna
x -= 3         # x = x - 3
# Multiplica y asigna
x *= 3         # x = x * 3
# Divide y asigna (división normal)
x /= 3         # x = x / 3
# Módulo y asigna (resto)
x %= 3         # x = x % 3
# División entera y asigna
x //= 3        # x = x // 3
# Potencia y asigna
x **= 3        # x = x ** 3
# AND bit a bit y asigna
x &= 3         # x = x & 3
# OR bit a bit y asigna
x |= 3         # x = x | 3
# XOR bit a bit y asigna
x ^= 3         # x = x ^ 3
# Desplazamiento a la derecha y asigna
x >>= 3        # x = x >> 3
# Desplazamiento a la izquierda y asigna
x <<= 3        # x = x << 3
x//y            Division entera aproxima la division al entero mas cercano
"""
"""
# =========================================
# OPERADORES DE COMPARACIÓN EN PYTHON
# =========================================
# Igual a
x == y      # True si x es igual a y
# Distinto de
x != y      # True si x es diferente de y
# Mayor que
x > y       # True si x es mayor que y
# Menor que
x < y       # True si x es menor que y
# Mayor o igual que
x >= y      # True si x es mayor o igual que y
# Menor o igual que
x <= y      # True si x es menor o igual que y
is: Returns true if both variables are the same object(x is y)
is not: Returns true if both variables are not the same object(x is not y)
in: Returns True if the queried list contains a certain item(x in y)
not in: Returns True if the queried list doesn't have a certain item(x not in y)
"""
print(3+3, 3-3, 3*3, 3**3)
x = 10

x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
print("hola mundo"+ str(5)) #esto da error y se puede arreglar con comillas o str()
print("hola mundo " * 2)
x=3
x &= 8
print(x,type(x))
x=4
print(3!=x)
print(3<=2)
print(3>=3)
print("hola"=="Hola") #ordenación alfabetica del ASCII cuando uso comparadores con letras
print((3<4) and (2==2))
#poca cosa sinceramente

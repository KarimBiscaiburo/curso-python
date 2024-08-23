# Tipos de datos Simples

# String
"string"
'string'

# Asi no funcion
# "Cadena
# de texto
# "

"""
    Cadena de
    texto
"""
40 # Int
40.2 # Float

True
False


# Tipos de datos Compuestos

# Listas

lista = ["Martin", True, 34]
print(lista[0])
# La lista se puede modificar
lista[0] = "Carlos"

# Tuplas 

tupla = ("Martin", True, 34, "Martin")
print(tupla[0])
# Cuando lo ejecutemos nos va a dar error porque no se pueden modificar
tupla[0] = "Carlos"


# Conjuntos
# No se puede acceder mediante indices, no se puede repetir valores y al igual que las tuplas, no se pueden moficar los elementos

conjunto = {"Martin", True, 34}


# Diccionario

diccionario = {
    "nombre": "Martin",
    "edad": 15,
    "Argentino": True
}

print(diccionario["nombre"])
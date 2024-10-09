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

# Listas (No se pueden crear listas vacias sin usar "list")

lista = ["Martin", True, 34]
print(lista[0])
# La lista se puede modificar
lista[0] = "Carlos"

lista2 = list()

# Tuplas (No se pueden crear tuplas vacios sin usar "tuple")

tupla = ("Martin", True, 34, "Martin")
print(tupla[0])
# Cuando lo ejecutemos nos va a dar error porque no se pueden modificar
tupla[0] = "Carlos"

otraTupla = tuple(["Otra", "tupla"])
print(type(otraTupla))

otraOtraTupla = "dato1", "dato2"

print(type(otraOtraTupla))

tuplaDeUnDato = "dato1",

print(type(tuplaDeUnDato))

tupla2 = tuple()


# Conjuntos
# No se puede acceder mediante indices, no se puede repetir valores y al igual que las tuplas, no se pueden moficar los elementos

conjunto = {"Martin", True, 34}


# Diccionario (No se pueden crear dicionarios vacios sin usar "dict")

diccionario = {
    "nombre": "Martin",
    "edad": 15,
    "Argentino": True
}

print(diccionario["nombre"])
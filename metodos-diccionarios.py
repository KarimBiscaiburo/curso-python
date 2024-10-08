diccionario = {
    "nombre": "Martin",
    "edad": 15,
    "Argentino": True
}

# KEYS - Devuelve las claves (Se puede iterar las claves)
print(diccionario.keys())

# GET - Devuelve el valor de una clave
print(diccionario.get("nombre"))

# POP - Elimina un elemento
diccionario.pop("nombre")
print(diccionario)

# ITEMS - Iterar el diccionario
print(diccionario.items())

# CLEAR - Elimina todos los elementos
diccionario.clear()
print(diccionario)
# LIST - Crea una lista
lista = list(["karim", 2, True])
lista2 = list()
lista3 = ["martin", 3, False]

print(lista)
print(lista2)
print(lista3)

# LEN - Cuenta la cantidad de elementos de una lista 
print(len(lista3))

# APPEND - Agrega un elemento a la lista
lista.append("Fulano")
print(lista)

# INSERT - Agrega un elemento a la lista en el indice especificado
lista.insert(2, "Otro dato")
print(lista)

# EXTEND - Agrega varios elementos a la lista
lista.extend(["Uno mas", "y otro mas"])
print(lista)

# POP - Elimina un elemento de una lista, pide indice y devuelve el valor eliminado
algo = lista.pop(2)
lista.pop(0) #Elimina el primer elemento
lista.pop(-1) #Elimina el ultimo elemento
lista.pop(-2) #Elimina el anteultimo elemento

print(lista)
print(algo)

# REMOVE - Remueve un elemento de una lista, pide valor
lista.remove(2) # Remueve el elemento que sea igual a 2
print(lista)

# CLEAR - Elimina todos los elementos de una lista
lista.clear()
print(lista)

# SORT - Ordena una lista de forma ascendente a descendente (solo si es numerica)
otraLista = [1,6,2,3,8,12,9,0]
otraLista.sort()
print(otraLista)

# Ordenar de manera descendente a ascendente
otraLista.sort(reverse=True)
print(otraLista)

# REVERSE - Invierte los elementos de una lista
lista2 = ["a", True, False, 3]
lista2.reverse()
print(lista2)
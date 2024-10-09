diccionario = dict(nombre="Krim", apellido="Biscaiburo")
print(diccionario)

# Crear un diccionario con todos los valores "None"
diccionario2 = dict.fromkeys(["nombre", "apellido"])
print(diccionario2)

# En realidad esto lo que hace es crear un diccionario y asignarle el mismo valor a cada elemento, ya que el primer parametro es un valor iterable y el segundo parametro es el valor que se le va a asignar a cada key (que por defecto es "None")
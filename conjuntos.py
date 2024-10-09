conjunto2 = set(["Martin", True, 34])

# Como meter un conjunto dentro de otro conjunto
conjunto3 = frozenset(["dato1", "dato2"])
conjunto4 = {conjunto3, "dato3"}

#Teoria de conjuntos

# Verificar si es un subconjunto
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}

resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

# Verificar si es un superconjunto

resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

# Verificar si hay un numero en comun (si solo un numero igual devuelve false, ya que verifica si son distintos)
resultado = conjunto2.isdisjoint(conjunto1)
# DIR - Devuelve la lista de atributos validos del objeto pasado
cadena1 = "Hola como estas"
print(dir(cadena1))

# UPPER - Convierte a mayusculas
print(cadena1.upper())

# LOWER - Convierte a minusculas
print(cadena1.lower())

# CAPITALIZE - Primera en mayuscula
print(cadena1.capitalize())

# FIND - Encuentra la primera aparicion del valor especificado, sino devuelve -1
print(cadena1.find("z"))

# INDEX - Encuentra la primera aparicion del valor especificado, sino devuelve una excepcion
print(cadena1.index("om"))

# ISNUMERIC - Si es numerico devuelve true
print(cadena1.isnumeric())
print("1".isnumeric())

# ISALPHA - Si es alfa numerico devuelve true (Los caracteres especiales no los tiene en cuenta, incluido el " ")
print("1".isalnum())

# COUNT - Devuelve el numero de ocurrencias de una subcadena en la cadena dada
print(cadena1.count("o"))

# LEN - Cuenta los caracteres de una cadena
print(len(cadena1))

# ENDSWITH - Verifica si una cadena termina con
print(cadena1.endswith("s"))

# STARTSWITH - Verifica si una cadena empieza con
print(cadena1.startswith("h"))

# REPLACE - Remplaza un valor por otro
print(cadena1.replace("o", "a"))

# SPLIT - Separa por el parametro dado
print(cadena1.split(" "))

# Pedir al usuario que ingrese el ciclo for
for_loop = input("Ingrese el ciclo for: ")

# Eliminar espacios innecesarios
for_loop = " ".join(for_loop.split())

# Analizar la sintaxis del ciclo for para extraer las partes necesarias
parts = for_loop.split("(")[1].split(")")[0].split(";")

# Crear la expresión while a partir de las partes extraídas
while_loop = "while (" + parts[0] + ") {\n" + parts[1] + ";\n" + parts[2] + "\n}"

# Mostrar el ciclo while resultante al usuario
print("El ciclo while equivalente es:\n")
print(while_loop)

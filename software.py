# Pedir al usuario que ingrese el código del bucle for
for_code = input("Ingrese el código del bucle for: ")

# Eliminar los caracteres no deseados del código del bucle for
for_code = for_code.replace("(", "").replace(")", "").replace("{", "").replace("}", "").strip()

# Extraer la variable y el rango del bucle for
var, range_str = "", ""
if "int " in for_code:
    _, var, range_str = for_code.split(" ")
    var = var.strip()
else:
    var, range_str = for_code.split(";")[0], for_code.split(";")[1]
var = var.strip()

# Extraer los límites del rango del bucle for
range_start, range_end, range_inc = "", "", ""
for s in range_str.split(";"):
    s = s.strip()
    if s.startswith(var):
        range_start = s.split("=")[1].strip()
    elif s.startswith("<"):
        range_end = s.split("<")[1].strip()
    elif s.startswith(range_end + "+"):
        range_inc = s.split("+")[1].strip()
if range_start == "" or range_end == "":
    print("Error: no se pudo encontrar el rango del bucle for")
    exit()

# Convertir los límites del rango a números enteros
range_start = int(eval(range_start))
range_end = int(eval(range_end))
if range_inc == "":
    range_inc = 1
else:
    range_inc = int(eval(range_inc))

# Generar el código equivalente del bucle while
while_code = "{0} = {1}\nwhile {0} < {2}:\n    {3}\n    {0} += {4}".format(var, range_start, range_end, for_code.split(";", 2)[2].strip(), range_inc)

# Imprimir el código equivalente del bucle while
print("El equivalente del bu")
print(while_code)
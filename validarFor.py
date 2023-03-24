def validar_arreglo(arreglo):
    if len(arreglo) < 7:
        return False
    if arreglo[0] != 'f' or arreglo[1] != 'o' or arreglo[2] != 'r' or arreglo[3] != '(':
        return False
    i = 4
    while arreglo[i] != ';':
        if i >= len(arreglo) - 1:
            return False
        i += 1
    i += 1
    while arreglo[i] != ';':
        if i >= len(arreglo) - 1:
            return False
        i += 1
    i += 1
    while arreglo[i] != ')':
        if i >= len(arreglo) - 1:
            return False
        i += 1
    if arreglo[i+1] != '{' or arreglo[-1] != '}':
        return False
    return True

arreglo_valido_1 = ['f', 'o', 'r', '(', 'i', '=', '1', ';', 'i', '<', '=', '1', '2', ';', 'i', '+', '+', ')', '{', '}']
arreglo_valido_2 = ['f', 'o', 'r', '(', 'j', '=', '0', ';', 'j', '<', '=', '9', ';', 'j', '+', '=', '2', ')', '{', '}']
arreglo_invalido_1 = ['f', 'o', 'r', '(', 'i', '=', '1', ',', 'i', '<', '=', '1', '2', ')', '{', '}']
arreglo_invalido_2 = ['f', 'o', 'r', '(', 'j', '=', '0', ';', 'j', '<', '=', '9', ';', 'j', '+', '=', '2', ')', '(']

print(validar_arreglo(arreglo_valido_1))   # Debe imprimir True
print(validar_arreglo(arreglo_valido_2))   # Debe imprimir True
print(validar_arreglo(arreglo_invalido_1)) # Debe imprimir False
print(validar_arreglo(arreglo_invalido_2)) # Debe imprimir False

def turing_machine(arr):
    state = 0
    current = 0

    while True:
        symbol = arr[current]

        if state == 0:
            if symbol == ' ':
                state = 1
            else:
                current += 1
        elif state == 1:
            if symbol == ' ':
                arr.pop(current)
            else:
                state = 0
                current += 1

        if current == len(arr):
            break

    return arr
cinta1 = []
#a = turing_machine(a)
#print(a)
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
def extraer_datos(arreglo):
    datos_for = []
    datos_otro = []
    i = 0
    while i < len(arreglo):
        if arreglo[i] == 'f' and arreglo[i+1] == 'o' and arreglo[i+2] == 'r' and arreglo[i+3] == '(':
            i += 4
            datos_temp = []
            while arreglo[i] != ')':
                if arreglo[i] == ';' or arreglo[i] == '{':
                    datos_for.append(''.join(datos_temp))
                    datos_temp = []
                else:
                    datos_temp.append(arreglo[i])
                i += 1
            if datos_temp:
                datos_for.append(''.join(datos_temp))
            if '{' in arreglo[i:]:
                inicio = arreglo.index('{', i) + 1
                fin = arreglo.index('}', inicio)
                datos_for.append(''.join(arreglo[inicio:fin]))
                i = fin + 1
            else:
                i += 1
        else:
            datos_temp = []
            while i < len(arreglo) and arreglo[i] != ';':
                datos_temp.append(arreglo[i])
                i += 1
            datos_otro.append(''.join(datos_temp))
            i += 1
    return datos_for, datos_otro

def rellenar_cinta2():
    expresion_for = input("Hola por favor ingresa la expresión for para transformarla a while \n Ejemplo: for(i=1;i<=10;i++) \n")
    for caracter in expresion_for:
        cinta1.append(caracter)
   # cinta1.append("B")
    print(cinta1)
    print()
    cinta = turing_machine(cinta1)
    print(cinta)
    print(validar_arreglo(cinta))
    datos_for, datos_otro = extraer_datos(cinta)
    print(datos_for)
    print(datos_otro)
    

   
def main():
    rellenar_cinta2()
   
main()
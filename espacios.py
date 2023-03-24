import tkinter as tk
k = [0, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '<', '>', '=', '+', '-']

root = tk.Tk()
root.title("Turing Machine")
root.geometry("400x400")

trancision = [
    [['q0','f','q1'],['q0','f','q1','D','D','S']],
    [['q1','o','q2'],['B','(','(','D','D']],
    [['q2','r','q3'],['D',';','B','D','S']],
    [['q3','(','q4'],['E','B',';','S','S']],
    [['q4','k','q5'],['F','while',')','D','D']],
    [['q5',')','q6'],['B','{','B','D','S']],
    [['q6','{','q7'],['B','{','B','D','S']],
    [['q7','}','q8'],['B','{','B','D','S']],
    [['q8',' ','q9'],['B','{','B','D','S']],
    [['q9',';','q10'],['B','{','B','D','S']],
    [['q4','1','q4'],['C','2','2','D','D']],
    [['q4','2','q4'],['C','3','3','D','D']],
    [['q4','3','q4'],['C','4','4','D','D']],
    [['q4','4','q4'],['C','5','5','D','D']],
    [['q4','5','q4'],['C','6','6','D','D']],
    [['q4','6','q4'],['C','7','7','D','D']],
    [['q4','7','q4'],['C','8','8','D','D']],
    [['q4','8','q4'],['C','9','9','D','D']],

]


def turing_machine(arr):
    state = 0
    current = 0

    while True:
        symbol = arr[current]
        
        if state == 0:
            if symbol == trancision[8][0][1]:
                state = 1
            else:
                current += 1
        elif state == 1:
            if symbol == trancision[8][0][1]:
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
    print(trancision[7][0][1])
    if len(arreglo) < 7:
        return False
    if arreglo[0] != trancision[0][0][1] or arreglo[1] != trancision[1][0][1] or arreglo[2] != trancision[2][0][1] or arreglo[3] != trancision[3][0][1]:
        return False
    i = 4
    while arreglo[i] != trancision[9][0][1]:
        if i >= len(arreglo) - 1:
            return False
        i += 1
    i += 1
    while arreglo[i] != trancision[9][0][1]:
        if i >= len(arreglo) - 1:
            return False
        i += 1
    i += 1
    while arreglo[i] != trancision[5][0][1]:
        if i >= len(arreglo) - 1:
            return False
        i += 1
    if arreglo[i+1] != trancision[6][0][1] or arreglo[-1] != trancision[7][0][1]:
        return False
    return True
def extraer_datos(arreglo):
    datos_for = []
    datos_otro = []
    i = 0
    while i < len(arreglo):
        if arreglo[i] == trancision[0][0][1] and arreglo[i+1] == trancision[1][0][1] and arreglo[i+2] == trancision[2][0][1] and arreglo[i+3] == trancision[3][0][1]:
            i += 4
            datos_temp = []
            while arreglo[i] != trancision[5][0][1]:
                if arreglo[i] == trancision[9][0][1] or arreglo[i] ==  trancision[6][0][1]:
                    datos_for.append(''.join(datos_temp))
                    datos_temp = []
                else:
                    datos_temp.append(arreglo[i])
                i += 1
            if datos_temp:
                datos_for.append(''.join(datos_temp))
            if trancision[6][0][1] in arreglo[i:]:
                inicio = arreglo.index(trancision[6][0][1], i) + 1
                fin = arreglo.index(trancision[7][0][1], inicio)
                datos_for.append(''.join(arreglo[inicio:fin]))
                i = fin + 1
            else:
                i += 1
        else:
            datos_temp = []
            while i < len(arreglo) and arreglo[i] != trancision[9][0][1]:
                datos_temp.append(arreglo[i])
                i += 1
            datos_otro.append(''.join(datos_temp))
            i += 1
    return datos_for, datos_otro

def rellenar_cinta2():
    expresion_for1 = expresion_for.get()
    for caracter in expresion_for1:
        cinta1.append(caracter)
   # cinta1.append("B")
    print(cinta1)
    print()
    cinta = turing_machine(cinta1)
    print(cinta)
    print(validar_arreglo(cinta))
    datos_for = extraer_datos(cinta)
    print(datos_for)
    print()
    while_loop = "" + datos_for[0][0] + ";\n" "while (" + datos_for[0][1] + ") {""\n" + datos_for[0][3] + "" "\n" +datos_for[0][2]+ "\n}"
   # print(while_loop)
    result_label.config(text=while_loop)
    result_label.pack()
    separador_label.config(text="--------------------------------")
    separador_label.pack()
    do_while_ = "" + datos_for[0][0] + ";\n" "if (" + datos_for[0][1] + ") {""\n" "do{ ""\n" + datos_for[0][3] + "" "\n" +datos_for[0][2]+ "\n }while(" + datos_for[0][1] + ");}"
   # print(while_loop)
    do_while.config(text=do_while_)
    do_while.pack()
   
def main():
  
   
    print(cinta1)
    print()
    cinta = turing_machine(cinta1)
    print(cinta)
    print(validar_arreglo(cinta))
    datos_for = extraer_datos(cinta)
    print(datos_for) 
    print()
    
   # while_loop = "" + datos_for[0][0] + ";\n" "while (" + datos_for[0][1] + ") {""\n" + datos_for[0][3] + "" "\n" +datos_for[0][2]+ "\n}"
    #print(while_loop)
    #result_label.config(text=while_loop)
    #result_label.pack()
    
    
root.title("Transformador de for a while")
label = tk.Label(root, text="Por favor ingresa la expresión for ")
label.pack()
expresion_for = tk.Entry(root)
expresion_for.pack()

convert_button = tk.Button(root, text="Convertir", command=rellenar_cinta2)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()
separador_label = tk.Label(root, text="")
separador_label.pack()
do_while = tk.Label(root, text="")
do_while.pack()
root.mainloop()
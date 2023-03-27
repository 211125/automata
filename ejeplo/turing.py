import tkinter as tk
from random import choice
# Crear la ventana principal de archivo1
root1 = tk.Tk()
root1.title("Archivo 1")
root1.title("Turing Machine")
root1.geometry("400x400")
# Crear el botón para mostrar la interfaz de archivo3
button = tk.Button(root1, text="preguntas", command=lambda: show_interface(root1))
button.pack()

trancision = [
    [['q0','f','q1'],['q0','f','','D','D','S']],
    [['q1','o','q2'],['q2','o','o','D','D']],
    [['q2','r','q3'],['q3','r','r','D','S']],
    [['q3','(','q4'],['q4','B','B','S','S']],
    [['q4','k','q5'],['q5','k','k','D','D']],
    [['q5',')','q6'],['q6',')',')','D','S']],
    [['q6','{','q7'],['q7','{','{','D','S']],
    [['q7','}','q8'],['q8','}','}','D','S']],
    [['q8',' ','q9'],['q9',' ','B','D','S']],
    [['q9',';','q10'],['q10',';','B','D','S']],
    [['q4','1','q4'],['q4','1','1','D','D']],
    [['q4','2','q4'],['q4','2','2','D','D']],
    [['q4','3','q4'],['q4','3','3','D','D']],
    [['q4','4','q4'],['q4','4','4','D','D']],
    [['q4','5','q4'],['q4','5','5','D','D']],
    [['q4','6','q4'],['q4','6','6','D','D']],
    [['q4','7','q4'],['q4','7','7','D','D']],
    [['q4','8','q4'],['q4','8','8','D','D']],
    [['q4','9','q4'],['q4','9','9','D','D']],   
     [['q4','a','q4'],['q4','a','a','D','D']],
    [['q4','b','q4'],['q4','b','b','D','D']],
    [['q4','c','q4'],['q4','c','c','D','D']],
    [['q4','d','q4'],['q4','d','d','D','D']],
    [['q4','e','q4'],['q4','e','e','D','D']],
    [['q4','f','q4'],['q4','f','f','D','D']],
    [['q4','g','q4'],['q4','g','g','D','D']],
    [['q4','h','q4'],['q4','h','h','D','D']],
    [['q4','i','q4'],['q4','i','i','D','D']],
    [['q4','j','q4'],['q4','j','j','D','D']],
    [['q4','k','q4'],['q4','k','k','D','D']],
    [['q4','l','q4'],['q4','l','l','D','D']],
    [['q4','m','q4'],['q4','m','m','D','D']],
    [['q4','n','q4'],['q4','n','n','D','D']],
    [['q4','o','q4'],['q4','o','o','D','D']],
    [['q4','p','q4'],['q4','p','p','D','D']],
    [['q4','q','q4'],['q4','q','q','D','D']],
    [['q4','r','q4'],['q4','r','r','D','D']],
    [['q4','s','q4'],['q4','s','s','D','D']],
    [['q4','t','q4'],['q4','t','t','D','D']],
    [['q4','u','q4'],['q4','u','u','D','D']],
    [['q4','v','q4'],['q4','v','v','D','D']],
    [['q4','w','q4'],['q4','w','w','D','D']],
    [['q4','x','q4'],['q4','x','x','D','D']],
    [['q4','y','q4'],['q4','y','y','D','D']],
    [['q4','z','q4'],['q4','z','z','D','D']],
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
        else:
             
              for1.config(text="no comple con la sintaxis de for en c++")
              for1.pack()
              return False;
              
   # print(while_loop)
             
    return datos_for, datos_otro

def rellenar_cinta2():
    expresion_for1 = expresion_for.get()
    for caracter in expresion_for1:
        cinta1.append(caracter)
   # cinta1.append("B")
   # print(cinta1)
    print()
    cinta = turing_machine(cinta1)
    #print(cinta)
    print(validar_arreglo(cinta))
    datos_for = extraer_datos(cinta)
    #print(datos_for)
    print()
    while_loop = "" + datos_for[0][0] + "; while (" + datos_for[0][1] + ") { " +datos_for[0][3]+ " " +datos_for[0][2]+ "}"
   # print(while_loop)
    result_label.config(text=while_loop)
    result_label.pack()
    separador_label.config(text="--------------------------------")
    separador_label.pack()
    do_while_ = "" + datos_for[0][0] + "; if (" + datos_for[0][1] + ") { ""do{" +datos_for[0][3]+ "" +datos_for[0][2]+ " }while(" + datos_for[0][1] + ");}"
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
    
    
root1.title("Transformador de for a while")
label = tk.Label(root1, text="Por favor ingresa la expresión for ")
label.pack()
expresion_for = tk.Entry(root1)
expresion_for.pack()

convert_button = tk.Button(root1, text="Convertir", command=rellenar_cinta2)
convert_button.pack()

result_label = tk.Label(root1, text="")
result_label.pack()
separador_label = tk.Label(root1, text="")
separador_label.pack()
do_while = tk.Label(root1, text="")
do_while.pack()
for1 = tk.Label(root1, text="")
for1.pack()

# Crear la función que muestra la interfaz de archivo3
def show_interface(root):
    # Ocultar la ventana actual
    root.withdraw()
    
    # Crear la ventana principal de archivo3
    root3 = tk.Tk()

    
    # Crear el botón para volver a la interfaz de archivo1
    button_back = tk.Button(root3, text="convertidor", command=lambda: back_to_interface(root3))
    button_back.pack()
# Definimos una lista con varios ejemplos de for, while y do while con errores en C++
   
# Ejemplos de conversiones correctas
    correct_conversions = [
        ("for (int i = 0; i < 10; i++) {\n    cout << i << endl;\n}", "si"),
        ("while (i < 10) {\n    cout << i << endl;\n    i++;\n}", "si"),
        ("int i = 1;\nif(i>=10){\ndo {\n      i++;\n} while (i<=10);}", "si"),
        ("int i = 0;\nwhile (i < 10) {\n    cout << 'Hola' << endl;\n    i++;\n}", "si")
    ]

    # Ejemplos de conversiones incorrectas
    incorrect_conversions = [
        ("fors (i = 0; i < 10; i++) {\n    cout << i << endl;\n}", "no"),
        ("while i < 10 {\n    cout << i << endl;\n    i++;\n}", "no"),
        ("int i = 0;\ndo {\n    cout << 'Hola' << endl;\n    i++;\n} while (i < 10);", "no"),
        ("int i = 0;\nwhile () {\n    cout << 'Hola' << endl;\n    i++;\n}", "no")
    ]

    # Función para elegir una conversión aleatoria
    def choose_conversion():
        conversion = choice(correct_conversions + incorrect_conversions)
        return conversion

    # Función para verificar la respuesta del usuario
    def check_answer(answer, correct_answer):
        if answer == correct_answer:
            result_label.config(text="Correcto!")
        else:
            result_label.config(text="Incorrecto.")

    # Función para mostrar una nueva conversión
    def new_conversion():
        conversion = choose_conversion()
        code_label.config(text=conversion[0])
        correct_answer = conversion[1]
        yes_button.config(command=lambda: check_answer("si", correct_answer))
        no_button.config(command=lambda: check_answer("no", correct_answer))
        result_label.config(text="")

    # Crear la ventana principal
 
    root3.title("Conversión de ciclos")

    # Crear los widgets
    title_label = tk.Label(root3, text="¿Es esta conversión correcta?")
    code_label = tk.Label(root3, text="")
    yes_button = tk.Button(root3, text="Si")
    no_button = tk.Button(root3, text="No")
    new_button = tk.Button(root3, text="Nueva conversión", command=new_conversion)
    result_label = tk.Label(root3, text="")

    # Colocar los widgets en la ventana
    title_label.pack(side="top", pady=10)
    code_label.pack(side="top", padx=10, pady=10)
    yes_button.pack(side="left", padx=10, pady=10)
    no_button.pack(side="right", padx=10, pady=10)
    new_button.pack(side="bottom", pady=10)
    result_label.pack(side="bottom", pady=10)

    # Mostrar la primera conversión
    new_conversion()




    # Mostrar la ventana de archivo3
    root3.mainloop()

    # Función para volver a la interfaz de archivo1
def back_to_interface(root):
    # Cerrar la ventana actual
    root.destroy()
    
    # Mostrar la ventana de archivo1
    root1.deiconify()

# Mostrar la ventana de archivo1
root1.mainloop()
 
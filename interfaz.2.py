import tkinter as tk
from random import choice

# Ejemplos de conversiones correctas
correct_conversions = [
    ("for (int i = 0; i < 10; i++) {\n    cout << i << endl;\n}", "si"),
    ("while (i < 10) {\n    cout << i << endl;\n    i++;\n}", "si"),
    ("int i = 1;\nif(i>=10){\ndo {\n      i++;\n} while (i<=10);}", "si"),
    ("int i = 0;\nwhile (i < 10) {\n    cout << 'Hola' << endl;\n    i++;\n}", "si")
]

# Ejemplos de conversiones incorrectas
incorrect_conversions = [
    ("for (i = 0; i < 10; i++) {\n    cout << i << endl;\n}", "no"),
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
root = tk.Tk()
root.title("Conversión de ciclos")

# Crear los widgets
title_label = tk.Label(root, text="¿Es esta conversión correcta?")
code_label = tk.Label(root, text="")
yes_button = tk.Button(root, text="Si")
no_button = tk.Button(root, text="No")
new_button = tk.Button(root, text="Nueva conversión", command=new_conversion)
result_label = tk.Label(root, text="")

# Colocar los widgets en la ventana
title_label.pack(side="top", pady=10)
code_label.pack(side="top", padx=10, pady=10)
yes_button.pack(side="left", padx=10, pady=10)
no_button.pack(side="right", padx=10, pady=10)
new_button.pack(side="bottom", pady=10)
result_label.pack(side="bottom", pady=10)

# Mostrar la primera conversión
new_conversion()

# Iniciar el bucle de eventos
root.mainloop()

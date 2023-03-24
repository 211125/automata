import random
import tkinter as tk

# Definimos una lista con varios ejemplos de for, while y do while con errores en C++
ejemplos = [
    "for (int i = 0; i < 10; i++) {\n    cout << i << endl;\n}",  # Sintaxis correcta
    "for (i = 0; i < 10; i++)\n    cout << i << endl;",  # Falta declarar la variable i
    "while (true) {\n    cout << 'Hola' << endl;\n}",  # Bucle infinito
    "do {\n    cout << 'Hola' << endl;\n} while (true);",  # Bucle infinito
]

# Función que selecciona aleatoriamente un ejemplo y lo muestra en la interfaz
def mostrar_ejemplo():
    ejemplo = random.choice(ejemplos)
    ejemplo_label.config(text=ejemplo)
    resultado_label.config(text="")

# Función que se llama cuando el usuario presiona uno de los botones
def verificar_respuesta(respuesta):
    ejemplo = ejemplo_label.cget("text")
    if respuesta == "si":
        if "for" in ejemplo:
            if "int" in ejemplo:
                resultado_label.config(text="Correcto")
            else:
                resultado_label.config(text="Incorrecto")
        elif "while" in ejemplo:
            resultado_label.config(text="Correcto")
        elif "do" in ejemplo:
            resultado_label.config(text="Correcto")
    elif respuesta == "no":
        if "for" in ejemplo:
            if "int" in ejemplo:
                resultado_label.config(text="Incorrecto")
            else:
                resultado_label.config(text="Correcto")
        elif "while" in ejemplo:
            resultado_label.config(text="Incorrecto")
        elif "do" in ejemplo:
            resultado_label.config(text="Incorrecto")

# Creamos la interfaz gráfica
root = tk.Tk()
root.title("Ejemplos de bucles en C++")

# Creamos los widgets necesarios
ejemplo_label = tk.Label(root, text="")
ejemplo_label.pack(pady=10)

si_button = tk.Button(root, text="Si", command=lambda: verificar_respuesta("si"))
no_button = tk.Button(root, text="No", command=lambda: verificar_respuesta("no"))
si_button.pack(side=tk.LEFT, padx=10)
no_button.pack(side=tk.RIGHT, padx=10)

resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=10)

nueva_conversión_button = tk.Button(root, text="Nueva conversión", command=mostrar_ejemplo)
nueva_conversión_button.pack(pady=10)

mostrar_ejemplo()

# Iniciamos el bucle principal de la interfaz
root.mainloop()

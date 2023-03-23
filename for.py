import tkinter as tk

def convert_for_to_while():
    # Obtener la entrada del usuario
    for_loop = for_entry.get()

    # Dividir la entrada en sus componentes
    for_parts = for_loop.split()
    

    # Extraer los valores relevantes para el bucle while
    variable = for_parts[1]
    start_value = for_parts[3]
    end_value = for_parts[5]

    # Crear la cadena del bucle while en C++
    while_loop = f" {variable} = {start_value};\nwhile ({variable} < {end_value}) {{\n\t// código a ejecutar en cada iteración\n\t{variable}++;\n}}"

    # Mostrar el bucle while resultante en la ventana
    result_label.config(text=while_loop)

# Crear la ventana principal
root = tk.Tk()
root.title("Convertir for a while")

# Crear el campo de entrada y la etiqueta correspondiente
for_label = tk.Label(root, text="Ingresa el bucle 'for' que quieres convertir a 'while':")
for_label.pack()
for_entry = tk.Entry(root)
for_entry.pack()

# Crear el botón para convertir el bucle
convert_button = tk.Button(root, text="Convertir", command=convert_for_to_while)
convert_button.pack()

# Crear la etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
result_label.pack()

# Ejecutar la ventana
root.mainloop()

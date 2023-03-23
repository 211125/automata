import random
import tkinter as tk
from tkinter import ttk

# Lista de conversiones posibles
conversions = [
    "for (int i = 0; i < n; i++) { ... }",
    "for (int i = 1; i <= n; i++) { ... }",
    "for (int i = n; i > 0; i--) { ... }",
    "while (i < n) { ... } do { ... } while (i < n);",
    "while (i <= n) { ... } do { ... } while (i <= n);",
    "while (i >= 0) { ... } do { ... } while (i >= 0);",
    "while (i > 0) { ... } do { ... } while (i > 0);"
]

# Función para verificar la respuesta del usuario
def verificar_respuesta(respuesta_usuario):
    respuesta_correcta = conversion == "for (int i = 0; i < n; i++) { ... }"
    if respuesta_usuario == respuesta_correcta:
        resultado_label.config(text="¡Correcto! Has seleccionado la conversión correcta.", foreground="green")
    else:
        resultado_label.config(text="Lo siento, esa no es la conversión correcta.", foreground="red")
        conversion_correcta_label.config(text=f"La conversión correcta es: {conversion}", foreground="gray25")

# Función para mostrar una nueva conversión al usuario
def mostrar_nueva_conversion():
    # Seleccione una conversión al azar
    global conversion
    conversion = random.choice(conversions)
    conversion_label.config(text=f"Conversión: {conversion}", foreground="white")
    resultado_label.config(text="")
    conversion_correcta_label.config(text="", foreground="white")

# Crea una ventana
ventana = tk.Tk()
ventana.title("Convertidor de For/While a Do-While")
ventana.geometry("400x250")
ventana.configure(bg="#292929")

# Crea estilo CSS para los botones
s = ttk.Style()
s.configure("Custom.TButton", foreground="black", background="#009900", font=("Arial", 12))


# Crea widgets
conversion_label = tk.Label(ventana, text="", font=("Arial", 12), fg="white", bg="#292929")
conversion_correcta_label = tk.Label(ventana, text="", font=("Arial", 12), fg="black")
resultado_label = tk.Label(ventana, text="", font=("Arial", 12), bg="#292929")
si_boton = ttk.Button(ventana, text="Sí", style="Custom.TButton", command=lambda: verificar_respuesta(True))
no_boton = ttk.Button(ventana, text="No", style="Custom.TButton", command=lambda: verificar_respuesta(False))
nueva_conversion_boton = ttk.Button(ventana, text="Nueva conversión", style="Custom.TButton", command=mostrar_nueva_conversion)

# Coloca widgets en la ventana
conversion_label.pack(pady=10)
conversion_correcta_label.pack(pady=10)
resultado_label.pack(pady=10)
botones_frame = tk.Frame(ventana, bg="#292929")
botones_frame.pack(pady=20)
si_boton.pack(side="left", padx=10)
no_boton.pack(side="left", padx=10)
nueva_conversion_boton.pack()

# Mostrar la primera conversión al usuario
mostrar_nueva_conversion()

# Ejec
ventana.mainloop()
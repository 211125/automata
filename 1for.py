import random
import tkinter as tk

# Lista de conversiones posibles
conversions = [
    "int i = 0; while (i < n) { ... }",
    "int i = 1; while (i <= n) { ... }",
    "int i = n - 1; while (i >= 0) { ... }",
    "int i = n; while (i-- > 0) { ... }"
]

# Función para verificar la respuesta del usuario
def verificar_respuesta(respuesta_usuario):
    respuesta_correcta = conversion == "int i = 0; for (int i = 0; i < n; i++) { ... }"
    if respuesta_usuario == respuesta_correcta:
        resultado_label.config(text="¡Correcto! Has seleccionado la conversión correcta.")
    else:
        resultado_label.config(text="Lo siento, esa no es la conversión correcta.")
        conversion_correcta_label.config(text=f"La conversión correcta es: {conversion}")

# Función para mostrar una nueva conversión al usuario
def mostrar_nueva_conversion():
    # Seleccione una conversión al azar
    global conversion
    conversion = random.choice(conversions)
    conversion_label.config(text=f"Conversión: {conversion}")
    resultado_label.config(text="")
    conversion_correcta_label.config(text="")

# Crea una ventana
ventana = tk.Tk()
ventana.title("Convertidor de For a While")
ventana.geometry("400x250")

# Crea widgets
conversion_label = tk.Label(ventana, text="")
conversion_correcta_label = tk.Label(ventana, text="")
resultado_label = tk.Label(ventana, text="")
si_boton = tk.Button(ventana, text="Sí", command=lambda: verificar_respuesta(True))
no_boton = tk.Button(ventana, text="No", command=lambda: verificar_respuesta(False))
nueva_conversion_boton = tk.Button(ventana, text="Nueva conversión", command=mostrar_nueva_conversion)

# Coloca widgets en la ventana
conversion_label.pack(pady=10)
conversion_correcta_label.pack(pady=10)
resultado_label.pack(pady=10)
si_boton.pack(side="left", padx=10)
no_boton.pack(side="left", padx=10)
nueva_conversion_boton.pack(pady=20)

# Mostrar la primera conversión al usuario
mostrar_nueva_conversion()

# Ejecuta la ventana
ventana.mainloop()

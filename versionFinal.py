
import tkinter as tk

ventana = tk.Tk()
ventana.title("Transformación de for a while")
ventana.geometry("500x500")
ventana.configure(background="cyan")

#Creamos un título
titulo = tk.Label(ventana, text="Transformación de for a while", bg="black", fg="white", font=("Arial", 18))
titulo.pack()

# Creamos una etiqueta
etiqueta1 = tk.Label(ventana, text="Por favor ingresa la expresión for para transformarla a while", bg="cyan", font=("Arial", 16))
etiqueta1.pack(pady=10)

# Creamos una caja de texto
caja_texto = tk.Entry(ventana, font=("Arial", 16))
caja_texto.pack(pady=10)

# Creamos un botón
boton = tk.Button(ventana, text="Transformar", command=rellenar_cinta2, font=("Arial", 16))
boton.pack(pady=10)

# Creamos una etiqueta
etiqueta2 = tk.Label(ventana, text="Resultado", bg="cyan", font=("Arial", 16))
etiqueta2.pack(pady=10)

# Creamos una caja de resultado
caja_resultado = tk.Entry(ventana, font=("Arial", 16))
caja_resultado.pack(pady=10)

ventana.mainloop()
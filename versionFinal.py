import tkinter as tk

# Definir la ventana
root = tk.Tk()
root.title("Turing Machine")
root.geometry("400x400")

# Definir los widgets
input_label = tk.Label(root, text="Input:")
input_entry = tk.Entry(root)
output_label = tk.Label(root, text="Output:")
output_text = tk.Text(root)
run_button = tk.Button(root, text="Run")

# Ubicar los widgets en la ventana
input_label.pack()
input_entry.pack()
output_label.pack()
output_text.pack()
run_button.pack()

# Ejecutar la ventana
root.mainloop()

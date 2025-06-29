import tkinter as tk
from tkinter import messagebox

class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None

    def verificar_edad(self, edad):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        self.edad = edad

    def imprimir(self):
        return f"Nombre del vendedor: {self.nombre}\nApellidos del vendedor: {self.apellidos}\nEdad del vendedor: {self.edad}"

# Función para crear y mostrar el vendedor
def crear_vendedor():
    try:
        nombre = entrada_nombre.get()
        apellidos = entrada_apellidos.get()
        edad = int(entrada_edad.get())

        vendedor = Vendedor(nombre, apellidos)
        vendedor.verificar_edad(edad)
        resultado = vendedor.imprimir()
        salida.config(state='normal')
        salida.delete(1.0, tk.END)
        salida.insert(tk.END, resultado)
        salida.config(state='disabled')

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Registro de Vendedor")
ventana.geometry("400x350")

tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Apellidos:").pack()
entrada_apellidos = tk.Entry(ventana)
entrada_apellidos.pack()

tk.Label(ventana, text="Edad:").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

tk.Button(ventana, text="Crear Vendedor", command=crear_vendedor).pack(pady=10)

tk.Label(ventana, text="Resultado:").pack()
salida = tk.Text(ventana, height=5, width=45, state='disabled')
salida.pack()

ventana.mainloop()

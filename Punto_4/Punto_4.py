import tkinter as tk
from tkinter import messagebox

class Programador:
    def __init__(self, nombre, apellidos):
        if not nombre.isalpha() or not apellidos.isalpha():
            raise ValueError("Nombre y apellidos deben contener solo letras.")
        if len(nombre) >= 20 or len(apellidos) >= 20:
            raise ValueError("Nombre y apellidos deben tener menos de 20 caracteres.")
        self.nombre = nombre
        self.apellidos = apellidos

class Equipo:
    def __init__(self, nombre_equipo, universidad, lenguaje, tamano):
        if not (2 <= tamano <= 3):
            raise ValueError("El tamaño del equipo debe ser entre 2 y 3.")
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano = tamano
        self.programadores = []

    def esta_completo(self):
        return len(self.programadores) == self.tamano

    def agregar_programador(self, nombre, apellidos):
        if self.esta_completo():
            raise Exception("El equipo ya está completo.")
        nuevo = Programador(nombre, apellidos)
        self.programadores.append(nuevo)

class InterfazEquipo:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Equipo de Programación")

        self.etiquetas = ["Nombre del equipo", "Universidad", "Lenguaje", "Tamaño (2-3)", "Nombre del programador", "Apellidos del programador"]
        self.entradas = []

        for idx, texto in enumerate(self.etiquetas):
            label = tk.Label(root, text=texto)
            label.grid(row=idx, column=0)
            entry = tk.Entry(root)
            entry.grid(row=idx, column=1)
            self.entradas.append(entry)

        self.boton_crear = tk.Button(root, text="Crear equipo", command=self.crear_equipo)
        self.boton_crear.grid(row=4, column=0, columnspan=2, pady=10)

        self.boton_agregar = tk.Button(root, text="Agregar programador", command=self.agregar_programador, state=tk.DISABLED)
        self.boton_agregar.grid(row=7, column=0, columnspan=2)

        self.resultado = tk.Label(root, text="")
        self.resultado.grid(row=8, column=0, columnspan=2)

        self.equipo = None

    def crear_equipo(self):
        try:
            nombre_equipo = self.entradas[0].get()
            universidad = self.entradas[1].get()
            lenguaje = self.entradas[2].get()
            tamano = int(self.entradas[3].get())
            self.equipo = Equipo(nombre_equipo, universidad, lenguaje, tamano)
            self.resultado.config(text="Equipo creado con éxito.")
            self.boton_agregar.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def agregar_programador(self):
        if not self.equipo:
            return
        try:
            nombre = self.entradas[4].get()
            apellidos = self.entradas[5].get()
            self.equipo.agregar_programador(nombre, apellidos)
            if self.equipo.esta_completo():
                self.resultado.config(text="Equipo completo con éxito.")
                self.boton_agregar.config(state=tk.DISABLED)
            else:
                self.resultado.config(text=f"Programador añadido. Faltan {self.equipo.tamano - len(self.equipo.programadores)}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazEquipo(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
import math

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular el logaritmo.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular la raíz cuadrada.")
        return math.sqrt(valor)

# Interfaz gráfica
def main():
    def calcular():
        try:
            valor = float(entrada.get())
            resultado_log = CalculosNumericos.calcular_logaritmo_neperiano(valor)
            resultado_raiz = CalculosNumericos.calcular_raiz_cuadrada(valor)
            messagebox.showinfo("Resultados", 
                f"Logaritmo Neperiano: {resultado_log:.4f}\nRaíz Cuadrada: {resultado_raiz:.4f}")
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un valor numérico.")
        except ArithmeticError as e:
            messagebox.showerror("Error aritmético", str(e))

    ventana = tk.Tk()
    ventana.title("Cálculos Numéricos")

    tk.Label(ventana, text="Ingrese un número:").pack(padx=10, pady=5)
    entrada = tk.Entry(ventana)
    entrada.pack(padx=10, pady=5)

    boton = tk.Button(ventana, text="Calcular", command=calcular)
    boton.pack(padx=10, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()

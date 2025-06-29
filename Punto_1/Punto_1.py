import tkinter as tk
from tkinter import scrolledtext

def ejecutar_programa():
    salida.delete(1.0, tk.END)

    # Primer try
    try:
        salida.insert(tk.END, "Ingresando al primer try\n")
        resultado = 10000 / 0
        salida.insert(tk.END, "Después de la división\n")
    except ZeroDivisionError:
        salida.insert(tk.END, "División por cero\n")
    finally:
        salida.insert(tk.END, "Ingresando al primer finally\n")

    # Segundo try
    try:
        salida.insert(tk.END, "Ingresando al segundo try\n")
        objeto = None
        objeto.to_string()
        salida.insert(tk.END, "Imprimiendo objeto\n")
    except ZeroDivisionError:
        salida.insert(tk.END, "División por cero\n")
    except Exception:
        salida.insert(tk.END, "Ocurrió una excepción\n")
    finally:
        salida.insert(tk.END, "Ingresando al segundo finally\n")

# Ventana principal
ventana = tk.Tk()
ventana.title("PruebaExcepciones")
ventana.geometry("550x320")

# Botón arriba
btn = tk.Button(ventana, text="Ejecutar programa", font=("Arial", 12), command=ejecutar_programa)
btn.pack(pady=8)

# Área de texto debajo
salida = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, font=("Consolas", 12))
salida.pack(padx=10, pady=5, expand=True, fill="both")

ventana.mainloop()

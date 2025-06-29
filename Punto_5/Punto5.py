import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

def abrir_archivo():
    archivo_path = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]
    )

    if archivo_path:
        try:
            with open(archivo_path, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                texto_area.delete("1.0", tk.END)  # Borra contenido previo
                texto_area.insert(tk.END, contenido)  # Muestra nuevo contenido
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo:\n{e}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lector de Archivos de Texto")
ventana.geometry("600x400")

# Botón para abrir archivo
boton_abrir = tk.Button(ventana, text="Abrir archivo .txt", command=abrir_archivo)
boton_abrir.pack(pady=10)

# Área de texto con scroll
texto_area = ScrolledText(ventana, wrap=tk.WORD, width=70, height=20)
texto_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Ejecutar la ventana
ventana.mainloop()

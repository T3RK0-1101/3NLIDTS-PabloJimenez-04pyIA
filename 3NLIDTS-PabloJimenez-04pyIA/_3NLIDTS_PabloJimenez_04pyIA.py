import tkinter as tk
from tkinter import messagebox, ttk
import os

# Definicion de funciones
FILE_PATH = "datos.txt" 

def limpiar_campos():
    """Limpia todos los campos de entrada y resetea los radio buttons."""
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)
    tbNombre.focus_set()

def validar_datos():
    """Valida los datos de entrada antes de guardarlos."""
    campos_obligatorios = [tbNombre.get(), tbApellidos.get(), tbEdad.get(), tbEstatura.get(), tbTelefono.get()]

    if any(campo == "" for campo in campos_obligatorios):
        messagebox.showwarning("Campos vacios", "Por favor, rellene todos los campos.")
        return False
    
    if var_genero.get() not in [1, 2]:
        messagebox.showwarning("Genero no seleccionado", "Por favor, seleccione un genero (Hombre o Mujer).")
        return False

    try:
        int(tbEdad.get())
        float(tbEstatura.get())
    except ValueError:
        messagebox.showerror("Datos incorrectos", "La Edad y la Estatura deben ser valores numericos validos.")
        return False
        
    return True

def guardar_valores():
    """Obtiene, valida y guarda los datos del formulario en un archivo."""
    if not validar_datos():
        return

    nombres = tbNombre.get().strip()
    apellidos = tbApellidos.get().strip()
    edad = tbEdad.get().strip()
    estatura = tbEstatura.get().strip()
    telefono = tbTelefono.get().strip()
    
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    
    datos = (
        f"Nombres: {nombres}\n"
        f"Apellidos: {apellidos}\n"
        f"Edad: {edad} anios\n"
        f"Estatura: {estatura} m\n"
        f"Telefono: {telefono}\n"
        f"Genero: {genero}\n"
    )
    
    try:
        with open(FILE_PATH, "a") as archivo:
            archivo.write(datos + "\n")
        
        messagebox.showinfo("Informacion", "Datos guardados con exito:\n\n" + datos)
        
    except IOError as e:
        messagebox.showerror("Error de archivo", f"No se pudo guardar el archivo: {e}")
    finally:
        limpiar_campos()

# Diseno de la interfaz de usuario
ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("400x480")
ventana.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

ventana.configure(bg="#f0f0f0")
style.configure("TLabel", font=("Arial", 10), background="#f0f0f0", foreground="#333333")
style.configure("TEntry", font=("Arial", 10))
style.configure("TRadiobutton", font=("Arial", 10), background="#f0f0f0", foreground="#333333")
style.configure("TButton", font=("Arial", 10, "bold"), background="#4CAF50", foreground="white",
                padding=5, relief="flat")
style.map("TButton", background=[("active", "#45a049")])

main_frame = ttk.Frame(ventana, padding="20 20 20 20", style="TFrame")
main_frame.pack(expand=True, fill="both")

main_frame.columnconfigure(1, weight=1)

var_genero = tk.IntVar(value=0)

row_idx = 0

ttk.Label(main_frame, text="Nombres:").grid(row=row_idx, column=0, sticky="w", pady=5)
tbNombre = ttk.Entry(main_frame)
tbNombre.grid(row=row_idx, column=1, sticky="ew", pady=5)
row_idx += 1

ttk.Label(main_frame, text="Apellidos:").grid(row=row_idx, column=0, sticky="w", pady=5)
tbApellidos = ttk.Entry(main_frame)
tbApellidos.grid(row=row_idx, column=1, sticky="ew", pady=5)
row_idx += 1

ttk.Label(main_frame, text="Telefono:").grid(row=row_idx, column=0, sticky="w", pady=5)
tbTelefono = ttk.Entry(main_frame)
tbTelefono.grid(row=row_idx, column=1, sticky="ew", pady=5)
row_idx += 1

ttk.Label(main_frame, text="Edad:").grid(row=row_idx, column=0, sticky="w", pady=5)
tbEdad = ttk.Entry(main_frame)
tbEdad.grid(row=row_idx, column=1, sticky="ew", pady=5)
row_idx += 1

ttk.Label(main_frame, text="Estatura (m):").grid(row=row_idx, column=0, sticky="w", pady=5)
tbEstatura = ttk.Entry(main_frame)
tbEstatura.grid(row=row_idx, column=1, sticky="ew", pady=5)
row_idx += 1

ttk.Label(main_frame, text="Genero:").grid(row=row_idx, column=0, sticky="nw", pady=10)
gender_frame = ttk.Frame(main_frame, style="TFrame")
gender_frame.grid(row=row_idx, column=1, sticky="ew", pady=10)
ttk.Radiobutton(gender_frame, text="Hombre", variable=var_genero, value=1).pack(anchor="w")
ttk.Radiobutton(gender_frame, text="Mujer", variable=var_genero, value=2).pack(anchor="w")
row_idx += 1

ttk.Label(main_frame, text="", background="#f0f0f0").grid(row=row_idx, column=0, columnspan=2, pady=10) 
row_idx += 1

button_frame = ttk.Frame(main_frame, style="TFrame")
button_frame.grid(row=row_idx, column=0, columnspan=2, pady=10)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

btnBorrar = ttk.Button(button_frame, text="Borrar", command=limpiar_campos, style="TButton")
btnBorrar.grid(row=0, column=0, padx=5, sticky="ew")

btnGuardar = ttk.Button(button_frame, text="Guardar", command=guardar_valores, style="TButton")
btnGuardar.grid(row=0, column=1, padx=5, sticky="ew")

# Ejecucion de ventana
ventana.mainloop()
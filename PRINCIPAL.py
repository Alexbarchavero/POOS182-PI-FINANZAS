from tkinter import messagebox
import tkinter as tk
import sqlite3

# Función que agrega una transacción a la lista de transacciones y la guarda en la base de datos
def agregar_transaccion():
    # Obtener la información de la transacción ingresada por el usuario
    categoria = categoria_var.get()
    tipo = tipo_var.get()
    descripcion = descripcion_entry.get()
    monto = monto_entry.get()
    
    if (descripcion=="" or monto==""):
        messagebox.showwarning("Advertencia!","Faltan datos!")
    else:
        # Agregar la transacción a la lista de transacciones
        transacciones_listbox.insert(tk.END, f'{categoria} - {tipo} - {descripcion} - {monto}')

        # Guardar la transacción en la base de datos
        conn = sqlite3.connect('C:/Users/Alejandro/Documents/GitHub/POOS182-PI-FINANZAS/database.db')
        c = conn.cursor()
        c.execute("INSERT INTO tbRegistros(categoria, tipo, descripcion, monto) VALUES (?, ?, ?, ?)", (categoria, tipo, descripcion, monto))
        conn.commit()
        conn.close()
        messagebox.showinfo("Exito!","Registro completo!")

    # Limpiar los campos de entrada
    descripcion_entry.delete(0, tk.END)
    monto_entry.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Registro de Transacciones')
ventana.geometry("400x300")

# Crear los widgets de la ventana
categoria_label = tk.Label(ventana, text='Categoría:')
categoria_var = tk.StringVar()
categoria_var.set('Ingreso')
categoria_optionmenu = tk.OptionMenu(ventana, categoria_var, 'Ingreso', 'Gasto', 'Compra', 'Venta', 'Pago')
tipo_label = tk.Label(ventana, text='Tipo:')
tipo_var = tk.StringVar()
tipo_var.set('Efectivo')
tipo_optionmenu = tk.OptionMenu(ventana, tipo_var, 'Efectivo', 'Tarjeta de Crédito', 'Tarjeta de Débito')
descripcion_label = tk.Label(ventana, text='Descripción:')
descripcion_entry = tk.Entry(ventana)
monto_label = tk.Label(ventana, text='Monto:')
monto_entry = tk.Entry(ventana)
agregar_button = tk.Button(ventana, text='Agregar Transacción', command=agregar_transaccion)
transacciones_label = tk.Label(ventana, text='Transacciones:')
transacciones_listbox = tk.Listbox(ventana)

# Colocar los widgets en la ventana
categoria_label.grid(row=0, column=0)
categoria_optionmenu.grid(row=0, column=1)
tipo_label.grid(row=1, column=0)
tipo_optionmenu.grid(row=1, column=1)
descripcion_label.grid(row=2, column=0)
descripcion_entry.grid(row=2, column=1)
monto_label.grid(row=3, column=0)
monto_entry.grid(row=3, column=1)
agregar_button.grid(row=4, column=1)
transacciones_label.grid(row=5, column=0)
transacciones_listbox.grid(row=6, column=1, columnspan=2)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
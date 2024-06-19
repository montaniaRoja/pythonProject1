import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='ofloda01',
                                     database='productos')
c = connection.cursor()

root = Tk()
root.title('Productos')

icon = tk.PhotoImage(master=root, file='images/iconoprincipal.png')
root.geometry('1100x450')
root.wm_iconphoto(True, icon)
root.configure(background='#bdc3c7')

main_frame = tk.Frame(root)
main_frame.pack()
frame = tk.Frame(main_frame, bg='#922B21')
frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
frameFields = tk.Frame(frame, bg='#EDBB99')
frameFields.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
frameSearch = tk.Frame(frame, bg='#F5B7B1')
frameSearch.grid(row=0, column=2)
frameTrv = tk.Frame(frame, bg='#D7BDE2')
frameTrv.grid(row=1, column=2)

frameBtn = tk.Frame(frame, bg='#85929E')
frameBtn.grid(row=3, column=0)

frameNavBtns = tk.Frame(frame, bg='#D6EAF8')
frameNavBtns.grid(row=3, column=2, columnspan=2, padx=20, pady=20)

# Configuración de columnas para que se expandan uniformemente
frameFields.grid_columnconfigure(0, weight=1)
frameFields.grid_columnconfigure(1, weight=2)

# Labels y Entries
idLabel = tk.Label(frameFields, text="Id", font=('Times New Roman', 12), bg='#bdc3c7')
idEntry = tk.Entry(frameFields)
idLabel.grid(row=0, column=0, sticky='e', padx=5, pady=5)
idEntry.grid(row=0, column=1, sticky='w', padx=5, pady=5, ipadx=50)

nameLabel = tk.Label(frameFields, text="Nombre", font=('Times New Roman', 12), bg='#bdc3c7')
nameEntry = tk.Entry(frameFields)
nameLabel.grid(row=1, column=0, sticky='e', padx=5, pady=5)
nameEntry.grid(row=1, column=1, sticky='w', padx=5, pady=5, ipadx=50)

categorias = ['Mobiles', 'Abarrotes', 'Medicamentos']
selected = StringVar(root)
catLabel = tk.Label(frameFields, text="Categoria", font=('Times New Roman', 12), bg='#bdc3c7')
catCombo = ttk.Combobox(frameFields, textvariable=selected, values=categorias)
catLabel.grid(row=2, column=0, sticky='e', padx=5, pady=5)
catCombo.grid(row=2, column=1, sticky='w', padx=5, pady=5, ipadx=50)
selected.set(categorias[0])

qtyLabel = tk.Label(frameFields, text="Cantidad", font=('Times New Roman', 12), bg='#bdc3c7')
qtyEntry = tk.Entry(frameFields)
qtyLabel.grid(row=3, column=0, sticky='e', padx=5, pady=5)
qtyEntry.grid(row=3, column=1, sticky='w', padx=5, pady=5, ipadx=50)

priceLabel = tk.Label(frameFields, text="Precio", font=('Times New Roman', 12), bg='#bdc3c7')
priceEntry = tk.Entry(frameFields)
priceLabel.grid(row=4, column=0, sticky='e', padx=5, pady=5)
priceEntry.grid(row=4, column=1, sticky='w', padx=5, pady=5, ipadx=50)

photoLabel = tk.Label(frameFields, text="Imagen", font=('Times New Roman', 12), bg='#bdc3c7')
photoEntry = tk.Entry(frameFields)
photoLabel.grid(row=5, column=0, sticky='e', padx=5, pady=5)
photoEntry.grid(row=5, column=1, sticky='w', padx=5, pady=5, ipadx=50)

displayPhotoLabel = tk.Label(frameFields)
btnBrowsePhoto = tk.Button(frameFields, text="Seleccione Imagen")
displayPhotoLabel.grid(row=7, column=0, sticky='w', padx=5, pady=5)
btnBrowsePhoto.grid(row=7, column=1, columnspan=2, sticky='w')

searchLabel = tk.Label(frameSearch, text="Buscar por nombre")
searchEntry = tk.Entry(frameSearch)
btnNameSearch = tk.Button(frameSearch, text="Buscar")
searchLabel.grid(row=0, column=0)
searchEntry.grid(row=0, column=1)
btnNameSearch.grid(row=0, column=3)

trv = ttk.Treeview(frameTrv, columns=(1, 2, 3, 4, 5, 6), show='headings')
trv.column(1, anchor=CENTER, width=100)
trv.column(2, anchor=CENTER, width=100)
trv.column(3, anchor=CENTER, width=100)
trv.column(4, anchor=CENTER, width=100)
trv.column(5, anchor=CENTER, width=100)
trv.column(6, anchor=CENTER, width=100)

trv.heading(1, text="id")
trv.heading(2, text="Nombre")
trv.heading(3, text="Categoria")
trv.heading(4, text="Cantidad")
trv.heading(5, text="Precio")
trv.heading(6, text="Imagen")

trv.grid(row=0, column=0, rowspan=2, columnspan=3)

btnAdd = tk.Button(frameBtn, text="Agregar")
btnAdd.grid(row=1, column=0, padx=5, pady=5)
btnEdit = tk.Button(frameBtn, text="Editar")
btnEdit.grid(row=1, column=1, padx=5, pady=5)
btnDelete = tk.Button(frameBtn, text="Borrar")
btnDelete.grid(row=1, column=2, padx=5, pady=5)
btnSearch = tk.Button(frameBtn, text="Buscar")
btnSearch.grid(row=1, column=3, padx=5, pady=5)
btnClear = tk.Button(frameBtn, text="Limpiar")
btnClear.grid(row=1, column=4, padx=5, pady=5)

# Nav buttons
btnFirst = tk.Button(frameNavBtns, text="<<")
btnFirst.grid(row=1, column=0)
btnRwd = tk.Button(frameNavBtns, text="<")
btnRwd.grid(row=1, column=1)
btnFwd = tk.Button(frameNavBtns, text=">")
btnFwd.grid(row=1, column=2)
btnLast = tk.Button(frameNavBtns, text=">>")
btnLast.grid(row=1, column=3)


def add():
    nombre = nameEntry.get()
    categoria = catCombo.get()
    cantidad = qtyEntry.get()
    precio = priceEntry.get()
    pic = photoEntry.get()
    print(nombre, categoria, cantidad, precio, pic)
    # Consulta de inserción
    insert_query = "INSERT INTO tbl_productos (nombre, categoria, cantidad, precio, imagen) VALUES (%s, %s, %s, %s, %s)"

    # Valores a insertar (suponiendo que tienes las variables nombre, categoria, cantidad, precio y pic definidas previamente)
    values = (nombre, categoria, cantidad, precio, pic)

    # Ejecutar la consulta
    c.execute(insert_query, values)

    # Confirmar la transacción (guardar los cambios en la base de datos)
    connection.commit()

    # Cerrar cursor y conexión
    c.close()
    connection.close()


btnAdd['command'] = add


def edit():
    pass


def searchbyid():
    pass


def remove():
    pass


def searchbyname():
    pass


def gofirst():
    pass


def golast():
    pass


def gonext():
    pass


def goprev():
    pass


def selectphoto():
    global img
    filename = filedialog.askopenfilename(initialdir='/images', title='Select Photo',
                                          filetypes=(('png images', '*.png'), ('jpg images', '*.jpg')))
    if filename:
        img = Image.open(filename)
        img = img.resize((100, 100), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        displayPhotoLabel.config(image=img)
        displayPhotoLabel.image = img  # Guardar referencia para evitar que el GC elimine la imagen
        photoEntry.delete(0, END)
        photoEntry.insert(0, filename)


btnBrowsePhoto.config(command=selectphoto)

root.mainloop()

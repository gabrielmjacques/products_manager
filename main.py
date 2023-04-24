from tkinter import *
from tkinter import ttk

import database

conn = database.DBConnect()

root = Tk()
root.title('Product Manager')

# Frame para botões
buttons_frame = Frame(root, padx=10)
buttons_frame.grid(column=0, row=0)

add_btn = ttk.Button(buttons_frame, text='Adicionar')
add_btn['command'] = lambda: database.AddProduct(conn, treeview)
add_btn.grid(column=0, row=0)

alt_btn = ttk.Button(buttons_frame, text='Alterar')
alt_btn.grid(column=0, row=1)

rem_btn = ttk.Button(buttons_frame, text='Remover')
rem_btn['command'] = lambda: database.RemProduct(conn, treeview)
rem_btn.grid(column=0, row=2)


# Frame da Treeview
treeview_frame = Frame(root, padx=10)
treeview_frame.grid(column=1, row=0)

treeview = ttk.Treeview(treeview_frame, columns=('col1', 'col2', 'col3'))
treeview.grid(column=0, row=0)

treeview.heading('#0', text='')
treeview.column('#0', width=0, stretch=False)

treeview.heading('#1', text='ID')
treeview.heading('#2', text='Produto')
treeview.heading('#3', text='Estoque')

database.ReloadTreeview(conn, treeview)


root.mainloop()
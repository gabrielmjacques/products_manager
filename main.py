from tkinter import *
from tkinter import ttk

import database

conn = database.DBConnect()

root = Tk()
root.configure(background='#09456c')
root.title('Product Manager')

import style

# Frame para botões
buttons_frame = Frame(root)
buttons_frame.grid(column=0, row=0)

add_btn = ttk.Button(buttons_frame, text='Adicionar')
add_btn['command'] = lambda: database.AddProduct(conn, treeview)
add_btn.grid(column=0, row=0)

alt_btn = ttk.Button(buttons_frame, text='Alterar')
alt_btn['command'] = lambda: database.AltProduct(conn, treeview)
alt_btn.grid(column=0, row=1)

rem_btn = ttk.Button(buttons_frame, text='Remover')
rem_btn['command'] = lambda: database.RemProduct(conn, treeview)
rem_btn.grid(column=0, row=2)


# Frame da Treeview
treeview_frame = Frame(root)
treeview_frame.grid(column=1, row=0)

treeview = ttk.Treeview(treeview_frame, columns=('col1', 'col2', 'col3'))
treeview.grid(column=0, row=0)

treeview.heading('#0', text='')
treeview.column('#0', width=0, stretch=False)

treeview.heading('#1', text='ID')
treeview.column('#1', width=50, anchor='center')

treeview.heading('#2', text='Produto')
treeview.column('#2', width=300, anchor='center')

treeview.heading('#3', text='Estoque')
treeview.column('#3', width=70, anchor='center')

database.ReloadTreeview(conn, treeview)


root.mainloop()
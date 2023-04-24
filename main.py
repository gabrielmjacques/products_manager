from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Product Manager')

# Frame para botões
buttons_frame = Frame(root, padx=10)
buttons_frame.grid(column=0, row=0)

add_btn = ttk.Button(buttons_frame, text='Adicionar')
add_btn.grid(column=0, row=0)

alt_btn = ttk.Button(buttons_frame, text='Alterar')
alt_btn.grid(column=0, row=1)

rem_btn = ttk.Button(buttons_frame, text='Remover')
rem_btn.grid(column=0, row=2)


# Frame da Treeview
treeview_frame = Frame(root, padx=10)
treeview_frame.grid(column=1, row=0)

treeview = ttk.Treeview(treeview_frame, columns=('col1', 'col2'))
treeview.grid(column=0, row=0)

treeview.heading('#0', text='ID')
treeview.heading('#1', text='Produto')
treeview.heading('#2', text='Estoque')


root.mainloop()
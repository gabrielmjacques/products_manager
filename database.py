from tkinter import *
from tkinter import ttk
from configparser import ConfigParser
import mysql.connector

configparser = ConfigParser()
configparser.read('db_config.ini')

bg_color = '#D7DAF0'

def DBConnect():
    try:
        connector = mysql.connector.connect(
            host = configparser.get('database', 'host'),
            user = configparser.get('database', 'user'),
            password = configparser.get('database', 'password'),
            database = configparser.get('database', 'database'),
        )
        
        print('Connected')
        return connector
        
    except Exception as e:
        print('Err: ', e)

def GetTreeviewItem(treeview, data):
    selected = treeview.focus()
    item_data = treeview.item(selected)
    
    if data == 'id':
        return item_data['values'][0]
    
    elif data == 'name':
        return item_data['values'][1]
    
    elif data == 'stock':
        return item_data['values'][2]

def ReloadTreeview(conn, treeview):
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM products;')
    data = cursor.fetchall()
    
    treeview.delete(*treeview.get_children())
    
    for prod in data:
        treeview.insert('', 'end', values=(prod))

def AddProduct(conn, treeview):
    def Add():
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO products (product_name, product_stock) VALUES ("{prodname_var.get()}", {int(prodstock_var.get())})')
        conn.commit()
        
        ReloadTreeview(conn, treeview)
        
        window.destroy()
    
    window = Toplevel(bg=bg_color, padx=50, pady=30)
    
    prodname_label = ttk.Label(window, text='Nome do Produto')
    prodname_label.grid(column=0, row=0, sticky=W)
    
    prodname_var = StringVar()
    prodname_entry = ttk.Entry(window, textvariable=prodname_var)
    prodname_entry.grid(column=0, row=1, sticky=EW)
    
    prodstock_label = ttk.Label(window, text='Estoque')
    prodstock_label.grid(column=0, row=2, sticky=W)
    
    prodstock_var = StringVar()
    prodstock_entry = ttk.Entry(window, textvariable=prodstock_var)
    prodstock_entry.insert(0, 0)
    prodstock_entry.grid(column=0, row=3, sticky=EW)
    
    add_btn = ttk.Button(window, text='Adicionar')
    add_btn['command'] = Add
    add_btn.grid(column=0, row=4, sticky=EW)

def AltProduct(conn, treeview):
    item_name = GetTreeviewItem(treeview, 'name')
    item_stock = GetTreeviewItem(treeview, 'stock')
    
    if item_name:
        def Alt():
            cursor = conn.cursor()
            
            cursor.execute(f'UPDATE products SET product_name = "{prodname_var.get()}" WHERE product_name = "{item_name}"')
            cursor.execute(f'UPDATE products SET product_stock = "{int(prodstock_var.get())}" WHERE product_stock = "{item_stock}"')
            
            conn.commit()
            ReloadTreeview(conn, treeview)
            window.destroy()
        
        window = Toplevel(bg=bg_color, padx=50, pady=30)
        
        prodname_label = ttk.Label(window, text='Nome do Produto')
        prodname_label.grid(column=0, row=0, sticky=W)
        
        prodname_var = StringVar()
        prodname_entry = ttk.Entry(window, textvariable=prodname_var)
        prodname_entry.insert(0, item_name)
        prodname_entry.grid(column=0, columnspan=2, row=1, sticky=EW)
        
        prodstock_label = ttk.Label(window, text='Estoque')
        prodstock_label.grid(column=0, row=2, sticky=W)
        
        prodstock_var = StringVar()
        prodstock_entry = ttk.Entry(window, textvariable=prodstock_var)
        prodstock_entry.insert(0, item_stock)
        prodstock_entry.grid(column=0, columnspan=2, row=3, sticky=EW)
        
        confirm_btn = ttk.Button(window, text='Confirmar')
        confirm_btn['command'] = Alt
        confirm_btn.grid(column=0, row=4)
        
        cancel_btn = ttk.Button(window, text='Cancelar')
        cancel_btn['command'] = window.destroy
        cancel_btn.grid(column=1, row=4)
        
        ReloadTreeview(conn, treeview)

def RemProduct(conn, treeview):
    item_name = GetTreeviewItem(treeview, 'name')
    
    if item_name:
        def Rem():
            cursor = conn.cursor()
            cursor.execute(f'DELETE FROM products WHERE product_name = "{item_name}"')
            conn.commit()
            
            ReloadTreeview(conn, treeview)
            window.destroy()
        
        window = Toplevel(bg=bg_color, padx=50, pady=30)
        
        confirmation_label = ttk.Label(window, text= f'Tem Certeza que deseja remover {item_name} do sistema?')
        confirmation_label.grid(column=0, columnspan=2, row=0)
        
        confirmation2_label = ttk.Label(window, text='Essa ação é irreversível')
        confirmation2_label.grid(column=0, columnspan=2, row=1)
        
        confirm_btn = ttk.Button(window, text='Confirmar')
        confirm_btn['command'] = Rem
        confirm_btn.grid(column=0, row=2, sticky=EW)
        
        cancel_btn = ttk.Button(window, text='Cancelar')
        cancel_btn['command'] = window.destroy
        cancel_btn.grid(column=1, row=2, sticky=EW)
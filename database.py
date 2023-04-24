from tkinter import *
from tkinter import ttk
from configparser import ConfigParser
import mysql.connector

configparser = ConfigParser()
configparser.read('db_config.ini')

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

def ReloadTreeview(conn, treeview):
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM products;')
    data = cursor.fetchall()
    
    treeview.delete(*treeview.get_children())
    
    for prod in data:
        treeview.insert('', 'end', values=(prod))

def AddProduct(conn, treeview):
    cursor = conn.cursor()
    
    def Add():
        cursor.execute(f'INSERT INTO products (product_name, product_stock) VALUES ("{prodname_var.get()}", {int(prodstock_var.get())})')
        conn.commit()
        
        ReloadTreeview(conn, treeview)
        
        window.destroy()
    
    window = Toplevel(padx=50, pady=30)
    
    prodname_label = ttk.Label(window, text='Nome do Produto')
    prodname_label.grid(column=0, row=0)
    
    prodname_var = StringVar()
    prodname_entry = ttk.Entry(window, textvariable=prodname_var)
    prodname_entry.grid(column=0, row=1)
    
    prodstock_label = ttk.Label(window, text='Estoque')
    prodstock_label.grid(column=0, row=2)
    
    prodstock_var = StringVar()
    prodstock_entry = ttk.Entry(window, textvariable=prodstock_var)
    prodstock_entry.grid(column=0, row=3)
    
    add_btn = ttk.Button(window, text='Adicionar')
    add_btn['command'] = Add
    add_btn.grid(column=0, row=4, sticky=EW)

def RemProduct(conn, treeview):
    selected = treeview.focus()
    item_data = treeview.item(selected)
    item_id = item_data['values'][0]
    item_name = item_data['values'][1]
    
    print(item_id)
    
    if selected:
        def Rem():
            cursor = conn.cursor()
            cursor.execute(f'DELETE FROM products WHERE id = {item_id}')
            conn.commit()
            
            ReloadTreeview(conn, treeview)
            window.destroy()
        
        window = Toplevel(padx=50, pady=30)
        
        confirmation_label = ttk.Label(window, text= f'Tem Certeza que deseja remover {item_name} do sistema?')
        confirmation_label.grid(column=0, columnspan=2, row=0)
        
        confirmation2_label = ttk.Label(window, text='Essa ação é irreversível')
        confirmation2_label.grid(column=0, columnspan=2, row=1)
        
        confirm_btn = ttk.Button(window, text='Confirmar')
        confirm_btn['command'] = Rem
        confirm_btn.grid(column=0, row=2)
        
        cancel_btn = ttk.Button(window, text='Cancelar')
        cancel_btn['command'] = window.destroy
        cancel_btn.grid(column=1, row=2)
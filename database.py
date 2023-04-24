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
    
    # treeview.insert(parent="", index="end", iid="3", text="3", values=("José", "40"))
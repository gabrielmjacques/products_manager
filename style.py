from tkinter import ttk

style = ttk.Style()
style.theme_use('clam')

style.configure('TLabel', font='Arial 10 bold', background='#D7DAF0', padding=5)

style.configure("TButton", padding=6, relief="flat", font='Arial 10 bold', foreground='white', width=25)
style.map('TButton', background=[ ('!active','#09456c'), ('pressed', '#062b44'), ('active', '#285c7e')])

style.configure('TEntry', padding=(10,5), fieldbackground='#F6F6F6')
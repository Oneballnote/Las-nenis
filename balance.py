import tkinter
from datetime import datetime
dt = datetime.now()

def ventana_balance():
    main_window = tkinter.Tk()
    
    balance = tkinter.Label(main_window, text = 'Balance')
    boton_venta= tkinter.Label(mainwindow, text = 'Registrar Venta',bg = '#6990D8')
    boton_carga= tkinter.Label(mainwindow,text = 'Registrar Carga',bg = '#6990D8')
    tkinter.mainloop()

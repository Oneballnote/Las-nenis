import tkinter
from datetime import datetime
dt = datetime.now()

def Almacen():
    #Personalización de la ventana
    main_window = tkinter.Tk()
    main_window.geometry('200x200')
    main_window.title('Almacen')
    
    #Textos
    Fecha = tkinter.Label(main_window, text = '{}/{}/{}'.format(dt.day, dt.month, dt.year), bg = '#6990D8').grid(row = 0, column = 3)
    nombre = tkinter.Label(main_window, text = 'Almacen',bg = '#6990D8').grid(row = 1, column = 2)
    producto = tkinter.Label(main_window, text = 'Producto',bg = '#6990D8').grid(row = 2,column = 1)
    Unidades = tkinter.Label(main_window, text = 'Unidades',bg = '#6990D8').grid(row = 2,column = 3)
    
    #Botones
    volver = tkinter.Button(main_window, text = 'volver',border = 0,command = main_window.destroy).grid(row = 3, column = 3)
    
    tkinter.mainloop()
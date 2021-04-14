import tkinter
from datetime import datetime
dt = datetime.now()

def Almacen():
    main_window = tkinter.Tk()
    Fecha = tkinter.Label(main_window, text = '{}/{}/{}'.format(dt.day, dt.month, dt.year), bg = '#6990D8').grid(row = 0, column = 3)
    tkinter.title = 'Almacen'
    tkinter.mainloop()
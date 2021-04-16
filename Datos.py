import tkinter
from datetime import datetime
dt = datetime.now()

def Ventana_datos():
    
    main_window = tkinter.Tk()
    Fecha = tkinter.Label(main_window, text = '{}/{}/{}'.format(dt.day, dt.month, dt.year), bg = '#6990D8').grid(row = 0, column = 3)
    datos = tkinter.Label(main_window, text = 'Datos').grid(row = 1, column = 2)
    promedio_ganancias = tkinter.Label(main_window, text = 'Promedio de ganancias').grid(row = 2, column = 1)
    Ganancia_mensual = tkinter.Label(main_window, text = 'Ganancia mensual').grid(row = 3, column = 1)
    Ganancia_neta = tkinter.Label(main_window, text = 'Ganancia neta').grid(row = 4, column = 1)
    graficas = tkinter.Button(main_window, text = 'Gráficas').grid(row = 5, column = 1)
    tkinter.mainloop()
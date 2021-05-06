import tkinter
from datetime import datetime
import pandas as pd
dt = datetime.now()

def Ventana_datos():
    
    df = pd.read_csv('registro botanas.csv')

   
    main_window = tkinter.Tk()
    main_window.geometry('600x500')
    main_window.title('Datos')
    historial = tkinter.Label(main_window, text = 'Historial').grid(row = 2, column = 2)
    Lunes = tkinter.Label(main_window, text = 'Lunes').grid(row = 3,column = 1)
    Martes = tkinter.Label(main_window, text = 'Martes').grid(row = 4,column = 1)
    Miercoles = tkinter.Label(main_window, text = 'Miércoles').grid(row = 5,column = 1)
    Jueves = tkinter.Label(main_window, text = 'Jueves').grid(row = 6,column = 1)
    Viernes = tkinter.Label(main_window, text = 'Viernes').grid(row = 7,column = 1)
    Sabado = tkinter.Label(main_window, text = 'Sábado').grid(row = 8,column = 1)
    Domingo = tkinter.Label(main_window, text = 'Domingo').grid(row = 9,column = 1)
    Fecha = tkinter.Label(main_window, text = '{}/{}/{}'.format(dt.day, dt.month, dt.year), bg = '#6990D8').grid(row = 0, column = 3)
    datos = tkinter.Label(main_window, text = 'Datos').grid(row = 1, column = 2)
    promedio_ganancias = tkinter.Label(main_window, text = 'Promedio de ganancias').grid(row = 2, column = 1)
    Ganancia_mensual = tkinter.Label(main_window, text = 'Ganancia mensual').grid(row = 3, column = 1)
    Ganancia_neta = tkinter.Label(main_window, text = 'Ganancia neta').grid(row = 4, column = 1)
    graficas = tkinter.Button(main_window, text = 'Gráficas').grid(row = 5, column = 1)
    
    tkinter.mainloop()
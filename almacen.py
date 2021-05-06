from tkinter import *
import tkinter
from Hoja_de_personalizacion import *
from datetime import datetime
import pandas as pd
dt = datetime.now()

def Almacen():
    #Personalización de la ventana
    main_window = tkinter.Tk()
    main_window.geometry('500x700')
    main_window.configure(bg = Color_de_fondo)
    main_window.title('Almacen')
    
    #Textos
    Fecha = tkinter.Label(main_window, 
                      text = '{}/{}/{}'.format(dt.day, dt.month, dt.year), 
                      bg = Color_de_fondo,
                      font = (Fuente_titulos, 10)).grid(column = 2)
    nombre = tkinter.Label(main_window, 
                           text = 'Almacen',
                           bg = Color_de_fondo,
                           font = (Fuente_titulos, Tamaño_titulos)).grid()
    producto = tkinter.Label(main_window, 
                             text = 'Producto',
                             bg = Color_de_fondo).grid(row = 2,column = 1)
    Unidades = tkinter.Label(main_window, 
                             text = 'Unidades',
                             bg = Color_de_fondo).grid(row = 2,column = 3)
    
    
    
    #almacen = pd.read_csv("inventario.csv",index_col="Tipo")
    #print(almacen)
    
    nombre = tkinter.Label(main_window, text = 'Almacen',bg = '#6990D8').grid(row = 1, column = 2)
    producto = tkinter.Label(main_window, text = 'Producto',bg = '#6990D8').grid(row = 2,column = 1)
    Unidades = tkinter.Label(main_window, text = 'Unidades',bg = '#6990D8').grid(row = 2,column = 3)
    
    almacen = pd.read_csv("inventario.csv",index_col="Tipo")
    print(almacen)
    #PAra click en botón bolis
    almacenbolis = almacen[almacen["Tipo"]=="Bolis"]
    print(almacenbolis)
    #PAra click en botón botanas
    almacenbotanas = almacen[almacen["Tipo"]=="Botanas"]
    print(almacenbotanas)

    #Botones
    volver = tkinter.Button(main_window, 
                            text = 'volver',
                            border = Tamaño_bordes,
                            bg = Color_de_botones, 
                            command = main_window.destroy,
                            heigh = altura_botones, 
                            width = ancho_botones,
                            activebackground = botones_activos,
                            cursor = Figura,
                            relief = Tipo_borde,
                            font = (Fuente_botones, Tamaño_fuente_botones)).grid(row = 3, column = 3)
    
    tkinter.mainloop()

import tkinter
from datetime import datetime
from Hoja_de_personalizacion import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dt = datetime.now()

def Ventana_datos():
    
    def Mostrar_graficas():
            #####GRAFICACIÓN######
        #Comparación de ganancias brutas
        plt.pie([gananciabrutabolis,gananciabrutabotanas], 
                                    labels=["Ganancia bruta Bolis","Ganancia Botanas"], 
                                    autopct="%1.1f%%", shadow=True, startangle=90)
        plt.show()
    def Mostrar_graficas2():
        #comparación de ganancias netas
        plt.pie([ganancianetabolis,ganancianetabotanas], 
                                    labels=["Ganancia Neta Bolis","Ganancia Botanas"], 
                                    autopct="%1.1f%%", shadow=True, startangle=90)
        plt.show()
   
        ######MUESTRA Y BÚSQUEDA EN EL HISTORIAL#######
    #Si click en botón bolis entonces:
    histbolis = pd.read_csv('lolo.csv')   
    #histbolis = pd.read_csv("registro_bolis.csv", index_col="Fecha")
    #Si botón en solo ventas entonces:
    soloventasbolis = histbolis[histbolis["Accion"]=="Venta"]

    #Sinosi botón en solo carga entonces:
    solocargabolis = histbolis[histbolis["Accion"]=="Carga"]
                          
    #si click en botón botanas entonces:
    histbotanas = pd.read_csv('lolo.csv')
    #histbotanas = pd.read_csv("registro_botanas.csv", index_col="Fecha")

    #Si botón en solo venta entonces:
    soloventabotanas = histbotanas[histbotanas["Accion"]=="Venta"]


    #Sinosi botón en solo carga entonces:
    solocargabotanas = histbotanas[histbotanas["Accion"]=='Carga']   


    ######GANANCIAS BRUTAS######
    gananciabrutabolis = sum(soloventasbolis["Ganancia"])
    totalbolisvendidos = sum(soloventasbolis["Cantidad"])
    gananciabrutabotanas = sum(soloventabotanas["Ganancia"])
    totalbotanasvendidas = sum(soloventabotanas["Cantidad"])

    ######GANANCIAS NETAS#######
    ganancianetabolis = sum(histbolis["Ganancia"])
    ganancianetabotanas = sum(histbotanas["Ganancia"])
    gananciahistorica = ganancianetabolis + ganancianetabotanas 
    gananciahistorica = str(gananciahistorica)
    
    VentanaDeDatos = tkinter.Tk()
    VentanaDeDatos.title("Datos")
    VentanaDeDatos.geometry('500x400')
    VentanaDeDatos.configure(bg = Color_de_fondo)

    datos = tkinter.Label(VentanaDeDatos, 
                          text = 'Datos',
                          bg = Color_de_fondo,
                          font = (Fuente_titulos, Tamaño_titulos + 3)).grid(row = 1, column = 2, padx = 20, pady = 5)
    Ganancia_semanal = tkinter.Label(VentanaDeDatos, 
                                     text = 'Ganancia de la semana',
                                     bg = Color_de_fondo,
                                     font = (Fuente_subtitulos, Tamaño_subtitulos )).grid(row = 2, column = 1, padx = 10, pady = 5)
    Ganancia_mensual = tkinter.Label(VentanaDeDatos, 
                                     text = 'Ganancia del mes',
                                     bg = Color_de_fondo,
                                     font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 3, column = 1, pady = 5)
    Ganancia_historica = tkinter.Label(VentanaDeDatos, 
                                       text = 'Ganancia histórica',
                                       bg = Color_de_fondo,
                                       font = (Fuente_subtitulos, Tamaño_subtitulos )).grid(row = 4, column = 1, pady = 5)
    cantidad_de_ganancia_semana = tkinter.Label(VentanaDeDatos, 
                                                text = gananciahistorica,
                                                bg = Color_de_fondo,
                                                font = (Fuente_subtitulos, Tamaño_subtitulos + 1)).grid(row = 2,column = 3, padx = 10, pady = 5)
    cantidad_de_ganancia_mes = tkinter.Label(VentanaDeDatos, 
                                             text = gananciahistorica,
                                             bg = Color_de_fondo,
                                             font = (Fuente_subtitulos, Tamaño_subtitulos + 1)).grid(row = 3,column = 3, pady = 5)
    cantidad_de_ganancia_historica = tkinter.Label(VentanaDeDatos, 
                                                   text = gananciahistorica,
                                                   bg = Color_de_fondo,
                                                   font = (Fuente_subtitulos, Tamaño_subtitulos + 1)).grid(row = 4,column = 3, pady = 5)
    Separacion = tkinter.Label(VentanaDeDatos, 
                               text = ' ',
                               bg = Color_de_fondo).grid(row = 5,column = 1,pady = Espacio_botones - 8)
    
    Zona_graficas = tkinter.Label(VentanaDeDatos,
                                  text = 'Gráficas',
                                  bg = Color_de_fondo,
                                  font = (Fuente_subtitulos, Tamaño_subtitulos + 2)).grid(row = 6, column = 1, pady = 7)
    graficas = tkinter.Button(VentanaDeDatos, 
                              text = 'Ganancias Brutas',
                              bg = Color_de_fondo,
                              height = altura_botones,
                              width = ancho_botones + 4,
                              activebackground = botones_activos,
                              cursor = Figura,
                              command = Mostrar_graficas).grid(row = 7, column = 1, pady = 10)
    salir = tkinter.Button(VentanaDeDatos, 
                              text = 'Salir',
                              bg = Color_de_fondo,
                              height = altura_botones,
                              width = ancho_botones + 4,
                              activebackground = botones_activos,
                              cursor = Figura,
                              command = VentanaDeDatos.destroy).grid(row = 8, column = 3, pady = 10)
    graficas = tkinter.Button(VentanaDeDatos, 
                              text = 'Ganancias Netas',
                              bg = Color_de_fondo,
                              height = altura_botones,
                              width = ancho_botones + 4,
                              activebackground = botones_activos,
                              cursor = Figura,
                              command = Mostrar_graficas2).grid(row = 7, column = 3, pady = 10)
    
    
    
    tkinter.mainloop()

Ventana_datos()
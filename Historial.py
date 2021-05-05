import tkinter
import pandas as pd
from datetime import datetime
dt = datetime.now()

def Ventana_Historial():
    main_window = tkinter.Tk()
    
    historial = tkinter.Label(main_window, text = 'Historial').grid(row = 2, column = 2)
    Lunes = tkinter.Label(main_window, text = 'Lunes').grid(row = 3,column = 1)
    Martes = tkinter.Label(main_window, text = 'Martes').grid(row = 4,column = 1)
    Miercoles = tkinter.Label(main_window, text = 'Miércoles').grid(row = 5,column = 1)
    Jueves = tkinter.Label(main_window, text = 'Jueves').grid(row = 6,column = 1)
    Viernes = tkinter.Label(main_window, text = 'Viernes').grid(row = 7,column = 1)
    Sabado = tkinter.Label(main_window, text = 'Sábado').grid(row = 8,column = 1)
    Domingo = tkinter.Label(main_window, text = 'Domingo').grid(row = 9,column = 1)
    
    ########Para  abrir historial########
#Si click en botón bolis entonces:
histbolis = pd.read_csv("registro_bolis.csv")
print(histbolis)
#Si botón en solo ventas entonces:
soloventasbolis = histbolis[histbolis["Acción"]=="Venta"]
print(soloventasbolis)
#Sinosi botón en solo carga entonces:
solocargabolis = histbolis[histbolis["Acción]=="Carga"]
print(solocargabolis)
                      
#si click en botón botanas entonces:
histbotanas = pd.read_csv("registro_botanas.csv")
print(histbotanas)
#Si botón en solo venta entonces:
soloventabotanas = histbotanas[histbotanas["Acción"]=="Venta"]
print(soloventabotanas)
#Sinosi botón en solo carga entonces:
solocargabotanas = histbotanas[histbotanas["Acción"]=='Carga']
print(solocargabotanas)
                                        
    #Para buscar un día en específico 
    #Para buscar un día en específico 
histbolis = pd.read_csv("registro_bolis.csv")
print(type(histbolis.iloc[0,0]))
histbolis.index = histbolis["Fecha"]
histbolis.drop("Fecha", axis=1, inplace=True)

busqueda = input("Ingrese día a buscar en formato dd/mm/aa: ")
try:
    histbolisbusquedadia = histbolis.loc[busqueda]    
except:
    print("No hay registro del día ingresado")

histbolis.reset_index(inplace=True)

    salir = tkinter.Button(main_window,text = 'Volver', command = main_window.destroy)
    
    tkinter.mainloop()
Ventana_Historial()

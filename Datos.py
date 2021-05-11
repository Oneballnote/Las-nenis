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
    
    import datetime
    import pandas as pd
    
        
    ######MUESTRA Y BÚSQUEDA EN EL HISTORIAL#######
    #Si click en botón bolis entonces:
    histbolis = pd.read_csv("registro_bolis.csv")   
    #histbolis = pd.read_csv("registro_bolis.csv", index_col="Fecha")
    print(histbolis)
    #Si botón en solo ventas entonces:
    soloventasbolis = histbolis[histbolis["Accion"]=="Venta"]
    print(soloventasbolis)
    #Sinosi botón en solo carga entonces:
    solocargabolis = histbolis[histbolis["Accion"]=="Carga"]
    print(solocargabolis)
                          
    #si click en botón botanas entonces:
   histbotanas = pd.read_csv("registro_botanas.csv")
    #histbotanas = pd.read_csv("registro_botanas.csv", index_col="Fecha")
    print(histbotanas)
    #Si botón en solo venta entonces:
    soloventabotanas = histbotanas[histbotanas["Accion"]=="Venta"]
    print(soloventabotanas)
    #Sinosi botón en solo carga entonces:
    solocargabotanas = histbotanas[histbotanas["Accion"]=='Carga']
    print(solocargabotanas)

    #Para buscar un día en específico  
    histbolis.index = histbolis["Fecha"]
    histbolis.drop("Fecha", axis=1, inplace=True)

    busqueda = input("Ingrese día a buscar en formato dd/mm/aaaa: ")
    try:
        histbolisbusquedadia = histbolis.loc[busqueda]    
    except:
        print("No hay registro del día ingresado")
    histbolis.reset_index(inplace=True)

    ######GANANCIAS BRUTAS######
    gananciabrutabolis = sum(soloventasbolis["Ganancia"])
    totalbolisvendidos = sum(soloventasbolis["Cantidad"])
    gananciabrutabotanas = sum(soloventabotanas["Ganancia"])
    totalbotanasvendidas = sum(soloventabotanas["Cantidad"])

    ######GANANCIAS NETAS#######
    ganancianetabolis = sum(histbolis["Ganancia"])
    ganancianetabotanas = sum(histbotanas["Ganancia"])

    """
    ######PROMEDIO GANANCIA MENSUAL######
    *****PROBLEMA, AL CONVERTIR A DATETIME LAS FECHAS PARA ASÍ PODER AGRUPARLAS
    SE CAMBIAN ALGUNOS REGISTROS: LOS DÍAS PASAN A SER MESES, LOS MESES DIAS.
    POR LO QUE APARECEN REGISTROS DE OCTUBRE 3, POR EJEMPLO
    ********
    #convertir a datetime las fechas
    soloventasbolis.loc[:,"Fecha"]= pd.to_datetime(soloventasbolis["Fecha"])
    print(soloventasbolis)
    #soloventasbolismeses = soloventasbolis.resample('M').agg({"Cantidad":"sum","Ganancia":"sum"}) 
    """
    #%%
    #####GRAFICACIÓN######
    import matplotlib.pyplot as plt
    #Comparación de ganancias brutas
    plt.pie([gananciabrutabolis,gananciabrutabotanas], 
                                labels=["Ganancia Bolis","Ganancia Botanas"], 
                                autopct="%1.1f%%", shadow=True, startangle=90)
    plt.show()
    #comparación de ganancias netas
    plt.pie([ganancianetabolis,ganancianetabotanas], 
                                labels=["Ganancia Bolis","Ganancia Botanas"], 
                                autopct="%1.1f%%", shadow=True, startangle=90)
    plt.show()
    
    tkinter.mainloop()

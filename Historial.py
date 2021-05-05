import tkinter
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
histbolis = pd.read_csv("registro_bolis.csv")
histbolis
#Para solo ventas / carga
soloventas = histbolis[histbolis["Acción"]=="Venta"]
soloventas
#convertir fecha en cadena a un datetime
from datetime import datetime 
fecha = input("Inserte fecha a buscar en formato dd/mm/aaaa")
fecha_object = datetime.strptime(fecha, "%d/%m/%Y")
"gay",fecha_object

    
    salir = tkinter.Button(main_window,text = 'Volver', command = main_window.destroy)
    
    tkinter.mainloop()
Ventana_Historial()

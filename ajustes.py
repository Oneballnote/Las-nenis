import tkinter
from datetime import datetime
dt = datetime.now()

def ventana_ajustes():
    main_window = tkinter.Tk()
    main_window.title("Ajustes")

    Nombre_ventana = tkinter.Label(main_window, text = 'Ajustes').grid(row = 0, column = 0)
    cambio_nombre = tkinter.Label(main_window, text = 'Introduzca el nombre de la empresa').grid(row = 1, column = 0)
    boton_salir = tkinter.Button(main_window, text = 'Salir', command = main_window.destroy).grid
    opcion = tkinter.Entry(main_window, width = 50).grid
    
    

    tkinter.mainloop()
    
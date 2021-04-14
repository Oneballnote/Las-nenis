import tkinter

def ventana_ajustes():
    main_window = tkinter.Tk()

    Nombre_ventana = tkinter.Label(main_window, text = 'Ajustes')
    cambio_nombre = tkinter.Label(main_window, text = 'Introduzca el nombre de la empresa')
    boton_salir = tkinter.Button(main_window, text = 'Salir', command = main_window.destroy)
    opcion = tkinter.Entry(main_window, width = 50)
    Nombre_ventana.grid(row = 0, column = 0)
    cambio_nombre.grid(row = 1, column = 0)
    opcion.grid()
    boton_salir.grid()
    tkinter.mainloop()
    
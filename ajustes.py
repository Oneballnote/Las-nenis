from datetime import datetime
import tkinter
import io

dt = datetime.now()    

def ventana_ajustes():
    main_window = tkinter.Tk()
    main_window.title("Ajustes")
    def save(self):
        archivo = open('nombre.txt','w')
   
        archivo.write(self)
        archivo.close()

    Nombre_ventana = tkinter.Label(main_window, text = 'Ajustes').grid(row = 0, column = 0)
    cambio_nombre = tkinter.Label(main_window, text = 'Introduzca el nombre de la empresa').grid(row = 1, column = 0)
    e = tkinter.Entry(main_window, width = 20)
    e.grid()
    guardar = tkinter.Button(main_window, text = 'Guardar').grid()
    boton_salir = tkinter.Button(main_window, text = 'Salir', command = main_window.destroy).grid()
    
   
    archivo = open('nombre.txt','w')
   
    archivo.write(e.get())
    archivo.close()
    
    

    tkinter.mainloop()
    
ventana_ajustes()
    
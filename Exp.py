#Trabajo con archivos
Archivo_productos = open('productos.txt', 'r')
Tipo_productos = Archivo_productos.readline()
Archivo_productos.close()

Archivo_costos = open('costo.txt', 'r')
costos_productos = Archivo_costos.readline()
Archivo_costos.close()

Archivo_Precio = open('Precio.txt', 'r')
Precio_productos = Archivo_Precio.readline()
Archivo_Precio.close()

#Trabajo con listas
Tipo_productos = Tipo_productos.split(',')
Tipo_productos.remove('')
costos_productos = costos_productos.split(',')
costos_productos.remove('')
Precio_productos = Precio_productos.split(',')
Precio_productos.remove('')
#Convierte las cadenas de la lista a enteros
for m in range(len(Tipo_productos)):
    Tipo_productos[m] = Tipo_productos[m].lower()
for i in range(len(costos_productos)):
    costos_productos[i] = int(costos_productos[i])
    
for j in range(len(Precio_productos)):
    Precio_productos[j] = int(Precio_productos[j])

#asignación de precios
if Tipo_productos[0] == 'bolis':
    preciobolis = Precio_productos[0]
    costobolis = Precio_productos[1]*(-1)
    preciobotana = costos_productos[0]
    costobotana = costos_productos[1]*(-1)
    
elif Tipo_productos[0] == 'botana':
    preciobolis = Precio_productos[1]
    costobolis = Precio_productos[0]*(-1)
    preciobotana = costos_productos[1]
    costobotana = costos_productos[0]*(-1)
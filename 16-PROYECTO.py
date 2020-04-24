import os
CARPETA="contactos/" #carpeta de contactos
EXTENSION=".txt"  #extension del archivo

#Contactos
class Contacto:
    def __init__(self,nombre,telefono,categoria):
        self.nombre=nombre
        self.telefono=telefono
        self.categoria=categoria




def app():
    #REVISA SI LA CARPETA EXISTE O NO
    crearDirectorio()
    mostrarMenu()

    #Preguntar al usuario
    preguntar=True
    while preguntar:
        opcion=input("Seleccione una opcion\r\n")
        opcion=int(opcion) #convertir a entero
        if opcion==1:
            crearContacto()
        elif opcion==2:
            editarContacto()
        elif opcion==3:
            mostrarContacto()
        elif opcion==4:
                buscarContacto()
        elif opcion==5:
            eliminarContacto()
        else:
            print("Seleccion una opcion del Menú")


def mostrarMenu():
    print("seleccione del menu lo que desea hacer")
    print("1)Agregar Nuevo Contacto")
    print("2)Editar un Contacto")
    print("3)Ver Contactos")
    print("4)Buscar Contacto")
    print("5)Eliminar Contacto")


def crearDirectorio():
    if not os.path.exists(CARPETA):
        #crear carpeta
        os.makedirs(CARPETA)

def crearContacto():
    print("Escribir los datos del nuevo contacto")
    nombreContacto=input("Nombre del Contacto:\r\n")
    #Revisar si el archivo ya existe

    existe= existeContacto(nombreContacto)
    if not existe:
        with open(CARPETA+nombreContacto+EXTENSION,"w") as archivo:
            telefonoContacto=input("Agrega al Telefono\r\n")
            categoriaContacto=input("Categoria Contacto\r\n")

         #Instanciar
            contacto=Contacto(nombreContacto,telefonoContacto,categoriaContacto)
            #escribir en el archivo
            archivo.write("Nombre: "+contacto.nombre+"\r\n")
            archivo.write("Telefono: "+contacto.telefono+"\r\n")
            archivo.write("Categoria: "+contacto.categoria+"\r\n")
            #Mensaje
            print("\r\n Contacto Creado Correctamente. \r\n")
    else:
        print("Contacto Existente")
    #reiniciar app
    app()

def editarContacto():
    print("Escribe El nombre del contacto que desea editar:")
    nombreAnterior=input("Nombre del contacto que desea editar\r\n")
    
    existe=existeContacto(nombreAnterior)

    if existe:
        with open(CARPETA+nombreAnterior+EXTENSION,"w") as archivo:
            #Resto de los campos
            nombreContacto=input("Agrega el nuevo Nombre\r\n")
            telefonoContacto=input("Agrega el nuevo Telefono\r\n")
            categoriaContacto=input("Agrega Categoria nueva del Contacto\r\n")
            
            contacto=Contacto(nombreContacto,telefonoContacto,categoriaContacto)
            #Escribir en el archivo
            archivo.write("Nombre: "+contacto.nombre+"\r\n")
            archivo.write("Telefono: "+contacto.telefono+"\r\n")
            archivo.write("Categoria: "+contacto.categoria+"\r\n")

            #Renoombrar el archivo
            #os.rename(CARPETA+nombreAnterior+EXTENSION, CARPETA+nombreContacto+EXTENSION)
            print("Contacto editado con exito")
            
    else:
        print("No existe contacto")
        app()

def mostrarContacto():
    archivos= os.listdir(CARPETA)
    archivos_txt=[i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open(CARPETA+archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip( )) #imprime el contenido
            print("\r\n")

def buscarContacto():
    nombre=input("Seleccione el contacto que desea buscar:\r\n")
    with open(CARPETA+nombre+EXTENSION)as contacto:
        print("\r\n Informacion del contacto:\r\n")
        for linea in contacto:
            print(linea.rstrip())
        print("\r\n")
    

def existeContacto(nombre):
    return os.path.isfile(CARPETA+nombre+EXTENSION)
app()

def eliminarContacto():
    nombre=input("Escriba el contacto que desea eliminar:\r\n")
    try:
        os.remove(CARPETA+nombre+EXTENSION)
        print("\r\nEliminado Correctamente")
     except expression as identifier:
        print("No existe ese contacto")
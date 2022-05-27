#Está desarrollando un sistema de rastreo de contactos simplificado para COVID-19.
#Biblioteca de la fecha y hora
from datetime import datetime

class cliente:
    def __init__(self,nombre,apellido,telef,estado):
        self.nombre=nombre
        self.apellid=apellido
        self.telef=telef
        self.estado=estado
    
    def menuClientes():
        while(True!=6):
            print("======== MENU CLIENTES ========")
            print("1.- Registrarse")
            print("2.- Iniciar sesion")
            print("3.- Registrarse en una Tienda")
            print("4.- Ver historial de Tiendas")
            print("5.- Ver su estado")
            print("6.- SALIR")
            print("================================")
            opcC=int(input("Seleccione una respuesta: "))
            if (opcC==1):
                #Registrar una cuenta en el sistema.
                print("=== REGISTRARSE ===")
                #Creacion de usuario
                cliente.nombre=input("Ingrese su nombre: ")
                nombre=cliente.nombre
                cliente.apellido=input("Ingrese su apellido: ")
                apellido=cliente.apellido
                cliente.telef=input("Ingrese su numero de telefono (10 digitos): ")
                telef=cliente.telef
                print("Normal: Sin Covid-19")
                print("Caso: Tiene Covid-19")
                print("Cercano: Tuvo un contacto cercano")
                cliente.estado=input("En que estado se encuentra?: ")
                #poner en minusculas con lower()
                estado=cliente.estado.lower()
                while estado!="normal" and estado!="caso" and estado!="cercano":
                    cliente.estado=input("Error, en que estado se encuentra?: ")
                    estado=cliente.estado.lower()
                #Minusculas al nombre,apellido y utilzar 3 primeras variables
                nombreCortado=cliente.nombre[0:3].lower()
                apellidoCortado=cliente.apellido[0:3].lower()
                telefCortado=cliente.telef[7:10]
                print("El nombre de usuario creado con sus datos es el siguiente")
                #asignacion de los datos a la variable user
                user=nombreCortado+telefCortado+ apellidoCortado
                print("→", user)
                #Creacion de contrasenia
                print("La contrasenia creada es la siguiente")
                password=apellidoCortado + nombreCortado + telefCortado
                print("→",password )

            elif opcC==2:
                #Inicio de sesion al cliente
                print("=== INICIO DE SESION ===")
                user2=input(print("Ingrese el usuario: "))
                if user2==user:
                    print("El usuario es correcto ")
                    password2=input(print("Ingrese su  contrasenia: "))
                    if password2==password:
                        print("La contrasenia es correcta ")
                    else:
                        print("La constrasenia es incorrecta")
                else:
                    print("El usuario o contrasenia es incorrecto")

            elif opcC==3:
                print(tienda.registroTienda())
            
            elif opcC==4:
                print("=== VER HISTORIAL DE TIENDAS ===")
                #fecha y hora
                fecha=datetime.today().strftime("%Y-%m-%d")
                hora=datetime.today().strftime("%H:%M")
                i=1
                for i in range(i):
                    print(" ___________________________________________") 
                    print(str(i+1)," | ",fecha," | ",hora," | ",tienda.nomT," | ")
                    print(" ___________________________________________")
            
            elif opcC==5:
                print("=== VER SU ESTADO ===")
                while estado=="normal" or estado=="caso" or estado=="cercano":
                    if estado=="normal":
                        print("El estado del cliente ", nombre, apellido, " es → Normal ←")
                        print("Quiere decir que usted no tiene COVID-19")
                    elif estado=="caso":
                        print("El estado del cleinte ", nombre, apellido, " es → Caso ←")
                        print("Quiere decir que usted si tiene COVID-19")
                    elif estado=="cercano":
                        print("El estado del cliente ", nombre,apellido," es → Cercano ←")
                    else:
                        print("Se a ingresado el estado de manera incorrecta")
                    break
                
            elif opcC==6:
                print("ACABA DE SALIR DEL PROGRAMA")
                break
            else:
                print("ERROR, INGRESO INCORRECTO")


class tienda:
    def __init__(self,nomT,telefT,estadoT,gerenteT):
        self.nomT=nomT
        self.telefT=telefT
        self.estadoT=estadoT
        self.gerenteT=gerenteT
    
    def registroTienda():
        print("=== REGISTRARSE EN UNA TIENDA ===")
        nomTienda=tienda.nomT=input("Ingrese el nombre de la tienda: ")
        telefTienda=tienda.telefT=input("Ingrese el numero de telefono de la tienda: ")                
        gerenteTienda=tienda.gerenteT=input("Ingrese nombre y apellido del gerente de la tienda: ")
        estadoTienda=tienda.estadoT=input("Ingrese el estado de la de la tienda (Caso,Normal,Cercano): ")
        print("...Tienda Agregada...")

class admin:
    #a- Ver los detalles de todos los clientes,tiendas,historial de visitas
    #b- Cambiar de estado a un cliente, si el cliente es Caso la tienda tambien y todo lo cercano como "Cercano"
    usuarioAd="adminGuber"
    contraAd="admin777"

    #inicio de sesion de personal de administracion
    def iniciosesionAd():
        print("INICIO DE SESION DE PERSONAL AUTORIZADO")
        usuAd=input("Ingrese el usuario: ")
        contra=input("Ingrese la contrasenia: ")
        if usuAd==admin.usuarioAd:
            if contra==admin.contraAd:
                print("Bienvenido al sistema")
                print(menuAdmin())
        else:
            #En caso de0 que se ingrese mal
            while usuAd != admin.usuarioAd or contra!=admin.contraAd:
                usuAd=input("Error, Ingrese el usuario: ")
                contra=input("Eror, Ingrese la contrasenia: ")
                if usuAd==admin.usuarioAd:
                    if contra==admin.contraAd:
                        print("Bienvenido al sistema")
                        print(menuAdmin())
    
def menuPrincipal():
    while(True!=3):
        print("======== MENU PRINCIPAL ========")
        print("1.- Cliente")
        print("2.- Administracion")
        print("3.- SALIR")
        print("================================")
        opc=int(input("Seleccione una respuesta: "))
        if (opc==1):
            print(cliente.menuClientes())

        elif (opc==2):
            #Inicio de sesion personalizada para admin
            print(admin.iniciosesionAd())

        elif opc==3:
            print("ACABA DE SALIR DEL PROGRAMA")
            break
        
        else:
            print("ERROR, INGRESO INCORRECTO")


def menuAdmin():
    while(True!=5):
        print("======== ADMINISTRACION ========")
        print("1.- Detalles de los cientes")
        print("2.- Detalles de tiendas")
        print("3.- Historial de visitas")
        print("4.- Cambiar de estado un cliente")
        print("5.- SALIR")
        print("================================")
        opcA=int(input("Seleccione una respuesta: "))
        if opcA==1:
            print("=== DETALLES DE CLIENTES ===")
            t=1
            for t in range(t):
                print(str(t+1)," | ",cliente.nombre," | ",cliente.telef," | ",cliente.estado," | ")
            
        elif opcA==2:
            print("=== DETALLES DE TIENDAS ===")
            m=1
            for m in range(m):
                print(str(m+1)," | ",cliente.nombre," | ",cliente.telef," | ",tienda.gerenteT," | ",tienda.estadoT," | ")

        elif opcA==3:
            print("=== HISTORIAL DE VISITAS ===")
            fecha=datetime.today().strftime("%Y-%m-%d")
            hora=datetime.today().strftime("%H:%M")
            m=1
            for m in range(m):
                print(str(m+1)," | ",fecha," | ",hora," | ",cliente.nombre," | ",tienda.nomT," | ")

        elif opcA==4:
            print("=== CAMBIAR DE ESTADO UN CLIENTE ===")

        elif opcA==5:
            print("ACABA DE SALIR DEL MENU DE ADMINISTRACION")
            break
        
        else:
            print("ERROR, INGRESO INCORRECTO")


print(menuPrincipal())
# Crear clientes
Clientes = {
}
def crearClientes (C,name, tel, email):
    if C in Clientes.keys() :
        print("Cliente ya existe")
        for n , t , e in Clientes.values():
            print(f"Informacion del cliente:\nNombre = {n}\nCedula = {C}\nTelefono = {t}\nCorreo = {e}\n")      
    else:
        Clientes[C]= (name , tel , email)
while True:
    try :
        Id = int (input("Digite la cedula del usuario:\n"))
        Telefono = int (input("Digite el numero de telefono del usuario:\n"))
        cantidadN = len(Telefono)
        if cantidadN != 10 : 
            print ("Un numero telefonico valido tiene 10 digitos.")
        else:
            break
    except ValueError:
        print("Digite solo numeros")
    Nombre = input ("Digite su nombre de usuario:")
    try:
        Correo = input ("Digite el correo elctronico\nRecuerde que debe terminar en (gmail.com)")
        if "@" not in Correo:
            raise ValueError("error falta el @")
        print(f"correo valido {Correo}")
    except ValueError as ve:
        print(ve)
        
        
        
        

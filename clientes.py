Clientes = {
    1 : {"nombre":"yisus","tel": 123456,"email":"correo"}
}
def crearClientes (C,name, tel, email):
    if C in Clientes.keys() :
        print("Cliente ya existe")
        for n , t , e in Clientes.values():
            print(f"Informacion del cliente:\nNombre = {n}\nCedula = {C}\nTelefono = {t}\nCorreo = {e}\n")      
    else:
        Clientes[C]= {"nombre": name , "tel": tel ,"email": email}
    while True:
        try :
            Id = int (input("Digite la cedula del usuario:\n"))
            Telefono = input("Digite el numero de telefono del usuario:\n")
            cantidadN = len(Telefono)
            if cantidadN < 10 or cantidadN >10: 
                print ("Un numero telefonico valido tiene 10 digitos.")
            else:
                print ("Numero registrado")
        except ValueError:
            print("Digite solo numeros")
        Nombre = input ("Digite su nombre de usuario:")
        try:
            Correo = input ("Digite el correo elctronico\nRecuerde que debe terminar en (gmail.com)")
            if "@" not in Correo:
                raise ValueError("error falta el @")
            print(f"correo valido {Correo}")
            break
        except ValueError as ve:
            print(ve)
        
def buscar_cliente(codigo):
    if codigo in Clientes:
        return Clientes[codigo]["nombre"]
    else:
        print("no existe un cliente con ese correo")                                                                                                                                                                   
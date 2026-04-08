Clientes = {
}
def crearClientes (C,name, tel, email):
    if C in Clientes.keys() :
        print("Cliente ya existe")
        for n , t , e in Clientes.values():
            print(f"Informacion del cliente:\nNombre = {n}\nCedula = {C}\nTelefono = {t}\nCorreo = {e}\n")      
    else:
        Clientes[C]= (name , tel , email)

        
        
        
        

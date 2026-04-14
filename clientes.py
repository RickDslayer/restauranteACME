import json
clientes = "clientes.json"
    #1 : {"nombre":"yisus","tel": 123456,"email":"correo"}
def cargar_clientes():
    try:
        with open(clientes, "r") as file:
            return json.load(file)
    except FileExistsError:
        return {}
    except json.JSONDecodeError:
        return {}
datos_clientes = cargar_clientes()
def guardar_datos_clientes(datos):
    with open(clientes, "w") as archivo:
        json.dump(datos, archivo, indent=4)
def crearClientes (C,name, tel, email):
    cc = str(C)
    if cc in datos_clientes:
        print("Cliente ya existe")
        for n , t , e in datos_clientes.values():
            print(f"Informacion del cliente:\nNombre = {n}\nCedula = {C}\nTelefono = {t}\nCorreo = {e}\n")      
    else:
        datos_clientes[cc]= {"nombre": name , "tel": tel ,"email": email}    
def buscar_cliente(codigo):
    if codigo in datos_clientes:
        return datos_clientes[codigo]["nombre"]
    else:
        print("no existe un cliente con ese correo")                                                                                                                                                                   
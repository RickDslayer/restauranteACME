import json
productos = "productos.json"
def cargar_productos():
    try:
        with open(productos, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
inventario = cargar_productos()
def guardar_datos(datos):
    with open(productos, "w") as archivo:
        json.dump(datos, archivo, indent=4)
def crear_producto(codigo, nombre, valor, iva):
    buscar = str(codigo)
    if buscar in inventario:
        print(f"El codigo {buscar} ya existe")
    else:
        inventario[buscar] = {
                        "nombre": nombre, 
                        "valor_unitario": valor, 
                        "iva": iva
                        }
        guardar_datos(inventario)
        print(f"Producto '{nombre}' registrado con éxito.")
def buscar_productos(codigo):
    inventario = cargar_productos()
    cod = str(codigo)
    if cod in inventario:
        return  inventario[cod]
        
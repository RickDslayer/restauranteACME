productos = {
    1 : {"nombre": "papas", "valor_unitario": 12, "iva" : 0.19},
    2 : {"nombre": "coca", "valor_unitario": 15, "iva" : 0.19}
}

#crea el producto
def crear_producto(codigo, nombre, valor_unitario, iva):
    if codigo in productos:
        print("ya existe un producto con ese codigo")
    else:
        productos[codigo] = {"nombre": nombre, "valor_unitario": valor_unitario, "iva": iva}

#lista todos los productos
def listar_productos():
    for clave,valor in productos.items():
        print(clave,valor)

#lista el producto del codigo especifico
def buscar_productos(codigo):
    if codigo in productos:
        return productos[codigo]
    else:
        print("no existe el producto con el codigo registrado")

#elimina el producto
def eliminar_productos(codigo):
    if codigo in productos:
        del(productos[codigo])
        print(f"el producto con codigo: {codigo}, fue eliminado")
    else:
        print("no hay un producto con ese codigo")

#edita un producto existente
def editar_producto(codigo,newNombre,newValor_unitario,newIva):
    if codigo in productos:
        productos[codigo] = {"nombre": newNombre, "valor_unitario": newValor_unitario, "iva": newIva}
        print(f"producto con codigo: {codigo} editado: {productos[codigo]}")
    else:
        print(f"el producto con codigo: {codigo} no se encuentra")

#listar_productos()
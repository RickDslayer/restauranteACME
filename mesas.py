mesas = {
      1 : {"nombre" : "mesa 1","puestos": 5}
}
def crear_mesas(codigo, nombre,puestos):
            if codigo in mesas:
                print("ya existe este codigo de mesa")
                print(f"{codigo}: {mesas[codigo]}")
            else:
                mesas[codigo] = (nombre,puestos)
#mesa_codigo = int(input("Dime el codigo:\n"))
#nombre = input("Dime el nombre de la mesa:\n")
#puestos = int(input("Dime el numero de puestos:\n"))
#crear_mesas(mesa_codigo,nombre,puestos)
def lista_mesas():
    for codigo, valores in mesas.items():
        nom, pues = valores
        print("--------------MESAS-------------")
        print(f"{codigo}: {nom}, {pues}")
def eliminar_mesa(codigo):
        if codigo in mesas:
            del(mesas[codigo])
            print("Mesa eliminada")
        else:
            print("El codigo no existe")
def editar_mesa(codigo):
      if codigo in mesas:
            nuevo_nombre = input("Dime el nuevo nombre:\n")
            nuevo_puesto = int(input("Dime cuantos puestos:\n"))
            mesas[codigo] = nuevo_nombre, nuevo_puesto
      else:
            print("No se encuentra la mesa")
def facturacion(mesa,cliente):
       if mesa in mesas:
             print("")
#lista_mesas()
#a = input("D")
#editar_mesa(a)
#lista_mesas()
#editar_mesa()
#eliminar_mesa(mesa_codigo)

def buscar_mesa(codigo):
      if codigo in mesas:
            return mesas[codigo]["nombre"]
      else:
            print("no existe una mesa con ese codigo")
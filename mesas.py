mesas = {}
def crear_mesas(codigo, nombre,puestos):
            if codigo in mesas:
                print("ya existe este codigo de mesa")
                print(f"{codigo}: {mesas[codigo]}")
            else:
                mesas[codigo] = (nombre,puestos)
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
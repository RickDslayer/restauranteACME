from datetime import datetime
import productos as p
import mesas as m
import clientes as c
fecha_completa = datetime.now()
fecha = fecha_completa.date()
hora = fecha_completa.time()
#print (f"{fecha}\n{hora}")
facturas = {}
contador = 0
total = 0
def  Facturacion():
    while True:
        global contador 
        contador += 1
        codigo_mesa = int(input("ingrese el codigo de la mesa que desea usar: "))
        mesa = m.buscar_mesa(codigo_mesa)
        codgio_cliente = int(input("ingrese el codigo del cliente: "))
        cliente = c.buscar_cliente(codgio_cliente)
        lista_productos = []
        while True:
            global total
            codigo_producto = int(input("ingrese el codigo del prodcto que desea ingresar: "))
            cantidad = int(input("ingrese la cantidad que desea: "))
            producto = p.buscar_productos(codigo_producto)
            subtotal = (producto["valor_unitario"]+cantidad)*producto["iva"]
            total += subtotal
            if producto:
                lista_productos.append({
                    "nombre":producto["nombre"],
                    "valor_unitario":producto["valor_unitario"],
                    "iva":producto["iva"],
                    "cantidad":cantidad,
                    "subtotal":subtotal
                })
            continuar = input("desea seguir agregando otro producto? (s/n): ")
            if continuar.lower() != "s":
                break
        facturas[contador] = {"fecha": fecha,"mesa" : mesa,"cliente": cliente,"productos": lista_productos, "total": total}
        print("\n========== FACTURA ==========")
        print(f"Factura N°: {contador}")
        print(f"Fecha: {fecha}")
        print(f"Mesa: {mesa}")
        print(f"Cliente: {cliente}")
        print("-----------------------------")
        print("Productos:")

        for prod in lista_productos:
            print(f"- {prod['nombre']}")
            print(f"  Cantidad: {prod['cantidad']}")
            print(f"  Valor unitario: {prod['valor_unitario']}")
            print(f"  Subtotal: {prod['subtotal']}")
            print("-----------------------------")

        print(f"TOTAL A PAGAR: {total}")
        print("========== FIN ==========\n")   
        break
Facturacion()


from datetime import datetime
import productos as p
import mesas as m
import clientes as c
import csv
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
            codigo_producto = int(input("ingrese el codigo del producto que desea ingresar: "))
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
            if continuar.lower() == "n":
                break
            elif continuar.lower() != "s":
                print("Opción inválida. Por favor ingrese 's' o 'n'.")

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
        seguro = input ("¿Desea guardar registro de la factura? (s/n)")
        if seguro.lower() == "s":
            nombre_archivo = f"Factura_{contador}.txt"
            with open (nombre_archivo, "w") as f :
                f.write("========== FACTURA ==========\n")
                f.write(f"Factura N#: {contador}\n")
                f.write(f"Fecha: {fecha}\n")
                f.write(f"Mesa: {mesa}\n")
                f.write(f"Cliente: {cliente}\n")
                f.write("-----------------------------\n")
                f.write("Productos:\n")
                f.write(f"- {prod['nombre']}\n")
                f.write(f"  Cantidad: {prod['cantidad']}\n")
                f.write(f"  Valor unitario: {prod['valor_unitario']}\n")
                f.write(f"  Subtotal: {prod['subtotal']}\n")
                f.write("-----------------------------\n")
                f.write(f"TOTAL A PAGAR: {total}\n")
                f.write("-----------------------------\n")
            print("========== FIN ==========\n")    
            break
        elif seguro.lower() == "n":
            print("Factura no guardada.")
            break
        else:
            print("Opción inválida. Por favor ingrese 's' o 'n'.")
        

def reporte_de_ventas():
    
    # Pedir fecha al usuario
    fecha_str = input("Ingrese la fecha del reporte (YYYY-MM-DD): ")
    try:
        fecha_reporte = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de fecha inválido. Use YYYY-MM-DD")
        return
    
    # Filtrar facturas por fecha
    facturas_filtradas = {}
    for clave, valor in facturas.items():
        if valor["fecha"] == fecha_reporte:
            facturas_filtradas[clave] = valor
    
    if not facturas_filtradas:
        print(f"No hay facturas registradas para la fecha {fecha_reporte}")
        return
    
    # Agrupar por mesa y calcular totales
    reporte_mesas = {}
    for factura_num, factura in facturas_filtradas.items():
        mesa_nombre = factura["mesa"]
        if mesa_nombre not in reporte_mesas:
            reporte_mesas[mesa_nombre] = {
                "cantidad_productos": 0,
                "subtotal_bruto": 0,
                "subtotal_iva": 0,
                "subtotal": 0
            }
        
        for prod in factura["productos"]:
            reporte_mesas[mesa_nombre]["cantidad_productos"] += prod["cantidad"]
            valor_bruto = prod["valor_unitario"] * prod["cantidad"]
            reporte_mesas[mesa_nombre]["subtotal_bruto"] += valor_bruto
            iva_prod = valor_bruto * prod["iva"]
            reporte_mesas[mesa_nombre]["subtotal_iva"] += iva_prod
            reporte_mesas[mesa_nombre]["subtotal"] += valor_bruto + iva_prod
    
    # Mostrar reporte en pantalla
    print("\n" + "="*100)
    print(f"REPORTE DE VENTAS - Fecha: {fecha_reporte}")
    print("="*100)
    print("Mesa Productos Subtotal Bruto Subtotal IVA Subtotal")
    print("-"*100)
    
    total_bruto = 0
    total_iva = 0
    total_ventas = 0
    
    for mesa, datos in reporte_mesas.items():
        print(f"{mesa} {datos['cantidad_productos']} ${datos['subtotal_bruto']} ${datos['subtotal_iva']} ${datos['subtotal']}")
        total_bruto += datos['subtotal_bruto']
        total_iva += datos['subtotal_iva']
        total_ventas += datos['subtotal']
    
    print("-"*100)
    print(f"TOTAL VENTA BRUTA ${total_bruto}")
    print(f"TOTAL IVA ${total_iva}")
    print(f"TOTAL VENTAS ${total_ventas}")
    print("="*100)
    
    # Preguntar si imprimir a CSV
    imprimir = input("\n¿Desea imprimir el reporte en CSV? (s/n): ")
    if imprimir.lower() == "s":
        nombre_archivo = f"Reporte_Ventas_{fecha_reporte}.csv"
        try:
            with open(nombre_archivo, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["REPORTE DE VENTAS"])
                writer.writerow([f"Fecha: {fecha_reporte}"])
                writer.writerow([])
                writer.writerow(["Mesa", "Cantidad Productos", "Subtotal Bruto", "Subtotal IVA", "Subtotal"])
                
                for mesa, datos in reporte_mesas.items():
                    writer.writerow([
                        mesa, 
                        datos['cantidad_productos'], 
                        datos['subtotal_bruto'], 
                        datos['subtotal_iva'], 
                        datos['subtotal']
                    ])
                
                writer.writerow([])
                writer.writerow(["TOTAL VENTA BRUTA", "", total_bruto])
                writer.writerow(["TOTAL IVA", "", total_iva])
                writer.writerow(["TOTAL VENTAS", "", total_ventas])
            
            print(f"Reporte guardado en: {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
    elif imprimir.lower() == "n":
        print("Reporte no guardado en archivo.")
    else:
        print("Opción inválida. Por favor ingrese 's' o 'n'.")



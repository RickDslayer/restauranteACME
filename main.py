import clientes
import mesas
import productos
while True:
    try:
        print("--------------Menu---------------")
        print("1. Crear productos\n2. Crear mesas\n3. Crear mesas\n4. Factura\n5. Reporte de ventas\n0. Salir")
        opcion = int(input(""))
        match opcion:
            case 1:
                producto_codigo = int(input("Ingrese el codigo del nuevo producto:\n"))
                producto_nombre = input("Ingrese el nombre:\n")
                producto_valor_unitario = int(input("Ingrese el valor unitario:\n"))
                producto_iva = int(input("Ingrese el valor del iva:\n"))
                productos.crear_producto(producto_codigo,producto_nombre,producto_valor_unitario,producto_iva)
    except ValueError:
        print("ERROR de valor (solo numeros)")       

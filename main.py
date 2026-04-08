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
                producto_nombre = input("")
                productos.crear_producto()

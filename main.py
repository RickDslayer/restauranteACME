import productos
import mesas
while True:
    try:
        print("--------------Menu---------------")
        print("1. Crear productos\n2. Crear mesas\n3. Crear mesas\n4. Factura\n5. Reporte de ventas\n0. Salir")
        opcion = int(input(""))
        match opcion:
            case 1:
                    producto_codigo = int(input("Ingrese el codigo del nuevo producto (solo numeros):\n"))
                    producto_nombre = input("Ingrese el nombre:\n")
                    producto_valor_unitario = int(input("Ingrese el valor unitario (solo numeros):\n"))
                    producto_iva = int(input("Ingrese el valor del iva (solo numeros):\n"))
                    productos.crear_producto(producto_codigo,producto_nombre,producto_valor_unitario,producto_iva)
            case 2:
                  mesa_codigo = int(input("Ingresa el codigo del la nueva mesa (solo numeros):\n"))
                  mesa_nombre = input("Ingresa el nombre de la mesa:\n")
                  mesa_puestos = int(input("Ingresa la cantidad de puestos (solo numeros):\n"))
                  mesas.crear_mesas(mesa_codigo,mesa_nombre,mesa_puestos)
    except ValueError:
        print("ERROR de valor (solo numeros)")       

import productos
import mesas
import clientes
import Facturacion
while True:
    try:
        print("--------------Menu---------------")
        print("1. Crear productos\n2. Crear mesas\n3. Crear clientes\n4. Factura\n5. Reporte de ventas\n0. Salir")
        opcion = int(input(""))
        match opcion:
            case 1:
                producto_codigo = int(input("Ingrese el codigo del nuevo producto (solo numeros):\n"))
                producto_nombre = input("Ingrese el nombre:\n")
                producto_valor_unitario = int(input("Ingrese el valor unitario (solo numeros):\n"))
                producto_iva = int(input("Ingrese el valor del iva (soo numeros):\n"))
                productos.crear_producto(producto_codigo,producto_nombre,producto_valor_unitario,producto_iva)
            case 2:
                mesa_codigo = int(input("Ingresa el codigo del la nueva mesa (solo numeros):\n"))
                mesa_nombre = input("Ingresa el nombre de la mesa:\n")
                mesa_puestos = int(input("Ingresa la cantidad de puestos (solo numeros):\n"))
                mesas.crear_mesas(mesa_codigo,mesa_nombre,mesa_puestos)
            case 3:
                while True:
                    try :
                        Id = int(input("Digite la cedula del usuario:\n"))
                        Telefono = int(input("Digite el numero de telefono del usuario:\n"))
                    except ValueError:
                        print("Digite solo numeros")
                    Nombre = input ("Digite su nombre de usuario:")
                    try:
                        Correo = input ("Digite el correo elctronico\nRecuerde que debe terminar en (gmail.com)")
                        if "@" not in Correo:
                            raise ValueError("error falta el @")
                        print(f"correo valido {Correo}")
                    except ValueError as ve:
                        print(ve)
                    clientes.crearClientes(Id,Nombre,Telefono,Correo)
                    break
            case 4:
                Facturacion.Facturacion()
            case 5:
                Facturacion.reporte_de_ventas()
            case 0:
                print("adios")
                break
    except ValueError:
            print("ERROR de valor (solo numeros)")       

from datetime import datetime
import Facturacion

facturas = {}

def Ranking_productos (inicio, fin ):
    with open("Factura_txt", "r") as f: 
        Contenido = f.read 
        facturas_filtradas[inicio] = Contenido
    try:
        fecha_inicio= datetime.strptime(inicio, "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(fin , "%Y-%m-%d").date()
    except ValueError:
        print("Formato de fecha inválido. Use YYYY-MM-DD")
        return
    facturas_filtradas = {}
    for clave, valor in facturas.items():
        if valor["fecha"] == fecha_inicio:
            facturas_filtradas[clave] = valor
        if not facturas_filtradas:
          print(f"No hay facturas registradas para la fecha {fecha_inicio}")
        if valor["fecha"] == fecha_fin:
            facturas_filtradas[clave]  = valor
        if not facturas_filtradas:
          print(f"No hay facturas registradas para la fecha {fecha_fin}")
    with open("Factura_txt", "r") as f: 
        Contenido = f.read 
        print (Contenido)  
  
inicio = input("Ingrese la fecha inicial del rango que desea asignar (YYYY-MM-DD): ")
fin  = input("Ingrese la fecha del final del rango que desea asignar reporte (YYYY-MM-DD): ")
Ranking_productos(inicio , fin)
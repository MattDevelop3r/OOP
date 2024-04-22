from gestorVentas import GestorVentas

def menu():
    print("1. Ingresar venta")
    print("2. Total de facturación de una sucursal")
    print("3. Sucursal que más facturó en un día")
    print("4. Sucursal con menos facturación en la semana")
    print("5. Total facturado por todas las sucursales en la semana")
    print("6. Salir")
    return int(input("Seleccione una opción: "))

gestor = GestorVentas()

while True:
    opcion = menu()
    if opcion == 1:
        dia = int(input("Ingrese el día de la semana (1-7): "))
        sucursal = int(input("Ingrese el número de sucursal (1-5): "))
        importe = float(input("Ingrese el importe de la factura: "))
        gestor.ingresar_venta((dia-1),(sucursal-1), importe)
    elif opcion == 2:
        sucursal = int(input("Ingrese el número de sucursal (1-5): "))
        total = gestor.total_facturacion_sucursal(sucursal-1)
        print(f"Total facturado por la sucursal {sucursal+1}: {total}")
    elif opcion == 3:
        dia = int(input("Ingrese el día de la semana (1-7): "))
        sucursal = gestor.sucursal_mas_facturo_dia(dia-1)
        print(f"La sucursal que más facturó el día {dia} fue: {sucursal+1}")
    elif opcion == 4:
        sucursal = gestor.sucursal_menos_facturacion_semana()
        print(f"La sucursal con menos facturación en la semana fue: {sucursal+1}")
    elif opcion == 5:
        total = gestor.total_facturado_semana()
        print(f"Total facturado por todas las sucursales en la semana: {total}")
    elif opcion == 6:
        break
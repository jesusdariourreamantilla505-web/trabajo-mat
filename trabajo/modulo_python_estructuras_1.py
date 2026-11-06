dias = ["Lunes", "Martes", "Miercoles", "Jueves",
        "Viernes", "Sabado", "Domingo"]

ventas = []
precios = []

print("VENTAS SEMANALES DE SWEETCO")

for i in range(5):
    print("\nProducto", i + 1)
    fila = []

    for j in range(7):
        cantidad = int(input(
            "Ventas del " + dias[j] + ": "
        ))
        fila.append(cantidad)

    ventas.append(fila)

    precio = float(input("Precio del producto: "))
    precios.append(precio)

ingresos_productos = []

for i in range(5):
    total = 0

    for j in range(7):
        total += ventas[i][j] * precios[i]

    ingresos_productos.append(total)

ingresos_dias = []

for j in range(7):
    total = 0

    for i in range(5):
        total += ventas[i][j] * precios[i]

    ingresos_dias.append(total)

print("\nMATRIZ DE VENTAS")
for fila in ventas:
    print(fila)

print("\nINGRESOS POR PRODUCTO")
for i in range(5):
    print("Producto", i + 1, ":", ingresos_productos[i])

print("\nINGRESOS POR DIA")
for j in range(7):
    print(dias[j], ":", ingresos_dias[j])

mayor_producto = ingresos_productos.index(
    max(ingresos_productos)
)

mayor_dia = ingresos_dias.index(max(ingresos_dias))

print("\nRESULTADOS")
print("Producto con mayores ingresos:",
      mayor_producto + 1)
print("Dia con mayores ingresos:", dias[mayor_dia])
print("Ingresos totales de la semana:",
      sum(ingresos_productos))
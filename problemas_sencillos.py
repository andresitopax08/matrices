def calcularTotal(precio, cantidad):
    total = precio * cantidad
    return total

if __name__ == "__main__":

    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    cantidad_producto = int(input("Ingrese la cantidad de productos: "))
    total_a_pagar = calcularTotal(precio_unitario, cantidad_producto)

print(f"El precio unitario es: {precio_unitario}")
print(f"El total a pagar es: {total_a_pagar}")
print("Gracias por su compra.")


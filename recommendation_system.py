
# Sistema de recomendaciones
# Proyecto de Inteligencia Artificial

productos = [
    {"nombre": "Python para principiantes", "categoria": "Educacion", "precio": 10000},
    {"nombre": "Curso de turismo", "categoria": "Educacion", "precio": 15000},
    {"nombre": "Audifonos Bluetooth", "categoria": "Tecnologia", "precio": 20000},
    {"nombre": "Mouse inalambrico", "categoria": "Tecnologia", "precio": 12000},
    {"nombre": "Guia de viajes", "categoria": "Turismo", "precio": 8000},
    {"nombre": "Mochila de viaje", "categoria": "Turismo", "precio": 25000}
]

def recomendar_productos(categoria, presupuesto):
    recomendaciones = []

    for producto in productos:
        if (producto["categoria"].lower() == categoria.lower()
                and producto["precio"] <= presupuesto):
            recomendaciones.append(producto)

    return recomendaciones


def main():
    print("=== SISTEMA DE RECOMENDACIONES ===")
    print("Categorias disponibles:")
    print("Educacion, Tecnologia, Turismo")

    categoria = input("Que categoria te interesa? ")
    
    try:
        presupuesto = float(input("Cual es tu presupuesto? "))

        resultados = recomendar_productos(categoria, presupuesto)

        print("\n=== RECOMENDACIONES ===")

        if resultados:
            for producto in resultados:
                print(
                    producto["nombre"],
                    "- Precio: $",
                    producto["precio"]
                )
        else:
            print("No se encontraron recomendaciones.")

    except ValueError:
        print("Por favor, ingresa un presupuesto valido.")


if __name__ == "__main__":
    main()

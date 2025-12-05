from datetime import date
from pathlib import Path

from alquileres import (
    Alquiler,
    alquileres_mas_largos,
    cliente_mayor_facturacion,
    indexar_por_estacion,
    lee_alquileres,
    media_dias_entre_alquileres,
    servicio_top_por_mes,
    total_facturado,
)


BASE = Path(__file__).resolve().parent.parent
DATASET = BASE / "data" / "alquileres.csv"


def cargar() -> list[Alquiler]:
    return lee_alquileres(DATASET)


def main() -> None:
    alquileres = cargar()
    print(f"Total alquileres: {len(alquileres)}")
    print("Tres primeros:")
    for a in alquileres[:3]:
        print("    ", a)

    print("\nTotal facturado febrero 2024:")
    print(
        total_facturado(
            alquileres,
            fecha_ini=date(2024, 2, 1),
            fecha_fin=date(2024, 2, 29),
        )
    )

    print("\nAlquileres más largos:")
    print(alquileres_mas_largos(alquileres, n=3))

    print("\nCliente mayor facturación con casco o candado:")
    print(
        cliente_mayor_facturacion(
            alquileres, servicios={"casco", "candado"}
        )
    )

    print("\nServicio top por mes (todas estaciones):")
    print(servicio_top_por_mes(alquileres))

    print("\nMedia días entre alquileres:")
    print(media_dias_entre_alquileres(alquileres))

    print("\nIndexado por estación (claves):")
    print(list(indexar_por_estacion(alquileres).keys()))


if __name__ == "__main__":
    main()

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime
from typing import NamedTuple


class Alquiler(NamedTuple):
    nombre: str
    dni: str
    fecha_inicio: date
    fecha_fin: date
    estacion: str
    bici_tipo: str
    precio_dia: float
    servicios: list[str]


def parse_fecha(cadena: str) -> date:
    """Convierte una fecha ISO (YYYY-MM-DD) a date."""
    return datetime.strptime(cadena, "%Y-%m-%d").date()


def lee_alquileres(ruta: str) -> list[Alquiler]:
    """Lee el CSV y devuelve una lista de Alquiler."""
    raise NotImplementedError


def total_facturado(
    alquileres: list[Alquiler],
    fecha_ini: date | None = None,
    fecha_fin: date | None = None,
) -> float:
    """Suma lo cobrado en el rango de fechas (fecha_inicio)."""
    raise NotImplementedError


def alquileres_mas_largos(
    alquileres: list[Alquiler],
    n: int = 3,
) -> list[tuple[str, date]]:
    """Top-N de alquileres más largos (nombre, fecha_inicio)."""
    raise NotImplementedError


def cliente_mayor_facturacion(
    alquileres: list[Alquiler],
    servicios: set[str] | None = None,
) -> tuple[str, float]:
    """Cliente con mayor gasto opcionalmente filtrando por servicios."""
    raise NotImplementedError


def servicio_top_por_mes(
    alquileres: list[Alquiler],
    estaciones: set[str] | None = None,
) -> dict[str, str]:
    """Servicio más contratado por mes (fecha_inicio), filtrando estaciones opcionalmente."""
    raise NotImplementedError


def media_dias_entre_alquileres(alquileres: list[Alquiler]) -> float:
    """Media de días entre alquileres consecutivos (por fecha_inicio)."""
    raise NotImplementedError


def indexar_por_estacion(alquileres: list[Alquiler]) -> dict[str, list[Alquiler]]:
    """Diccionario estacion -> lista de Alquiler."""
    raise NotImplementedError


if __name__ == "__main__":
    # Espacio para pruebas rápidas
    import pathlib

    ruta = pathlib.Path(__file__).resolve().parent.parent / "data" / "alquileres.csv"
    print(f"Dataset: {ruta}")

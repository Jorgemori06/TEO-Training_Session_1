from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime
from typing import NamedTuple
import csv


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
    alquileres=[]
    with open (ruta, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for linea in lector:
            nombre=linea[0]
            dni=linea[1]
            fecha_inicio=parse_fecha(linea[2])
            fecha_fin=parse_fecha(linea[3])
            estacion=linea[4]
            bici_tipo=linea[5]
            precio_dia=float(linea[6])
            servicios=linea[7].split(',')
            alquiler=Alquiler(nombre,dni,fecha_inicio,fecha_fin,estacion,bici_tipo,precio_dia,servicios)
            alquileres.append(alquiler)
    return alquileres


def total_facturado(alquileres: list[Alquiler],fecha_ini: date | None = None,fecha_fin: date | None = None) -> float:
    facturado=0
    for alquiler in alquileres:
        if alquiler.fecha_inicio<fecha_ini and alquiler.fecha_fin>fecha_fin or fecha_ini==None:
            facturado+=alquiler.precio_dia*(alquiler.fecha_fin-fecha_ini)

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

from __future__ import annotations

import csv
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


MESES = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}


def parse_fecha(cadena: str) -> date:
    return datetime.strptime(cadena, "%Y-%m-%d").date()


def dias(alquiler: Alquiler) -> int:
    return (alquiler.fecha_fin - alquiler.fecha_inicio).days


def lee_alquileres(ruta: str) -> list[Alquiler]:
    res: list[Alquiler] = []
    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, dni, f_ini, f_fin, estacion, bici_tipo, precio, servicios in lector:
            servicios_lst = (
                [s.strip() for s in servicios.split(",") if s.strip()]
                if servicios
                else []
            )
            res.append(
                Alquiler(
                    nombre=nombre,
                    dni=dni,
                    fecha_inicio=parse_fecha(f_ini),
                    fecha_fin=parse_fecha(f_fin),
                    estacion=estacion,
                    bici_tipo=bici_tipo,
                    precio_dia=float(precio),
                    servicios=servicios_lst,
                )
            )
    return res


def total_facturado(
    alquileres: list[Alquiler],
    fecha_ini: date | None = None,
    fecha_fin: date | None = None,
) -> float:
    total = 0.0
    for a in alquileres:
        if (fecha_ini is None or fecha_ini <= a.fecha_inicio) and (
            fecha_fin is None or a.fecha_inicio <= fecha_fin
        ):
            total += dias(a) * a.precio_dia
    return total


def alquileres_mas_largos(
    alquileres: list[Alquiler],
    n: int = 3,
) -> list[tuple[str, date]]:
    ordenadas = sorted(alquileres, key=dias, reverse=True)
    return [(a.nombre, a.fecha_inicio) for a in ordenadas[:n]]


def cliente_mayor_facturacion(
    alquileres: list[Alquiler],
    servicios: set[str] | None = None,
) -> tuple[str, float]:
    total_por_cliente: defaultdict[str, float] = defaultdict(float)
    for a in alquileres:
        if servicios is None or servicios.intersection(a.servicios):
            total_por_cliente[a.dni] += dias(a) * a.precio_dia
    return max(total_por_cliente.items(), key=lambda t: t[1])


def servicio_top_por_mes(
    alquileres: list[Alquiler],
    estaciones: set[str] | None = None,
) -> dict[str, str]:
    servicios_mes: defaultdict[str, Counter[str]] = defaultdict(Counter)
    for a in alquileres:
        if estaciones is not None and a.estacion not in estaciones:
            continue
        if not a.servicios:
            continue
        mes = MESES[a.fecha_inicio.month]
        servicios_mes[mes].update(a.servicios)
    resultado: dict[str, str] = {}
    for mes, conteo in servicios_mes.items():
        if conteo:
            resultado[mes] = conteo.most_common(1)[0][0]
    return resultado


def media_dias_entre_alquileres(alquileres: list[Alquiler]) -> float:
    if len(alquileres) < 2:
        return 0.0
    ordenadas = sorted(alquileres, key=lambda a: a.fecha_inicio)
    diferencias = [
        (a2.fecha_inicio - a1.fecha_inicio).days
        for a1, a2 in zip(ordenadas, ordenadas[1:])
    ]
    return sum(diferencias) / len(diferencias)


def indexar_por_estacion(alquileres: list[Alquiler]) -> dict[str, list[Alquiler]]:
    idx: defaultdict[str, list[Alquiler]] = defaultdict(list)
    for a in alquileres:
        idx[a.estacion].append(a)
    return dict(idx)


if __name__ == "__main__":
    import pathlib

    ruta = pathlib.Path(__file__).resolve().parent.parent / "data" / "alquileres.csv"
    for a in lee_alquileres(ruta)[:3]:
        print(a)

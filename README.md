# Fundamentos de Programación
## Práctica de patrones de examen: Alquiler de bicis

**Objetivo**: que el alumno practique los patrones de lectura de CSV, modelado con `NamedTuple`, filtrado opcional, contadores, ordenaciones, sets, recorridos consecutivos, reutilización de helpers e índices.

## Contexto

Dispones de datos de alquileres de bicicletas en varias estaciones de una ciudad en un fichero CSV codificado en UTF-8. Cada línea contiene: el nombre y DNI del cliente, la fecha de inicio y fin del alquiler, la estación, el tipo de bici, el precio por día y una lista de servicios adicionales contratados (separados por comas, pueden estar vacíos).

Ejemplo de líneas en `data/alquileres.csv`:

```
nombre,dni,fecha_inicio,fecha_fin,estacion,bici_tipo,precio_dia,servicios
Ana Paredes,12345678A,2024-02-01,2024-02-04,Central,Urbana,15.5,"cesta,candado"
Luis Moya,87654321B,2024-02-03,2024-02-05,Rio,MTB,18.0,"casco"
```

## NamedTuple obligatoria

```python
from typing import NamedTuple
from datetime import date

class Alquiler(NamedTuple):
    nombre: str
    dni: str
    fecha_inicio: date
    fecha_fin: date
    estacion: str
    bici_tipo: str
    precio_dia: float
    servicios: list[str]
```

## Observaciones

- Las fechas están en formato `YYYY-MM-DD`.
- Los servicios se separan por comas; si no hay servicios, el campo viene vacío.
- El dataset **no** está ordenado por fecha.
- El número de días de un alquiler es `(fecha_fin - fecha_inicio).days`.

## Estructura recomendada del proyecto

* **/src**: módulos Python del proyecto.
    * **alquileres.py**: implementa las funciones pedidas.
    * **alquileres_test.py**: pruebas y `main` para lanzar los tests.
* **/data**: dataset del proyecto.
    * **alquileres.csv**: alquileres de bicicletas.

## Ejercicios a implementar (en `src/alquileres.py`)

1. **lee_alquileres**: lee el CSV y devuelve una lista de `Alquiler`. (1 punto)

    ```python
    def lee_alquileres(ruta: str) -> list[Alquiler]: ...
    ```

2. **total_facturado**: suma lo cobrado (días * precio_dia) filtrando por fecha_inicio en el rango `[fecha_ini, fecha_fin]`. Si alguno es `None`, no se limita por ese extremo. (1 punto)

    ```python
    def total_facturado(alquileres: list[Alquiler], fecha_ini: date | None = None, fecha_fin: date | None = None) -> float: ...
    ```

3. **alquileres_mas_largos**: devuelve las `n` tuplas `(nombre, fecha_inicio)` con más días de alquiler, ordenadas de mayor a menor. (1 punto)

    ```python
    def alquileres_mas_largos(alquileres: list[Alquiler], n: int = 3) -> list[tuple[str, date]]: ...
    ```

4. **cliente_mayor_facturacion**: dado un conjunto de servicios (o `None`), devuelve `(dni, total)` del cliente con mayor facturación considerando solo alquileres que incluyan alguno de esos servicios. (1,5 puntos)

    ```python
    def cliente_mayor_facturacion(alquileres: list[Alquiler], servicios: set[str] | None = None) -> tuple[str, float]: ...
    ```

5. **servicio_top_por_mes**: devuelve un diccionario mes → servicio más demandado (por número de alquileres) usando la fecha de inicio. Se pueden filtrar estaciones con un conjunto (`None` para todas). (2 puntos)

    ```python
    def servicio_top_por_mes(alquileres: list[Alquiler], estaciones: set[str] | None = None) -> dict[str, str]: ...
    ```

6. **media_dias_entre_alquileres**: media de días entre alquileres consecutivos en el tiempo (usa `fecha_inicio`). (1,5 puntos)

    ```python
    def media_dias_entre_alquileres(alquileres: list[Alquiler]) -> float: ...
    ```

7. **indexar_por_estacion**: construye y devuelve un diccionario `estacion -> list[Alquiler]`. (0,5 puntos)

    ```python
    def indexar_por_estacion(alquileres: list[Alquiler]) -> dict[str, list[Alquiler]]: ...
    ```

Puedes añadir funciones auxiliares (`dias`, normalización de servicios, etc.) y tests adicionales. Usa los patrones del tema 10: `Counter`, `defaultdict`, filtros opcionales, ordenaciones con `key`, sets y recorridos con `zip`.

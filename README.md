Proyecto Spark Peaje

Análisis en tiempo real de datos de peaje utilizando Apache Spark y Kafka

-
Descripción del problema

En los peajes modernos, el registro de vehículos genera grandes volúmenes de datos en tiempo real. Analizar esta información permite conocer el flujo vehicular, detectar congestiones, estimar ingresos por categoría y optimizar la operación.

El objetivo de este proyecto es **simular un sistema de procesamiento de datos de peaje en tiempo real**, utilizando las tecnologías **Apache Kafka** y **Apache Spark Streaming**, para analizar los datos conforme son generados.

---

Conjunto de datos

El conjunto de datos simulado representa el paso de vehículos por diferentes estaciones de peaje e incluye campos como:

| Campo | Descripción |
|-------|--------------|
| id_peaje | Identificador del peaje |
| tipo_vehiculo | Categoría del vehículo (liviano, pesado, moto, etc.) |
| valor_peaje | Tarifa pagada por el vehículo |
| hora_registro | Hora exacta de paso |
| placa | Placa del vehículo |

Los datos se generan mediante un **productor Kafka (productor_peaje.py)** y son consumidos en tiempo real por **Spark Streaming (consumidor_peaje.py)**.



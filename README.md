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

Arquitectura 

1. **Kafka Producer (`productor_peaje.py`)**  
   Genera datos simulados del flujo vehicular y los envía a un *topic* de Kafka.  

2. **Kafka Broker y Zookeeper**  
   Administran la mensajería y la coordinación de los eventos.  

3. **Spark Streaming (`consumidor_peaje.py`)**  
   Consume los mensajes del topic Kafka y realiza análisis en tiempo real como:
   - Conteo de vehículos por tipo
   - Promedio de valor pagado
   - Identificación de horas pico

4. **Salida de resultados**  
   Los resultados procesados se visualizan en consola o pueden almacenarse en archivos CSV para su análisis posterior.

---

 Tecnologías utilizadas

- **Apache Kafka 3.7.0**
- **Apache Spark 3.x (PySpark)**
- **Python 3.10**
- **VirtualBox / Ubuntu**
- **Git & GitHub**









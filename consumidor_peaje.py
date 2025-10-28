from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

# Crear sesión de Spark con soporte para Kafka
spark = SparkSession.builder \
    .appName("ConsumoPeajeKafka") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Definir esquema de los datos JSON que vienen del productor
schema = StructType() \
    .add("vehiculo", StringType()) \
    .add("placa", StringType()) \
    .add("hora", StringType()) \
    .add("valor", IntegerType())

# Leer el flujo de datos desde Kafka
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "peaje") \
    .load()

# Convertir los valores binarios en JSON legible
df = df_raw.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Mostrar los datos en consola en tiempo real
consulta = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

consulta.awaitTermination()

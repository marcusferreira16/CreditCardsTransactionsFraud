from pyspark.sql import SparkSession
from pyspark.sql.functions import col, isnan, when, count, median, mean, length
from pyspark.sql.types import IntegerType, StringType, FloatType, DateType

# Inicializa uma SparkSession com um nome de aplicação descritivo
spark = SparkSession.builder \
    .appName("CreditCardTransactions") \
    .master('local[*]') \
    .getOrCreate()
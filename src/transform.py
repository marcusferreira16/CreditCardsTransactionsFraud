import config
from utils.functions import spark, median, length, col
from extract import extract_database_kaggle

# spark.stop()

transacoes = extract_database_kaggle(spark, 'ealtman2019/credit-card-transactions')

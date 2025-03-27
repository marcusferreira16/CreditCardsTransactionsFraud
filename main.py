from utils.functions import extract_database_kaggle, spark

df = extract_database_kaggle(spark, 'ealtman2019/credit-card-transactions')
df.show()

spark.stop()
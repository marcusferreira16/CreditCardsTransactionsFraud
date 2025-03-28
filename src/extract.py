import config
import kagglehub
from utils.functions import spark

# Baixa a base do Kaggle e retorna o DataFrame
def extract_database_kaggle(spark, caminho_database: str):
    path = kagglehub.dataset_download(caminho_database)
    df = spark.read.option('delimiter', ',').option("header", True).csv(path)
    return df
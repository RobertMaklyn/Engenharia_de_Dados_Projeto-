from pyspark.sql.functions import *

df_bronze_emailaddress = spark.table("bronze.person_emailaddress")
df_bronze_emailaddress.write.format("delta").mode("overwrite").saveAsTable("prata.person_emailaddress")
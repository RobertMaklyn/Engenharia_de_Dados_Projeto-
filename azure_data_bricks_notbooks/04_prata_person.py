from pyspark.sql.functions import *

df_bronze_person = spark.table("bronze.person_person")
df_prata_person = df_bronze_person.filter(col("Title").isNotNull())
df_prata_person.write.format("delta").mode("overwrite").saveAsTable("prata.person_person")
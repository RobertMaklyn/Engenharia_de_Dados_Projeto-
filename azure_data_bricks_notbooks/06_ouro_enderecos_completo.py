from pyspark.sql.functions import *

df_prata_person = spark.table("prata.person_person")
df_prata_emailaddress = spark.table("prata.person_emailaddress")

df_ouro_endereco_completo = df_prata_person.join(
    df_prata_emailaddress,
    df_prata_person.BusinessEntityID == df_prata_emailaddress.BusinessEntityID
).select(
    df_prata_person.BusinessEntityID,
    df_prata_person.FirstName,
    df_prata_person.LastName,
    df_prata_emailaddress.EmailAddress
)

df_ouro_endereco_completo.write.format("delta").mode("overwrite").saveAsTable("ouro.endereco_completo")
df_ouro_endereco_completo.display()

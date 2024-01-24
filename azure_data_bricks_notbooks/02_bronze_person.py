table = 'person_person'
database_name = 'bronze'

df_person = spark.read.parquet(f'{folder_path}/{table}.parquet')

df_person.write.format('delta')\
    .mode('overwrite')\
    .option('overwriteSchema', True)\
    .saveAsTable(f'{database_name}.{table}')

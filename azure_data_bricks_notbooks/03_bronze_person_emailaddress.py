table = 'person_emailaddress'
database_name = 'bronze'

folder_path = '/mnt/lakehouseprojetoaw/landing-zone/projeto1'

df_person = spark.read.parquet(f'{folder_path}/{table}.parquet')

df_person.write.format('delta')\
    .mode('overwrite')\
    .option('overwriteSchema', True)\
    .saveAsTable(f'{database_name}.{table}')

scope = "adls-scope-kv"
key = "adls"
storage_account_name = "lakehouseprojetoaw"
container_name = "landing-zone"
mount_point = '/mnt/landing-zone'
connect_str = dbutils.secrets.get(scope=scope, key=key)

if not any(mount.mountPoint == mount_point for mount in dbutils.fs.mounts()):
  
  connect_str = dbutils.secrets.get(scope=scope, key=key)

  dbutils.fs.mount(
    source=f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net",
    mount_point=mount_point,
    extra_configs={
      f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": connect_str
    }
  )
  print(f"Mounted {mount_point}")
else:
  print(f"{mount_point} is already mounted")
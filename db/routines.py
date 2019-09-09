import ix.db.schema_ix as db_ix


def ix_dx_transaction(method, args):
  conn, cursor = db_ix.getdb()

  method(cursor, args)
  conn.commit()

  cursor.close()
  conn.close()


def delete_backups(cursor):
  cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.tables WHERE "
                 "TABLE_NAME LIKE '%_bak';")

  result = cursor.fetchall()
  for table_name in result:
    print(f"Dropping: {table_name[0]}")
    cursor.execute(f"DROP TABLE `altairix`.`{table_name[0]}`;")


def truncate_tables(cursor, tables):

  for table in tables:
    print(f"Truncating table: {table}")
    cursor.execute(f"TRUNCATE TABLE `{table}`;")


def backup_tables(cursor, tables):

  for table in tables:
    print(f"Duplicating table: {table}")
    cursor.execute(f"DROP TABLE IF EXISTS {table}_bak;")
    cursor.execute(f"CREATE TABLE {table}_bak LIKE {table};")
    cursor.execute(f"INSERT {table}_bak SELECT * FROM {table};")


def restore_tables(cursor, tables):

  for table in tables:
    print(f"Restoring table: {table}")
    cursor.execute(f"TRUNCATE TABLE {table};")
    cursor.execute(f"INSERT {table} SELECT * FROM {table}_bak;")


def delete_duplicates(cursor, args):
  cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.tables WHERE "
                 "TABLE_NAME LIKE '%_bak';")

  results = cursor.fetchall()
  for res in results:
    print(f"Dropping: {res[0]}")
    cursor.execute(f"DROP TABLE `altairix`.`{res[0]}`;")

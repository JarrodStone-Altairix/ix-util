import click
from ix.db.schema_ix import cursor, conn, close


@click.group()
def cli():
  pass


@cli.command()
def delete_bak():
  cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.tables WHERE "
                 "TABLE_NAME LIKE '%_bak';")

  result = cursor.fetchall()
  for table_name in result:
    print(f"Dropping: {table_name[0]}")
    cursor.execute(f"DROP TABLE `altairix`.`{table_name[0]}`;")

  close()


@cli.command()
@click.argument("tables", nargs=-1)
def truncate(tables):
  for table in tables:
    print(f"Truncating table: {table}")
    cursor.execute(f"TRUNCATE TABLE `{table}`;")


@cli.command()
@click.argument("tables", nargs=-1)
def backup(tables):
  for table in tables:
    print(f"Backing up table: {table}")
    cursor.execute(f"DROP TABLE IF EXISTS {table}_bak;")
    cursor.execute(f"CREATE TABLE {table}_bak LIKE {table};")
    cursor.execute(f"INSERT {table}_bak SELECT * FROM {table};")

  conn.commit()
  close()


@cli.command()
@click.argument("tables", nargs=-1)
def restore(tables):
  for table in tables:
    print(f"Restoring table: {table}")
    cursor.execute(f"TRUNCATE TABLE {table};")
    cursor.execute(f"INSERT {table} SELECT * FROM {table}_bak;")

  conn.commit()
  close()


if __name__ == "__main__":
  cli()

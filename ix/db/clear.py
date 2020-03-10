import ix.db.ara as aradb


def clear_recursively(uid_name, uid_value, root, *children):
  db = aradb.getdb()

  cursor = db.cursor()

  for child in children:
    cursor.execute(
        f"""DELETE from altairix.{child} where {uid_name}='{uid_value}'""")
    print(f"Table - {child}: {cursor.rowcount} row(s) affected.")

  cursor.execute(
      f"""DELETE from altairix.{root} where {uid_name}='{uid_value}'""")
  print(f"Table - {root}: {cursor.rowcount} row(s) affected.")

  db.commit()

  cursor.close()
  db.close()

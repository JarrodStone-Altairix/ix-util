import mysql.connector
from config.db import Config as Cfg


conn = mysql.connector.connect(
    host=Cfg.HOST,
    user=Cfg.USER,
    passwd=Cfg.PASSW,
    database=Cfg.DB
)
cursor = conn.cursor()


def close():
  cursor.close()
  conn.close()

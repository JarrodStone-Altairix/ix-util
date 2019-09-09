import mysql.connector
import ix.config as config
import ix.parse.properties as propFile


_prop = propFile.loadPropFile(config.bxServerFile())
conn = mysql.connector.connect(
    host=_prop['dbInstanceNm'],
    user=_prop['dbUserNm'],
    passwd=_prop['dbUserPassw'],
    database=_prop['dbSchemaNm']
)
cursor = conn.cursor()


def close():
  cursor.close()
  conn.close()

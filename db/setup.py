import mysql.connector
import ix.config as config
import ix.parse.properties as propFile

pwHash = 'DbS6UPgGpb52+N8M25NMIp91TtGBFfXqm002WQ=='
properties = propFile.loadPropFile(config.BxServerFile)

mydb = mysql.connector.connect(
  host=properties['dbInstanceNm'],
  user=properties['dbUserNm'],
  passwd=properties['dbUserPassw'],
  database=properties['dbSchemaNm']
)

myCursor = mydb.cursor()
myCursor.execute(f"""UPDATE arausr SET STATUS_TCD ='A', USER_PASSW = '{pwHash}' WHERE LOGIN_ID ='ixadmin';""")
myCursor.execute(f"""UPDATE arausr SET STATUS_TCD ='A', USER_PASSW = '{pwHash}' WHERE LOGIN_ID ='ixpc';""")
myCursor.execute(f"""UPDATE arausr SET STATUS_TCD ='A', USER_PASSW = '{pwHash}' WHERE LOGIN_ID ='ixteacher';""")
myCursor.execute(f"""UPDATE arausr SET STATUS_TCD ='A', USER_PASSW = '{pwHash}' WHERE LOGIN_ID ='ixSuper';""")
myCursor.execute(f"""UPDATE arausr SET STATUS_TCD ='A', USER_PASSW = '{pwHash}' WHERE LOGIN_ID ='ixsaa';""")
myCursor.execute(f"""UPDATE arastud SET STUDENT_PASSW = '{pwHash}' WHERE STUDENT_UID ='01001-005666';""")

mydb.commit()
# print(myCursor.rowcount, "record(s) affected.")

myCursor.close()
mydb.close()
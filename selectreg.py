print("Iniciando con MySql PRUEBA 3RE COMMIT")
import mysql.connector
miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='lara', db='prueba' )
cur = miConexion.cursor()
cur.execute( "SELECT * FROM usuarios" )
for correo,clave in cur.fetchall() :
  print(correo,clave)
miConexion.close()
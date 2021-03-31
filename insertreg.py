print("Iniciando con MySql")
import mysql.connector
import time
mydb = mysql.connector.connect(host='localhost', user='root',password='lara', database='prueba')

mycursor = mydb.cursor()
print("Concetando con MySql")

#sql = "insert into prueba.usuarios(correo, clave) values (%s,%s)" 
#val = ("mi.desarrolloalexa@gmail.com", "fbdesarrollo")
#mycursor.execute(sql, val)
#sql = "insert into prueba.usuarios(correo, clave) values (%s,%s)" 
#val = ("christian.desarrollosoft@gmail.com", "Funcion1")
#mycursor.execute(sql, val)
sql = "insert into prueba.usuarios(correo, clave) values (%s,%s)" 
val = ("leasenc@yahoo.com", "desarrollo2020")
mycursor.execute(sql, val)
sql = "insert into prueba.usuarios(correo, clave) values (%s,%s)" 
val = ("gzambrano85@protonmail.com", "xS4dZ1kB5mB7qC8t")
mycursor.execute(sql, val)
mydb.commit()
mydb.close()
print("Ejewcuto con MySql")
print(mycursor.rowcount, "record inserted")




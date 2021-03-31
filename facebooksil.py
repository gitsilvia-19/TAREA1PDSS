from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("Iniciando con Selenium")
import mysql.connector
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lara",
  database="prueba"
)
print("Iniciando con MySql")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM usuarios")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  correo=x[0]
  contraseña=x[1]
  driver = webdriver.Firefox()
  time.sleep(5)
  driver.get("https://www.facebook.com")

  #correo="christian.desarrollosoft@gmail.com"
  #contraseña="Funcion1"
  print("Abriendo FaceBook", correo)
  time.sleep(5) #espera que cargue la página
  elem = driver.find_element_by_id("email")
  elem.clear()
  elem.send_keys(correo)

  elem = driver.find_element_by_id("pass")
  elem.clear() 
  elem.send_keys(contraseña)
  
  time.sleep(5)
  elem.send_keys(Keys.RETURN)
  #elem = driver.find_element_by_xpath('//*[@id="u_0_b"]')
  #elem.click()
  time.sleep(10)
  driver.get("https://www.facebook.com/christian.desarrollo.35")
  time.sleep(5)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(5)
  postbutton = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div/span[1]/div/div/span/div[1]/div')
  postbutton.click()  #like

  postbutton = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div[1]/div/div/div/form/div/div/div[2]/div')
  postbutton.click()
  postbutton.send_keys("Prueba comentario")
  postbutton.send_keys(Keys.RETURN)
  postbutton =driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/span/div/div[1]/img')
  postbutton.click()
  #driver.execute_script("window.scrollTo(0, 100)")
  postbutton=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]/div[1]/div')
  postbutton.click()
  time.sleep(3)
  driver.close()
mydb.close()

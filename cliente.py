#client
# 21838024  Javier González

#Variables
host = 'localhost'
port = 8050
#Se importa el módulo
import socket

#Creación de un objeto socket (lado cliente)
obj = socket.socket()

#Conexión con el servidor. Parametros: la IP (puede ser del tipo 192.168.1.1 o localhost) y el puerto que utilizamos
obj.connect((host, port))
print("Conectado al servidor")

#Creamos un bucle para mantener la conexion
while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    mens = input("Introduzca su numero de expediente: ")
    #Con send, enviamos el mensaje al servidor
    obj.send(mens.encode('ascii'))
    #recibimos la contestacion del servidor, diciendo que ha sido recibido
    recibido = obj.recv(1024)
    print(recibido)

#Cerramos la instancia del objeto servidor
obj.close()

#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Conexión cerrada")
//Checked

#server
# 21838024  Javier González

#Se importa el módulo
import socket

#instanciamos el objeto para utilizar socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Puerto y servidor que debe quedarse a la espera
ser.bind(('localhost', 8050))
print("esta activo")
#Conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(1)

#Instanciamos un objeto cli (socket cliente) para recibir datos de la clase cliente
cli, addr = ser.accept()
1838024
while True:
    #Recibimos el mensaje. Por parametro la cantidad de bytes que se pueden recibir
    recibido = cli.recv(1024)

    #forzamos el paso de bytes a int
    mInt = int(recibido)

    #Si se reciben datos nos muestra el int(en este caso el expediente) multiplicado por 2
    print((mInt*2))

    #Devolvemos el mensaje al cliente
    msg_toSend=("Numero de expediente recibido")
    cli.send(msg_toSend.encode('ascii'))

#Cerramos la instancia del socket cliente y servidor
cli.close()




    
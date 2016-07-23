#Leer link de variable cola

#Entrar en el link y leer todos los enlaces de la página
    #buscarlink()
#Añadir los enlaces a cola y pasar el enlace analizado a analizados

#Repetir



#Creamos la clase araña, de la que posteriormente se instanciarán tantas como sea posible
class araña():

    #Variables de clase que compartirán todos los bots

    dominio=""
    ruta_espera=""
    ruta_indexados=""
    espera_archivo =""
    indexados_archivo=""
    espera = set()
    indexados = set()

    #Constructor
    def __init__(self):
        rutaEspera = "/" + araña.dominio + "/espera.txt"
        rutaIndexados = "/" + araña.dominio + "/indexados.txt"

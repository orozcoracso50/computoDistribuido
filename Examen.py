#Importar las Libreria
#Green Threath
import gevent.monkey
from urllib2 import urlopen
gevent.monkey.patch_all()
#Tornado
import tornado.ioloop
import sys
from tornado.httpclient import AsyncHTTPClient

#SE Crea el arreglo donde se guardaran los urls
urls = []
#Se creo una clase donde se guardaran los metodos Green que mandaremos a llamar
class Metodos(object):
    #Se creo el metodo GreenT por Green Thread
    def GreenT(self):
        Cantidad = input('Cantidad de Trabajos: ')
        for i in range(Cantidad):
            pag = raw_input('Ingresa los Urls:')
            urls.append(pag)
        def handle_response(response):
            if response.error:
                print("Error:", response.error)
            else:
                url = response.request.url
                data = response.body
                print('{}: {} bytes: {}'.format(url, len(data), data))

        http_client = AsyncHTTPClient()
        for url in urls:
            http_client.fetch(url, handle_response)

        tornado.ioloop.IOLoop.instance().start()

  #Se creo el metodo del CallBack
    def CallBack(self):
        Cantidad = input('Cantidad de Trabajos: ')
        for i in range(Cantidad):
            pag = raw_input('Ingresa los Urls:')
            urls.append(pag)
        def handle_response(response):
            if response.error:
                print("Error:", response.error)
            else:
                url = response.request.url
                data = response.body
                print('{}: {} bytes: {}'.format(url, len(data), data))

        http_client = AsyncHTTPClient()
        for url in urls:
            http_client.fetch(url, handle_response)
        tornado.ioloop.IOLoop.instance().start()

    #Se creo el metodo del MENU
    def MENU(self):
        print (30 * '-')
        print (9* ' ' + "- - MENU - -")
        print (30 * '-')
        print ("1. Estilo Green Thread.")
        print ("2. Estilo callback ")

        Opcion = raw_input('Elige una opcion [1 - 2]: ')
        Opcion = int(Opcion)
        #SE crearon las distintas opciones para los metodos
        if Opcion == 1:
            # se hereda la instancia de la clase metodos y se le denomina como a
            a = Metodos()
            #siendo a hereditaria de Metodos puede tomar los metodos, en este caso el metodo de
            #GreenT
            a.GreenT()

        elif Opcion == 2:
            # se hereda la instancia de la clase metodos y se le denomina como b
            b = Metodos()
            #siendo b hereditaria de Metodos puede tomar los metodos, en este caso el metodo de
            #CallBack
            b.CallBack()

        elif Opcion != 1 & 2:
            print('\nOpcion Invalida')
            Opcion

#Fuera de la clase en el Main se manda a llamar al Menu que ejecutara el codigo englobado en la clase
m = Metodos()
m.MENU()

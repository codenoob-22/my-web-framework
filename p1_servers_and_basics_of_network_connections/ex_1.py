
'''
    excercise - 1>
    Description:
    learning how to write servers with wsgi
'''
#attempt1
# from wsgiref.simple_server import make_server, demo_app

# if __name__ == '__main__':
#     with make_server('', 5000, demo_app) as server:
#         server.serve_forever()


#attempt-2
from twisted.internet.protocol import Protocol

class Echo(Protocol):
    '''
        Protocols class basically does event handling 
        such as when a client is connected to the port. when client
        closes the connection. or sends any messages

        A class of event handling methods for a particular protocol type
    '''
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            "welcome!, there are currently %d open connections \n" %
            (self.factory.numProtocols)
        )

    def connectionLost(self, reason):
        self.factory.numprotocols = self.factory.numProtocols -1
        
    def dataRecieved(self, data):
        self.transport.write(data)




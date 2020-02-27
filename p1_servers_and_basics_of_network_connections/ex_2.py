from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class QOTD(Protocol):
    '''
        created a protocol class  which on connection sends the quote and
        closes the connection

        there are three main events:
        connectionMade - when connection is established, an instance is 
                         created
        dataRecieved- to handle data recieved
        connectionlost - instance is deleted 
    '''
    def connectionMade(self):
        self.transport.write(b'An Apple A Day keeps the doctor away')
        self.transport.loseConnection()
    

class QOTDFactory(Factory):
    '''
        built a factory class which creates a new instance of protocol class
        buildProtocol is called i.e everytime it gets the connection request
    '''
    def buildProtocol(self, addr):
        return QOTD()
        
#binds a socket to a port which uses TCP for listening   
endpoint = TCP4ServerEndpoint(reactor, 8000)

#tells the reactor to handle connections to the endpoint’s address 
# using a particular protocol, 
# but the reactor needs to be running in order for it to do anything.
endpoint.listen(QOTDFactory())
print('server is running')

#starts the reactor and then waits forever for connections to arrive on the 
# port you’ve specified
reactor.run()


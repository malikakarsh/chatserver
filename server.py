from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol

class IChatServ(Protocol):
    def connectionMade(self):
        self.factory.clients.append(self);
	print "Connected Clients are:", self.factory.clients

    def connectionLost(self, reason):
	print "Somebody left" 

    def dataReceived(self, data):
	a = data.split(':')
	print a
	if len(a) > 1:
	    command = a[0]
	    content = a[1]
	
       	    msg = ""
	    if command == "iam":
		koil = content.split('\\n')
                self.name = koil[0]
		msg = self.name + " has joined the room."
	
	    elif command == "msg":
		msg = self.name + " says: " + content
		print msg
	
	    for c in self.factory.clients:
		c.message(msg)

    def message(self,message):
	self.transport.write(message + '\n')

factory = Factory()
factory.clients = []
factory.protocol = IChatServ
reactor.listenTCP(1234, factory)
print "Iphone chat server started" 
reactor.run()





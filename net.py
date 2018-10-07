from core import *
from socketserver import StreamRequestHandler


class Node(StreamRequestHandler):
	
	def __init__(self, request, client_address, server):
		super().__init__(request, client_address, server)

	@ignore(SerializationFailure)
	def handle(self):
		pass


if __name__ == '__main__':
	pass


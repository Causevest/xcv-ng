import json
from core import *
from socketserver import StreamRequestHandler


MAX_CLIENTS = 10
CLIENT_LIST = []


class Server(StreamRequestHandler):
	
	def __init__(self, request, client_address, server):
		super().__init__(request, client_address, server)
	
	@ignore(Exception)
	def handle(self):
		msg = self.rfile.read().decode()
		msg = json.loads(msg)
		msg = Message.from_dict(msg)
		if msg.version != 1:
			return
		if msg.command == 'list':
			sender = msg.arguments[0]
			msg.arguments = CLIENT_LIST
			with client(sender) as c:
				c.send()

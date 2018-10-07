from socket import socket, AF_INET, SOCK_STREAM
from contextlib import contextmanager
from time import time


@contextmanager
def client(target):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect(target)
	yield sock
	sock.close()


def ignore(exception, ret=None):
	def _(old_fx):
		def new_fx(*args, **kwargs):
			try:
				return old_fx(*args, **kwargs)
			except exception:
				return ret
		return new_fx
	return _


def logged(message, rethrow=True):
	def _(old_fx):
		def new_fx(*args, **kwargs):
			print(F'[Enter] [{old_fx.__name__}] {message}')
			now = time()
			try:
				old_fx(*args, **kwargs)
			except Exception as e:
				print(F'[Error] [{old_fx.__name__}] {e}')
				if rethrow:
					raise
			print(F'[Exit ] [{old_fx.__name__}] {time() - now}')
		return new_fx
	return _



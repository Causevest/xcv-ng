from typing import NamedTuple


class BlockChain:
	
	def __init__(self):
		pass
	
	def find_reference(self, ref):
		pass
	
	def reference_used(self, ref):
		pass
	
	def add_block(self, block):
		pass

	@staticmethod
	def instance():
		return BlockChain()

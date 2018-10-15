from construct import *


def verify_transaction(tx: Transaction):
	total_input = 0
	for ti in tx.inputs:
		ref: TxOutput = bc.find_reference(ti.reference)
		if ref is None:
			return False
		if bc.reference_used(ti.reference):
			return False
		total_input += ref.amount
	total_output = [to.amount for to in tx.outputs]
	if total_output != total_input:
		return False
	return True


def verify_block(bl: Block):
	pass


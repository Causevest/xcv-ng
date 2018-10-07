from typing import NamedTuple, List
from uuid import UUID, uuid4
from time import time


class TxInput(NamedTuple):
	sender: UUID
	reference: UUID
	signature: UUID


class TxOutput(NamedTuple):
	receiver: UUID
	amount: int
	reference: UUID = uuid4()


class Transaction(NamedTuple):
	inputs: List[TxInput]
	output: List[TxOutput]
	time_stamp: float = time()


class BlockHeader(NamedTuple):
	previous_hash: UUID
	difficulty: UUID
	solution: UUID
	message: str
	tx_hash: UUID
	time_stamp: float = time()


class Block(NamedTuple):
	header: BlockHeader
	transactions: List[Transaction]


ti = TxInput(uuid4(), uuid4(), uuid4())
to = TxOutput(uuid4(), 100, uuid4())
tx = Transaction([ti], [to])
bh = BlockHeader(uuid4(), uuid4(), uuid4(), 'message', uuid4())
bx = Block(bh, [tx])
by = str(bx)
print(eval(by))

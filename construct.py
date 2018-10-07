from typing import NamedTuple, List, Tuple
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
	outputs: List[TxOutput]
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


def genesis_block(max_amount: int, owners: List[Tuple[UUID, int]]):
	sh = sum([share for oid, share in owners])
	ow = [(oid, int(max_amount*share/sh)) for oid, share in owners]
	ti = [TxInput(UUID(int=0), uuid4(), uuid4())]
	to = [TxOutput(oid, share, uuid4()) for oid, share in ow]
	tx = Transaction(ti, to)
	bh = BlockHeader(uuid4(), uuid4(), uuid4(), 'Dawn of a new world!', uuid4())
	bl = Block(bh, [tx])
	return bl


print(genesis_block(10**12, [(uuid4(), 1)]))

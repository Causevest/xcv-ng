from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ARRAY, Integer, DateTime, String, create_engine


Base = declarative_base()


class Transaction(Base):
    __tablename__ = __qualname__

    amount = Column(Integer)
    inputs = Column(ARRAY(UUID))
    outputs = Column(ARRAY(UUID))
    used_id = Column(UUID)
    signature = Column(UUID)
    reference = Column(UUID, primary_key=True)
    time_stamp = Column(DateTime)


class Block(Base):
    __tablename__ = __qualname__

    height = Column(Integer, primary_key=True)
    tx_hash = Column(UUID)
    message = Column(String)
    solution = Column(UUID)
    prev_hash = Column(UUID)
    difficulty = Column(UUID)
    time_stamp = Column(DateTime)
    transactions = Column(ARRAY(UUID))


class BlockChain:

    def __init__(self):
        self.engine = create_engine('postgresql:///block_chain.db')
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
        self.session = sessionmaker(self.engine)()

    def find_transaction(self, tx_id):
        pass

    def add_transaction(self, tx):
        pass

    def add_block(self, block):
        pass

    def validate_transaction(self, tx):
        pass

    def validate_block(self, block):
        pass


if __name__ == '__main__':
    chain = BlockChain()



import hashlib
import time

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = time.time()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
    
    def calc_hash(self, string):
      sha = hashlib.sha256()
      hash_str = string.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

    def __repr__(self):
        return 'Block is: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)


class BlockChain:
    def __init__(self):
        self.tail = None
    
    def append(self, data):
        if self.tail is None:
            self.tail = Block(data=data, previous_hash = None)
        else:
            self.tail = Block(data=data, previous_hash = self.tail)
    
    def search(self, data):
        if self.tail is None:
            print("BlockChain is empty!")
            return
        
        current_block = self.tail
        while current_block is not None:
            if current_block.data == data:
                return current_block
            current_block = current_block.previous_hash

        return None
    
    def size(self):
        length = 0
        current_block = self.tail

        while current_block is not None:
            current_block = current_block.previous_hash
            length += 1

        return length
    
    def to_list(self):
        block_list = []

        current_block = self.tail
        while current_block is not None:
            block_list.append((current_block.data, current_block.timestamp, current_block.hash))
            current_block = current_block.previous_hash
        
        return block_list



# Testing
chain = BlockChain()
# Test 1
print(chain.size())
# 0
print(chain.to_list())
# []

# Test 2
print("Test 2")
chain.append('prev balance: 0 | cash flow: +200 | current balance: 200')
print(chain.size())
# 1
print("The content of the block chain:")
print(chain.to_list())
# [('prev balance: 0 | cash flow: +200 | current balance: 200', 1601493677.9444437, '5ad4f71bdd9f18dbe5b2b9e23b7bac5e30245352148beccf50e89ff0d52b530d')]


# Test 3
chain.append('my balance: 200 | cash flow: +25 | final balance: 225')
chain.append('my balance: 225 | cash flow: -150 | final balance: 75')
print(chain.size())
# 3
print("The content of the block chain:")
print(chain.to_list())
# [('my balance: 225 | cash flow: -150 | final balance: 75', 1601493677.9444933, '43c4e02af4036f0e750afaf46f196cab7cb671a85f1dd19f2ebdef85e1de9451'), 
# ('my balance: 200 | cash flow: +25 | final balance: 225', 1601493677.944488, 'd633387734b05d47eb2bbb30353a3b5574537556103c61f5659e596b7ebe40ab'), 
# ('prev balance: 0 | cash flow: +200 | current balance: 200', 1601493677.9444437, '5ad4f71bdd9f18dbe5b2b9e23b7bac5e30245352148beccf50e89ff0d52b530d')]

# Test 4
print(chain.search('my balance: 200 | cash flow: +25 | final balance: 225'))
# Block is:
# Data: my balance: 200 | cash flow: +25 | final balance: 225
# Timestamp: 1601493677.944488, 
# Hash: d633387734b05d47eb2bbb30353a3b5574537556103c61f5659e596b7ebe40ab

# Test 5
# Edge case:
print(chain.search('my balance: 200 | cash flow: +100 | final balance: 300'))
# None

# Test 6
chain = BlockChain()
print(chain.search('my balance: 200 | cash flow: +100 | final balance: 300'))
# BlockChain is empty!
# None
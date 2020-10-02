import hashlib
import time

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = time.time()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    
    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = (str(self.timestamp) +
                  str(self.data) +
                  str(self.previous_hash)).encode('utf-8')
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
        all_matched_blocks = []
        while current_block is not None:
            if current_block.data == data:
                all_matched_blocks.append(current_block)
            current_block = current_block.previous_hash

        return all_matched_blocks
    
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
print("Test 1")
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
# [('prev balance: 0 | cash flow: +200 | current balance: 200', 1601584887.291065, 'b90276a461a57c01b89f34db1d97c7bd281ad33f9ed6e099907df8686dabe784')]


# Test 3
chain.append('my balance: 200 | cash flow: +25 | final balance: 225')
chain.append('my balance: 225 | cash flow: -150 | final balance: 75')
print(chain.size())
# 3
print("The content of the block chain:")
print(chain.to_list())
# [('my balance: 225 | cash flow: -150 | final balance: 75', 1601584887.291455, '63a3176266afb5bb22691770407f2ce944e7496f7578bb7a1785db3ac68d247a'), 
#  ('my balance: 200 | cash flow: +25 | final balance: 225', 1601584887.291166, '5fb4396f072225b906bd23eda274968aaebc85e7d5f527a15154a0afc1f5f27d'), 
#  ('prev balance: 0 | cash flow: +200 | current balance: 200', 1601584887.291065, 'b90276a461a57c01b89f34db1d97c7bd281ad33f9ed6e099907df8686dabe784')]

# Test 4
print(chain.search('my balance: 200 | cash flow: +25 | final balance: 225'))
# Block is: 
#  Data: my balance: 200 | cash flow: +25 | final balance: 225 
#  Timestamp: 1601584887.29 
#  Hash: 5fb4396f072225b906bd23eda274968aaebc85e7d5f527a15154a0afc1f5f27d

# Test 5
# Edge case:
print(chain.search('my balance: 200 | cash flow: +100 | final balance: 300'))
# None

# Test 6
chain = BlockChain()
print(chain.search('my balance: 200 | cash flow: +100 | final balance: 300'))
# BlockChain is empty!
# None


# Test 6
chain = BlockChain()
chain.append('some information')
chain.append('some information')
chain.append('some more information')
print(chain.search('some information'))

# [Block is: 
#  Data: some information 
#  Timestamp: 1601587775.61 
#  Hash: 13c889c2544618a2b89d13b2b5f7b6ff52081207c89366d1245e02bf7173d25f, 
#  Block is: 
#  Data: some information 
#  Timestamp: 1601587775.61 
#  Hash: 4955501d47c35a44227396e388bbf2c74d90afa53244356c03e5f5dca24f9f65]
#  when the block chain has two the same input, it wil have to different blocks with different hash
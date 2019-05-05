from hashlib import sha256
from time import time, sleep

class Block:
    def __init__(self, data, height):
        self.data = data
        self.height = height
        self.hash = sha256(str(time()).encode('utf-8')).hexdigest()
        self.next = None
        self.time_stamp = int(time())
    
    def __str__(self):
        block = '{\ndata: %s\nheight: %d\nhash: %s\nnext: %s\ntime_stamp: %d\n}' % (self.data, self.height, self.hash, self.next.hash if self.next else self.next, self.time_stamp)
        return block


class BlockChain:
    def __init__(self):
        genesis_block = Block('Genesis Block', 0)
        self.head = genesis_block

    def __str__(self):
        cur_head = self.head
        output = ''
        while cur_head:
            output += str(cur_head) + (' => ' if cur_head.next else '')
            cur_head = cur_head.next
        return output
    
    def addBlock(self, data):
        cur_head = self.head
        while cur_head.next:
            cur_head = cur_head.next
        height = cur_head.height + 1
        new_block = Block(data, height)
        cur_head.next = new_block

    def getBlockByHeight(self, height):
        cur_head = self.head
        while height > cur_head.height:
            cur_head = cur_head.next
        return cur_head

    def getBlockByHash(self, hash):
        cur_head = self.head
        while hash < cur_head.hash:
            cur_head = cur_head.next
        return cur_head


block_chain = BlockChain()

# Adding test blocks:
for index in range(0, 5):
    block_chain.addBlock('new block %d' % index)
    sleep(1)

# Test Case: 1
print(block_chain.getBlockByHeight(1))

# Test Case: 2
print(block_chain.getBlockByHeight(4))

# Test Case: 3
print(block_chain)

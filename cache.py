from sequence import Sequence

class CacheBlock:

    def __init__(self, data: int, ctr: int ) -> None:
        self.data = data 
        self.ctr = ctr 

    def getCtr(self):
        return self.ctr
    
    def getData(self):
        return self.data 
    
    def update(self, newData, newCtr):
        self.ctr = newCtr
        self.data = newData

class CacheMemory:

    def __init__(self, numBlocks: int ) -> None:
        self.numBlocks = numBlocks
        self.cacheBlocks = [CacheBlock(data=-1, ctr=-1) for _ in range(numBlocks)]
        self.accessLog = [] # List to track cache hit and misses
        self.iteration = 0

    def accessMemory(self, sequence):
        for data in sequence:
            cacheBlock = self.findCacheBlockByData(data)

            # 1. Check for cache hits
            if cacheBlock is not None: 
                cacheBlock.update( data, self.iteration )
                self.accessLog.append(1)
                # print( f"Iteration[{self.iteration}]: CacheBlock Hit at Block {self.iteration%self.numBlocks} of Ctr {cacheBlock.getCtr()} and Data {data}" )
            else:
                cacheBlock = self.findEmptyCacheBlock()

                # 2. Check for empty cache blocks
                if cacheBlock is not None:
                    cacheBlock.update( data, self.iteration )
                    self.accessLog.append(0)
                    # print( f"Iteration[{self.iteration}]: CacheMiss (Empty) at Block {self.iteration%self.numBlocks} of Ctr {cacheBlock.getCtr()} and Data {data}" )

                # 3. LRU replacement 
                else:
                    cacheBlock = self.findLRUCacheBlock()
                    cacheBlock.update( data, self.iteration )
                    self.accessLog.append(0)
                    # print( f"Iteration[{self.iteration}]: CacheMiss (LRU) at Block {self.iteration%self.numBlocks} of Ctr {cacheBlock.getCtr()} and Data {data} " )

            self.iteration += 1

    # Linear Search: O(n) 
    def findCacheBlockByData(self, data):
        for cacheBlock in self.cacheBlocks:
            if cacheBlock.getData() == data:
                return cacheBlock
        return None
    
    # Linear Search: O(n)
    def findEmptyCacheBlock(self):
        for cacheBlock in self.cacheBlocks:
            if cacheBlock.getData() == -1:
                return cacheBlock 
        return None
    
    # Linear Search: O(n)
    def findLRUCacheBlock(self):
        minimumValue = float('inf')
        lruCacheBlock = None
        
        # Find cache block with the lowest counter
        for cacheBlock in self.cacheBlocks:
            if cacheBlock.getCtr() < minimumValue:
                minimumValue = cacheBlock.getCtr()
                lruCacheBlock = cacheBlock

        return lruCacheBlock
    
    def displayFinalSnapshot(self):
        for i, cacheBlock in enumerate(self.cacheBlocks):
            data = cacheBlock.getData()
            print(f"Block {i}: {data}")

num = 8    
sequence = Sequence(num)
list = sequence.initSequence(2) 
print( f"Sequence Length = {len(list)}" ) 
print( f"Sequence List:\n{list}" ) 

cacheMemory = CacheMemory(int(num/2))
cacheMemory.accessMemory(list)
cacheMemory.displayFinalSnapshot()
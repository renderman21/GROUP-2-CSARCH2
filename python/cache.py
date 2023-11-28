from python.sequence import Sequence

class CacheBlock:

    def __init__(self, number: int, data: int, ctr: int ) -> None:
        self.number = number
        self.data = data 
        self.ctr = ctr 
    
    def update(self, newData, newCtr):
        self.ctr = newCtr
        self.data = newData

# TODO: Implement access time count
class CacheMemory:

    def __init__(self, numBlocks: int ) -> None:
        self.numBlocks = numBlocks
        self.cacheBlocks = [CacheBlock(number = i, data=-1, ctr=-1) for i in range(numBlocks)]
        self.cacheTagLog = []       # List to track cache hit and misses
        self.cacheTimeLog = []      # Access time for each step
        self.cacheAccessLog = []    # List of updated cache block per iteration
        self.cacheTextLog = []      # List of text log per iteration
        self.iteration = 0          # Counter for current iteration
        self.cacheAccessTime = 10
        self.missPenalty = 1 + (self.cacheAccessTime*numBlocks) + 1 

    def accessMemory(self, sequence):
        for data in sequence:
            cacheBlock = self.findCacheBlockByData(data)
            message = "" # for debugging

            # 1. Check for cache hits
            if cacheBlock is not None: 
                strPreviousBlock = f"Block {cacheBlock.number}, Ctr {cacheBlock.ctr}, Data {cacheBlock.data}"
                cacheBlock.update( data, self.iteration )
                self.cacheTagLog.append(1)  # 1 = cache hit
                self.cacheTimeLog.append(self.cacheAccessTime)
                # message = "Cache Hit"

            else:
                cacheBlock = self.findEmptyCacheBlock()

                # 2. Check for empty cache blocks
                if cacheBlock is not None:
                    strPreviousBlock = f"Block {cacheBlock.number}, Ctr {cacheBlock.ctr}, Data {cacheBlock.data}"
                    cacheBlock.update( data, self.iteration )
                    self.cacheTagLog.append(2) # 2 - empty cache
                    self.cacheTimeLog.append(self.missPenalty)
                    # message = "Cache Miss (Empty)"

                # 3. LRU replacement 
                else:
                    cacheBlock = self.findLRUCacheBlock()
                    strPreviousBlock = f"Block {cacheBlock.number}, Ctr {cacheBlock.ctr}, Data {cacheBlock.data}"
                    cacheBlock.update( data, self.iteration )
                    self.cacheTagLog.append(3) # 3 - LRU replacement
                    self.cacheTimeLog.append(self.missPenalty)
                    # message = "Cache Miss (LRU)"

            # print( f"Iteration[{self.iteration}]: {message} at Block {cacheBlock.number} of Ctr {cacheBlock.ctr} and Data {cacheBlock.data}" )
            strNewBlock = f"Block {cacheBlock.number}, Ctr {cacheBlock.ctr}, Data {cacheBlock.data}"    # For text log
            self.cacheTextLog.append( f"[{self.iteration}] {strPreviousBlock} → {strNewBlock}" )        # For text log
            newCacheBlock = CacheBlock( cacheBlock.number, cacheBlock.data, cacheBlock.ctr )            # For access log
            self.cacheAccessLog.append(newCacheBlock)                                                   # For access log
            self.iteration += 1

    # Linear Search: O(n) 
    def findCacheBlockByData(self, data):
        for cacheBlock in self.cacheBlocks:
            if cacheBlock.data == data:
                return cacheBlock
        return None
    
    # Linear Search: O(n)
    def findEmptyCacheBlock(self):
        for cacheBlock in self.cacheBlocks:
            if cacheBlock.data == -1:
                return cacheBlock 
        return None
    
    # Linear Search: O(n)
    def findLRUCacheBlock(self):
        minimumValue = float('inf')
        lruCacheBlock = None
        
        # Find cache block with the lowest counter
        for cacheBlock in self.cacheBlocks:
            if cacheBlock.ctr < minimumValue:
                minimumValue = cacheBlock.ctr
                lruCacheBlock = cacheBlock

        return lruCacheBlock
    
    def getCacheHitCount(self):
        return self.cacheTagLog.count(1)

    def getCacheMissCount(self):
        return self.cacheTagLog.count(2) + self.cacheTagLog.count(3)
    
    def getCacheHitRate(self):
        return self.getCacheHitCount()/self.iteration 

    def getCacheMissRate(self):
        return self.getCacheMissCount()/self.iteration
    
    def getAverageMAT(self):
        hitTime = self.getCacheHitRate() * self.cacheAccessTime
        missTime = self.getCacheMissRate() * self.missPenalty
        return hitTime + missTime
    
    def getTotalMAT(self):
        return sum(self.cacheTimeLog)

    def getFinalSnapshot(self):
        finalSnapshot = []
        for cacheBlock in self.cacheBlocks:
            finalSnapshot.append(cacheBlock)
        return finalSnapshot

    # For terminal debugging
    def displayFinalSnapshot(self):
        for i, cacheBlock in enumerate(self.cacheBlocks):
            data = cacheBlock.data
            print(f"Block {i}: {data}")
'''
num = 8   
sequence = Sequence(num)
list = sequence.initSequence(0) 
print( f"Sequence Length = {len(list)}" ) 
print( f"Sequence List:\n{list}" ) 

cacheMemory = CacheMemory(32)
cacheMemory.accessMemory(list)
cacheMemory.displayFinalSnapshot()
'''
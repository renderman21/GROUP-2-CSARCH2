from python.sequence import Sequence
from python.cache import CacheMemory, CacheBlock

num = 32   
sequence = Sequence(num)
list = sequence.initSequence(0) 
print( f"Sequence Length = {len(list)}" ) 
print( f"Sequence List:\n{list}" ) 

cacheMemory = CacheMemory(32)
cacheMemory.accessMemory(list)
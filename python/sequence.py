import random

class Sequence:
    '''
        numBlocks are for memory Blocks
    '''
    def __init__(self, numBlocks:int) -> None:
        self.numBlocks = numBlocks
    
    def initSequence(self, testCase) -> list:
        list = []
        match testCase:
            case 0: 
                list = self.sequentialSequence()
            case 1: 
                list = self.randomSequence()
            case 2: 
                list = self.repeatSequence()
            
        return list

    def sequentialSequence(self):
        list = []
        upperLimit = self.numBlocks * 2
        for i in range(0, 4):
            for a in range(0, upperLimit):
                list.append(a)
        return list

    def randomSequence(self):
        list = []
        upperLimit = self.numBlocks * 4
        for i in range(upperLimit):
            list.append(random.randint(0, upperLimit))
        return list

    def repeatSequence(self):
        list = []
        firstLimit = self.numBlocks - 1
        secondLimit = self.numBlocks * 2
        for j in range(0, 4):
            for i in range(0, firstLimit):
                list.append(i)
            for a in range(1, secondLimit):
                list.append(a)
        return list
    
# sequence = Sequence(32)
# list = sequence.initSequence(0) 
# print( list )
# print( f"\n{len(list)}")
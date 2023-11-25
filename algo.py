import random
'''
This file contains the algorithm of FA+LRU

'''

class FALRU:

    """ 
        This initializes the FALRU class. Used for choosing which test case be utilized,
        and how many memory blocks the user requested 

        testCase (int): This is based on the user's choice of what test case will be used
        numBlocks (int): This is the user's requested amount of memory blocks to be outputed
        
    """
    def __init__(self, testCase:int, numBlocks:int) -> None:
        self.testCase = testCase
        self.numBlocks = numBlocks
    

    """This will initialize the sequence, depending on what the test cases had been inputted
    
    Returns:
        list: This contains the sequence
    """
    def initSequence(self) -> list:
        list = []
        match self.testCase:
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

    def mainAlgo(self) -> list:
        """This is the function that performs FA + LRU

        Returns:
            list: This contains the cache block
        """
        
        #TODO: Complete this function
        pass

test = FALRU(2,8)

print(test.initSequence())
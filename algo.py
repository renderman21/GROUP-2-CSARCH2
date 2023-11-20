'''
This file contains the algorithm of FA+LRU

'''

import random as r

class FALRU:
    def __init__(self, testCase:int, numBlocks:int) -> None:
        """This initializes the FALRU class. Used for choosing which test case be utilized,
        and how many memory blocks the user requested 

        Args
            testCase (int): This is based on the user's choice of what test case will be used
            numBlocks (int): This is the user's requested amount of memory blocks to be outputed
            
        """
        self.testCase = testCase
        self.numBlocks = numBlocks
    
    def initSequence(self) -> list:
        """This will initialize the sequence, depending on what the test cases had been inputted
        
        Returns:
            list: This contains the sequence
        """
        
        retList = []
        match self.testCase:
            #Sequential Sequencing
            case 0: 
                upperLimit = self.numBlocks * 2
                for i in range(0, 4):
                    for a in range(0, upperLimit):
                        retList.append(a)
                
                return retList
            #Random Sequencing
            case 1: 
                upperLimit = self.numBlocks * 4
                
                for i in range(upperLimit):
                    retList.append(r.randint(0, upperLimit))
                return retList
            #Mid-Repeat Blocks
            case 2: 
                firstLimit = self.numBlocks - 1
                secondLimit = self.numBlocks * 2
                
                for j in range(0, 4):
                    for i in range(0, firstLimit):
                        retList.append(i)
                    
                    for a in range(1, secondLimit):
                        retList.append(a)
                
                return retList
            
    def mainAlgo(self) -> list:
        """This is the function that performs FA + LRU

        Returns:
            list: This contains the cache block
        """
        
        #TODO: Complete this function
        pass

test = FALRU(1,8)

print(test.initSequence())


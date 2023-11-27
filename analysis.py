#!/usr/bin/env python3
import cache as ch
import sequence as sq

def main():
    #Test case 1
    
    n = 20
    
    print(f"N={n}")
    
    s = sq.Sequence(n)
    
    
    print("TEST CASE 1: SEQUENTIAL SEQUENCE")
   
    case_list = s.sequentialSequence()
    
    print(case_list)
    
    cache = ch.CacheMemory(32)
    cache.accessMemory(case_list)
    cache.displayFinalSnapshot()
    
    print("---------------------------------------")
    
    print("TEST CASE 2: RANDOM SEQUENCE")

 
    case_list = s.randomSequence()
    
    print(case_list)
    
    cache = ch.CacheMemory(32)
    cache.accessMemory(case_list)
    cache.displayFinalSnapshot()
    
    print("-------------------------------------")
    
    print("TEST CASE 3: MID REPEAT BLOCKS")
    
    case_list = s.repeatSequence()
    
    print(case_list)
    
    cache = ch.CacheMemory(32)
    cache.accessMemory(case_list)
    cache.displayFinalSnapshot()


if __name__ == '__main__':
    main()
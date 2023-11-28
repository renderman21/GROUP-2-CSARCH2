# CSARC2 (GROUP 2)

This is a project where we perform FA+LRU

Analysis 

Test Case 1 (Sequential Sequence)
Since, with this particular test case, we need to have up to `2n` cache blocks, and have a sequence
${0,1,2,3...2_n-1}$ 

In this particular test, we will have `n=32`. We will use the program that we have made for this analysis. 

![alt text](/analysis_image/input.png)

As you can see in this screenshot, we have used sequential and the inputted number is 32. 

Going with the rules for sequential sequence, we have a sequence 

${[0,1,2...63,0,1,2...,63,0,1,2...,63,0,1,2,..,63}]$

We will analyze the sequence via iterations, this means the first ${0,1,2...63}$ is the first iteration, and then the second ${0,1,2...63}$, etc. 

For the first iteration. 

![alt text](/analysis_image/sequence_iteration1-1.png)
![alt text](/analysis_image/sequence_iteration1-2.png)
![alt text](/analysis_image//sequence_iteration1-3.png)

In the first 32 access of the memory, the cache memory is empty, therefore we place first all the sequences 32 times. However, since the cache memory is full, `Data 32` has been placed at `Block 0` due to the replacement algorithm *LRU* or *Least Recently Used*. Because *2n* is bigger than the the 32 cache blocks, there are no repeated values, meaning there will be misses than hits, and the values are replaced.

We can now get the Memory Access count, cache hit, cache miss, cache hit rate, 
cache miss rate, average memory access time and the total memory access time. 

We can determine the memory access count by the length of the sequence. So this is 256. 

Since there are no cache hits and all are a miss, we get only 0 and 256, respectively. 

To compute the rate, we have the computation

$hitrate = hits/lengthofsequence$

$missrate = miss/lengthofsequences$

For the average memory access time, we have the formula

$T_a = hC + (1-h)*M$

Where:
$h$ is the hirate
$C$ is the cache access time *assuming this to be 10*
$M$ is the miss penalty.

Before getting the average memory access time, we need to get the miss penalty. 
This is done by the formula

$misspenalty = 1ns + (10 * 32) + 1$

32 is the cache block size. 

After defining the Miss Penalty we will have

$T_a = 0(10) + (1-0.0) * 322$

$T_a = 322$

We have an average memory access time of 322

To get the total memory access time, we use the formula 

$Total = T_a * memoryaccesscount$

$Total = 322 * 256$

$Total = 82432$


In summary we have: 
```
Memory access count: 256
Cache hit: 0
Cache miss: 256
Cache hit rate: 0%
Cache miss rate: 100%
Average memory access time: 322
Total Memory Access Time: 82432

```




Test Case 2 (Random Sequence)
// Perform analysis

Test Case 3 (Mid-Repeat Blocks)
// Perform analysis


# CSARC2 (GROUP 2)

This is a project where we perform FA+LRU

# Link
insert link
# Video Demo
insert lnk

# Analysis 

# Test Case 1 (Sequential Sequence)
Since, with this particular test case, we need to have up to `2n` cache blocks, and have a sequence
${0,1,2,3...2_n-1}$ 

In this particular test, we will have `n=32`. We will use the program that we have made for this analysis. 

![alt text](/analysis_image/input.png)

As you can see in this screenshot, we have used sequential and the inputted number is 32. 

Going with the rules for sequential sequence, we have a sequence 

${[0,1,2...63,0,1,2...,63,0,1,2...,63,0,1,2,..,63}]$

We will analyze the sequence via iterations, this means the first ${0,1,2...63}$ is the first iteration, and then the second ${0,1,2...63}$, etc. 

## For the first iteration. 
<div style="display: flex; ">

<img src="/analysis_image/sequence_iteration1-1.png" width = "200" height="200">

<img src= "/analysis_image/sequence_iteration1-2.png" width = "200" height = "200">

<img src="/analysis_image/sequence_iteration1-3.png" width = "200" height = "200">

</div>
In this iteration, there were 64 misses and no hits. 

## For the second iteration 

<div style = "display: flex;"> 

<img src="/analysis_image/sequence_iteration2-1.png" width = "200" height = 200>

<img src="/analysis_image/sequence_iteration2-2.png" width = "200" height = 200>

<img src="/analysis_image/sequence_iteration2-3.png" width = "200" height = 200>

<img src="/analysis_image/sequence_iteration2-4.png" width = "200" height = 200>

</div> 
In this iteration there were 64 misses and no hits

## For the third iteration

![alt text](/analysis_image/sequence_iteration3-1.png)

![alt text](/analysis_image/sequence_iteration3-2.png)

![alt text](/analysis_image/sequence_iteration3-3.png)

## In this iteration there were 64 misses and no hits

Fourth and final iteration

![alt text](/analysis_image/sequence_iteration4-1.png)

![alt text](/analysis_image/sequence_iteration4-2.png)

![alt text](/analysis_image/sequence_iteration4-3.png)

![alt text](/analysis_image/sequence_iteration4-4.png)

In this iteration there were 64 misses and no hits

## Final snapshot
![alt text](/analysis_image/sequential_final.png)

*Read the order from the top left to the right*

Therefore, we have a total of 256 misses and no hits at all.

## Summary and Compuation

In the first 32 access of the memory, the cache memory is empty, therefore we place first all the sequences 32 times. However, since the cache memory is full, `Data 32` has been placed at `Block 0` due to the replacement algorithm *LRU* or *Least Recently Used*. Because *2n* is bigger than the the 32 cache blocks, there are no repeated values, meaning there will be misses than hits, and the values are replaced.

We can now get the Memory Access count, cache hit, cache miss, cache hit rate, 
cache miss rate, average memory access time and the total memory access time. 

## Formulas 
But before we continue to compute them, we have to defined the formulas used.

To get the memory access count, we can simply get the length of the sequence or in this way

$memoryaccesscount = hitcount + misscount$

To get the hitrate and missrate, we have the following

$hitrate = hitcount/memoryaccesscount$ 

$missrate = misscount/memoryaccesscount$

To get the average memory access time we have to define two formulas. 

First is the miss penalty, this is done via the following: 

$misspenalty = 1 + (10 * blocksize) + 1$

But since the blocksize is always 32, we will have this 

$ misspenalty = 322 $ 

Then, we get to the formula of the average memory access time 

$T_a = hitrate(cacheaccesstime) + (1-hitrate) * misspenalty$

*Note: cacheaccesstime is assumed to be 10ns*

Finally we can get the total memory access time

$total = T_a * memoryaccesscount$

Now we have defined the formulas, let's compute

## Memory access count
$memoryaccesscount = 256 + 0$

$memoryaccesscount = 256$

## Cache hit rate 

$hitrate = 0 / 256$

$hitrate = 0$

## Cache miss rate

$missrate = 256/256$

$missrate = 1$

## Average memory access time

$T_a = 0(10) + (1-0) * 322$

$T_a = 322ns$

## Total memory access time

$total = 322 * 256$

$total = 82432ns$

In summary we have: 
```
Memory access count: 256
Cache hit: 0
Cache miss: 256
Cache hit rate: 0%
Cache miss rate: 100%
Average memory access time: 322ns
Total Memory Access Time: 82432ns

```




# Test Case 2 (Random Sequence)
// Perform analysis

# Test Case 3 (Mid-Repeat Blocks)
With this test sequence, this starts at block 0, after which it will start at 1 again and continue up to $2n-1$ times. This sequence will be repeated four times. 

Let's assume that $n = 32$, we have a sequence the following sequence of 

${0,1,2,...,31,1,2,3,...,63}$

This pattern is repeated four times for the sequence. 

We will now analyze the sequence by looking the duplicate last number of the $n-1$ and its $2n-1$

First we input our $n$ and select into mid-repeat

![alt text](/analysis_image/mid-repeat_input.png)

Then, the following images are the text log

## First iteration

![alt text](/analysis_image/repeat_iteration1-1.png)

![alt text](/analysis_image/repeat_iteration1-2.png)

![alt text](/analysis_image/repeat_iteration1-3.png)

![alt text](/analysis_image/repeat_iteration1-4.png)

There are 64 misses and 30 hits, for this iteration. 

## Second iteration 


![alt text](/analysis_image/repeat_iteration2-1.png)

![alt text](/analysis_image/repeat_iteration2-2.png)

![alt text](/analysis_image/repeat_iteration2-3.png)

![alt text](/analysis_image/repeat_iteration2-4.png)

![alt text](/analysis_image/repeat_iteration2-5.png)

There are 64 misses and 30 hits, for this iteration

## Third iteration 

![alt text](/analysis_image/repeat_iteration3-1.png)

![alt text](/analysis_image/repeat_iteration3-2.png)

![alt text](/analysis_image/repeat_iteration3-3.png)

![alt text](/analysis_image/repeat_iteration3-4.png)

![alt text](/analysis_image/repeat_iteration3-5.png)

There are 64 misses and 30 hits for this iteration

## Fourth and final iteration 

![alt text](/analysis_image/repeat_iteration4-1.png)

![alt text](/analysis_image/repeat_iteration4-2.png)

![alt text](/analysis_image/repeat_iteration4-3.png)

![alt text](/analysis_image/repeat_iteration4-4.png)

![alt text](/analysis_image/repeat_iteration4-5.png)

There are 64 misses and 30 hits for this iteration.

## Final snapshot

![alt text](/analysis_image/repeat_output.png)

*Read the order from the top left to the right*

In total, there are 256 misses and 120 hits made. 

## Summary and Computation

Same fashion for the first iteration, since all are empty, all cache blocks must be filled up. However, since we have reached the first $n-1$ pattern, we go back to 1. This time, there's a hit and, since the next pattern (the $2n$) starts at 1, all of these elements are present and there a hit. So, unlike the sequential test case that if $2n$ higher than 32 cache blocks all will be a miss, this case, there will be a hit. 

Using the same formula we have defined in the first test case, we can find the memory access count, cache hit count, cache miss count, cache hit rate, cache miss rate, average memory access time and total memory access time. 

We have already have cache hit count, and cache miss count. 

Now we it's the matter of getting the memory access count, cache hit rate, cache hit rate, average memory access time and the total memory access time. 

All formulas will be referred to the first test case

### Memory access count: 

$memoryaccesscount = 256 + 120$

$memoryaccesscount = 376$

### Cache hit rate

$hitrate = 120/376$

$hitrate = 0.31914893617$ or 31.91%

## Cache miss rate

$missrate = 256/376$

$missrate = 0.68085106383$ or 68.09%

## Average memory access time 

$T_a = 0.31914893617(10) + (1-0.31914893617) * 322$

$T_a = 222.4255319$

## Total memory access time 
$total = 222.4255319 * 83632$

$total = 83632$


In summary we have the following results

```

Memory access count: 376
Cache hit count: 120
Cache miss count: 256
Cache hit rate: 31.91%
Cache miss rate: 68.09%
Average memory access time: 222.43s
Total memory access time: 83632ns

```


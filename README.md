# CSARC2 (GROUP 2)

This is a project where we perform FA+LRU

## Analysis 

Test Case 1 (Sequential Sequence)
In this case, we first perform Sequential Sequence. 

Since, with this particular test case, we need to have up to `2n` cache blocks, and have a sequence
${0,1,2,3...2_n-1}$

Assuming we have `n = 20`. 

In this case we need to have up to: 

${ 
    2(20) = 40
}$

We will have the following sequence 

${[0,1,2,3...,39]}$

This, however, will be repeated four times, and appended to the sequence

${[0,1,2,3...,39,0,1,2,...,39,0,1,2,...,39,0,1,2...39]}$


Afterwards, since it is defined that a cache block has 32 blocks. So we create a table like so: 

| | Data|
|------|-----|
| 0 | 
| 1 |
| 2 |
| ..|
| 31|

If we iterate through the sequence, we will acquire the following after each end of the iteration

1st Iteration *(First 0...39)* 
|  Block  | Data  |
|----|----|
| 0  | 32 |
| 1  | 33 |
| 2  | 34 |
| 3  | 35 |
| 4  | 36 |
| 5  | 37 |
| 6  | 38 |
| 7  | 39 |
| 8  | 8  |
| 9  | 9  |
| 10 | 10 |
| 11 | 11 |
| 12 | 12 |
| 13 | 13 |
| 14 | 14 |
| 15 | 15 |
| 16 | 16 |
| 17 | 17 |
| 18 | 18 |
| 19 | 19 |
| 20 | 20 |
| 21 | 21 |
| 22 | 22 |
| 23 | 23 |
| 24 | 24 |
| 25 | 25 |
| 26 | 26 |
| 27 | 27 |
| 28 | 28 |
| 29 | 29 |
| 30 | 30 |
| 31 | 31 |

| data | hit | miss |
|------|-----|------|
| 0    |     | x    |
| 1    |     | x    |
| 2    |     | x    |
| 3    |     | x    |
| 4    |     | x    |
| 5    |     | x    |
| 6    |     | x    |
| 7    |     | x    |
| 8    |     | x    |
| 9    |     | x    |
| 10   |     | x    |
| 11   |     | x    |
| 12   |     | x    |
| 13   |     | x    |
| 14   |     | x    |
| 15   |     | x    |
| 16   |     | x    |
| 17   |     | x    |
| 18   |     | x    |
| 19   |     | x    |
| 20   |     | x    |
| 21   |     | x    |
| 22   |     | x    |
| 23   |     | x    |
| 24   |     | x    |
| 25   |     | x    |
| 26   |     | x    |
| 27   |     | x    |
| 28   |     | x    |
| 29   |     | x    |
| 30   |     | x    |
| 31   |     | x    |
| 32   |     | x    |
| 33   |     | x    |
| 34   |     | x    |
| 35   |     | x    |
| 36   |     | x    |
| 37   |     | x    |
| 38   |     | x    |
| 39   |     | x    |



2nd Iteration *(Second 0..39)*
|    |    |
|----|----|
| 0  | 24 |
| 1  | 25 |
| 2  | 26 |
| 3  | 27 |
| 4  | 28 |
| 5  | 29 |
| 6  | 30 |
| 7  | 31 |
| 8  | 32 |
| 9  | 33 |
| 10 | 34 |
| 11 | 35 |
| 12 | 36 |
| 13 | 37 |
| 14 | 38 |
| 15 | 39 |
| 16 | 8  |
| 17 | 9  |
| 18 | 10 |
| 19 | 11 |
| 20 | 12 |
| 21 | 13 |
| 22 | 14 |
| 23 | 15 |
| 24 | 16 |
| 25 | 17 |
| 26 | 18 |
| 27 | 19 |
| 28 | 20 |
| 29 | 21 |
| 30 | 22 |
| 31 | 23 |

| data | hit | miss |
|------|-----|------|
| 0    |     | x    |
| 1    |     | x    |
| 2    |     | x    |
| 3    |     | x    |
| 4    |     | x    |
| 5    |     | x    |
| 6    |     | x    |
| 7    |     | x    |
| 8    |     | x    |
| 9    |     | x    |
| 10   |     | x    |
| 11   |     | x    |
| 12   |     | x    |
| 13   |     | x    |
| 14   |     | x    |
| 15   |     | x    |
| 16   |     | x    |
| 17   |     | x    |
| 18   |     | x    |
| 19   |     | x    |
| 20   |     | x    |
| 21   |     | x    |
| 22   |     | x    |
| 23   |     | x    |
| 24   |     | x    |
| 25   |     | x    |
| 26   |     | x    |
| 27   |     | x    |
| 28   |     | x    |
| 29   |     | x    |
| 30   |     | x    |
| 31   |     | x    |
| 32   |     | x    |
| 33   |     | x    |
| 34   |     | x    |
| 35   |     | x    |
| 36   |     | x    |
| 37   |     | x    |
| 38   |     | x    |
| 39   |     | x    |


3rd Iteration *(3rd 0..39)*
|    |    |
|----|----|
| 0  | 16 |
| 1  | 17 |
| 2  | 18 |
| 3  | 19 |
| 4  | 20 |
| 5  | 21 |
| 6  | 22 |
| 7  | 23 |
| 8  | 24 |
| 9  | 25 |
| 10 | 26 |
| 11 | 27 |
| 12 | 28 |
| 13 | 29 |
| 14 | 30 |
| 15 | 31 |
| 16 | 32 |
| 17 | 33 |
| 18 | 34 |
| 19 | 35 |
| 20 | 36 |
| 21 | 37 |
| 22 | 38 |
| 23 | 39 |
| 24 | 8  |
| 25 | 9  |
| 26 | 10 |
| 27 | 11 |
| 28 | 12 |
| 29 | 13 |
| 30 | 14 |
| 31 | 15 |


| data | hit | miss |
|------|-----|------|
| 0    |     | x    |
| 1    |     | x    |
| 2    |     | x    |
| 3    |     | x    |
| 4    |     | x    |
| 5    |     | x    |
| 6    |     | x    |
| 7    |     | x    |
| 8    |     | x    |
| 9    |     | x    |
| 10   |     | x    |
| 11   |     | x    |
| 12   |     | x    |
| 13   |     | x    |
| 14   |     | x    |
| 15   |     | x    |
| 16   |     | x    |
| 17   |     | x    |
| 18   |     | x    |
| 19   |     | x    |
| 20   |     | x    |
| 21   |     | x    |
| 22   |     | x    |
| 23   |     | x    |
| 24   |     | x    |
| 25   |     | x    |
| 26   |     | x    |
| 27   |     | x    |
| 28   |     | x    |
| 29   |     | x    |
| 30   |     | x    |
| 31   |     | x    |
| 32   |     | x    |
| 33   |     | x    |
| 34   |     | x    |
| 35   |     | x    |
| 36   |     | x    |
| 37   |     | x    |
| 38   |     | x    |
| 39   |     | x    |




4th and Final Iteration *(Last 0...39)*
|    Block   |   Data |
|----------|----|
|  0  | 8  |
|  1  | 9  |
|  2  | 10 |
|  3  | 11 |
|  4  | 12 |
|  5  | 13 |
|  6  | 14 |
|  7  | 15 |
|  8  | 16 |
|  9  | 17 |
|  10 | 18 |
|  11 | 19 |
|  12 | 20 |
|  13 | 21 |
|  14 | 22 |
|  15 | 23 |
|  16 | 24 |
|  17 | 25 |
|  18 | 26 |
|  19 | 27 |
|  20 | 28 |
|  21 | 29 |
|  22 | 30 |
|  23 | 31 |
|  24 | 32 |
|  25 | 33 |
|  26 | 34 |
|  27 | 35 |
|  28 | 36 |
|  29 | 37 |
|  30 | 38 |
|  31 | 39 |


| data | hit | miss |
|------|-----|------|
| 0    |     | x    |
| 1    |     | x    |
| 2    |     | x    |
| 3    |     | x    |
| 4    |     | x    |
| 5    |     | x    |
| 6    |     | x    |
| 7    |     | x    |
| 8    |     | x    |
| 9    |     | x    |
| 10   |     | x    |
| 11   |     | x    |
| 12   |     | x    |
| 13   |     | x    |
| 14   |     | x    |
| 15   |     | x    |
| 16   |     | x    |
| 17   |     | x    |
| 18   |     | x    |
| 19   |     | x    |
| 20   |     | x    |
| 21   |     | x    |
| 22   |     | x    |
| 23   |     | x    |
| 24   |     | x    |
| 25   |     | x    |
| 26   |     | x    |
| 27   |     | x    |
| 28   |     | x    |
| 29   |     | x    |
| 30   |     | x    |
| 31   |     | x    |
| 32   |     | x    |
| 33   |     | x    |
| 34   |     | x    |
| 35   |     | x    |
| 36   |     | x    |
| 37   |     | x    |
| 38   |     | x    |
| 39   |     | x    |


As we can see, this sequence has no repeated data. Meaning, there will be no cache hits if the number of memory blocks are higher than the cache block size of 32. 

If n = 20,
    cache hit rate = 0% 
    cache miss rate = 100%



Test Case 2 (Random Sequence)
// Perform analysis

Test Case 3 (Mid-Repeat Blocks)
// Perform analysis


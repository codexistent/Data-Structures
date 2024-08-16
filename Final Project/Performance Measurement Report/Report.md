# Performance Measurement Report

We use the code graph.py to test various algorithms on solving the following problem: in an array of randomly generated values, find a pair of numbers summing up to a given target value. Testing arrays of sizes `10000`, `20000`, `40000`, `80000`, and `160000` elements, our program solves the problem using various algorithms such as Nested For Loops, Merge Sort, Hash Tables, and AVL Trees. Finally, the code outputs the amount of time taken by each algorithm and a graph showing the times of each algorithm on different sized arrays(note we take the average of the running times of 10 runs of every single algorithm on each array size for higher accuracy).

The image below shows proof that at various array sizes, our various algorithms take the following amounts of time to run.

| | Nested For Loops | Merge Sort | Hash Table | AVL Tree
--- | --- | --- | --- | ---
Array Size = 10,000 | 2.2930 sec | 0.0211 sec | 0.0260 sec | 0.0663 sec
Array Size = 20,000 | 9.2408 sec | 0.0448 sec | 0.0448 sec | 0.1443 sec
Array Size = 40,000 | 37.0893 sec | 0.0964 sec | 0.0979 sec | 0.3126 sec
Array Size = 80,000 | 146.8152 sec | 0.2030 sec | 0.2189 sec | 0.6825 sec
Array Size = 160,000 | 587.6189 sec | 0.4301 sec | 0.4960 sec | 1.4814 sec

![Screenshot 1](https://github.com/user-attachments/assets/8f5f3796-8cb8-4735-a766-d4ce3768dbb5)

The program also generates the following graph:

![graph](https://github.com/user-attachments/assets/8cce9440-cc5a-4108-9326-4b99d972f5bb)

# Analysis
| | Nested For Loops | Merge Sort | Hash Table | AVL Tree
--- | --- | --- | --- | ---
Array Size = 10,000 | 2.2930 sec | 0.0211 sec | 0.0260 sec | 0.0663 sec
Array Size = 20,000 | 9.2408 sec | 0.0448 sec | 0.0448 sec | 0.1443 sec
Array Size = 40,000 | 37.0893 sec | 0.0964 sec | 0.0979 sec | 0.3126 sec
Array Size = 80,000 | 146.8152 sec | 0.2030 sec | 0.2189 sec | 0.6825 sec
Array Size = 160,000 | 587.6189 sec | 0.4301 sec | 0.4960 sec | 1.4814 sec

As we can see from the table above, as well as the graph our program generated, the smaller the array size is the less of a running time difference the algorithms have. However, as our array size gradually increases, so does the gap in running times for all the algorithms.

The algorithm that uses Nested For Loops takes the longest according to our graph, while the Merge Sort, Hash Table, and AVL Tree functions take a similar amount of time. Let's check if this is valid.

## Nested For Loops
The nested for loops algorithm should take `O(N^2)` time. 
It checks every pair of unequal indicies in the array for a pair of numbers that will add up to the given target value. To do this, it runs a nested for loop where the outer for loop represents the first number in the pair, and the inner for loop represents the second number in the pair. Each for loop iterates around `N` times, therefore creating an `O(N^2)` time complexity.

## Algorithm using Merge Sort
The part of this algorithm that dominates time complexity is the merge sorting. We start out by merge sorting our array of random integers. Then, we keep track of an index value, say `pointer`, that monotonically is increased to the right. As we iterate over all possible indicies `i` in increasing order, we increment `pointer` when the sum of the values at indicies `i` and `pointer` in our sorted array become too small. Note we will never decrease `pointer`

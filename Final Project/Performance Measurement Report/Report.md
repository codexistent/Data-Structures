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

As we can see from the table above, as well as the graph our program generated, the smaller the array size, the less of a running time difference the algorithms have.

However, as apparent when our array sizes increase, the algorithm that uses Nested For Loops takes the longest according to our graph, while the Merge Sort, Hash Table, and AVL Tree functions take a similar amount of time. Let's check if this is valid.

## Algorithm 1 - Nested For Loops
The nested for loops algorithm should take `O(N^2)` time. 
It checks every pair of unequal indicies in the array for a pair of numbers that will add up to the given target value. To do this, it runs a nested for loop where the outer for loop represents the first number in the pair, and the inner for loop represents the second number in the pair. Each for loop iterates around `N` times, therefore creating an `O(N^2)` time complexity.

## Algorithm 2 - Merge Sort
The part of this algorithm that dominates time complexity is the merge sorting. We start out by merge sorting our array of random integers. Then, we keep track of an index value, say `pointer`, that starts at the maximum index of the array monotonically is increased to the left. As we iterate over all possible indicies `i` in increasing order, we decrement `pointer` when the sum of the values at indicies `i` and `pointer` in our sorted array become too big for our target value.

Merge sorting runs in `O(N log N)`. Our loop runs `N` iterations. Note we will never increase `pointer`, so the total times we move pointer to the left is `N`. Therefore, the operations that dominate our time complexity is Merge Sorting, leading us to conclude Algorithm 2 has time complexity `O(N log N)`.

## Algorithm 3 - Hash Table
This algorithm uses a hash table to insert keys and check if they exist. We insert `N` keys(one for each element of the array) and check if keys exist on `N` occasions. Therefore, we do around `2N` hash table operations, each of which take `O(1)` on average. 

Therefore, our time complexity here is `O(N)`.

## Algorithm 3 - AVL Tree
This algorithm also inserts keys and checks if they exist; it just uses an AVL tree for this. We insert `N` keys(one for each element of the array) and check if keys exist on `N` occasions. Therefore, we do around `2N` AVL Tree operations, each of which take `O(log N)` on average. This means we have a `2N * log N` = `O(N log N)` time complexity.

## Comparison of Algorithms
Nested For Loops must take the longest at `O(N^2)` time. Next, Merge Sort and AVL Tree take much less time at `O(N log N)`.
Finally, hash table should be fastest at `O(N)`. 

As the array sizes get larger, the difference between Nested Loop's large `N^2` runtime and `N log N` or `N` get larger. This is clearly shown in the graph, as Nested For Loops runtime increases significantly above all the other algorithms as `N` increases.

Next, AVL Tree, Merge Sort and Hash Table algorithms use about the same amounts of time, as apparent from the graph(where the 3 algorithms' lines clearly intersect). This makes sense because AVL Tree and Merge Sort take the same time complexity of `O(N log N)`. Additionally, while Hash Table takes `O(N)` on average, collisions can cause its performance to drop at times. Also, `log N` is actually quite small, so the difference between `O(N)` and `O(N log N)` should be insignificant especially at large array sizes like `160,000`.

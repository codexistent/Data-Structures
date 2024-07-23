# Performance Measurement Report

We use the code [Graph.py]([url](https://github.com/codexistent/Data-Structures/blob/main/Week%202/Assignment%203/Performance%20Measurement%20Report/Graph.py)) to test different sorting algorithms on arrays of size `ct = 10000`. Testing on an array of `10000` random(and afterwards, `10000` sorted) elements, our program sorts the array using various sorting algorithms such as Quicksort, Merge Sort, and Bubble Sort. Finally, the code outputs the amount of time taken by each sorting algorithm and a graph showing the times of each sorting algorithm on unsorted and sorted arrays.

The image below shows proof that at `ct = 10000` array elements, our various sorting algorithms take the following amounts of time to run.

| | Bubble Sort | Quick Sort | Merge Sort
--- | --- | --- | --- 
Sorted Array | 0.0015 sec | 5.1528 sec | 0.0162 sec
Unsorted Array | 17.7664 sec | 0.0152 sec | 0.0421 sec

<img width="1680" alt="Screenshot 2024-07-23 at 1 27 57 PM" src="https://github.com/user-attachments/assets/57a40024-3244-48cd-90f8-7aa5a36b0a6b">

The program also generates the following graph:

![Figure_1](https://github.com/user-attachments/assets/b713f430-c55d-4520-bc38-3bd874252dee)

# Analysis
| | Bubble Sort | Quick Sort | Merge Sort
--- | --- | --- | --- 
Sorted Array | 0.0015 sec | 5.1528 sec | 0.0162 sec
Unsorted Array | 17.7664 sec | 0.0152 sec | 0.0421 sec
## Sorted Input
As we can see from the table above, bubble sort is the fastest out of all 3 algorithms when our input is sorted. This is because in a sorted array, bubble sort will check and see that in the first iteration, the elements are all sorted. It will then immediately return, giving us an `O(n)` time complexity.

Merge sort is the second-fastest out of 3 algorithms when our input is sorted. It as fast as bubble sort for sorted inputs because it's time complexity is `O(n log n)` for worst, best, and average cases.

Finally, Quick sort is surprisingly the slowest when our input is sorted. This is because we choose our pivot as the final element every time. Because of this, the size of segment we are recursively Quick sorting decreases very slowly(specifically, by around only 1 element each time). Thus, we get the absolute worst case `O(n^2)` time complexity.

## Unsorted Input
At `17.7664 sec`, Bubble sort is significantly slower than Merge Sort and Quicksort algorithms when we have an unsorted input. This is because when our array elements are in random order, its average time complexity is `O(n^2)`.

Merge Sort and Quicksort algorithms will usually take about the same amount of time with unsorted/random arrays. In our example, their runtimes are both less than `0.05 sec` and differ by only `0.0269 sec`. Ofcourse, there will be tiny differences in their running times. Or very rarely, bigger differences, for example if Quicksort encounters its worst case `O(n^2)` runtime. But on average, with an array of random elements, both Merge Sort and Quicksorts' time complexities will be similar and at around `O(n log n)`.

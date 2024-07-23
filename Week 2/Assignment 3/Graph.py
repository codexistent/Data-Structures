import random
import time
import matplotlib.pyplot as plt
import sys

# Sorting Algorithms

# Sorts arr using bubble sort
def bubble_sort(arr):
    while(True):
        # Iterate through all elements in arr
        for i in range(1, len(arr)):
            # Swap adjacent elements if they are in the wrong order
            if(arr[i - 1] > arr[i]):
                (arr[i], arr[i - 1]) = (arr[i - 1], arr[i])

        # Check if arr is fully sorted
        ret = True
        for i in range(1, len(arr)):
            ret &= (arr[i - 1] <= arr[i])

        # If arr is fully sorted, return the sorted arr; otherwise, our while loop keeps going
        if (ret):
            return arr

# Sorts arr using quick sort, where lo...hi represents the segment of the indicies of elements to be quick sorted
def quick_sort(arr, lo, hi):
    # If our segment lo...hi consists of 2 or more elements, then quick sort the range
    if(lo < hi):
        # i tracks our current index for elements smaller than the partition
        i = lo

        # Iterate over each element of indicies in range lo...hi
        for j in range(lo, hi):
            # If the current element belongs on the left of our partition, then we put in its correct side
            # Our partition is the highest element of the range
            if(arr[j] <= arr[hi]):
                (arr[j], arr[i]) = (arr[i], arr[j])
                i = i + 1

        # We place the partition right after all elements who are less than or equal to the partition's value
        (arr[i], arr[hi]) = (arr[hi], arr[i])

        # Quick sort/recursively repeat this process with the left and right sections of the array
        arr = quick_sort(arr, lo, i - 1)
        arr = quick_sort(arr, i + 1, hi)

    # Return the quick-sorted arr
    return arr

# Sorts arr using merge sort
def merge_sort(arr):
    # If the length of arr is 0 or less, then just return arr
    if(len(arr) <= 1):
        return arr
    
    # Otherwise, split arr into two roughly equal sections named 'left' and 'right', and recursively sort them
    mid = len(arr) // 2
    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])

    # After both 'left' and 'right' are fully sorted, return their merged array
    return merge(left, right)

# Helper function of merge_sort that merges two sorted 'left' and 'right' arrays
def merge(left, right):
    # rarr stores resulting merged array
    rarr = []

    # lefti and righti keep track of our current index in the 'left' and 'right' arrays
    lefti = righti = 0

    # while we still have elements to iterate over in both the 'left' and 'right' arrays, according to righti and lefti
    while(lefti < len(left) and righti < len(right)):
        # then append the smallest element out of left[lefti] and right[righti] to 'rarr', the resulting array 
        if(left[lefti] < right[righti]):
            rarr.append(left[lefti])
            lefti += 1
        else:
            rarr.append(right[righti])
            righti += 1

    # Once we run out of elements for 'left' or 'right' arrays, append all leftover elements to 'rarr' and return our merged array
    rarr.extend(left[lefti:])
    rarr.extend(right[righti:])
    return rarr

# Function to generate input data
def generate_input(cnt, input_type):
    if input_type == 1:  # Totally random numbers
        return [random.randint(0, cnt) for _ in range(cnt)]
    elif input_type == 2:  # Sorted numbers
        return list(range(cnt))
    else:
        raise ValueError("Invalid input type")

# Function to sort the array and measure the execution time
def sort_and_measure(cnt, sorting, input_type):
    arr = generate_input(cnt, input_type)
    start_time = time.time()
    
    if sorting == "Bubble sort":
        sorted_arr = bubble_sort(arr)
    elif sorting == "Quick sort":
        sorted_arr = quick_sort(arr, 0, len(arr) - 1)
    elif sorting == "Merge sort":
        sorted_arr = merge_sort(arr)
    else:
        raise ValueError("Invalid sorting algorithm")
    
    elapsed_time = time.time() - start_time
    print(f"{cnt} elements sorted using {sorting}. Time taken: {elapsed_time:.4f} seconds.")
    return elapsed_time

# Function to plot the performance of the sorting algorithms
def plot_performance(cnt, input_types, sorting_algorithms):
    results = {alg: {inp: [] for inp in input_types} for alg in sorting_algorithms}
    
    for alg in sorting_algorithms:
        for inp in input_types:
            time_taken = sort_and_measure(cnt, alg, inp)
            results[alg][inp].append(time_taken)
    
    for alg in sorting_algorithms:
        plt.plot(input_types, [results[alg][inp][0] for inp in input_types], label=alg)
    
    plt.xlabel('Input Type')
    plt.ylabel('Time (seconds)')
    plt.title(f'Performance of Sorting Algorithms for {cnt} elements')
    plt.xticks(input_types, ['Random', 'Sorted'])
    plt.legend()
    plt.show()

if __name__ == "__main__":
    sys.setrecursionlimit(1000000000)
    cnt = 10000 # Large input size
    input_types = [1, 2]  # 1: Random, 2: Sorted
    sorting_algorithms = ["Bubble sort", "Quick sort", "Merge sort"]
    
    plot_performance(cnt, input_types, sorting_algorithms)

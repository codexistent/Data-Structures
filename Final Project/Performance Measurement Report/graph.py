import random
import time
import sys
import matplotlib.pyplot as plt

#   ALGORITHM 1 - NESTED FOR LOOPS - O(N^2)
# Go through every pair of non-equal indicies in our array to check if the sum of any two elements at these indicies equals the sum 'k'
def algorithm_1(array, k):
    # for every index 'i' in range 0...len(array)-1
    for i in range(0, len(array)): 
            # For every index 'j' in range i+1...len(array)-1
            for j in range(i + 1, len(array)):
                # Check if the sum of the two elements at indicies 'i' and 'j' is our desired sum 'k'
                if(array[i] + array[j] == k):
                    # If the sum is what we want, return the two elements' values
                    return (array[i], array[j])
    
    # If we find no good pair, we return None
    return None

#   ALGORITHM 2 - MERGE SORT - O(N LOG N)
# Algorithm 2 Helper Function: Sorts arr using merge sort
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

# Algorithm 2 Helper Function: helps merge_sort with merging two sorted 'left' and 'right' arrays
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

# Use merge sort to sort the array, then two pointers to check for sums
def algorithm_2(array, k):
    # merge sort array
    sorted_array = merge_sort(array)

    # keep a variable 'pointer' representing an index value that monotonically moves left
    pointer = len(sorted_array) - 1
    # for every index 'i' in range 0...len(sorted_array)-1
    for i in range(0, len(sorted_array)):
        # since the array is sorted, while sorted_array[i] + sorted_array[pointer] is GREATER than target value 'k'...
        while(i < pointer - 1 and sorted_array[i] + sorted_array[pointer] > k):
            # ... we will be more likely to get our target value if we move 'pointer' LEFT to a smaller value(once again, this is because since our array is sorted)
            pointer = pointer - 1
        
        if(i >= pointer):
            break
        
        # check if sorted_array[i] + sorted_array[pointer] gets us to our target sum 'k'
        if(sorted_array[i] + sorted_array[pointer] == k):
            # If so, we will return the pair (sorted_array[i], sorted_array[pointer])
            return (sorted_array[i], sorted_array[pointer])
    
    # If we never return a valid pair, then there must be no valid pair so we return None
    return None

# ALGORITHM 3
# Algorithm 3 Helper Class: HashTable
class HashTable:
    def __init__(self, size=10):
        """
        Initialize the hash table with the given size.
        Each bucket is initialized as an empty list.
        """
        self.size = size
        self.table = [[] for _ in range(size)]
        self.elements = 0

    def _hash_function(self, key):
        """
        Compute the hash index for a given key.
        Uses Python's built-in hash function and mod operation.
        """
        return hash(key) % self.size
    
    def rehash(self):
        """
        Rehashes the table if number of elements(or the load factor) becomes too high
        """
        old_size = self.size
        old_table = self.table

        # Double the size of the table
        self.size = old_size * 2

        # Recreate the table with doubled size
        self.table = [[] for _ in range(self.size)] 
        self.elements = 0

        # Rehash/re-insert all elements from our old table to our new table
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update the value.
        """
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Check if key already exists and update it
        for i, (k, v) in enumerate(bucket):
            if(k == key):
                bucket[i] = (key, value)
                return

        # If key does not exist, add new key-value pair
        bucket.append((key, value))

        # Increment number of elements in table
        self.elements = self.elements + 1

        # rehash if table getting too full(if the load factor >= 0.9)
        if(self.elements / self.size >= 0.9):
            self.rehash()


    def search(self, key):
        """
        Search for a key in the hash table and return the associated value.
        Returns None if the key is not found.
        """
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Search through the bucket for the key
        for (k, v) in bucket:
            if(k == key):
                return v

        # Return the value if found, else return None
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        If the key is not found, do nothing.
        """
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Find the key in the bucket and remove it
        for i, (k, v) in enumerate(bucket):
            if(k == key):
                del bucket[i]

                # Decrement number of elements in table
                self.elements = self.elements - 1

# Uses Hash Table to check if desired elements exist in array
def algorithm_3(array, k):
    # Create Hash Table 'ht'
    ht = HashTable()

    # For every element i in array
    for i in array:
        # If k - i was one of the past elements we've gone through
        if ht.search(k - i) != None:
            # This means we have a pair of elements that can sum to 'k', so we return (i, k - i)
            return (i, k - i)
        
        # Insert i into ht, tracking that i is an element we've gone through
        ht.insert(i, 1)

    # If we never get a valid pair, return None
    return None

#   ALGORITHM 4
# Algorithm 4 Helper Class: 'Node' for AVL Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Algorithm 4 Helper Class: 'AVLTree'
class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):  
        # Check if we can insert node here, or we need to traverse to left/right keys of 'root'
        if root == None:
            # Insert key if no key at this position
            return Node(key)
        elif key < root.key:
            # Traverse to left branch of 'root'
            root.left = self.insert(root.left, key)
        else:
            # Traverse to right branch of 'root'
            root.right = self.insert(root.right, key)

        # Update height of 'root'
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Balance the tree
        # First find balance factor of current node
        balance = self.getBalance(root)

        if balance < -1 and key < root.right.key:
            # Case 1 - Right Left rotation
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        elif balance > 1 and key > root.left.key:
            # Case 2 - Left Right rotation
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        elif balance < -1 and key > root.right.key:
            # Case 3 - Right Right rotation
            return self.leftRotate(root)
        elif balance > 1 and key < root.left.key:
            # Case 4 - Left Left rotation
            return self.rightRotate(root)

        # Return root
        return root
        

    # Performs left rotation on 'z'
    def leftRotate(self, z):
        y = z.right
        T2 = y.left # T2 stores 'y's left subtree...

        # Performing rotation
        y.left = z
        z.right = T2 # ... which will be reassigned as the right subtree of 'z'

        # Update heights; we only have to update the heights of 'y' and 'z', since all heights of nodes inside 'T2' remain the same
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return new root 'y'
        return y

    # Performs right rotation on 'z'
    def rightRotate(self, z):
        y = z.left
        T2 = y.right # T2 stores 'y's right subtree...

        # Performing rotation
        y.right = z
        z.left = T2 # ... which will be reassigned as the left subtree of 'z'

        # Update heights; we only have to update the heights of 'y' and 'z', since all heights of nodes inside 'T2' remain the same
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return new root 'y'
        return y

    def getHeight(self, root):
        # Return the height of the node
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        # Return the balance factor of the node
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def contains(self, root, key):
        # Check if the key exists in the AVL tree
        if not root:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self.contains(root.left, key)
        else:
            return self.contains(root.right, key)

# Uses AVL Tree to tell if a pair of elements in array adds up to desired sum 'k'
def algorithm_4(array, k):
    # Create AVL Tree 'avl_tree'
    avl_tree = AVLTree()
    root = None

    # For each element i in array
    for i in array:
        # If we have gone over a past element with value k - i, then the avl_tree will contain it...
        if(avl_tree.contains(root, k - i) == True):
            # .. so we will return the valid pair of values (i, k - i) that sum up to i + (k - i) = k as desired
            return (i, k - i)
        
        # Insert the value i into avl_tree
        root = avl_tree.insert(root, i)

    # Return None if no valid pair found
    return None

# GRAPHING FUNCTIONS
# Function to sort the array and measure the execution time
# Parameter 'algorithm' is algorithm number, for instance 1; parameter 'algorithm_name' is name of the algorithm, for instance "Hash Table"
def sort_and_measure(n, algorithm, algorithm_name):
    array = generate_input(n)
    start_time = time.time()

    # Run the chosen 'algorithm' 10 times
    # Algorithm 1 - Nested Loops - O(N^2)
    if(algorithm == 0):
        for i in range(0, 10): 
            algorithm_1(array, 0)
    # Algorithm 2 - Merge Sorting - O(N log N)
    elif(algorithm == 1):
        for i in range(0, 10): 
            algorithm_2(array, 0)
    # Algorithm 3 - Hash Table - O(N)
    elif(algorithm == 2):
        for i in range(0, 10):
            algorithm_3(array, 0)
    # Algorithm 4 - AVL Tree - O(N log N)
    elif(algorithm == 3):
        for i in range(0, 10):
            algorithm_4(array, 0)
    else:
        print("Invalid algorithm.")
        sys.exit()

    elapsed_time = time.time() - start_time
    elapsed_time = elapsed_time / 10 # Take the average of 10 runs of 'algorithm'
    print(f"{n} elements processed using {algorithm_name}. Time taken on average: {elapsed_time:.4f} seconds.")

    return elapsed_time

# Function to plot the performance of the sorting algorithms
# Parameter 'algorithms' input algorithm numbers, for instance 1; parameter 'algorithm_names' have names of the algorithms, for instance "Hash Table"
def plot_performance(algorithms, sizes, algorithm_names):
    results = {alg: {n: [] for n in sizes} for alg in algorithms}

    for alg in algorithms:
        for n in sizes:
            time_taken = sort_and_measure(n, alg, algorithm_names[alg])
            results[alg][n].append(time_taken)
    
    # Make legend
    for alg in algorithms:
        plt.plot(sizes, [results[alg][n][0] for n in sizes], label=algorithm_names[alg])
    
    plt.xlabel('Number of Elements')
    plt.ylabel('Average Time (seconds)')
    plt.title('Algorithm Performance for Searching an Array for Pair with Target Sum')
    plt.xticks(sizes, ['10000', '20000', '40000', '80000', '160000'])
    plt.legend()
    plt.show()

# PRIMARY FUNCTIONS
def generate_input(cnt):
    # Generate an array of 'cnt' totally random numbers in the range 0...10,000,000 inclusive
    return [random.randint(0, 999999) for _ in range(cnt)] 

if __name__ == "__main__":
    plot_performance([0, 1, 2, 3], [10000, 20000, 40000, 80000, 160000], ["Nested Loops", "Merge Sorting", "Hash Table", "AVL Tree"])

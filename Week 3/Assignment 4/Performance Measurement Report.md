# Performance Measurement Report

We will analyze the time complexity of each of the member functions of `AVLTree` individually. 

The sort version: All functions run in worst-case `O(log_2(n))` time because the AVL tree gaurantees an approximate `log_2(n)` height at all times, except for the `printTree()` function which takes `O(n)` since it must traverse over all nodes in order to print the entire tree.

## Insert
Our function `insert()` takes at most `O(log_2(n))` time, where `n` represents the number of nodes in our tree. This is because the AVL tree gaurantees an approximate `log_2(n)` height for the entire tree, even with all insertions and deletions. 

When we first call `insert()`, we start at the root of the AVL Tree and go downward, in total traversing a maximum of around `log_2(n)` nodes. For each of the nodes, there are some constant-time operations. Thus, our worst-case time complexity for `insert()` is `O(log_2(n))`.

## Left / Right Rotation
The functions `leftRotate()` and `rightrotate()` run in `O(1)`, or "constant-time". This is because when we rotate the tree, we are only re-assigning some left and right pointers, and updating a few heights. All operations of these two functions happen in constant time, thus they have a total `O(1)` time complexity.

## Contains
The function `contains()` takes worst case `O(log_2(n))` time, because we need to traverse at most `log_2(n)` levels to determine if a key exists in a tree(the AVL tree gaurantees an approximate `log_2(n)` height at all times). All the rest of the operations in the three functions, such as the comparisons, run in constant time.

## Find Min / Max
The functions `findMin()` and `findMax()` take worst case `O(log_2(n))` time too. We need to traverse at most `log_2(n)` levels to determine the key of the leftmost/rightmost node in the tree(the AVL tree gaurantees an approximate `log_2(n)` height at all times). All the rest of the operations in the two functions, such as the comparisons, run in constant time.

## Get a Key's Height / Depth
The functions `getHeightOfKey()` and `getDepth()` take worst case `O(log_2(n))` time too. We need to recursively traverse at most `log_2(n)` levels to find the node with the matching in the tree(the AVL tree gaurantees an approximate `log_2(n)` height at all times) and return its height/depth. All the rest of the operations in the two functions, such as the comparisons, run in constant time.

## Print Tree
The function `printTree()` takes `O(n)` since it must traverse over all nodes in order to print the entire tree. The function takes constant time to process/print each node, thus its total time complexity is worst case `O(n)`.

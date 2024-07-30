class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

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

    # Finds minimum key in the Tree, assumming that the Tree is not empty
    def findMin(self, root):
        # If tree is empty, return nothing so our program will show the user an error
        if(self.root == None):
            pass

        # Otherwise, recursively use the 'findMin' function to get the leftmost key in the tree
        if(root.left == None):
            return root
        else:
            return self.findMin(root.left)

    # Finds maximum key in the Tree, assumming that the Tree is not empty
    def findMax(self, root):
        # If tree is empty, return nothing so our program will show the user an error
        if(self.root == None):
            pass

        # Otherwise, recursively use the 'findMax' function to get the rightmost key in the tree
        if(root.right == None):
            return root
        else:
            return self.findMax(root.right)

    # Get height of key; the function assumes that 'key' is contained in the AVL tree; If it is not, the function returns -1
    def getHeightOfKey(self, root, key):
        # In new Nodes, the height was set to default = 1(even though new nodes start out with height of 0), so we always return 'root.height - 1' to account for this
        if root == None:
            # If 'key' does not exist in AVL tree, then return -1
            return -1
        if root.key == key:
            # If 'root's key is equal to target 'key', return 'key's height
            return root.height - 1
        elif key < root.key:
             # Otherise, traverse to the left...
            return self.getHeightOfKey(root.left, key)
        elif root.key < key:
            # Or right branches of 'root' depending on how 'key' compares to 'root.key'
            return self.getHeightOfKey(root.right, key)

    # Get depth of key; the function assumes that 'key' is contained in the AVL tree; If it is not, the function returns -1
    def getDepth(self, root, key, depth=0):
        if root == None:
            # If 'key' does not exist in AVL tree, then return -1
            return -1
        elif root.key == key:
            # If 'root's key is equal to target 'key', return 'key's depth
            return depth
        elif key < root.key:
             # Otherise, traverse to the left...
            return self.getDepth(root.left, key, depth + 1)
        elif root.key < key:
            # Or right branches of 'root' depending on how 'key' compares to 'root.key'
            return self.getDepth(root.right, key, depth + 1)

    def printTree(self, root, level=0, pref="Root:"):
        # Print the AVL tree
        if root is not None:
            print("-" * level, pref, root.key)
            if root.left is not None:
                self.printTree(root.left, level + 1, "L---")
            if root.right is not None:
                self.printTree(root.right, level + 1, "R---")

def run_avl_tree():
    avl_tree = AVLTree()
    root = None

    while True:
        print("\n------------ AVL Tree ------------")
        print("0. Show menu")
        print("1. Insert a new key")
        print("2. Check if key exists")
        print("3. Find node’s height")
        print("4. Find node’s depth")
        print("5. Find min value")
        print("6. Find max value")
        print("7. Print tree")
        print("8. Exit")

        try:
            choice = int(input("> "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 0:
            print("\n------------ AVL Tree ------------")
            print("0. Show menu")
            print("1. Insert a new key")
            print("2. Check if key exists")
            print("3. Find node’s height")
            print("4. Find node’s depth")
            print("5. Find min value")
            print("6. Find max value")
            print("7. Print tree")
            print("8. Exit")
        elif choice == 1:
            try:
                key = int(input("input a key: "))
                root = avl_tree.insert(root, key)
                print(f"{key} is added to the tree")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == 2:
            try:
                key = int(input("input a key: "))
                if avl_tree.contains(root, key):
                    print(f"{key} exists in the tree")
                else:
                    print(f"{key} does not exist in the tree")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == 3:
            try:
                key = int(input("input a key: "))
                height = avl_tree.getHeightOfKey(root, key)
                if height != -1:
                    print(f"{key}’s height is {height}")
                else:
                    print(f"{key} does not exist in the tree")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == 4:
            try:
                key = int(input("input a key: "))
                depth = avl_tree.getDepth(root, key)
                if depth != -1:
                    print(f"{key}’s depth is {depth}")
                else:
                    print(f"{key} does not exist in the tree")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == 5:
            min_node = avl_tree.findMin(root)
            if min_node:
                print(f"{min_node.key} is the minimum value in the tree")
            else:
                print("The tree is empty")
        elif choice == 6:
            max_node = avl_tree.findMax(root)
            if max_node:
                print(f"{max_node.key} is the maximum value in the tree")
            else:
                print("The tree is empty")
        elif choice == 7:
            if root:
                avl_tree.printTree(root)
            else:
                print("The tree is empty")
        elif choice == 8:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_avl_tree()

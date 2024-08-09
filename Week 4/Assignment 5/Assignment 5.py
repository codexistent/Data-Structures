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
            self.rehash(self)


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

# Testing the HashTable class
if __name__ == "__main__":
    ht = HashTable()

    # Insert key-value pairs
    ht.insert("name", "Alice")
    ht.insert("age", 25)
    ht.insert("city", "New York")
    ht.insert("email", "alice@example.com")
    ht.insert("phone", "123-456-7890")

    # Search for keys
    print(ht.search("name"))   # Expected Output: Alice
    print(ht.search("age"))    # Expected Output: 25
    print(ht.search("city"))   # Expected Output: New York
    print(ht.search("email"))  # Expected Output: alice@example.com
    print(ht.search("phone"))  # Expected Output: 123-456-7890
    print(ht.search("country"))  # Expected Output: None

    # Delete a key
    ht.delete("email")

    # Search again
    print(ht.search("email"))  # Expected Output: None

    # Verify remaining key-value pairs
    print(ht.search("name"))   # Expected Output: Alice
    print(ht.search("age"))    # Expected Output: 25
    print(ht.search("city"))   # Expected Output: New York
    print(ht.search("phone"))  # Expected Output: 123-456-7890

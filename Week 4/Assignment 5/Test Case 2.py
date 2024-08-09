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

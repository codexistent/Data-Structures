# Testing the HashTable class
if __name__ == "__main__":
    ht = HashTable()

    print(ht.size)                    # Expected Output: 10

    # Insert key-value pairs
    ht.insert("diamond", "clear")
    ht.insert("ruby", "red")
    ht.insert("emerald", "green")
    ht.insert("beryl", "red")
    ht.insert("jadenite", "purple")
    ht.insert("rose gold", "pink")
    ht.insert("musgravite", "grey")
    ht.insert("tanzanite", "pink")
    ht.insert("opal", "rainbow")

    print(ht.size)                    # Expected Output: 20 (from rehashing)

    # Delete keys
    ht.delete("rose gold")
    ht.delete("emerald")

    # Search for keys
    print(ht.search("beryl"))         # Expected Output: "red"
    print(ht.search("musgravite"))    # Expected Output: "grey"

    # Delete more keys
    ht.delete("opal")

    # Search again
    print(ht.search("diamond"))       # Expected Output: "clear"
    print(ht.search("opal"))          # Expected Output: None
    print(ht.search("tanzanite"))     # Expected Output: "pink"

    # Insert/change the value of key "tanzanite"
    ht.insert("tanzanite", "rose")

    # Verify change
    print(ht.search("tanzanite"))     # Expected Output: "rose"

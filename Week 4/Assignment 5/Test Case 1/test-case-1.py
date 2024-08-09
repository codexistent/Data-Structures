# Testing the HashTable class
if __name__ == "__main__":
    ht = HashTable()

    print(ht.size)                    # Expected Output: 10

    # Insert key-value pairs
    ht.insert("order id", 123)
    ht.insert("product", "Butter Shampoo")
    ht.insert("price", 45)
    ht.insert("discount", "butter")

    # If key "discount" has value "butter"
    if(ht.search("discount") == "butter"):
        # Then change key "price" to have value 30
        ht.insert("price", 30)

    print(ht.search("price"))         # Expected Output: 30

    # Insert more key-value pairs
    ht.insert("goodies", 11)
    # If the value of key "price" is greater than 40, then insert a key "free shipping" with value True
    # Otherwise, insert key "free shipping" with value False
    ht.insert("free shipping", (ht.search("price") > 40)) 

    # If key "free shipping" is False
    if(not ht.search("free shipping")):
        # Change key "price" to its current value + 20
        ht.insert("price", ht.search("price") + 20)

    print(ht.search("price"))         # Expected Output: 50

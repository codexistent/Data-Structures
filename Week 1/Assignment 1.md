# [1] Code (with comments)
```python
def min_coins_dp(coins, amount):
    # Initialize an array dp of size amount + 1 with a high value (infinity)
    dp = [float('inf')] * (amount + 1)
    # Base case: No coins are needed to make up the amount 0
    dp[0] = 0

    # Compute the minimum number of coins by using a nested for loop, and updating higher 
    # Loop through each possible idx from 0...amount - 1, where idx represents the amount of money
    for idx in range(amount): # We do not have to iterate when idx = amount because it cannot update higher indexes
        # Loop through each possible coin value
        for coin in coins:
            # if dp[idx] is infinity, we cannot achieve 'idx' amount of money
            if dp[idx] == float('inf'): 
                # so we continue
                continue

            # if idx + coin amount of money does not acceed amount
            if idx + coin <= amount:
                # update dp at index 'idx + coin'
                dp[idx + coin] = min(dp[idx] + 1, dp[idx + coin])

    # If dp[amount] is still infinity, return -1
    if dp[amount] == float('inf'):
        return -1

    # Otherwise, return dp[amount]
    return dp[amount]

def main():
    # Read input
    coins = list(map(int, input("Enter the denominations (space-separated): ").split()))
    amount = int(input("Enter the amount: "))

    # Call the min_coins_dp function
    result = min_coins_dp(coins, amount)
    
    # Print the result

    print(f"Minimum number of coins needed: {result}")

if __name__ == "__main__":
    main()
```

# [2] Testing the Code
## First Test
![Screenshot](https://github.com/codexistent/Data-Structures/assets/77512088/6b19bfae-25ce-43da-bdde-85ab5da38590)
## Second Test
![Screenshot](https://github.com/codexistent/Data-Structures/assets/77512088/48994bf1-d468-4002-9b4d-17f96f2c9ac0)
## Third Test
![Screenshot](https://github.com/codexistent/Data-Structures/assets/77512088/54bf21e6-957f-4799-86d2-851ab75702de)


# [3] Time Complexity
The time complexity of this code in Big-O notation is `O(amount * (size of coins list))`(**NOT** `O((amount + 1) * (size of coins list))`) because the most time-consuming part of the code is the nested for loop. The outer loop of the nested for loops has `amount` iterations, and the inner loop of the nested for loops has `size of coins list` iterations. The time complexity of the code inside the nested for loops is constant, so that's why our final time complexity is `O(amount * (size of coins list))`. 

# [4] Space Complexity Analysis
We use :
- `1` variable each for `amount` and `result`
- `size of coins list` variables for the `coins` list
- `amount + 1` variables for the `dp` array

So, our space complexity is `2 + (size of coins list) + (amount + 1)` = `3 + (size of coins list) + amount` variables.

# [1] Code

In the nested for loop, we will update the indicies of the `dp` array.
The outer loop of the nested loops iterates through each coin `coin` in coins array. 
For each `coin`, we iterate through the dp indicies `idx` from 0...`amt` in reverse order(so that we don't reuse any coin), where `idx` represents money. 

Now, inside the inner for loop: 
We first check if it is possible to have `idx - coin` money with `dp[idx - coin]` coins. If this is true, then we can make `idx` money with `dp[idx - coin] + 1` coins.
We do NOT update `dp[idx]` if `idx - coin` is a negative value, because we cannot have a negative amount of money.
We do NOT update `dp[idx]` if `dp[idx - coin]` equals `float('inf')`, because it is NOT currently possible to make `'idx - coin'` money with any amount of coins.
Otherwise, we update `dp[idx]` with the minimum of its current value and `dp[idx - coin] + 1`.

Our answer is ten `dp[amount]`.
```python
def min_coins_dp(coins, amount):
    # Initialize an array dp of size amount + 1 with a high value (infinity)
    dp = [float('inf')] * (amount + 1)
    # Base case: No coins are needed to make up the amount 0
    dp[0] = 0

    # Loop through each coin in coins array
    for coin in coins:
        # Loop through the dp indicies from 0...amt in reverse order(so that we don't reuse any coin), where the index idx represents money
        for idx in reversed(range(amount + 1)): 
            # if it is possible to have 'idx - coin' money with dp[idx - coin] coins, then we can make 'idx' money with dp[idx - coin] + 1 coins
            #   we do NOT update dp[idx] if 'idx - coin' is a negative value, because we cannot have a negative amount of money
            #   we do NOT update dp[idx] if dp[idx - coin] equals float('inf'), because it is NOT currently possible to make 'idx - coin' money with any amount of coins
            if 0 <= idx - coin and dp[idx - coin] != float('inf'): 
                # so we update dp at index 'idx'
                dp[idx] = min(dp[idx - coin] + 1, dp[idx])

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
![Screenshot1](https://github.com/user-attachments/assets/9e862429-8ff6-4ec9-b4e0-bcf0478524cc)
## Second Test
![Screenshot2](https://github.com/user-attachments/assets/d56be87a-2ea1-46e0-a43d-7dbc3c95f8ea)
## Third Test
![Screenshot3](https://github.com/user-attachments/assets/73e4989b-37e5-4667-a29b-ab82fe3da679)


# [3] Time Complexity
The time complexity of this code in Big-O notation is `O((size of coins list) * (amount + 1))`.

This is because the most time-consuming part of the code is the nested for loop. The outer loop of the nested for loops has `size of coins list` iterations, and the inner loop of the nested for loops has `amount + 1` iterations. The time complexity of the code inside the nested for loops is constant, so that's why our final time complexity is `O((size of coins list) * (amount + 1))`. 

# [4] Space Complexity Analysis
We use :
- `1` variable each for `amount` and `result`
- `size of coins list` variables for the `coins` list
- `amount + 1` variables for the `dp` array

So, our space complexity is `2 + (size of coins list) + (amount + 1)` = `3 + (size of coins list) + amount` variables.

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

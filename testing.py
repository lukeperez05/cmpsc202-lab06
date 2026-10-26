def coin_change_dp(coins, amount):
    dp = [0]
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]

print("min coins:", coin_change_dp([1, 2, 5], 11))
# Lab 06: Demystifying Dynamic Programming with Coin Change

**The Problem**: Given an array of coin denominations (e.g., [1, 2, 5]) and a target amount V, find the minimum number of coins needed to make exact change.

In this lab, you will implement three different approaches to solve the coin change problem: a naive recursive approach, a top-down dynamic programming approach (memoization), and a bottom-up dynamic programming approach (tabulation). You will also compare the performance of these approaches empirically.

You may work in small groups or individually. If you work in pairs, please submit a single solution and note your names in the final write-up.

## Phase 1: The Naive Recursive Approach

**Task**: Write a Python function `coin_change_recursive(coins, amount)`, then test it on a small amount (e.g., `amount = 11` with `coins = [1, 2, 5]`). It should run in less than a second.
```
def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    opt = []
    for coin in coins:
        if coin <= amount:
            opt.append(1 + coin_change_recursive(coins, amount-coin))
    return min(opt)

print("min coins:", coin_change_recursive([1, 2, 5], 11))
```

## Phase 2: Top-Down DP (Memoization)

Recall that the naive recursive approach might solve the same subproblems multiple times. We can optimize it by storing previously computed results in a dictionary (memoization).

**Task**: Modify your `coin_change_recursive` function to `coin_change_memoized(coins, amount, memo)`, where you use a `dict` to store the minimum number of coins needed for each amount. 

**Logic**:
- If the amount is 0, return 0 (base case).
- If the amount is already in `memo`, return the stored value.
- Otherwise, iterate through each coin and recursively compute the minimum number of coins needed for the remaining amount (i.e., `amount - coin`). Store the result in `memo` before returning it.
```
def coin_change_memoized(coins, amount, memo):
    if amount == 0:
        return 0
    if amount in memo:
        return memo[amount]
    opt = []
    for coin in coins:
        if coin <= amount:
            opt.append(1 + coin_change_memoized(coins, amount-coin, memo))
    memo[amount] = min(opt)
    return memo[amount]

print("min coins:", coin_change_memoized([1, 2, 5], 11, {}))
```

## Phase 3: Bottom-Up DP (Tabulation)

Rather than using recursion, we can build up a solution iteratively. This is known as the Bottom-Up approach. Essentially, we will create an array `L`, where `L[i]` will hold the minimum number of coins needed to make change for amount `i`. We will initialize `L[0] = 0` (since no coins are needed to make change for 0) and fill in the rest of the array based on previously computed values. You can think of this as directly computing the cached table from the memoization approach.

**Task**: Write `coin_change_dp(coins, amount)`.

**Logic**: 
- Initialize a list `dp`. Set `dp[0] = 0`. 
- Iterate through each amount from `1` to `amount`, and for each `coin`, update `dp[i] = min(dp[i], dp[i - coin] + 1)`.
```
def coin_change_dp(coins, amount):
    dp = [0] + [float('i')] * amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]

print("min coins:", coin_change_dp([1, 2, 5], 11))
```

## Phase 4: Empirical Comparison

**Task**: Compare the performance of the three approaches (naive recursive, memoized, and bottom-up) on a collection of amounts for a given set of coins. Measure the time taken for each approach and report your findings either in a table or a plot. Then, write up a brief summary of the setup and your findings in a markdown file called `empirical_comparison.md`, which includes your plot or table. This write-up should contain no more than a paragraph or two of text.

## Phase 5: Submission

Your submission should include:
- The three functions: `coin_change_recursive`, `coin_change_memoized`, and `coin_change_dp` in a single Python file called `coin_change.py`
- A brief write-up on the performance comparison (no more two paragraphs), including any plots or tables you created in a markdown file called `empirical_comparison.md`.
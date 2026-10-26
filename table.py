import matplotlib.pyplot as plt
from pathlib import Path
from time import perf_counter

def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    opt = []
    for coin in coins:
        if coin <= amount:
            opt.append(1 + coin_change_recursive(coins, amount-coin))
    return min(opt)

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

def coin_change_dp(coins, amount):
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]

def benchmark(solve, amounts, repeats):
    times = []
    for amount in amounts:
        elapsed = 0
        for _ in range(repeats):
            start = perf_counter()
            solve(amount)
            elapsed += perf_counter() - start
        times.append(elapsed / repeats)
    return times

if __name__ == "__main__":
    coins = [1, 2, 5]
    amounts = list(range(1, 26))
    repeats = 3
    algorithms = {
        "Naive recursion": lambda amount: coin_change_recursive(coins, amount),
        "Memoization": lambda amount: coin_change_memoized(coins, amount, {}),
        "Bottom-up DP": lambda amount: coin_change_dp(coins, amount),}

    timings = {
        name: benchmark(solve, amounts, repeats)
        for name, solve in algorithms.items()}

    for amount in amounts:
        answers = [solve(amount) for solve in algorithms.values()]
        if len(set(answers)) != 1:
            raise ValueError(f"Algorithms disagree for amount {amount}: {answers}")

    for name, times in timings.items():
        plt.plot(amounts, times, marker="o", label=name)

    plt.xlabel("Amount")
    plt.ylabel("Average running time (seconds)")
    plt.title(f"Coin-change runtime comparison (coins: {coins})")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    graph_path = Path(__file__).with_name("coin_change_performance.png")
    plt.savefig(graph_path, dpi=300)
    print(f"Saved runtime graph to {graph_path}")
    plt.show()
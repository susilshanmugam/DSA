import math

def coin_change(coins: list[int], amount: int) -> int:
    """
    Calculates the fewest number of coins needed to make up a given amount.

    Args:
        coins: A list of integers representing coin denominations.
        amount: The target amount to make up.

    Returns:
        The fewest number of coins, or -1 if the amount cannot be made up.

    Approach: Dynamic Programming (Bottom-Up Tabulation)
    1. DP State: dp[i] will store the minimum number of coins required to make amount `i`.
    2. Initialization:
       - dp[0] = 0 (0 coins are needed for amount 0).
       - All other dp[i] are initialized to a value indicating "not possible"
         (e.g., amount + 1, since using `amount + 1` coins of value 1 would exceed `amount`).
         `float('inf')` is also a good choice.
    3. Transitions:
       - Iterate through each possible amount `i` from 1 to `amount`.
       - For each amount `i`, iterate through each `coin` in the `coins` list.
       - If a `coin` is less than or equal to the current amount `i` (i.e., `i - coin >= 0`):
         It means we can potentially use this `coin`.
         The number of coins to make amount `i` using this `coin` would be `1 + dp[i - coin]`
         (1 for the current coin, plus the minimum coins needed for the remaining amount `i - coin`).
         We update `dp[i]` with the minimum of its current value and `1 + dp[i - coin]`.
    4. Result:
       - After filling the dp table, `dp[amount]` will contain the minimum coins for the target amount.
       - If `dp[amount]` is still the initial "not possible" value, it means the amount cannot be formed,
         so return -1. Otherwise, return `dp[amount]`.
    """
    if amount < 0:
        return -1 # Cannot make a negative amount
    if amount == 0:
        return 0

    # Initialize dp array. dp[i] will be the minimum coins to make amount i.
    # Using amount + 1 as a stand-in for infinity, as it's an impossible number of coins.
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # 0 coins to make amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                # If we use this coin, the remaining amount is i - coin.
                # We need dp[i - coin] coins for that, plus 1 for the current coin.
                if dp[i - coin] != amount + 1: # Check if dp[i-coin] is reachable
                    dp[i] = min(dp[i], 1 + dp[i - coin])

    # If dp[amount] is still amount + 1, it means it's not possible to make that amount.
    if dp[amount] == amount + 1:
        return -1
    else:
        return dp[amount]

if __name__ == "__main__":
    # Example 1
    coins1 = [1, 2, 5]
    amount1 = 11
    print(f"Coins: {coins1}, Amount: {amount1}, Min Coins: {coin_change(coins1, amount1)}") # Expected: 3 (5+5+1)

    # Example 2: Amount cannot be made
    coins2 = [2]
    amount2 = 3
    print(f"Coins: {coins2}, Amount: {amount2}, Min Coins: {coin_change(coins2, amount2)}") # Expected: -1

    # Example 3: Amount is 0
    coins3 = [1, 2, 3]
    amount3 = 0
    print(f"Coins: {coins3}, Amount: {amount3}, Min Coins: {coin_change(coins3, amount3)}") # Expected: 0

    # Example 4: Single coin type, possible
    coins4 = [3]
    amount4 = 9
    print(f"Coins: {coins4}, Amount: {amount4}, Min Coins: {coin_change(coins4, amount4)}") # Expected: 3 (3+3+3)

    # Example 5: Single coin type, not possible
    coins5 = [5]
    amount5 = 7
    print(f"Coins: {coins5}, Amount: {amount5}, Min Coins: {coin_change(coins5, amount5)}") # Expected: -1

    # Example 6: Larger amount
    coins6 = [1, 5, 10, 25]
    amount6 = 137 # 5*25 (125) + 1*10 (10) + 2*1 (2) = 137 -> 5+1+2 = 8 coins. No, better: 13*10 + 7*1 -> 20 coins
                 # 25*5 = 125, rem 12. 10*1 = 10, rem 2. 1*2=2. Total 5+1+2 = 8 coins.
                 # DP should find optimal. (e.g. for 30, 25+5 is 2 coins, 10+10+10 is 3 coins)
                 # For 137: 25*5 = 125 (5 coins), remaining 12.
                 # For 12: 10*1 (1 coin), remaining 2.
                 # For 2: 1*2 (2 coins).
                 # Total = 5 + 1 + 2 = 8 coins.
    print(f"Coins: {coins6}, Amount: {amount6}, Min Coins: {coin_change(coins6, amount6)}")

    # Example 7: No coins
    coins7 = []
    amount7 = 1
    print(f"Coins: {coins7}, Amount: {amount7}, Min Coins: {coin_change(coins7, amount7)}") # Expected: -1

    # Example 8: No coins, amount 0
    coins8 = []
    amount8 = 0
    print(f"Coins: {coins8}, Amount: {amount8}, Min Coins: {coin_change(coins8, amount8)}") # Expected: 0

    # Example 9: Amount is smaller than any coin
    coins9 = [5, 10]
    amount9 = 3
    print(f"Coins: {coins9}, Amount: {amount9}, Min Coins: {coin_change(coins9, amount9)}") # Expected: -1
    
    # Example 10: LeetCode case: coins = [186,419,83,408], amount = 6249
    # Expected: 20 (e.g. 83*1 + 408*2 + 186*28 = 83 + 816 + 5208 = 6107 (too complex to do by hand quickly)
    # The DP will find it. Let's take a smaller one from there:
    # coins = [2], amount = 1 -> -1
    # coins = [1], amount = 1 -> 1
    # coins = [1], amount = 2 -> 2
    coins10 = [186,419,83,408]
    amount10 = 6249
    #This might be slow to run in __main__ if amount is very large, but the logic is sound.
    #For testing, it's better suited for a unit test that might be skipped in quick runs.
    print(f"Coins: {coins10}, Amount: {amount10}, Min Coins: {coin_change(coins10, amount10)}")

```

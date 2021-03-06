class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mincoinstable= [float("inf") for i in range(amount+1)]
        mincoinstable[0]=0
        
        for eachcoin in coins:
            for target in range(0,amount+1):
                if eachcoin <= target:
                    mincoinstable[target]= min(mincoinstable[target],1+mincoinstable[target-eachcoin])
        return mincoinstable[target] if mincoinstable[target]!= float("inf") else -1
        
        
        
        O(nd) -> Time
        O(n) -> Space
        
        
        You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2

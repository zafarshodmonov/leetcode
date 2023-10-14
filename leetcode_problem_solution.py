
class Solution:

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cur = 0 
        dp0 = cost[0]
        if len(cost) >= 2:
            dp1 = cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = cur

        return min(dp0, dp1)
    
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        return count
        


def main() -> None:
    pass

if __name__ == "__main__":
    main()


class Solution:

    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        m = {"type": 0, "color": 1, "name": 2}
        for i in items:
            if ruleValue == i[m[ruleKey]]:
                count += 1
        return count
        

    def decompressRLElist(self, nums: list[int]) -> list[int]:
        rel, i = [], 0
        while len(nums) > 2 * i + 1:
            rel += nums[2 * i] * [nums[2 * i + 1]]
            i += 1
        return rel

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

    def leftRightDifference(self, nums: list[int]) -> list[int]:
        rs, ls, ans = sum(nums), 0, []
        for i in nums:
            rs -= i 
            ans.append(abs(ls - rs))
            ls += i
        return ans
      
        

def main() -> None:
    pass

if __name__ == "__main__":
    main()

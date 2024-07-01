
class LeetCode:

    def F1(self, nums: list[int], target: int) -> list[int]:
        m = {}
        for i, e in enumerate(nums):
            if e in m:
                return [m[e], i]
            
            m[target - e] = i
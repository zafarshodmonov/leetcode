
class LeetCode:

    def F1(self, nums: list[int], target: int) -> list[int]:
        m = {}
        for i, e in enumerate(nums):
            if e in m:
                return [m[e], i]
            
            m[target - e] = i

    @staticmethod
    def F1_test():
        return [
            ([1, 2, 3, 4, 5, 6], 4, [0, 2])
        ]
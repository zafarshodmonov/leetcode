from typing import List
from functools import lru_cache

class WeeklyContest400:
    pass


class WeeklyContest401:
    pass


class WeeklyContest402:
    pass


class WeeklyContest403:
    pass


class WeeklyContest404:

    def help_B1(self, nums: list[int]) -> list[list[int]]:
        
        rel = []
        n = len(nums)

        for i in range(n):

            item = nums[i]

            if not (rel == []):
                kel = rel.copy()
                for j in kel:
                    h = j[:]
                    h.append(item)
                    rel.append(h)

            rel.append([item])

        return rel

    def help_B(self, nums: list[int]) -> bool:
        
        n = len(nums)
        if n <= 1:
            return
        juft_or_toq = (nums[0] + nums[1]) % 2
        for i in range(n - 1):
            if (nums[i] + nums[i + 1]) % 2 == juft_or_toq:
                pass
            else:
                return False
        return True

    def help_A(self, A: int, B: int) -> int:
        nav = True
        zamax = 0
        i = 1
        while True:
            if nav:
                if A >= i:
                    zamax += 1
                    A -= i
                    nav = not nav
                else:
                    break
            else:
                if B >= i:
                    zamax += 1
                    B -= i
                    nav = not nav
                else:
                    break

            i += 1
        
        return zamax

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.help_A(red, blue), self.help_A(blue, red))
    
    def maximumLength(self, nums: List[int]) -> int:

        @lru_cache
        def dfs(i, m):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) % 2 == m:
                    return dfs(j, m) + 1

            return 0

        best = 0
        for i in range(len(nums)):
            best = max(best, max(dfs(i, 0), dfs(i, 1)) + 1)

        return best
    
    def maximumLength2(self, nums: list[int], k: int) -> int:
        pass

    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        pass
   
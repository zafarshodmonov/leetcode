
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
        # nums = [1, 2, 3]
        rel = []  # rel = [[1], [1, 2], [2]]
        n = len(nums)  # n = 3

        for i in range(n):  # 0 +1 2
            item = nums[i]  # item = 2
            if not (rel == []):
                for j in rel:  # [1]
                    h = j[:]  # h = [1, 2]
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
    
    def maximumLength(self, nums: list[int]) -> int:
        pass

    def maximumLength2(self, nums: list[int], k: int) -> int:
        pass

    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        pass
   
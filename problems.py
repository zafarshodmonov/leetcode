

class LeetCodeTest:

    @staticmethod
    def F1_test():
        return [
            # ([2, 7, 11, 15], 9, [0, 1]),
            # ([3, 2, 4], 6, [1, 2]),
            # ([3, 3], 6, [0, 1]),
            ([1, 2, 3, 4, 5, 6], 5, [0, 3], [[0, 3], [1, 2]]),
            # ([1, 7, 8, 3, 5], 9, [0, 2])
        ]
    
    @staticmethod
    def F20_test():
        return [
            ('()', True),
            ('()[]{}', True),
            ('(]', False),
            ('(', False),
            (']', False)
        ]

    @staticmethod
    def F412_test():
        return [
            (3, ["1","2","Fizz"]),
            (5, ["1","2","Fizz","4","Buzz"]),
            (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
        ]


class LeetCodeHelp:

    @staticmethod
    def F412_help_1():
        return "FizzBuzz"

    @staticmethod
    def F412_help_2():
        return "Fizz"
    
    @staticmethod
    def F412_help_3():
        return "Buzz"

    def F412_help_4(self, n: int) -> str:
        return str(n)


class LeetCode(LeetCodeTest, LeetCodeHelp):

    def F1(self, nums: list[int], target: int) -> list[int]:
        m = {}
        for i, e in enumerate(nums):
            if e in m:
                return [m[e], i]
            
            m[target - e] = i

    def F20(self, s: str) -> bool:
        zamap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for l in s:
            if l in zamap:
                if stack == []:
                    return False
                if zamap[l] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        return True if stack == [] else False

    def F412(self, n: int) -> list[str]:
        rel = []
        for i in range(1, n + 1):
            a = i % 3 == 0
            b = i % 5 == 0
            if a and b:
                rel.append(self.F412_help_1())
            elif a:
                rel.append(self.F412_help_2())
            elif b:
                rel.append(self.F412_help_3())
            else:
                rel.append(self.F412_help_4(i))
        return rel 
    
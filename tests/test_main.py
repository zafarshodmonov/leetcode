import pytest
from test_random import N

from leetcode_problem_solution import Solution

sol = Solution()

@pytest.mark.parametrize("s, nums", N)
def test_1(s, m):
    assert sol.minCostClimbingStairs(s) == m

print(N)

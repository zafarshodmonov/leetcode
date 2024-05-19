import pytest

from leetcode_problem_solution import Solution
from tests.test_random import random_IP, restoreIpAddresses

sol = Solution()
N = []

for ip in random_IP(100):
    N.append((ip, restoreIpAddresses(ip)))

@pytest.mark.parametrize("s, m", N)
def test_1(s, m):
    assert sol.restoreIpAddresses(s) == m



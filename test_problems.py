import pytest

from biweekly_contest import BiweeklyContest130
from problems import LeetCode
from weekly_contest import WeeklyContest400

leetcode = LeetCode()

@pytest.mark.parametrize(
        "n, out",
        leetcode.F412_test()
)
def test_leetcode(n, out):
    assert leetcode.F412(n) == out
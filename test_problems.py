import pytest

from biweekly_contest import BiweeklyContest130
from problems import LeetCode
from weekly_contest import WeeklyContest400

leetcode = LeetCode()

@pytest.mark.parametrize(
        "s, out",
        leetcode.F20_test()
)
def test_leetcode(s, out):
    assert leetcode.F20(s) == out
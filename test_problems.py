import pytest

from biweekly_contest import BiweeklyContest130
from problems import LeetCode
from weekly_contest import WeeklyContest400

leetcode = LeetCode()

@pytest.mark.parametrize(
        "nums, target, out",
        leetcode.F1_test()
)
def test_F1(nums, target, out):
    assert leetcode.F1(nums, target) == out
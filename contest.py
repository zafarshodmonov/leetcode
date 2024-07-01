from biweekly_contest import BiweeklyContest131
from weekly_contest import WeeklyContest404


def main():
    weekly = WeeklyContest404()
    biweekly = BiweeklyContest131()

    # Input
    nums = [1, 2, 3]

    # processing
    ans = weekly.help_B1(nums)

    # Output
    print(ans)

if __name__ == "__main__":
    main()

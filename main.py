import calendar
import datetime

def main() -> None:
    ca = calendar.Calendar()
    for i in ca.itermonthdates(2023, 10):
        print(i)

if __name__ == "__main__":
    main()

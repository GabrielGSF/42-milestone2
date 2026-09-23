def print_days(day: int, total_days: int) -> None:
    if day > total_days:
        print("Harvest time!")
        return
    else:
        print(f"Day {day}")
    print_days((day + 1), total_days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    print_days(1, days)

def calculate_pay(hours, wage):
    total_wage = 0
    double_wage = 2 * wage
    over_time_hours = 0
    if hours <= 0 or wage <= 0:
        return 0
    if hours > 40:
        total_wage += wage * 40
        over_time_hours = hours - 40
        total_wage += double_wage * over_time_hours
    else:
        total_wage += wage * hours
    return total_wage





def main():
    print("calculate_pay(10,10): ", calculate_pay(10, 10))
    print()
    print("calculate_pay(40,10): ", calculate_pay(40, 10))
    print()
    print("calculate_pay(50,10): ", calculate_pay(50, 10))


if __name__ == "__main__":
    main()

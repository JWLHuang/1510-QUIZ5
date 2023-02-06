def calculate_pay(hours, wage):
    total_wage = 0
    double_wage = 2 * wage
    if hours <= 0 or wage <= 0:
        return 0

    if hours > 40:
        range_of_hours = range(41, hours+1)
        for i in range_of_hours:
            wages
    if hours <= 40:
        total_wage += hours * wage

    while hours > 40:
        total_wage += hours * double_wage
    return total_wage





def main():
    print("calculate_pay(10,10): ", calculate_pay(10, 10))
    print()
    print("calculate_pay(50,10): ", calculate_pay(50, 10))


if __name__ == "__main__":
    main()

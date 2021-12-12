def bank(money, years, interest):
    for month in range(years * 12):
        money += (money / 100) * interest / 12
    return money


print(int(bank(int(input()), int(input()), float(input()))))

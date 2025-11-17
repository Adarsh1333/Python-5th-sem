num=input()

years =int(num) // 365
num = int(num) % 365

months = int(num) // 30
num = int(num) % 30

days = int(num)
print(years, "years")
print(months, "months")
print(days, "days")
        
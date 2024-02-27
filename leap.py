# This python program inputs a year and it checks if the inputted
# year is a leap year or not
# A leap year is divisble by 4 but it is not divisible by 100 and it is also
# divisble by 400
# It outputs True if it is a leap year and False if not
year = int(input("Enter a year to check if its leap or not: "))

def is_leap(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        return True
    else:
        return False
print(year, " is a leap year is ",is_leap(year))
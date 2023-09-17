# Michelle Oteri
# 2252197

import datetime

def calculate_age(birthdate, current_date):
    years_difference = current_date.year - birthdate.year
    is_before_birthday = (current_date.month, current_date.day) < (birthdate.month, birthdate.day)
    age = years_difference - int(is_before_birthday)
    return age

print("Current day")
current_month = int(input("Month: "))
current_day = int(input("Day: "))
current_year = int(input("Year: "))

print("Birthday")
birth_month = int(input("Month: "))
birth_day = int(input("Day: "))
birth_year = int(input("Year: "))

current_date = datetime.date(current_year, current_month, current_day)
birthday = datetime.date(birth_year, birth_month, birth_day)

age = calculate_age(birthday, current_date)

print("You are", age, "years old.")

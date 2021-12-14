# function calculating a leap year

def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# function calculating the number of days in a month

days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]       

def days_in_month(month, year):
    if leap_year(year) and month == 2:
        return 29
    return days_in_months[month]
    
# function calculating the day of the year

def day_of_the_year(day, month, year):
    total = sum(days_in_months[:month]) + day
    # print(total)
    if month > 2 and leap_year(year) == True:
        total += 1
    return total
    
     
year = int(input("Enter the number of the year: "))  
print(f"Whether {year} is a leap year?")    
print(leap_year(year))

month = int(input("Enter the number of the month: "))
year = int(input("Enter the number of the year: "))
print(f"You have chosen {month} month and the year {year}. This month has", (days_in_month(month, year)), "days.")
  
day = int(input("Enter the number of the day: "))
month = int(input("Enter the number of the month: "))
year = int(input("Enter the number of the year: "))
print(day_of_the_year(day, month, year))

input = input('Enter a year to know if it is a leap year: ')
year = int(input)

def leapYear(year):
    if year % 4 == 0:
        return 'it\'s leap year'
    else:
        return 'it isn\'t leap year'



print(leapYear(year))
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

result = filter(lambda num: num % 2 != 0, numbers)
print(f'The result of odd sum is: {reduce(lambda a, b: a + b, result)}')





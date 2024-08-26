integer = 2 + 3 * 5
print(integer)

my_integer = 4
my_float = 2.5
summary = my_float + my_integer
print(summary)

my_float = float(input('input the number: '))
my_int = int(my_float)
print(my_int)

ten_1 = 10
ten_2 = 10
equal = ten_1 == ten_2
print(equal)

nine = 9
ten_1 = 10
not_equal = nine != ten_1
print(not_equal)

# == - сравнение
# <= or => - больше меньше или равно 
# = - равно

year = int(input('enter the year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'{year} is a leap year')

else:
    print(f'{year} is not a leap year')

print(not 3)

my_list = list(range(10))
print(my_list)

number_multiply = 1
number_index = 1

for i in range(1,100):
    result = number_multiply * number_index
    print(f'{number_multiply} * {number_index} = {result}')
    number_index += 1 
    if number_index == 10:
        number_index = 1
        number_multiply += 1
        if number_multiply == 10:
            break

def finder_alph(string):
    count = 0
    alph = "aeiouAEIOU"
    for i in string:
        if i in alph:
            count += 1

    return count

print(finder_alph('Hello World'))
print(finder_alph('Python Programming'))

def dayOfMounth(day: int, mounth: str):
    return f"{day} of {mounth}"

print(dayOfMounth(1, 'September'))
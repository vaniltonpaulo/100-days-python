import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


Test.assert_equals(fizz_buzz(3), "Fizz", "You gave " + fizz_buzz(3) + " and Fizz was needed")
Test.assert_equals(fizz_buzz(5), "Buzz", "You gave " + fizz_buzz(5) + " and Buzz was needed")
Test.assert_equals(fizz_buzz(15), "FizzBuzz", "You gave " + fizz_buzz(15) + " and FizzBuzz was needed")
Test.assert_equals(fizz_buzz(10), "Buzz", "You gave " + fizz_buzz(10) + " and Buzz was needed")
Test.assert_equals(fizz_buzz(98), "98", "You gave " + fizz_buzz(98) + " and 98 was needed")
Test.summary()


def face_interval(num):
    if len(num) > 0 and all(isinstance(i, int) for i in num):
        x = max(num) - min(num)
        if x in num:
            return ":)"
        else:
            return ":("
    else:
        return ":/"



Test.assert_equals(face_interval([1, 2, 5, 8, 3, 9]), ":)")
Test.assert_equals(face_interval([5, 2, 6, 3, 11]), ":(")
Test.assert_equals(face_interval([20, 50, 13, 60, 79, 72, 99]), ":(")
Test.assert_equals(face_interval([11, 42, 83, 28, 47, 94]), ":)")
Test.assert_equals(face_interval("bruh"), ":/")


def is_alpha(word):
    return  sum(ord(c.lower()) - 96 for c in word if c.isalpha()) % 2 == 0

Test.assert_equals(is_alpha("i'am king"), True)
Test.assert_equals(is_alpha("True"), True)
Test.assert_equals(is_alpha("alexa"), False)
Test.summary()  


def sum_missing_numbers(lst):
    s = list()
    for i in range(min(lst), max(lst) + 1):
        if i not in lst:
            s.append(i)
    return sum(s)

Test.assert_equals(sum_missing_numbers([1, 3, 5, 7, 10]), 29)
Test.assert_equals(sum_missing_numbers([10, 20, 30, 40, 50, 60]), 1575)
Test.assert_equals(sum_missing_numbers([7, 3, 8, 5, 12]), 40)
Test.assert_equals(sum_missing_numbers([99, 2, 45, 4, 17]), 4782)
Test.assert_equals(sum_missing_numbers([10, 7, 5, 3, 1]), 29)
Test.assert_equals(sum_missing_numbers([7, 8, 9, 10]), 0)
Test.summary()


def fruit_salad(fruits):
    chunks  = []
    for fruit in fruits:
        mid = len(fruit) // 2
        chunks.append(fruit[:mid])
        chunks.append(fruit[mid:])
    return ''.join(sorted(chunks))

Test.assert_equals(fruit_salad(['apple', 'pear', 'grapes']), 'apargrapepesple')
Test.assert_equals(fruit_salad(['banana', 'kiwi', 'strawberry', 'blueberries']), 'anabanberryblueberrieskistrawwi')
Test.assert_equals(fruit_salad(['raspberries', 'mango']), 'erriesmangoraspb')
Test.assert_equals(fruit_salad(['banana']), 'anaban')
Test.summary()


def cons(lst):
    for i in range(min(lst), max(lst) + 1):
        if i not in lst:
            return False
        elif len(lst) != len(set(lst)):
            return False
    return True

Test.assert_equals(cons([5, 1, 4, 3, 2]), True)
Test.assert_equals(cons([55, 59, 58, 56, 57]), True)
Test.assert_equals(cons([-3, -2, -1, 1, 0]), True)
Test.assert_equals(cons([5, 1, 4, 3, 2, 8]), False)
Test.assert_equals(cons([5, 6, 7, 8, 9, 9]), False)
Test.assert_equals(cons([5, 3]), False)
Test.summary()


def largest_gap(lst):
    x = sorted(set(lst))
    return max(x[i +1] - x[i]for i in range(len(x) - 1))       



Test.assert_equals(largest_gap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]), 11)
Test.assert_equals(largest_gap([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]), 4)
Test.assert_equals(largest_gap([1, 2, 2, 3, 4, 5, 5, 6, 8, 8, 9, 10, 11, 13, 13, 14]), 2)
Test.assert_equals(largest_gap([21, 28, 0, 5, 11, 6, 17, 25, 2, 19]), 6)
Test.assert_equals(largest_gap([8, 11, 24, 2, 7, 4, 4, 25, 24, 14, 8, 0, 7]), 10)
Test.assert_equals(largest_gap([26, 17, 4, 25, 29, 26, 8, 30, 4, 20, 2, 7, 29, 7, 20, 30, 23, 5]), 9)
Test.summary()





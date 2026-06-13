import sys
from unittest import result
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test

def bound_sort(lst, bounds):
    start, end  = bounds
    result = lst[:start] + sorted(lst[start:end + 1]) + lst[end+1:]
    return result == sorted(lst)



Test.assert_equals(bound_sort([1, 6, 5, 3, 8, 9], [0, 3]), True)
Test.assert_equals(bound_sort([1, 6, 5, 3, 8, 9], [0, 2]), False)
Test.assert_equals(bound_sort([1, 9, 2, 5, 7], [0, 4]), True)
Test.assert_equals(bound_sort([1, 9, 2, 5, 7], [0, 3]), False)
Test.assert_equals(bound_sort([1, 2, 3, 4, 5, 8, 9], [0, 1]), True)
Test.assert_equals(bound_sort([1, 2, 3, 5, 4, 8, 9], [0, 4]), True)
Test.assert_equals(bound_sort([1, 2, 3, 5, 4, 8, 9], [0, 3]), False)


Test.summary()


def canConcatenate(lst, target):
    result = []
    for i in lst:
        result += i
    return sorted(result) == sorted(target)






Test.assert_equals(canConcatenate([[1, 2, 3, 4], [5, 6], [7]], [1, 2, 3, 4, 5, 6, 7]), True)
Test.assert_equals(canConcatenate([[2, 1, 3], [5, 4, 7, 6]], [1, 2, 3, 4, 5, 6, 7]), True)
Test.assert_equals(canConcatenate([[2, 1, 3], [5, 4, 7, 6]], [7, 6, 5, 4, 3, 2, 1]), True)
Test.assert_equals(canConcatenate([[2, 1, 3], [5, 4, 7, 6, 7]], [1, 2, 3, 4, 5, 6, 7]), False)
Test.assert_equals(canConcatenate([[2, 1, 3], [5, 4, 7]], [1, 2, 3, 4, 5, 6, 7]), False)
Test.assert_equals(canConcatenate([[1, 4], [3]], [1, 3, 4]), True)
Test.assert_equals(canConcatenate([[1, 4], [3]], [1, 2, 3, 4]), False)
Test.assert_equals(canConcatenate([[1, 4], [3]], [4, 3, 1]), True)
Test.assert_equals(canConcatenate([[1, 4], [2, 3]], [4, 3, 1, 2]), True)
Test.assert_equals(canConcatenate([[1], [2], [3, 4]], [4, 3, 1, 2]), True)
Test.assert_equals(canConcatenate([[1], [2], [3], [4]], [4, 3, 1, 2]), True)
Test.summary()


def str_to_dict(lst):
    result = {}
    for item in lst:
       key,value = item.split('=')
       result[key] = value
    return result



Test.assert_equals(str_to_dict(["name=bob","balance=500","salary=10000","friends=0"]), {"name": "bob", "balance": "500", "salary": "10000", "friends": "0"})
Test.assert_equals(str_to_dict(["bob=human", "lola=dog", "mittens=cat", "todd=frog"]),{"bob": "human", "lola": "dog", "mittens": "cat", "todd": "frog"} )
Test.assert_equals(str_to_dict(["greeting=Hello There!", "dismissal=Goodbye!","thanks=Thank you!"]), {"greeting": "Hello There!", "dismissal": "Goodbye!", "thanks": "Thank you!"} )
Test.assert_equals(str_to_dict(["dog=bark", "cat=meow", "cow=moo"]),{"dog": "bark", "cat": "meow", "cow": "moo"} )
Test.assert_equals(str_to_dict(["1=one","2=two","3=three","4=four"]), {"1": "one", "2": "two", "3": "three", "4": "four"})
Test.summary()


def gen_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [f'{rank} of {suit}' for suit in suits for rank in ranks]

ordered1 = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
ordered2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#if [r for r, s in gen_deck()] not in (ordered1, ordered2, ordered1[::-1], ordered2[::-1]):
#	print('**EXTRA POINTS!**')

Test.assert_equals(sorted(gen_deck()), [(2, 'c'), (2, 'd'), (2, 'h'), (2, 's'), (3, 'c'), (3, 'd'), (3, 'h'), (3, 's'), (4, 'c'), (4, 'd'), (4, 'h'), (4, 's'), (5, 'c'), (5, 'd'), (5, 'h'), (5, 's'), (6, 'c'), (6, 'd'), (6, 'h'), (6, 's'), (7, 'c'), (7, 'd'), (7, 'h'), (7, 's'), (8, 'c'), (8, 'd'), (8, 'h'), (8, 's'), (9, 'c'), (9, 'd'), (9, 'h'), (9, 's'), (10, 'c'), (10, 'd'), (10, 'h'), (10, 's'), (11, 'c'), (11, 'd'), (11, 'h'), (11, 's'), (12, 'c'), (12, 'd'), (12, 'h'), (12, 's'), (13, 'c'), (13, 'd'), (13, 'h'), (13, 's'), (14, 'c'), (14, 'd'), (14, 'h'), (14, 's')])
Test.summary()

def same_upsidedown(num):
    flipped = {
        "0": "0",
        "6": "9",
        "9": "6"
    }

    upside_down = ""

    for digit in num[::-1]:
        upside_down += flipped[digit]

    return upside_down == num


Test.assert_equals(same_upsidedown("9"), False)
Test.assert_equals(same_upsidedown("0"), True)
Test.assert_equals(same_upsidedown("6090609"), True)
Test.assert_equals(same_upsidedown("9669"), False)
Test.assert_equals(same_upsidedown("69069069"), True)
Test.assert_equals(same_upsidedown("60906096090609"), True)
Test.assert_equals(same_upsidedown("966909669"), False)
Test.assert_equals(same_upsidedown("6000000009"), True)
Test.assert_equals(same_upsidedown("6666660999999"), True)
Test.assert_equals(same_upsidedown("96666660999999"), False)
Test.summary()

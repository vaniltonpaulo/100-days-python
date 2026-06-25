import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test

import math
def square_digits(n):
    return int("".join(str(int(digit) ** 2) for digit in str(n)))

Test.assert_equals(square_digits(9119), 811181)
Test.assert_equals(square_digits(8726), 6449436)
Test.assert_equals(square_digits(9763), 8149369)
Test.assert_equals(square_digits(2230), 4490)
Test.assert_equals(square_digits(2797), 4498149)
Test.assert_equals(square_digits(233), 499)
Test.assert_equals(square_digits(7437), 4916949)
Test.assert_equals(square_digits(2483), 416649)
Test.assert_equals(square_digits(5742), 2549164)
Test.assert_equals(square_digits(5636), 2536936)
Test.assert_equals(square_digits(841), 64161)



def paths(n):
    return math.factorial(n)


Test.assert_equals(paths(1), 1)
Test.assert_equals(paths(2), 2)
Test.assert_equals(paths(3), 6)
Test.assert_equals(paths(4), 24)
Test.assert_equals(paths(5), 120)
Test.assert_equals(paths(6), 720)
Test.assert_equals(paths(7), 5040)
Test.assert_equals(paths(8), 40320)
Test.summary()

def eda_bit(start, end):
    x = []
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 ==0:
            x.append("EdaBit")
        elif i % 3 == 0:
            x.append('Eda')
        elif i % 5 == 0:
            x.append('Bit')
        else:
            x.append(i)
    return x




Test.assert_equals(eda_bit(1, 20), [1,2,'Eda',4,'Bit','Eda',7,8,'Eda','Bit',11,'Eda',13,14,'EdaBit',16,17,'Eda',19,'Bit'])
Test.assert_equals(eda_bit(-250, -230), ['Bit', 'Eda', -248, -247, 'Eda', 'Bit', -244, 'Eda', -242, -241, 'EdaBit', -239, -238, 'Eda', -236, 'Bit', 'Eda', -233, -232, 'Eda', 'Bit'])
Test.assert_equals(eda_bit(-10, 5), ['Bit', 'Eda', -8, -7, 'Eda', 'Bit', -4, 'Eda', -2, -1, 'EdaBit', 1, 2, 'Eda', 4, 'Bit'])
Test.assert_equals(eda_bit(33, 45), ['Eda', 34, 'Bit', 'Eda', 37, 38, 'Eda', 'Bit', 41, 'Eda', 43, 44, 'EdaBit'])
Test.assert_equals(eda_bit(50, 90), ['Bit', 'Eda', 52, 53, 'Eda', 'Bit', 56, 'Eda', 58, 59, 'EdaBit', 61, 62, 'Eda', 64, 'Bit', 'Eda', 67, 68, 'Eda', 'Bit', 71, 'Eda', 73, 74, 'EdaBit', 76, 77, 'Eda', 79, 'Bit', 'Eda', 82, 83, 'Eda', 'Bit', 86, 'Eda', 88, 89, 'EdaBit'])
Test.summary()

import statistics
def mean(num):
    x = list(str(num))
    x = list(map(lambda i: int(i),x))
    return statistics.mean(x)


Test.assert_equals(mean(666), 6)
Test.assert_equals(mean(80), 4)
Test.assert_equals(mean(789), 8)
Test.assert_equals(mean(417), 4)
Test.assert_equals(mean(1357), 4)
Test.assert_equals(mean(42), 3)
Test.assert_equals(mean(12345), 3)

def cars_needed(n):
    return math.ceil(n/5)


Test.assert_equals(cars_needed(0), 0)
Test.assert_equals(cars_needed(1), 1)
Test.assert_equals(cars_needed(2), 1)
Test.assert_equals(cars_needed(3), 1)
Test.assert_equals(cars_needed(4), 1)
Test.assert_equals(cars_needed(5), 1)
Test.assert_equals(cars_needed(6), 2)
Test.assert_equals(cars_needed(7), 2)
Test.assert_equals(cars_needed(8), 2)
Test.assert_equals(cars_needed(9), 2)
Test.assert_equals(cars_needed(10), 2)
Test.assert_equals(cars_needed(11), 3)
Test.assert_equals(cars_needed(12), 3)
Test.assert_equals(cars_needed(13), 3)
Test.assert_equals(cars_needed(14), 3)
Test.assert_equals(cars_needed(15), 3)
Test.assert_equals(cars_needed(16), 4)
Test.assert_equals(cars_needed(17), 4)
Test.assert_equals(cars_needed(18), 4)
Test.assert_equals(cars_needed(19), 4)
Test.assert_equals(cars_needed(20), 4)
Test.assert_equals(cars_needed(21), 5)
Test.assert_equals(cars_needed(22), 5)
Test.assert_equals(cars_needed(23), 5)
Test.assert_equals(cars_needed(24), 5)
Test.assert_equals(cars_needed(25), 5)
Test.assert_equals(cars_needed(26), 6)
Test.assert_equals(cars_needed(27), 6)
Test.assert_equals(cars_needed(28), 6)
Test.assert_equals(cars_needed(29), 6)
Test.assert_equals(cars_needed(30), 6)
Test.summary()


def unique(lst):
    for i in lst:
        if lst.count(i) == 1:
            return i 


Test.assert_equals(unique([3, 3, 3, 7, 3, 3]), 7)
Test.assert_equals(unique([0, 0, 0.77, 0, 0]), 0.77)
Test.assert_equals(unique([0, 1, 1, 1, 1, 1, 1, 1]), 0)
Test.assert_equals(unique([-4, -4, -4, 4]), 4)
Test.assert_equals(unique([8, 8, 8, 8, 8, 8, 8, 0.5]), 0.5)
Test.assert_equals(unique([2, 1, 2, 2, 2, 2, 2, 2]), 1)


def equal(a, b, c):
    if a == b  == c:
        return 3
    if a == b or c== a or c == b:
        return 2
    else :
        return 0


Test.assert_equals(equal(2,3,4), 0, "All values are differents")
Test.assert_equals(equal(7,3,7), 2, "Two values are equal")
Test.assert_equals(equal(4,4,4), 3, "All 3 values are equal")
Test.assert_equals(equal(7,3,4), 0, "All values are differents")
Test.assert_equals(equal(3,3,6), 2, "Two values are equal")
Test.assert_equals(equal(1,1,1), 3, "All 3 values are equal")
Test.assert_equals(equal(1,7,6), 0, "All values are differents")
Test.assert_equals(equal(7, 7, 7), 3, "All 3 values are equal")
Test.assert_equals(equal(6, 3, 3), 2, "Two values are equal")


import math

def century_from_year(year):
    return (year -1) // 100 +1

Test.assert_equals(century_from_year(2020), 21)
Test.assert_equals(century_from_year(200), 2)
Test.assert_equals(century_from_year(2005), 21)
Test.assert_equals(century_from_year(1700), 17)
Test.assert_equals(century_from_year(1705), 18)
Test.summary()


def get_discounts(nums, d):
    d = d.strip("%")
    x = int(d[:2]) / 100
    return list(map(lambda i : i * x,nums))

Test.assert_equals(get_discounts([2, 4, 6, 11], "50%"), [1, 2, 3, 5.5])
Test.assert_equals(get_discounts([10, 20, 40, 80], "75%"), [7.5, 15, 30, 60])
Test.assert_equals(get_discounts([100], "45%"), [45])
Test.assert_equals(get_discounts([20], "1%"), [0.2])
Test.assert_equals(get_discounts([100, 1000, 10000], "5%"), [5, 50, 500])
Test.summary()


def scale_tip(lst):
    x = lst.index("I")
    if sum(lst[:x]) > sum(lst[x+1:]):
        return "left"
    elif sum(lst[:x]) < sum(lst[x+1:]):
        return "right"
    else:
        return "balanced"



Test.assert_equals(scale_tip([0, 0, 0, "I", 1, 1, 1]), "right", "0 < 3 so it will tip right")
Test.assert_equals(scale_tip([1, 2, 3, "I", 4, 0, 0]), "left", "6 > 4 so it will tip left")
Test.assert_equals(scale_tip([5, 5, 5, "I", 10, 2, 3]), "balanced", "15 = 15 so it will stay balanced")
Test.assert_equals(scale_tip([2, 3, 1, "I", 6, 0, 0]), "balanced")
Test.assert_equals(scale_tip([500, 0, 0, "I", 32, 53, 12]), "left")
Test.assert_equals(scale_tip([500, 0, 0, "I", 302, 53, 12]), "left")
Test.assert_equals(scale_tip([50, 0, 0, "I", 32, 53, 12]), "right")
Test.assert_equals(scale_tip([5, "I", 3]), "left")
Test.assert_equals(scale_tip([500, 0, 0, "I", 500, 0, 0]), "balanced")
Test.assert_equals(scale_tip([500, 0, 0, 0, 0, 0, "I", 32, 53, 12, 0, 0, 0]), "left")
Test.assert_equals(scale_tip([1, 300, "I", 300, 1]), "balanced")
Test.assert_equals(scale_tip([1, 300, "I", 300, 2]), "right")


def even_or_odd(s):
    x = list(s)
    x = list(map(lambda i : int(i),x))
    evs = []
    odds = []
    for i in x :
        if i % 2 ==0:
            evs.append(i)
        else:
            odds.append(i)
    if sum(evs) > sum(odds):
        return "Even is greater than Odd"
    elif sum(evs) < sum(odds):
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"



Test.assert_equals(even_or_odd('12345'), 'Odd is greater than Even')
Test.assert_equals(even_or_odd('143'), 'Even and Odd are the same')
Test.assert_equals(even_or_odd('2221'), 'Even is greater than Odd')
Test.assert_equals(even_or_odd('23456'), 'Even is greater than Odd')
Test.assert_equals(even_or_odd('4321'), 'Even is greater than Odd')
Test.assert_equals(even_or_odd('3245'), 'Odd is greater than Even')
Test.assert_equals(even_or_odd('14256'), 'Even is greater than Odd')
Test.assert_equals(even_or_odd('11234'), 'Even is greater than Odd')
Test.assert_equals(even_or_odd('1734'), 'Odd is greater than Even')
Test.assert_equals(even_or_odd('145'), 'Odd is greater than Even')
Test.assert_equals(even_or_odd('22471'), 'Even and Odd are the same')
Test.assert_equals(even_or_odd('213613'), 'Even and Odd are the same')
Test.assert_equals(even_or_odd('23456'), 'Even is greater than Odd')
Test.assert_equals(even_or_odd('9738'), 'Odd is greater than Even')
Test.assert_equals(even_or_odd('34522'), 'Even and Odd are the same')
Test.assert_equals(even_or_odd('12378'), 'Odd is greater than Even')
Test.assert_equals(even_or_odd('45228'), 'Even is greater than Odd')
Test.assert_equals(even_or_odd('4455'), 'Odd is greater than Even')
Test.assert_equals(even_or_odd('6721'), 'Even and Odd are the same')
Test.assert_equals(even_or_odd('92184'), 'Even is greater than Odd') 
Test.assert_equals(even_or_odd('12'), 'Even is greater than Odd')
Test.assert_equals(even_or_odd('123'), 'Odd is greater than Even')
Test.assert_equals(even_or_odd('112'), 'Even and Odd are the same')
Test.assert_equals(even_or_odd('124'), 'Even is greater than Odd')
Test.summary()

import string
def alph_num(txt):
    return " ".join(str(string.ascii_uppercase.index(i))for i in txt)

Test.assert_equals(alph_num("ABCD"), "0 1 2 3")
Test.assert_equals(alph_num("BCDA"), "1 2 3 0")
Test.assert_equals(alph_num("AAA"), "0 0 0")
Test.assert_equals(alph_num("XYZ"), "23 24 25")
# Algebra (very easy)

def addition(a, b):
    return a + b


def calc_age(age):
    return age * 365

print(calc_age(65)) #➞ 23725

print(calc_age(0)) #➞ 0

print(calc_age(20)) #➞ 7300


def addition(num):
    return num + 1


print(addition(0)) #➞ 1

print(addition(9)) #➞ 10

print(addition(-3)) #➞ -2


def squared(a):
	return a ** 2

print(squared(5)) #➞ 25

print(squared(9)) #➞ 81

print(squared(100)) #➞ 10000

def football_points(wins, draws, losses):
    return wins * 3 + draws * 1 + losses * 0

print(football_points(3, 4, 2)) #➞ 13

print(football_points(5, 0, 2)) #➞ 15

print(football_points(0, 0, 1)) #➞ 0 

def divisible(num):
     return num % 100 == 0

print(divisible(1)) #➞ False

print(divisible(1000)) #➞ True

print(divisible(100)) #➞ True


def calculator(txt):
     return int(eval(txt))


print(calculator("23+4")) #➞ 27

print(calculator("45-15")) #➞ 30

print(calculator("13+2-5*2")) #➞ 5

print(calculator("49/7*2-3")) #➞ 11


def area(h, w):
    if h <= 0 or w <= 0:
        return -1
    return h * w


print(area(3, 4)) #➞ 12

print(area(10, 11)) #➞ 110

print(area(-1, 5)) #➞ -1

print(area(0, 2)) #➞ 0


def pos_com(num):
     return 2 ** num

print(pos_com(1)) #➞ 2

print(pos_com(3)) #➞ 8

print(pos_com(10)) #    ➞ 1024


def star_number(n):
        return 6*n*(n - 1) + 1


print(star_number(2)) #➞ 13
# n = 2
# 2nd star number = 13

print(star_number(3)) #  ➞ 37
# n = 3
# 3rd star number = 37

print(star_number(5)) # ➞ 121
# n = 5
# 5th star number = 121


def how_many_stickers(n):
     return 6 * (n**2)

print(how_many_stickers(1)) # ➞ 6

print(how_many_stickers(2)) # ➞ 24

print(how_many_stickers(3)) # ➞ 54


def stack_boxes(n):
     return n ** 2

print(stack_boxes(1)) # ➞ 1

print(stack_boxes(2)) # ➞ 4

print(stack_boxes(0)) # ➞ 0

def calculate(num1, num2, op):
    result =eval(f"{num1} {op} {num2}")
    if result < 0:
        return -1 * result 
    return result

print(calculate(4, 9, "+")) # ➞ 13

print(calculate(12, 5, "-")) # ➞ 7

print(calculate(6, 3, "*")) #          ➞ 18

print(calculate(25, 5, "//")) # ➞ 5

print(calculate(14, 3, "%")) # ➞ 2

print(calculate(7, 2, "/")) # ➞ 3.5
print(calculate(-20, -30, "+")) # ➞ -50


def fifty_thirty_twenty(ati):
     needs = ati * 0.5
     wants = ati * 0.3
     savings = ati * 0.2
     return {"Needs": needs, "Wants": wants, "Savings": savings}

print(fifty_thirty_twenty(10000)) # ➞ { "Needs": 5000, "Wants": 3000, "Savings": 2000 }

print(fifty_thirty_twenty(50000)) # ➞ { "Needs": 25000, "Wants": 15000, "Savings": 10000 }

print(fifty_thirty_twenty(13450)) # ➞ { "Needs": 6725, "Wants": 4035, "Savings": 2690 }


import math

def next_square(n):
    root = math.sqrt(n)
    if root.is_integer():
      result = math.floor(root) + 1
      return result ** 2
    else:
        return None

print(next_square(121)) # ➞ 144

print(next_square(625)) # ➞ 676

print(next_square(114)) #     ➞ None
# 114 is not a perfect square



def perfect_roots(n):
     x = n ** 0.5 
     y = n ** 0.25
     z = n ** 0.125
     return True if x.is_integer() and y.is_integer() and z.is_integer() else False
      
     
     


print(perfect_roots(256)) # ➞ True
# 2nd root of 256 is 16
# 4th root of 256 is 4
# 8th root of 256 is 2

print(perfect_roots(1000)) # ➞ False

print(perfect_roots(6561)) # ➞ True



#Array

def get_first_value(number_list):
     return number_list[0]


print(get_first_value([1, 2, 3])) # ➞ 1

print(get_first_value([80, 5, 100])) # ➞ 80

print(get_first_value([-500, 0, 50])) # ➞ -500

print(get_first_value([-52320, 0, 50])) # ➞ -52320

def total_amount_adjectives(dct):
    return len(dct)

print(total_amount_adjectives({ "a": "moron" })) # ➞ 1

print(total_amount_adjectives({ "a": "idiot", "b": "idiot", "c": "idiot" })) # ➞ 3

print(total_amount_adjectives({ "a": "moron", "b": "scumbag", "c": "moron", "d": "dirtbag" })) # ➞ 4

obj3 = {'b': "scumbag", 'c': "moron", 'd': "dirtbag" } 


print(total_amount_adjectives(obj3))


def findLargestNum(nums):
    return max(nums)

print(findLargestNum([4, 5, 1, 3])) # ➞ 5

print(findLargestNum([300, 200, 600, 150])) # ➞ 600

print(findLargestNum([1000, 1001, 857, 1])) # ➞ 1001
print(findLargestNum([1000, 1001, 857, 1, 1002])) # ➞ 1002
print(findLargestNum([27364, 837363, 736736, 73635]))

def find_smallest_num(nums):
    return min(nums)

print(find_smallest_num([34, 15, 88, 2])) # ➞ 2

print(find_smallest_num([34, -345, -1, 100])) # ➞ -345

print(find_smallest_num([-76, 1.345, 1, 0])) # ➞ -76

print(find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999])) # ➞ -0.9999

print(find_smallest_num([7, 7, 7])) # ➞ 7



def difference_max_min(lst):
     return max(lst) - min(lst)

print(difference_max_min([10, 4, 1, 4, -10, -50, 32, 21])) # ➞ 82
# Smallest number is -50, biggest is 32.

print(difference_max_min([44, 32, 86, 19])) # ➞ 67
# Smallest number is 19, biggest is 86.

print(difference_max_min([-70,43,34,54,22])) # ➞ 113

def concat(lst1, lst2):
        return lst1 + lst2


print(concat([1, 3, 5], [2, 6, 8])) # ➞ [1, 3, 5, 2, 6, 8]

print(concat([7, 8], [10, 9, 1, 1, 2])) # ➞ [7, 8, 10, 9, 1, 1, 2]

print(concat([4, 5, 1], [3, 3, 3, 3, 3])) # ➞ [4, 5, 1, 3, 3, 3, 3, 3]




def get_last_item(lst):
     return lst[-1]

print(get_last_item([1, 2, 3])) # ➞ 3

print(get_last_item(["cat", "dog", "duck"])) # ➞ "duck"

print(get_last_item([True, False, True])) # ➞ True

print(get_last_item([7, "String", False])) # ➞ False

print(get_last_item([False])) # ➞ False

print(get_last_item([True, False, 'Apple'])) # ➞ 'Apple'
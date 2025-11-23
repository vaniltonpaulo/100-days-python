# VERY EASY

import math


def addition(a, b):
    return a + b

print(addition(1, 3))

def addition(num):
    return num + 1

print(addition(73))

def squared(a):
    return a * a

print(squared(21))

def football_points(wins, draws, losses):
    wins = wins * 3
    draws = draws * 1
    losses = losses * 0
    return wins + draws + losses

print(football_points(3, 4, 2))
print(football_points(0, 0, 15))
print(football_points(0, 7, 0))


def divisible(num):
 if num % 100 == 0:
     return True
 return False

print(divisible(1))
print(divisible(111000))
print(divisible(-1))

def calculator(txt):
    return int(eval(txt))

print(calculator("23+4"))
print(calculator("49/7*2-3"))
print(calculator("4+2+3-5*2-8/4-12-0+3-14"))


def area(h, w):
    if h <0 or w< 0:
        return -1
    return h * w

print(area(10, 11))
print(area(10000, 10000))
print(area(-1, 5))

def pos_com(num):
    return 2 ** num

print(pos_com(10))
print(pos_com(25))
print(pos_com(6))

def star_number(n):
     return 6*n * (n - 1) + 1

print(star_number(5))
print(star_number(11))

#lean arithmetic , geometric and quadratic sequence
def how_many_stickers(n):
    return 6*(n **2)

for i in range(1, 16):
    print(i,how_many_stickers(i))

def stack_boxes(n):
    if n == 0: return 0
    if n == 1: return 1
    return n ** 2

print(stack_boxes(196))
print(stack_boxes(0))


def calculate(num1, num2, op):
    result = f"{num1} {op} {num2}"
    return eval(result)

print(calculate(6, 3, "*"))
print(calculate(7,2, "/"))
print(calculate(38,3, "*"))

def fifty_thirty_twenty(ati):
    return { "Needs": ati * 0.5, "Wants": ati * 0.3, "Savings": ati * 0.2 }


print(fifty_thirty_twenty(13450))
print(fifty_thirty_twenty(347100))

def next_square(n):
    if math.sqrt(n).is_integer():
        while True:
            n += 1
            result = math.sqrt(n)
            if result.is_integer():
                return n
                break
    else:
        return "none"

print(next_square(121))
print(next_square(625))
print(next_square(155))
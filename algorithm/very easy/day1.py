import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test


def next_edge(side1, side2):
    return (side1 + side2) - 1



Test.assert_equals(next_edge(5, 4), 8)
Test.assert_equals(next_edge(8, 3), 10)
Test.assert_equals(next_edge(7, 9), 15)
Test.assert_equals(next_edge(10, 4), 13)
Test.assert_equals(next_edge(7, 2), 8)
Test.summary()

def animals(chickens, cows, pigs):
    animals = (chickens * 2) + (cows * 4) + (pigs * 4)
    return animals



Test.assert_equals(animals(5, 2, 8), 50)
Test.assert_equals(animals(3, 4, 7), 50)
Test.assert_equals(animals(1, 2, 3), 22)
Test.assert_equals(animals(3, 5, 2), 34)
Test.summary()


def makes10(a, b):
    if a == 10 or b ==10 or a+b == 10:
        return True
    else:        
        return False


Test.assert_equals(makes10(9, 10), True)	
Test.assert_equals(makes10(9, 9), False)	
Test.assert_equals(makes10(1, 9), True)	
Test.assert_equals(makes10(10, 1), True)	
Test.assert_equals(makes10(10, 10), True)	
Test.assert_equals(makes10(8, 2), True)	
Test.assert_equals(makes10(8, 3), False)	
Test.assert_equals(makes10(10, 42), True)	
Test.assert_equals(makes10(12, -2), True)
Test.summary()


def frames(minutes, fps):
    return minutes * fps * 60



Test.assert_equals(frames(1, 1), 60)
Test.assert_equals(frames(10, 1), 600)
Test.assert_equals(frames(10, 25), 15000)
Test.assert_equals(frames(500, 60), 1800000)
Test.assert_equals(frames(0, 60), 0)
Test.assert_equals(frames(99, 1), 5940)
Test.assert_equals(frames(419, 70), 1759800)
Test.assert_equals(frames(52, 33), 102960)
Test.summary()


def ctoa(char):
    return ord(char)



Test.assert_equals(ctoa(' '), 32)
Test.assert_equals(ctoa('A'), 65)
Test.assert_equals(ctoa(']'), 93)
Test.assert_equals(ctoa('^'), 94)
Test.assert_equals(ctoa('c'), 99)


def area_shape(base, height, shape):
    if shape == "triangle":
        return (base * height) / 2
    elif shape == "parallelogram":
        return base * height
    else:
        return None



Test.assert_equals(area_shape(2, 3, "triangle"), 3)
Test.assert_equals(area_shape(8, 6, "parallelogram"), 48)
Test.assert_equals(area_shape(0, 1, "triangle"), 0)
Test.assert_equals(area_shape(2.9, 1.3, "parallelogram"), 3.77)
Test.assert_equals(area_shape(0.01, 5, "triangle"), 0.025)



def accept_into_movie(age, is_supervised):
    if age >= 15 or is_supervised:
        return True
    else:
        return False



Test.assert_equals(accept_into_movie(14, True), True)
Test.assert_equals(accept_into_movie(15, True), True)
Test.assert_equals(accept_into_movie(16, True), True)
Test.assert_equals(accept_into_movie(14, False), False)
Test.assert_equals(accept_into_movie(15, False), True)
Test.assert_equals(accept_into_movie(16, False), True)
Test.assert_equals(accept_into_movie(14.99999, True), True)
Test.assert_equals(accept_into_movie(14.99999, False), False)
Test.summary()


def add_up(num):
    total = 0
    for i in range(num+ 1):
        total += i
    return total 


Test.assert_equals(add_up(4), 10)
Test.assert_equals(add_up(13), 91)
Test.assert_equals(add_up(600), 180300)
Test.assert_equals(add_up(392), 77028)
Test.assert_equals(add_up(53), 1431)
Test.assert_equals(add_up(897), 402753)
Test.assert_equals(add_up(23), 276)
Test.assert_equals(add_up(1000), 500500)
Test.assert_equals(add_up(738), 272691)
Test.assert_equals(add_up(100), 5050)
Test.assert_equals(add_up(925), 428275)
Test.assert_equals(add_up(1), 1)
Test.assert_equals(add_up(999), 499500)
Test.assert_equals(add_up(175), 15400)
Test.assert_equals(add_up(111), 6216)
Test.summary()




def programmers(one, two, three):
    return max(one, two, three) - min(one,two, three)


Test.assert_equals(programmers(1, 5, 9), 8)
Test.assert_equals(programmers(43, 33, 43), 10)
Test.assert_equals(programmers(88, 14, 23), 74)
Test.assert_equals(programmers(33, 72, 74), 41)
Test.assert_equals(programmers(147, 33, 526), 493)
Test.assert_equals(programmers(234, 345, 457), 223)


def add_binary(a, b):
    return bin(a + b)[2:]



Test.assert_equals(add_binary(1,1), '10')
Test.assert_equals(add_binary(1,2), '11')
Test.assert_equals(add_binary(4,5),'1001')
Test.assert_equals(add_binary(8,20),'11100')
Test.assert_equals(add_binary(100,20),'1111000')
Test.assert_equals(add_binary(40,50),'1011010')
Test.assert_equals(add_binary(65,77),'10001110')
Test.assert_equals(add_binary(40,50),'1011010')
Test.assert_equals(add_binary(1,0),'1')

def leap_year(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)


Test.assert_equals(leap_year(2004), True)
Test.assert_equals(leap_year(8), True)
Test.assert_equals(leap_year(4), True)
Test.assert_equals(leap_year(2019), False)
Test.assert_equals(leap_year(1970), False)
Test.assert_equals(leap_year(2021), False)
Test.assert_equals(leap_year(1934), False)
Test.assert_equals(leap_year(1874), False)
Test.assert_equals(leap_year(1968), True)
Test.assert_equals(leap_year(2024), True)
Test.assert_equals(leap_year(1900), False)
Test.assert_equals(leap_year(2100), False)
Test.assert_equals(leap_year(2200), False)
Test.summary()


def sum_cubes(n):
    total = 0
    for i in range(1, n+1):
        total += i ** 3
    return total


Test.assert_equals(sum_cubes(1), 1)
Test.assert_equals(sum_cubes(2), 9)
Test.assert_equals(sum_cubes(3), 36)
Test.assert_equals(sum_cubes(4), 100)
Test.assert_equals(sum_cubes(5), 225)
Test.assert_equals(sum_cubes(6), 441)
Test.assert_equals(sum_cubes(7), 784)
Test.assert_equals(sum_cubes(8), 1296)
Test.assert_equals(sum_cubes(9), 2025)
Test.assert_equals(sum_cubes(10), 3025)
Test.assert_equals(sum_cubes(123), 58155876)
Test.assert_equals(sum_cubes(125), 62015625)
Test.assert_equals(sum_cubes(133), 79405921)
Test.assert_equals(sum_cubes(167), 196784784)
Test.assert_equals(sum_cubes(188), 315630756)
Test.assert_equals(sum_cubes(199), 396010000)
Test.assert_equals(sum_cubes(200), 404010000)
Test.assert_equals(sum_cubes(300), 2038522500)
Test.assert_equals(sum_cubes(400), 6432040000)
Test.assert_equals(sum_cubes(500), 15687562500)
Test.assert_equals(sum_cubes(12345), 5807306426319225)



def total_cups(n):
    return n + (n//6)



Test.assert_equals(total_cups(6), 7)
Test.assert_equals(total_cups(3), 3)
Test.assert_equals(total_cups(7), 8)
Test.assert_equals(total_cups(12), 14)
Test.assert_equals(total_cups(213), 248)
Test.assert_equals(total_cups(16), 18)
Test.summary()


def largest_numbers(n, lst):
    if n  == 0:
        return []
    return sorted(lst)[-n:]


Test.assert_equals(largest_numbers(2, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [9, 10])
Test.assert_equals(largest_numbers(3, [5, 1, 5, 2, 3, 1, 2, 3, 5]), [5, 5, 5])
Test.assert_equals(largest_numbers(7, [9, 1, 50, 22, 3, 13, 2, 63, 5]), [3, 5, 9, 13, 22, 50, 63])
Test.assert_equals(largest_numbers(0, [1, 2, 3, 4, 8, 7, 6, 5]), [])
Test.assert_equals(largest_numbers(2, [4, 3, 2, 1]), [3, 4])
Test.assert_equals(largest_numbers(1, [7, 19, 4, 2]), [19])
Test.assert_equals(largest_numbers(3, [14, 12, 57, 11, 18, 16]), [16, 18, 57])

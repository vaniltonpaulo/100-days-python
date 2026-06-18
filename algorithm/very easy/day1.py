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
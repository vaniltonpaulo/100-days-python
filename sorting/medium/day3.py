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

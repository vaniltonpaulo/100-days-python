import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test



def is_adjacent(matrix, node1, node2):
    return matrix[node1][node2] == 1



matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
Test.assert_equals(is_adjacent(matrix, 0, 1), True)
Test.assert_equals(is_adjacent(matrix, 0, 2), False)
Test.assert_equals(is_adjacent(matrix, 2, 1), True)

matrix = [[0,1,0,1,1], [1,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]]
Test.assert_equals(is_adjacent(matrix, 0, 3), True)
Test.assert_equals(is_adjacent(matrix, 1, 4), False)
Test.assert_equals(is_adjacent(matrix, 3, 2), True)


def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    lsmax = find_highest(lst[1:])
    return lst[0] if lst[0] > lsmax else lsmax


Test.assert_equals(find_highest([8]), 8)
Test.assert_equals(find_highest([-1, 3, 5, 6, 99, 12, 2]), 99)
Test.assert_equals(find_highest([0, 12, 4, 87]), 87)

Test.summary()


def sum_odd_and_even(lst):
    odd_sum = sum(i for i in lst if i % 2 == 1)
    even_sum = sum(i for i in lst if i % 2 == 0)
    return [even_sum, odd_sum]


Test.assert_equals(sum_odd_and_even([1, 2, 3, 4, 5, 6]), [12, 9])
Test.assert_equals(sum_odd_and_even([-1, -2, -3, -4, -5, -6]), [-12, -9])
Test.assert_equals(sum_odd_and_even([0, 0]), [0, 0])
Test.assert_equals(sum_odd_and_even([]), [0, 0])


def find_it(items, name):
    if name.lower() in (key.lower() for key in items):
        return f"{name.capitalize()} is gone..."
    else:
        return f"{name.capitalize()} is here!"


Test.assert_equals(find_it({}, "rambo"),"Rambo is here!")
Test.assert_equals(find_it({}, "heman"),"Heman is here!")

Test.assert_equals(find_it({
  "tv": 30,
  "stereo": 50,
}, "rocky"),"Rocky is here!")

Test.assert_equals(find_it({
  "tv": 30,
  "stereo": 50,
}, "spiderman"),"Spiderman is here!")

Test.assert_equals(find_it({
  "tv": 30,
  "stereo": 50,
	"julius": 100,											 
}, "julius"),"Julius is gone...")

Test.assert_equals(find_it({
  "tv": 30,
  "stereo": 50,
	"batman": 200,											 
}, "batman"),"Batman is gone...")

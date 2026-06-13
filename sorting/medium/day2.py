import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test



def merge_sort(lst1, lst2):
    if lst1 == sorted(lst1):
        return sorted(lst1 + lst2)
    else:
        lst1 = sorted(lst1, reverse = True)
        return sorted(lst1 + lst2, reverse = True)


Test.assert_equals(merge_sort([1, 2, 3], [5, 4, 6]), [1, 2, 3, 4, 5, 6])
Test.assert_equals(merge_sort([8, 6, 4, 2], [-2, -6,  0, -4 ]), [8, 6, 4, 2, 0, -2, -4, -6])
Test.assert_equals(merge_sort([120, 180, 200], [190, 175, 130]), [120, 130, 175, 180, 190, 200])
Test.assert_equals(merge_sort([25, 21, 17, 13], []), [25, 21, 17, 13])
Test.assert_equals(merge_sort([1024, 2048], [512, 128, 64]), [64, 128, 512, 1024, 2048])
Test.assert_equals(merge_sort([0, 1], [1, 1, 1, 1, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
Test.assert_equals(merge_sort([-1, -3], [11, -5, 7, -11]), [11, 7, -1, -3, -5, -11])
Test.assert_equals(merge_sort([10, 20, 30, 40, 50, 60, 80, 90], [70]), [10, 20, 30, 40, 50, 60, 70, 80, 90])
Test.summary()


from operator import itemgetter 

def sort_drinks_by_price(drinks):
    return sorted(drinks, key = itemgetter('price'))

# Original challenge by @meesie1

drinks = [
	{"name": 'lemonade', "price": 90}, 
	{"name": 'lime', "price": 432}, 
	{"name": 'peach', "price": 23}
]

ans = [
	{"name": 'peach', "price": 23},
	{"name": 'lemonade', "price": 90}, 
	{"name": 'lime', "price": 432}
]

Test.assert_equals(sort_drinks_by_price(drinks), ans, "Object is not sorted.")
Test.assert_equals(sort_drinks_by_price([{'name': 'lemonade', 'price': 266}, {'name': 'cola', 'price': 71}, {'name': 'lime', 'price': 467}, {'name': 'peach', 'price': 203}, {'name': 'water', 'price': 216}]), [{'name': 'cola', 'price': 71}, {'name': 'peach', 'price': 203}, {'name': 'water', 'price': 216}, {'name': 'lemonade', 'price': 266}, {'name': 'lime', 'price': 467}], 'Object is not sorted.')
Test.assert_equals(sort_drinks_by_price([{'name': 'lemonade', 'price': 467}, {'name': 'cola', 'price': 486}, {'name': 'lime', 'price': 469}]), [{'name': 'lemonade', 'price': 467}, {'name': 'lime', 'price': 469}, {'name': 'cola', 'price': 486}], 'Object is not sorted.')
Test.assert_equals(sort_drinks_by_price([{'name': 'lemonade', 'price': 373}, {'name': 'cola', 'price': 459}, {'name': 'lime', 'price': 461}]), [{'name': 'lemonade', 'price': 373}, {'name': 'cola', 'price': 459}, {'name': 'lime', 'price': 461}], 'Object is not sorted.')
Test.assert_equals(sort_drinks_by_price([{'name': 'lemonade', 'price': 16}, {'name': 'cola', 'price': 284}, {'name': 'lime', 'price': 233}, {'name': 'peach', 'price': 87}]), [{'name': 'lemonade', 'price': 16}, {'name': 'peach', 'price': 87}, {'name': 'lime', 'price': 233}, {'name': 'cola', 'price': 284}], 'Object is not sorted.')
Test.assert_equals(sort_drinks_by_price([{'name': 'lemonade', 'price': 213}, {'name': 'cola', 'price': 42}, {'name': 'lime', 'price': 478}, {'name': 'peach', 'price': 450}, {'name': 'water', 'price': 256}]), [{'name': 'cola', 'price': 42}, {'name': 'lemonade', 'price': 213}, {'name': 'water', 'price': 256}, {'name': 'peach', 'price': 450}, {'name': 'lime', 'price': 478}], 'Object is not sorted.')
Test.assert_equals(sort_drinks_by_price([{'name': 'lemonade', 'price': 115}, {'name': 'cola', 'price': 164}, {'name': 'lime', 'price': 88}, {'name': 'peach', 'price': 57}, {'name': 'water', 'price': 407}]), [{'name': 'peach', 'price': 57}, {'name': 'lime', 'price': 88}, {'name': 'lemonade', 'price': 115}, {'name': 'cola', 'price': 164}, {'name': 'water', 'price': 407}], 'Object is not sorted.')
Test.assert_equals(sort_drinks_by_price([{'name': 'lemonade', 'price': 382}, {'name': 'cola', 'price': 363}]), [{'name': 'cola', 'price': 363}, {'name': 'lemonade', 'price': 382}], 'Object is not sorted.')
Test.assert_equals(sort_drinks_by_price([{'name': 'lemonade', 'price': 13}, {'name': 'cola', 'price': 184}]), [{'name': 'lemonade', 'price': 13}, {'name': 'cola', 'price': 184}], 'Object is not sorted.')
Test.assert_equals(sort_drinks_by_price([{'name': 'lemonade', 'price': 147}, {'name': 'cola', 'price': 289}, {'name': 'lime', 'price': 42}, {'name': 'peach', 'price': 486}, {'name': 'water', 'price': 87}]), [{'name': 'lime', 'price': 42}, {'name': 'water', 'price': 87}, {'name': 'lemonade', 'price': 147}, {'name': 'cola', 'price': 289}, {'name': 'peach', 'price': 486}], 'Object is not sorted.')
Test.assert_equals(sort_drinks_by_price([{'name': 'lemonade', 'price': 422}, {'name': 'cola', 'price': 43}]), [{'name': 'cola', 'price': 43}, {'name': 'lemonade', 'price': 422}], 'Object is not sorted.')
Test.summary()



def bound_sort(lst, bounds):
    sorted_lst = sorted(lst)
    return lst[bounds[0]: bounds[1] + 1] == sorted_lst



Test.assert_equals(bound_sort([1, 6, 5, 3, 8, 9], [0, 3]), True)
Test.assert_equals(bound_sort([1, 6, 5, 3, 8, 9], [0, 2]), False)
Test.assert_equals(bound_sort([1, 9, 2, 5, 7], [0, 4]), True)
Test.assert_equals(bound_sort([1, 9, 2, 5, 7], [0, 3]), False)
Test.assert_equals(bound_sort([1, 2, 3, 4, 5, 8, 9], [0, 1]), True)
Test.assert_equals(bound_sort([1, 2, 3, 5, 4, 8, 9], [0, 4]), True)
Test.assert_equals(bound_sort([1, 2, 3, 5, 4, 8, 9], [0, 3]), False)







Test.summary()

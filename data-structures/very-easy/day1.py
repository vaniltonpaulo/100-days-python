import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test


def last_ind(lst):
    return lst[-1] if lst else None


Test.assert_equals(last_ind([0, 4, 19, 34, 50, -9, 2]), 2)
Test.assert_equals(last_ind(["Hello", "There", "Python", "User"]), "User")
Test.assert_equals(last_ind([]), None)
Test.assert_equals(last_ind([True, False, False, True]), True)
Test.assert_equals(last_ind([(5, 0), (0, 5, 6, 7), (3, 5, 67, 7), (0, -9, 3, 45, 5)]), (0, -9, 3, 45, 5))
Test.assert_equals(last_ind("Python is a great programming langauge."), ".")
Test.assert_equals(last_ind(["H", "E", "L", "L", "O"]), "O")
Test.assert_equals(last_ind("The quick brown fox jumped over the lazy dog"), "g")
Test.assert_equals(last_ind([{"name": "batman"}, {"kids": "none"}, {"parents": "also none"}]), {"parents": "also none"})
Test.assert_equals(last_ind(""), None)


def print_list(n):
	result, i = [], 1
	while i<=n:
		result += [i]
		i += 1
	return result



Test.assert_equals(print_list(1), [1])
Test.assert_equals(print_list(2), [1,2])
Test.assert_equals(print_list(3), [1,2,3])
Test.assert_equals(print_list(4), [1,2,3,4])
Test.assert_equals(print_list(5), [1,2,3,4,5])
Test.assert_equals(print_list(6), [1,2,3,4,5,6])
Test.assert_equals(print_list(7), [1,2,3,4,5,6,7])
Test.assert_equals(print_list(8), [1,2,3,4,5,6,7,8])
Test.assert_equals(print_list(9), [1,2,3,4,5,6,7,8,9])
Test.assert_equals(print_list(10), [1,2,3,4,5,6,7,8,9,10])
# Mubashir




lambda_func = lambda x: x
if('<function lambda_func at' in str(lambda_func)):
	Test.assert_equals(0,1,"Your code does not use an lambda function")

Test.assert_equals(lambda_func(3),3)
Test.assert_equals(lambda_func("3"),"3")
Test.assert_equals(lambda_func(True),True)
Test.assert_equals(lambda_func("test"),"test")


Test.summary()


def nothing_is_nothing(*args):
	return all(args)


Test.assert_equals(nothing_is_nothing(0, False, [], {}), False)
Test.assert_equals(nothing_is_nothing(33, 'Hello', (True, True, 3)), True)
Test.assert_equals(nothing_is_nothing(True, None), False)
Test.assert_equals(nothing_is_nothing(None, None), False)
Test.assert_equals(nothing_is_nothing(None, True), False)
Test.assert_equals(nothing_is_nothing(221), True)
Test.assert_equals(nothing_is_nothing(221, 0, 0, 0), False)
Test.assert_equals(nothing_is_nothing([221, 0, 0, 0]), True)


def assign_person_to_job(names, jobs):
	return dict(zip(names, jobs))



pl = ["Annie", "Steven", "Lisa", "Osman"]
jl = ["Teacher", "Engineer", "Doctor", "Cashier"]
Test.assert_equals(assign_person_to_job(pl, jl), {'Annie': 'Teacher', 'Steven': 'Engineer', 'Lisa': 'Doctor', 'Osman': 'Cashier'})


def rotate_by_one(lst):
	return [lst[-1]] + lst[0:-1]


Test.assert_equals(rotate_by_one([1,2,3,4,5]), [5, 1, 2, 3, 4])
Test.assert_equals(rotate_by_one([6,5,8,9,7]), [7, 6, 5, 8, 9])
Test.assert_equals(rotate_by_one([20,15,26,8,4]), [4, 20, 15, 26, 8])
Test.assert_equals(rotate_by_one([7,8,6,4,5]), [5, 7, 8, 6, 4])
Test.assert_equals(rotate_by_one([5,9,45,1,2]), [2, 5, 9, 45, 1])
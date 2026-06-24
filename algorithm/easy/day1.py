import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test

def stutter(word):
	return word[:2] +"..." + " " + word[:2] +"..." + " " + word+"?"


actual_param, expected_param = [
	"increasing", "adventures", "enticing", "unacceptable", "accountable", "incredible", "exquisite",
	"am", "enduring", "outstanding", "astonishing", "astounding", "impressive", "revolutionize",
	"recurring", "recollection", "so", "gorgeous", "captivating"
], [
	"in... in... increasing?", "ad... ad... adventures?", "en... en... enticing?", "un... un... unacceptable?",
    "ac... ac... accountable?", "in... in... incredible?", "ex... ex... exquisite?", "am... am... am?",
    "en... en... enduring?", "ou... ou... outstanding?", "as... as... astonishing?", "as... as... astounding?",
    "im... im... impressive?", "re... re... revolutionize?", "re... re... recurring?", "re... re... recollection?",
    "so... so... so?", "go... go... gorgeous?", "ca... ca... captivating?",
]
for i, w in enumerate(actual_param):
	Test.assert_equals(stutter(w), expected_param[i])
	

import math 
def solve_for_exp(a, b):
	return round(math.log(b) / math.log(a))


Test.assert_equals(solve_for_exp(4, 1024), 5)
Test.assert_equals(solve_for_exp(2, 1024), 10)
Test.assert_equals(solve_for_exp(9, 3486784401), 10)
Test.assert_equals(solve_for_exp(4, 4294967296), 16)
Test.assert_equals(solve_for_exp(8, 134217728), 9)
Test.assert_equals(solve_for_exp(19, 47045881), 6)
Test.assert_equals(solve_for_exp(10, 100000000), 8)

def triangle(n):
    return n*(n+1)//2

Test.assert_equals(triangle(1), 1)
Test.assert_equals(triangle(2), 3)
Test.assert_equals(triangle(3), 6)
Test.assert_equals(triangle(8), 36)
Test.assert_equals(triangle(2153), 2318781)


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
Test.summary()
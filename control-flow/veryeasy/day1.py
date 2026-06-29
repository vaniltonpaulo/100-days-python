import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test

def get_container(product):
	matches = {
	"Bread" : "bag",
	"Milk" : "bottle",
	"Beer" : "bottle",
	"Eggs" : "carton",
	"Cerials" : "box",
	"Candy" : "plastic",
	"Cheese" : None
	}
	return matches[product]


Test.assert_equals(get_container("Bread"), "bag")
Test.assert_equals(get_container("Milk"), "bottle")
Test.assert_equals(get_container("Beer"), "bottle")
Test.assert_equals(get_container("Eggs"), "carton")
Test.assert_equals(get_container("Candy"), "plastic")
Test.assert_equals(get_container("Cheese"), None)


def is_truthy(val):
    return 1 if val else 0


Test.assert_equals(is_truthy(1), 1)
Test.assert_equals(is_truthy(-1), 1)
Test.assert_equals(is_truthy("false"), 1)
Test.assert_equals(is_truthy(True), 1)
Test.assert_equals(is_truthy(lambda n: n), 1)
Test.assert_equals(is_truthy(0), 0)
Test.assert_equals(is_truthy(""), 0)
Test.assert_equals(is_truthy({}), 0)
Test.assert_equals(is_truthy([]), 0)
Test.assert_equals(is_truthy(None), 0)
Test.assert_equals(is_truthy(False), 0)
Test.assert_equals(is_truthy(''), 0)
# Test.assert_equals(str(type(is_truthy('123'))), "<class 'int'>")

def say_hello_bye(name, num):
      return "Hello " + name[:1].upper() + name[1:] if num == 1 else "Bye " + name[:1].upper() + name[1:]
      


Test.assert_equals(say_hello_bye("jose", 1), "Hello Jose")
Test.assert_equals(say_hello_bye("barry", 1), "Hello Barry")
Test.assert_equals(say_hello_bye("jon", 0), "Bye Jon")
Test.assert_equals(say_hello_bye("khloy", 1), "Hello Khloy")
Test.assert_equals(say_hello_bye("sara", 0), "Bye Sara")
Test.assert_equals(say_hello_bye("Jon", 0), "Bye Jon")
Test.assert_equals(say_hello_bye("Matt", 1), "Hello Matt")



def test_jackpot(result):
      return True if len(set(result)) == 1 else False
      


Test.assert_equals(test_jackpot(['@', '@', '@', '@']), True)
Test.assert_equals(test_jackpot(['!', '!', '!', '!']), True)
Test.assert_equals(test_jackpot(['abc', 'abc', 'abc', 'abc']), True)
Test.assert_equals(test_jackpot(['karaoke', 'karaoke', 'karaoke', 'karaoke']), True)
Test.assert_equals(test_jackpot(['SS', 'SS', 'SS', 'SS']), True)
Test.assert_equals(test_jackpot([':(', ':)', ':|', ':|']), False)
Test.assert_equals(test_jackpot(['&&', '&', '&&&', '&&&&']), False)
Test.assert_equals(test_jackpot(['hee', 'heh', 'heh', 'heh']), False)
Test.assert_equals(test_jackpot(['SS', 'SS', 'SS', 'Ss']), False)


def hurdle_jump(hurdles, jump_height):
      return all(jump_height >= hurdle for hurdle in hurdles)


Test.assert_equals(hurdle_jump([1, 2, 3, 4, 5], 5), True)
Test.assert_equals(hurdle_jump([5, 5, 3, 4, 5], 3), False)
Test.assert_equals(hurdle_jump([5, 4, 5, 6], 10), True)
Test.assert_equals(hurdle_jump([1,2,1], 1), False)
Test.assert_equals(hurdle_jump([3,3,3], 4), True)
Test.assert_equals(hurdle_jump([4,4], 3), False)
Test.assert_equals(hurdle_jump([], 4), True)


def factorize(num):
      result = []
      for i in range(1,num + 1):
            if num % i == 0:
                  result.append(i)
      return result


Test.assert_equals(factorize(12), [1, 2, 3, 4, 6, 12])
Test.assert_equals(factorize(4), [1, 2, 4])
Test.assert_equals(factorize(17), [1, 17])
Test.assert_equals(factorize(24), [1, 2, 3, 4, 6, 8, 12, 24])
Test.assert_equals(factorize(1), [1])


import math

def darts_scoring(x, y):
      r = math.sqrt(x ** 2 + y ** 2)
      if r > 10:
            return 0
      elif 10 >= r > 5:
            return 1
      elif 5 >= r > 1:
            return 5
      else:
            return 10
    


Test.assert_equals(darts_scoring(-9, 9), 0, " ")
Test.assert_equals(darts_scoring(0, 10), 1, " ")
Test.assert_equals(darts_scoring(-5, 0), 5, " ")
Test.assert_equals(darts_scoring(0, -1), 10, " ")
Test.assert_equals(darts_scoring(0, 0), 10, " ")
Test.assert_equals(darts_scoring(-0.1, -0.1), 10, " ")
Test.assert_equals(darts_scoring(0.7, 0.7), 10, " ")
Test.assert_equals(darts_scoring(0.8, -0.8), 5, " ")
Test.assert_equals(darts_scoring(-3.5, 3.5), 5, " ")
Test.assert_equals(darts_scoring(-3.6, -3.6), 1, " ")
Test.assert_equals(darts_scoring(-7.0, 7.0), 1, " ")
Test.assert_equals(darts_scoring(7.1, -7.1), 0, " ")
Test.assert_equals(darts_scoring(0.5, -4), 5, " ")










Test.summary()
import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test


def return_only_integer(lst):
    return [i for i in lst if type(i) == int]


Test.assert_equals(return_only_integer([9, 2, "space", "car", "lion", 16]), [9, 2, 16])
Test.assert_equals(return_only_integer(["hello", 81, "basketball", 123, "fox"]), [81, 123])
Test.assert_equals(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]), [10, 56, 20, 3])
Test.assert_equals(return_only_integer(["String", True, 3.3, 1]), [1])


def unique_sort(lst):
    return sorted(set(lst))


Test.assert_equals(
  unique_sort([1, 5, 8, 2, 3, 4, 4, 4, 10]),
  [1, 2, 3, 4, 5, 8, 10]
)

Test.assert_equals(
	unique_sort([1, 2, 5, 4, 7, 7, 7]),
  [1, 2, 4, 5, 7]
)

Test.assert_equals(
	unique_sort([7, 6, 5, 4, 3, 2, 1, 0, 1]),
  [0, 1, 2, 3, 4, 5, 6, 7]
)

Test.assert_equals(
	unique_sort([3, 6, 5, 4, 3, 27, 1, 100, 1]),
  [1, 3, 4, 5, 6, 27, 100]
)

Test.assert_equals(
	unique_sort([-9, -3.1414, -87, 8, -4.323827, -3.1415, -3.1415]),
  [-87, -9, -4.323827, -3.1415, -3.1414, 8]
)



def nth_smallest(lst, n):
    return sorted(lst)[n-1] if len(lst) >= n else None


Test.assert_equals(nth_smallest([1, 3, 5, 7], 1), 1)
Test.assert_equals(nth_smallest([1, 3, 5, 7], 3), 5)
Test.assert_equals(nth_smallest([1, 3, 5, 7], 5), None)
Test.assert_equals(nth_smallest([7, 3, 5, 1], 2), 3)
Test.assert_equals(nth_smallest([5, 4, 3, 2, 1, -3], 1), -3)
Test.assert_equals(nth_smallest([5, 4, 3, 2, 1, -3], 5), 4)
Test.assert_equals(nth_smallest([4, 5], 3), None)
Test.assert_equals(nth_smallest([4, 5], 2), 5)
Test.assert_equals(nth_smallest([4, 5], 1), 4)



def first_and_last(s):
    return [''.join(sorted(s)), ''.join(sorted(s,reverse = True))]   


Test.assert_equals(first_and_last("marmite"), ["aeimmrt", "trmmiea"])
Test.assert_equals(first_and_last("bench"), ["bcehn", "nhecb"])
Test.assert_equals(first_and_last("scoop"), ["coops", "spooc"])
Test.assert_equals(first_and_last("fanatic"), ["aacfint", "tnifcaa"])
Test.summary()


def sort_by_length(lst):
    return sorted(lst, key = len)


Test.assert_equals(sort_by_length(["Google", "Apple", "Microsoft"]), ["Apple", "Google", "Microsoft"])
Test.assert_equals(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]), ["Raphael", "Leonardo", "Donatello", "Michelangelo"])
Test.assert_equals(sort_by_length(["Turing", "Einstein", "Jung"]), ["Jung", "Turing", "Einstein"])
Test.assert_equals(sort_by_length(["Tatooine", "Hoth", "Yavin", "Dantooine"]), ["Hoth", "Yavin", "Tatooine", "Dantooine"])
Test.assert_equals(sort_by_length(["Mario", "Bowser", "Link"]), ["Link", "Mario", "Bowser"])


import re

def left_digit(num):
    return int(re.findall('\d',num)[0])



Test.assert_equals(left_digit("TrAdE2W1n95!"), 2)
Test.assert_equals(left_digit("V3r1ta$"), 3)
Test.assert_equals(left_digit("U//DertHe1nflu3nC3"), 1)
Test.assert_equals(left_digit("J@v@5cR1PT"), 5)
Test.assert_equals(left_digit("0nSlaUgh7*d3atH"), 0)
Test.assert_equals(left_digit("F8andD3st1nY"), 8)
Test.summary()


def remove_smallest(lst):
    if not lst:
        return []
    
    result = lst.copy()
    result.remove(min(result))
    return result

Test.assert_equals(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5])
Test.assert_equals(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4])
Test.assert_equals(remove_smallest([2, 2, 1, 2, 1]), [2, 2, 2, 1])
Test.assert_equals(remove_smallest([3, 1, 6, 7, 3, 7, 6]), [3, 6, 7, 3, 7, 6])
Test.assert_equals(remove_smallest([4, 4, 4, 1]), [4, 4, 4])
Test.assert_equals(remove_smallest([5, 4, 5, 3, 1, 1]), [5, 4, 5, 3, 1])
Test.assert_equals(remove_smallest([1, 5, 3]), [5, 3])
Test.assert_equals(remove_smallest([]), [])
Test.assert_equals(remove_smallest([6, 2, 5, 4, 8, 6, 3, 2, 7]), [6, 5, 4, 8, 6, 3, 2, 7])
Test.assert_equals(remove_smallest([3]), [])
Test.summary()



def sort_by_length(lst):
    return sorted(lst, key = len)


Test.assert_equals(sort_by_length(["a", "ccc", "dddd", "bb"]), ["a", "bb", "ccc", "dddd"])
Test.assert_equals(sort_by_length(["apple", "pie", "shortcake"]), ["pie", "apple", "shortcake"])
Test.assert_equals(sort_by_length(["may", "april", "september", "august"]), ["may", "april", "august", "september"])
Test.assert_equals(sort_by_length(["maybe"]), ["maybe"])
Test.assert_equals(sort_by_length([]), [])
Test.summary()


def high_low(txt):
    txt = list(map(int, txt.split()))
    return f"{max(txt)} {min(txt)}"



Test.assert_equals(high_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
Test.assert_equals(high_low("1 -1"), "1 -1")
Test.assert_equals(high_low("1 1"), "1 1")
Test.assert_equals(high_low("-1 -1"), "-1 -1")
Test.assert_equals(high_low("1 -1 0"), "1 -1")
Test.assert_equals(high_low("1 1 0"), "1 0")
Test.assert_equals(high_low("-1 -1 0"), "0 -1")
Test.assert_equals(high_low("42"), "42 42")


import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test

def middle_earth(lst):
    x = lst.index("Frodo")
    y = lst.index('Sam')
    if x - 1 == y or x + 1 == y:
        return True
    else:
        return False  



Test.assert_equals(middle_earth(['Frodo', 'Sam', 'Gandalf']), True)
Test.assert_equals(middle_earth(['Orc', 'Sam', 'Gandalf', 'Frodo']), False)
Test.assert_equals(middle_earth(['Sam', 'Frodo', 'Saruman']), True)
Test.assert_equals(middle_earth(['Orc', 'Frodo', 'Legolas', 'Sam', 'Bilbo']), False)
Test.assert_equals(middle_earth(['Aragorn', 'Gandalf', 'Sam', 'Frodo', 'Gollum']), True)
Test.assert_equals(middle_earth(['Arwen', 'Sam', 'Gandalf', 'Frodo', 'Boromir']), False)
Test.assert_equals(middle_earth(['Faramir', 'Frodo', 'Sam', 'Galadriel']), True)
Test.assert_equals(middle_earth(['Eowin', 'Gimli', 'Bilbo', 'Frodo', 'Sam', 'Sauron']), True)
Test.assert_equals(middle_earth(['Gandalf', 'Sam', 'Bilbo', 'Legolas', 'Frodo']), False)
Test.assert_equals(middle_earth(['Legolas', 'Eowyn', 'Gandalf', 'Sam', 'Frodo', 'Gimli']), True)
Test.summary()

def is_omnipresent(lst, val):
    return all(val in sublist for sublist in lst)


Test.assert_equals(is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1), True)
Test.assert_equals(is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6), False)
Test.assert_equals(is_omnipresent([[5], [5], [5], [6, 5]], 5), True)
Test.assert_equals(is_omnipresent([[5], [5], [5], [6, 5]], 6), False)
Test.assert_equals(is_omnipresent([[5, 1], [5, 1], [5, 1], [6, 5, 1]], 1), True)
Test.summary()


def multiply_by_length(arr):
    return list(map(lambda x : x * len(arr),arr))



Test.assert_equals(multiply_by_length([2,6,4,9]), [8,24,16,36])
Test.assert_equals(multiply_by_length([4,1,1]), [12,3,3])
Test.assert_equals(multiply_by_length([1,0,3,3,7,2,1]), [7,0,21,21,49,14,7])
Test.assert_equals(multiply_by_length([0]), [0])


def n_tables_plus_one(num):
    x = []
    for i in range(1,11):
        x.append((num * i) + 1)
    return ",".join(map(str,x))



Test.assert_equals(n_tables_plus_one(1), "2,3,4,5,6,7,8,9,10,11")
Test.assert_equals(n_tables_plus_one(7), "8,15,22,29,36,43,50,57,64,71")
Test.assert_equals(n_tables_plus_one(134), "135,269,403,537,671,805,939,1073,1207,1341")
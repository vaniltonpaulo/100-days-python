import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test


def assign_person_to_job(names, jobs):
    return dict(zip(names,jobs))



pl = ["Annie", "Steven", "Lisa", "Osman"]
jl = ["Teacher", "Engineer", "Doctor", "Cashier"]
Test.assert_equals(assign_person_to_job(pl, jl), {'Annie': 'Teacher', 'Steven': 'Engineer', 'Lisa': 'Doctor', 'Osman': 'Cashier'})


def calculate_losses(items):
    if not items:
        return "Lucky you!"
    return sum(items.values())


Test.assert_equals(calculate_losses({
  "tv": 30,
  "skate": 20,
  "stereo": 50,
}), 100)

Test.assert_equals(calculate_losses({
  "ring": 30000,
  "painting": 20000,
  "bust": 1,
}), 50001)

Test.assert_equals(calculate_losses({
  "chair": 3500,
}), 3500)

Test.assert_equals(calculate_losses({}), "Lucky you!")



def convert(data1, data2):
    return type(data1)(data2)

    
Test.assert_equals(convert([1, 2, 4, 8], [1, 2, 4, 8]), [1, 2, 4, 8])
Test.assert_equals(convert([1, 2, 4, 8], (7, 8, 9)), [7, 8, 9])
Test.assert_equals(convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}), [2, 3, 5, 7, 11, 13])
Test.assert_equals(convert((7, 8, 9), (7, 8, 9)), (7, 8, 9))
Test.assert_equals(convert((7, 8, 9), [1, 2, 4, 8]), (1, 2, 4, 8))
Test.assert_equals(convert((7, 8, 9), {2, 3, 5, 7, 11, 13}), (2, 3, 5, 7, 11, 13))
Test.assert_equals(convert({2, 3, 5, 7, 11, 13}, [1, 2, 4, 8]), {8, 1, 2, 4})
Test.assert_equals(convert({2, 3, 5, 7, 11, 13}, (7, 8, 9)), {8, 9, 7})
Test.assert_equals(convert({2, 3, 5, 7, 11, 13}, {2, 3, 5, 7, 11, 13}), {2, 3, 5, 7, 11, 13})


def count_unique(s1, s2):
    return len(set(s1 + s2))


Test.assert_equals(count_unique("apple", "play"), 5)
Test.assert_equals(count_unique("sore", "zebra"), 7)
Test.assert_equals(count_unique("pip", "geeks"), 6)
Test.assert_equals(count_unique("a", "soup"), 5)
Test.assert_equals(count_unique("maniac", "maniac"), 5)


def odd_sum_list(lst):
    return [(lst[i] + lst[i+ 1]) % 2 == 0 for i in range(len(lst) - 1)]
    

Test.assert_equals(odd_sum_list([11, 15, 6, 8, 9, 10]), [True, False, True, False, False])
Test.assert_equals(odd_sum_list([12,21,5,9,65,32]),[False, True, True, True, False])
Test.assert_equals(odd_sum_list([12,21,5,9,65,32]),[False, True, True, True, False])
Test.assert_equals(odd_sum_list([1,2,3,4,5,6]),[False, False, False, False, False])
Test.assert_equals(odd_sum_list([4,5,6,7,9,45,12,32,65,49,45,840]),[False, False, False, True, True, False, True, False, True, True, False])
Test.assert_equals(odd_sum_list([88,45,654,123]),[False, False, False])
Test.assert_equals(odd_sum_list([98,4,12,565,798,465,13,1,365,14,89,565]),[True, True, False, False, False, True, True, True, False, False, True])


Test.summary()


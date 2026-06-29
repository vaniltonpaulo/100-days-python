import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test

def even_odd_transform(lst, n):
    for i in range(len(lst)):
        if lst[i] % 2== 0:
            lst[i] -= (2 * n)
        else:
            lst[i] +=  (2 * n)
    return lst





Test.assert_equals(even_odd_transform([3, 4, 9], 3), [9, -2, 15])
Test.assert_equals(even_odd_transform([0, 0, 0], 10), [-20, -20, -20])
Test.assert_equals(even_odd_transform([1, 2, 3], 1), [3, 0, 5])
Test.assert_equals(even_odd_transform([55, 90, 830], 2), [59, 86, 826])


def describe_num(n):
    senetence = "The most"

    if n % 1 == 0:
        senetence += " brilliant"

    if n % 2 == 0:
        senetence += " exciting"
    if n % 3 == 0:
        senetence += " fantastic"
    if n % 4== 0:
        senetence += " virtuous"
    if n % 5 == 0:
        senetence += " heart-warming"
    if n % 6 == 0:
        senetence += " tear-jerking"
    if n % 7 == 0:
        senetence += " beautiful"
    if n % 8 == 0:
        senetence += " exhilarating"
    if n % 9 == 0:
        senetence += " emotional"
    if n % 10 == 0:
        senetence += " inspiring"
    return senetence + f" number is {n}!"



Test.assert_equals(describe_num(13), 'The most brilliant number is 13!')
Test.assert_equals(describe_num(4), 'The most brilliant exciting virtuous number is 4!')
Test.assert_equals(describe_num(21), 'The most brilliant fantastic beautiful number is 21!')
Test.assert_equals(describe_num(60), 'The most brilliant exciting fantastic virtuous heart-warming tear-jerking inspiring number is 60!')
Test.assert_equals(describe_num(56), "The most brilliant exciting virtuous beautiful exhilarating number is 56!")
Test.assert_equals(describe_num(47), "The most brilliant number is 47!")
Test.assert_equals(describe_num(115), "The most brilliant heart-warming number is 115!")
Test.assert_equals(describe_num(300), "The most brilliant exciting fantastic virtuous heart-warming tear-jerking inspiring number is 300!")
Test.assert_equals(describe_num(201), "The most brilliant fantastic number is 201!")
Test.assert_equals(describe_num(224), "The most brilliant exciting virtuous beautiful exhilarating number is 224!")
Test.assert_equals(describe_num(42), "The most brilliant exciting fantastic tear-jerking beautiful number is 42!")
Test.assert_equals(describe_num(22), "The most brilliant exciting number is 22!")
Test.assert_equals(describe_num(23), "The most brilliant number is 23!")
Test.assert_equals(describe_num(108), "The most brilliant exciting fantastic virtuous tear-jerking emotional number is 108!")
Test.assert_equals(describe_num(58), "The most brilliant exciting number is 58!")
Test.assert_equals(describe_num(184), "The most brilliant exciting virtuous exhilarating number is 184!")
Test.assert_equals(describe_num(46), "The most brilliant exciting number is 46!")
Test.assert_equals(describe_num(43), "The most brilliant number is 43!")
Test.assert_equals(describe_num(178), "The most brilliant exciting number is 178!")
Test.assert_equals(describe_num(191), "The most brilliant number is 191!")
Test.assert_equals(describe_num(175), "The most brilliant heart-warming beautiful number is 175!")
Test.assert_equals(describe_num(264), "The most brilliant exciting fantastic virtuous tear-jerking exhilarating number is 264!")
Test.assert_equals(describe_num(130), "The most brilliant exciting heart-warming inspiring number is 130!")
Test.assert_equals(describe_num(213), "The most brilliant fantastic number is 213!")
Test.assert_equals(describe_num(25), "The most brilliant heart-warming number is 25!")
Test.assert_equals(describe_num(219), "The most brilliant fantastic number is 219!")
Test.assert_equals(describe_num(173), "The most brilliant number is 173!")
Test.assert_equals(describe_num(212), "The most brilliant exciting virtuous number is 212!")
Test.assert_equals(describe_num(116), "The most brilliant exciting virtuous number is 116!")
Test.assert_equals(describe_num(103), "The most brilliant number is 103!")
Test.assert_equals(describe_num(34), "The most brilliant exciting number is 34!")
Test.assert_equals(describe_num(89), "The most brilliant number is 89!")
Test.assert_equals(describe_num(40), "The most brilliant exciting virtuous heart-warming exhilarating inspiring number is 40!")
Test.assert_equals(describe_num(138), "The most brilliant exciting fantastic tear-jerking number is 138!")
Test.assert_equals(describe_num(153), "The most brilliant fantastic emotional number is 153!")
Test.assert_equals(describe_num(201), "The most brilliant fantastic number is 201!")
Test.assert_equals(describe_num(262), "The most brilliant exciting number is 262!")
Test.assert_equals(describe_num(232), "The most brilliant exciting virtuous exhilarating number is 232!")
Test.assert_equals(describe_num(128), "The most brilliant exciting virtuous exhilarating number is 128!")
Test.assert_equals(describe_num(129), "The most brilliant fantastic number is 129!")
Test.assert_equals(describe_num(264), "The most brilliant exciting fantastic virtuous tear-jerking exhilarating number is 264!")
Test.assert_equals(describe_num(24), "The most brilliant exciting fantastic virtuous tear-jerking exhilarating number is 24!")
Test.assert_equals(describe_num(124), "The most brilliant exciting virtuous number is 124!")
Test.assert_equals(describe_num(163), "The most brilliant number is 163!")
Test.assert_equals(describe_num(80), "The most brilliant exciting virtuous heart-warming exhilarating inspiring number is 80!")
Test.assert_equals(describe_num(130), "The most brilliant exciting heart-warming inspiring number is 130!")
Test.assert_equals(describe_num(46), "The most brilliant exciting number is 46!")
Test.assert_equals(describe_num(247), "The most brilliant number is 247!")
Test.assert_equals(describe_num(89), "The most brilliant number is 89!")
Test.assert_equals(describe_num(127), "The most brilliant number is 127!")
Test.assert_equals(describe_num(169), "The most brilliant number is 169!")
Test.assert_equals(describe_num(195), "The most brilliant fantastic heart-warming number is 195!")
Test.assert_equals(describe_num(192), "The most brilliant exciting fantastic virtuous tear-jerking exhilarating number is 192!")
Test.assert_equals(describe_num(146), "The most brilliant exciting number is 146!")





def check(lst):
    if lst  == sorted(lst):
        return "increasing"
    elif lst  == sorted(lst,reverse= True):
        return "decreasing"
    else:
        return "neither"



Test.assert_equals(check([1, 2, 3]), "increasing")
Test.assert_equals(check([3, 2, 1]), "decreasing")
Test.assert_equals(check([1, 2, 1]), "neither")
Test.assert_equals(check([1, 1, 2]), "neither")
Test.assert_equals(check([1, 3, 5, 7, 9, 10]), "increasing")
Test.assert_equals(check([5, 6, 5, 7, 9, 10]), "neither")
Test.assert_equals(check([5, 7]), "increasing")
Test.assert_equals(check([9, 7, 1]), "decreasing")



















Test.summary()
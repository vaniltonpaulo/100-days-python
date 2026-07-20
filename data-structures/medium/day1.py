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


def profit(info):
    return round(info['sell_price'] * info['inventory'] - info['cost_price']*info['inventory'],0)


Test.assert_equals(profit({'cost_price': 32.67, 'sell_price': 45.00, 'inventory': 1200}), 14796)
Test.assert_equals(profit({'cost_price': 0.1, 'sell_price': 0.18, 'inventory': 259800}), 20784)
Test.assert_equals(profit({'cost_price': 185.00, 'sell_price': 299.99, 'inventory': 300}), 34497)
Test.assert_equals(profit({'cost_price': 378.11, 'sell_price': 990.00, 'inventory': 99}), 60577)
Test.assert_equals(profit({'cost_price': 4.67, 'sell_price': 5.00, 'inventory': 78000}), 25740)
Test.assert_equals(profit({'cost_price': 19.87, 'sell_price': 110.00, 'inventory': 350}), 31546)
Test.assert_equals(profit({'cost_price': 2.91, 'sell_price': 4.50, 'inventory': 6000}), 9540)
Test.assert_equals(profit({'cost_price': 68.01, 'sell_price': 149.99, 'inventory': 500}), 40990)
Test.assert_equals(profit({'cost_price': 1.45, 'sell_price': 8.50, 'inventory': 10000}), 70500)
Test.assert_equals(profit({'cost_price': 10780, 'sell_price': 34999, 'inventory': 10}), 242190)


def sum_fractions(lst):
    return round(sum(num/dem for num, dem in lst), 0)


Test.assert_equals(sum_fractions([[36, 4], [22, 60]]), 9)
Test.assert_equals(sum_fractions([[-11, 12], [18, 13], [4, 5]]), 1)
Test.assert_equals(sum_fractions([[11, 12], [18, 13], [4, 5]]), 3)
Test.assert_equals(sum_fractions([[18, 13], [4, 5]]), 2)
Test.assert_equals(sum_fractions([[41, 14], [10, 91]]), 3)
Test.assert_equals(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]), 11)


def histogram(lst, char):
    return "\n".join( i * char for i  in lst)



Test.assert_equals(histogram([2,4,5,6], "o"), 'oo\noooo\nooooo\noooooo')
Test.assert_equals(histogram([4,2], "*"), '****\n**')
Test.assert_equals(histogram([20,1,12], "H"), 'HHHHHHHHHHHHHHHHHHHH\nH\nHHHHHHHHHHHH')
Test.assert_equals(histogram([2,1,2,4,5,2,3], "#"), '##\n#\n##\n####\n#####\n##\n###')



def unrepeated(word):
    seen = set()
    result = []
    for ch in word:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)


Test.assert_equals(unrepeated("hello"), "helo")
Test.assert_equals(unrepeated("aaaaa"), "a")
Test.assert_equals(unrepeated("WWE!!!"), "WE!")
Test.assert_equals(unrepeated("call 911"), "cal 91")
Test.assert_equals(unrepeated("altwaff test"), "altwf es")
Test.assert_equals(unrepeated("Mississippi"), "Misp")
Test.assert_equals(unrepeated("Tennessee"), "Tens")
Test.assert_equals(unrepeated("Massachusetts"), "Maschuet")



def filter_by_rating(d, rating):
    caugth = {n:s for n,s in d.items() if s == rating}
    return caugth if caugth else "No results found"


Test.assert_equals(filter_by_rating({"Brand A": "*", "Brand B": "*****", "Brand C": "*", "Brand D": "**", "Brand E": "****", "Brand F": "*****", "Brand G": "****", "Brand H": "****", "Brand I": "*****", "Brand K": "***", "Brand L": "*****", "Brand M": "***", "Brand N": "*", "Brand O": "***", "Brand P": "*****", "Brand Q": "**", "Brand R": "****"}, "***"), {"Brand K": "***", "Brand M": "***", "Brand O": "***"})
Test.assert_equals(filter_by_rating({"Brand A": "*", "Brand B": "***", "Brand C": "**", "Brand D": "*****", "Brand E": "*", "Brand F": "****", "Brand G": "*****", "Brand H": "*****", "Brand I": "**", "Brand K": "*", "Brand L": "*", "Brand M": "***", "Brand N": "*", "Brand O": "*", "Brand P": "**", "Brand Q": "**", "Brand R": "****", "Brand S": "****", "Brand T": "**", "Brand U": "*", "Brand V": "*", "Brand W": "*", "Brand X": "***", "Brand Y": "*****", "Brand Z": "****"}, "**"), {"Brand C": "**", "Brand I": "**", "Brand P": "**", "Brand Q": "**", "Brand T": "**"})
Test.assert_equals(filter_by_rating({"Brand A": "***", "Brand B": "**", "Brand C": "****", "Brand D": "*", "Brand E": "*", "Brand F": "**", "Brand G": "***", "Brand H": "*", "Brand I": "**", "Brand K": "*****", "Brand L": "**", "Brand M": "*"}, "**"), {"Brand B": "**", "Brand F": "**", "Brand I": "**", "Brand L": "**"})
Test.assert_equals(filter_by_rating({"Brand A": "*", "Brand B": "***", "Brand C": "***", "Brand D": "***", "Brand E": "*", "Brand F": "**", "Brand G": "***", "Brand H": "*****", "Brand I": "**", "Brand K": "***", "Brand L": "*", "Brand M": "****", "Brand N": "****", "Brand O": "***", "Brand P": "**", "Brand Q": "*****", "Brand R": "*", "Brand S": "*", "Brand T": "*****", "Brand U": "*****", "Brand V": "*", "Brand W": "*****", "Brand X": "****", "Brand Y": "*", "Brand Z": "*****"}, "****"), {"Brand M": "****", "Brand N": "****", "Brand X": "****"})
Test.assert_equals(filter_by_rating({"Brand A": "*", "Brand B": "****", "Brand C": "*****", "Brand D": "*", "Brand E": "**", "Brand F": "***", "Brand G": "*", "Brand H": "**", "Brand I": "*", "Brand K": "**", "Brand L": "****"}, "*"), {"Brand A": "*", "Brand D": "*", "Brand G": "*", "Brand I": "*"})
Test.assert_equals(filter_by_rating({"Brand A": "****", "Brand B": "****", "Brand C": "**", "Brand D": "*", "Brand E": "**", "Brand F": "***", "Brand G": "***", "Brand H": "**", "Brand I": "*", "Brand K": "*", "Brand L": "****", "Brand M": "*", "Brand N": "*****", "Brand O": "**", "Brand P": "*", "Brand Q": "*****", "Brand R": "*"}, "****"), {"Brand A": "****", "Brand B": "****", "Brand L": "****"})
Test.assert_equals(filter_by_rating({"Brand A": "**", "Brand B": "*", "Brand C": "*"}, "**"), {"Brand A": "**"})
Test.assert_equals(filter_by_rating({"Brand A": "****", "Brand B": "*", "Brand C": "****", "Brand D": "***", "Brand E": "*****"}, "**"), "No results found")
Test.assert_equals(filter_by_rating({"Brand A": "****", "Brand B": "****", "Brand C": "***", "Brand D": "****", "Brand E": "*****", "Brand F": "*", "Brand G": "****", "Brand H": "*****", "Brand I": "*", "Brand K": "****", "Brand L": "****", "Brand M": "*", "Brand N": "***", "Brand O": "**", "Brand P": "*", "Brand Q": "*", "Brand R": "****", "Brand S": "*****", "Brand T": "****", "Brand U": "*****", "Brand V": "****", "Brand W": "****", "Brand X": "**", "Brand Y": "*"}, "****"), {"Brand A": "****", "Brand B": "****", "Brand D": "****", "Brand G": "****", "Brand K": "****", "Brand L": "****", "Brand R": "****", "Brand T": "****", "Brand V": "****", "Brand W": "****"})
Test.assert_equals(filter_by_rating({"Brand A": "**", "Brand B": "****", "Brand C": "***", "Brand D": "****", "Brand E": "*", "Brand F": "*", "Brand G": "**", "Brand H": "***", "Brand I": "***", "Brand K": "**", "Brand L": "***", "Brand M": "**", "Brand N": "**", "Brand O": "*", "Brand P": "*", "Brand Q": "*****", "Brand R": "***", "Brand S": "**", "Brand T": "*", "Brand U": "**", "Brand V": "*", "Brand W": "**", "Brand X": "****"}, "**"), {"Brand A": "**", "Brand G": "**", "Brand K": "**", "Brand M": "**", "Brand N": "**", "Brand S": "**", "Brand U": "**", "Brand W": "**"})
Test.assert_equals(filter_by_rating({"Brand A": "*", "Brand B": "**", "Brand C": "****", "Brand D": "*****", "Brand E": "*****", "Brand F": "*****", "Brand G": "****", "Brand H": "*", "Brand I": "*", "Brand K": "*", "Brand L": "****", "Brand M": "*", "Brand N": "***", "Brand O": "****", "Brand P": "****", "Brand Q": "****", "Brand R": "****", "Brand S": "**", "Brand T": "****"}, "*"), {"Brand A": "*", "Brand H": "*", "Brand I": "*", "Brand K": "*", "Brand M": "*"})
Test.assert_equals(filter_by_rating({"Brand A": "**", "Brand B": "*", "Brand C": "*****", "Brand D": "*****"}, "*****"), {"Brand C": "*****", "Brand D": "*****"})
Test.assert_equals(filter_by_rating({"Brand A": "*****", "Brand B": "***", "Brand C": "***", "Brand D": "***", "Brand E": "***", "Brand F": "***", "Brand G": "****", "Brand H": "*", "Brand I": "**", "Brand K": "***", "Brand L": "****", "Brand M": "*", "Brand N": "*****", "Brand O": "**", "Brand P": "*", "Brand Q": "****", "Brand R": "**", "Brand S": "****", "Brand T": "*", "Brand U": "*****", "Brand V": "**", "Brand W": "*", "Brand X": "**", "Brand Y": "*****"}, "****"), {"Brand G": "****", "Brand L": "****", "Brand Q": "****", "Brand S": "****"})
Test.assert_equals(filter_by_rating({"Brand A": "*", "Brand B": "*****", "Brand C": "*****", "Brand D": "*", "Brand E": "****", "Brand F": "*", "Brand G": "****", "Brand H": "*****", "Brand I": "***", "Brand K": "***", "Brand L": "***", "Brand M": "*", "Brand N": "****", "Brand O": "****", "Brand P": "**", "Brand Q": "*****", "Brand R": "***"}, "****"), {"Brand E": "****", "Brand G": "****", "Brand N": "****", "Brand O": "****"})
Test.assert_equals(filter_by_rating({"Brand A": "***", "Brand B": "****", "Brand C": "****", "Brand D": "*", "Brand E": "**", "Brand F": "****", "Brand G": "*****", "Brand H": "****", "Brand I": "*"}, "****"), {"Brand B": "****", "Brand C": "****", "Brand F": "****", "Brand H": "****"})
Test.assert_equals(filter_by_rating({"Brand A": "*", "Brand B": "*****", "Brand C": "**", "Brand D": "*****", "Brand E": "**", "Brand F": "*", "Brand G": "**", "Brand H": "***", "Brand I": "***", "Brand K": "*****"}, "*****"), {"Brand B": "*****", "Brand D": "*****", "Brand K": "*****"})
Test.assert_equals(filter_by_rating({"Brand A": "****", "Brand B": "****", "Brand C": "*****", "Brand D": "*****", "Brand E": "****", "Brand F": "***", "Brand G": "**", "Brand H": "**", "Brand I": "****", "Brand K": "****", "Brand L": "****", "Brand M": "****", "Brand N": "***", "Brand O": "**"}, "****"), {"Brand A": "****", "Brand B": "****", "Brand E": "****", "Brand I": "****", "Brand K": "****", "Brand L": "****", "Brand M": "****"})
Test.assert_equals(filter_by_rating({"Brand A": "***", "Brand B": "***"}, "*****"), "No results found")
Test.assert_equals(filter_by_rating({"Brand A": "***", "Brand B": "*****", "Brand C": "*", "Brand D": "****", "Brand E": "*", "Brand F": "**", "Brand G": "**", "Brand H": "*****", "Brand I": "**", "Brand K": "****", "Brand L": "**", "Brand M": "**", "Brand N": "****", "Brand O": "****", "Brand P": "*****"}, "***"), {"Brand A": "***"})
Test.assert_equals(filter_by_rating({"Brand A": "**", "Brand B": "*", "Brand C": "*****", "Brand D": "*****", "Brand E": "*", "Brand F": "***", "Brand G": "*", "Brand H": "**", "Brand I": "*", "Brand K": "**", "Brand L": "*", "Brand M": "***", "Brand N": "*****", "Brand O": "*"}, "*****"), {"Brand C": "*****", "Brand D": "*****", "Brand N": "*****"})
Test.assert_equals(filter_by_rating({"Brand A": "*", "Brand B": "*", "Brand C": "*", "Brand D": "***", "Brand E": "****", "Brand F": "***", "Brand G": "*****", "Brand H": "**", "Brand I": "*", "Brand K": "*****", "Brand L": "***", "Brand M": "***", "Brand N": "***", "Brand O": "**", "Brand P": "**", "Brand Q": "*****", "Brand R": "****", "Brand S": "***", "Brand T": "****", "Brand U": "*****", "Brand V": "***", "Brand W": "*****", "Brand X": "*****", "Brand Y": "***"}, "*****"), {"Brand G": "*****", "Brand K": "*****", "Brand Q": "*****", "Brand U": "*****", "Brand W": "*****", "Brand X": "*****"})
Test.assert_equals(filter_by_rating({"Brand A": "*****", "Brand B": "****", "Brand C": "****", "Brand D": "*", "Brand E": "*", "Brand F": "****", "Brand G": "****", "Brand H": "**", "Brand I": "****", "Brand K": "****", "Brand L": "*****", "Brand M": "*****", "Brand N": "***", "Brand O": "****", "Brand P": "**", "Brand Q": "***", "Brand R": "***", "Brand S": "*****", "Brand T": "*", "Brand U": "*****", "Brand V": "****", "Brand W": "***"}, "****"), {"Brand B": "****", "Brand C": "****", "Brand F": "****", "Brand G": "****", "Brand I": "****", "Brand K": "****", "Brand O": "****", "Brand V": "****"})
Test.assert_equals(filter_by_rating({"Brand A": "*", "Brand B": "****", "Brand C": "*", "Brand D": "*****", "Brand E": "**", "Brand F": "****", "Brand G": "***", "Brand H": "****", "Brand I": "*", "Brand K": "*", "Brand L": "*****", "Brand M": "*****", "Brand N": "*", "Brand O": "**", "Brand P": "*****", "Brand Q": "**", "Brand R": "*****", "Brand S": "*****", "Brand T": "****", "Brand U": "*****", "Brand V": "*****", "Brand W": "**", "Brand X": "***"}, "**"), {"Brand E": "**", "Brand O": "**", "Brand Q": "**", "Brand W": "**"})
Test.assert_equals(filter_by_rating({"Brand A": "**", "Brand B": "**", "Brand C": "**", "Brand D": "***", "Brand E": "*****", "Brand F": "**"}, "****"), "No results found")
Test.assert_equals(filter_by_rating({"Brand A": "*", "Brand B": "*", "Brand C": "**", "Brand D": "*", "Brand E": "****", "Brand F": "****", "Brand G": "**", "Brand H": "*", "Brand I": "***", "Brand K": "**", "Brand L": "***", "Brand M": "***", "Brand N": "****", "Brand O": "*", "Brand P": "*****", "Brand Q": "*****", "Brand R": "*", "Brand S": "****", "Brand T": "****", "Brand U": "*", "Brand V": "**", "Brand W": "****", "Brand X": "****", "Brand Y": "****", "Brand Z": "**"}, "***"), {"Brand I": "***", "Brand L": "***", "Brand M": "***"})
Test.assert_equals(filter_by_rating({"Brand A": "**", "Brand B": "*****", "Brand C": "***", "Brand D": "**", "Brand E": "*", "Brand F": "****", "Brand G": "****", "Brand H": "*", "Brand I": "*", "Brand K": "*", "Brand L": "****", "Brand M": "*", "Brand N": "**", "Brand O": "*", "Brand P": "**", "Brand Q": "*"}, "*****"), {"Brand B": "*****"})
Test.assert_equals(filter_by_rating({"Brand A": "****", "Brand B": "*****", "Brand C": "*****", "Brand D": "****", "Brand E": "**", "Brand F": "*", "Brand G": "**", "Brand H": "**", "Brand I": "***", "Brand K": "***", "Brand L": "***", "Brand M": "***", "Brand N": "****", "Brand O": "*****", "Brand P": "*", "Brand Q": "*", "Brand R": "****", "Brand S": "**", "Brand T": "**", "Brand U": "*****", "Brand V": "***", "Brand W": "***"}, "**"), {"Brand E": "**", "Brand G": "**", "Brand H": "**", "Brand S": "**", "Brand T": "**"})


Test.summary()
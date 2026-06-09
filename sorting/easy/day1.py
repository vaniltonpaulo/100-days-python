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
Test.summary()




def sort_descending(num):
    return int("".join(sorted(str(num), reverse=True)))



Test.assert_equals(sort_descending(123), 321)
Test.assert_equals(sort_descending(670276097), 977766200)
Test.assert_equals(sort_descending(2619805), 9865210)
Test.assert_equals(sort_descending(81294), 98421)
Test.assert_equals(sort_descending(0000000), 0000000)
Test.assert_equals(sort_descending(321), 321)
Test.assert_equals(sort_descending(628904), 986420)
Test.assert_equals(sort_descending(289327560), 987653220)
Test.assert_equals(sort_descending(6456), 6654)
Test.assert_equals(sort_descending(444111888555333), 888555444333111)



Test.summary()



def reverse(txt):
    x = txt.split(" ")
    for i in x:
        if len(i) >= 5:
            txt = txt.replace(i,i[::-1])
    return txt



Test.assert_equals(reverse("Reverse"), "esreveR")
Test.assert_equals(reverse("This is a typical sentence."), "This is a lacipyt .ecnetnes")
Test.assert_equals(reverse("The dog is big."), "The dog is big.")
Test.assert_equals(reverse("Reverse the order of every word greater than or equal to five characters."), "esreveR the redro of yreve word retaerg than or lauqe to five .sretcarahc")
Test.assert_equals(reverse("Lets all be unique together until we realise we are all the same."), "Lets all be euqinu rehtegot litnu we esilaer we are all the .emas")
Test.assert_equals(reverse("The old apple revels in its authority."), "The old elppa slever in its .ytirohtua")
Test.assert_equals(reverse("The shooter says goodbye to his love."), "The retoohs says eybdoog to his .evol")
Test.assert_equals(reverse("Please wait outside of the house."), "esaelP wait edistuo of the .esuoh")
Test.assert_equals(reverse("Two seats were vacant."), "Two staes were .tnacav")
Test.assert_equals(reverse("Sixty-Four comes asking for bread."), "ruoF-ytxiS semoc gniksa for .daerb")


def number_len_sort(lst):
    x = sorted([str(i) for i in lst], key = len)
    return [int(i) for i in x]



Test.assert_equals(number_len_sort([1, 54, 1, 2, 463, 2]), [1, 1, 2, 2, 54, 463])
Test.assert_equals(number_len_sort([999, 421, 22, 990, 32]), [22, 32, 999, 421, 990])
Test.assert_equals(number_len_sort([9, 8, 7, 6, 5, 4, 31, 2, 1, 3]), [9, 8, 7, 6, 5, 4, 2, 1, 3, 31])
Test.assert_equals(number_len_sort([755, 1109, 9374, 94, 3683, 8695, 4135, 5177, 3216]), [94, 755, 1109, 9374, 3683, 8695, 4135, 5177, 3216])
Test.assert_equals(number_len_sort([8013, 1753, 7283, 6830, 73, 6278, 4931, 4556]), [73, 8013, 1753, 7283, 6830, 6278, 4931, 4556])
Test.assert_equals(number_len_sort([2762, 5905, 9433, 9809, 6511, 7141, 1050, 2610, 8123]), [2762, 5905, 9433, 9809, 6511, 7141, 1050, 2610, 8123])
Test.assert_equals(number_len_sort([9103, 5630, 7273, 2024]), [9103, 5630, 7273, 2024])
Test.assert_equals(number_len_sort([1342, 7567, 3504, 4378, 3070, 6592, 3645]), [1342, 7567, 3504, 4378, 3070, 6592, 3645])
Test.assert_equals(number_len_sort([237, 574, 3703, 2251, 4963, 2640]), [237, 574, 3703, 2251, 4963, 2640])
Test.assert_equals(number_len_sort([3633, 4402, 6745]), [3633, 4402, 6745])
Test.assert_equals(number_len_sort([6053, 2486, 8238]), [6053, 2486, 8238])
Test.assert_equals(number_len_sort([7919, 2725, 6296, 3517, 1788, 1321, 9049, 4481]), [7919, 2725, 6296, 3517, 1788, 1321, 9049, 4481])
Test.assert_equals(number_len_sort([1488, 764, 1053, 7053, 1718, 2950, 4697]), [764, 1488, 1053, 7053, 1718, 2950, 4697])
Test.assert_equals(number_len_sort([1321, 7671, 4235, 5989]), [1321, 7671, 4235, 5989])
Test.assert_equals(number_len_sort([3640, 4634, 9183, 6361, 7823]), [3640, 4634, 9183, 6361, 7823])
Test.assert_equals(number_len_sort([2900, 7995]), [2900, 7995])
Test.assert_equals(number_len_sort([7620, 3510]), [7620, 3510])
Test.assert_equals(number_len_sort([5533, 8639, 8297, 7591, 3280, 3354]), [5533, 8639, 8297, 7591, 3280, 3354])
Test.assert_equals(number_len_sort([9403, 9403]), [9403, 9403])
Test.assert_equals(number_len_sort([3470, 8155, 6086, 2095, 3445, 1869]), [3470, 8155, 6086, 2095, 3445, 1869])
Test.assert_equals(number_len_sort([3772, 9711, 1576, 5919, 7966, 1528]), [3772, 9711, 1576, 5919, 7966, 1528])
Test.assert_equals(number_len_sort([5751, 5472, 6910, 3678]), [5751, 5472, 6910, 3678])
Test.assert_equals(number_len_sort([7195, 9518, 9523, 7713, 6969, 739, 7313, 8588, 8545, 4414]), [739, 7195, 9518, 9523, 7713, 6969, 7313, 8588, 8545, 4414])
Test.assert_equals(number_len_sort([2209, 918, 8152, 1726, 8326, 2734]), [918, 2209, 8152, 1726, 8326, 2734])
Test.assert_equals(number_len_sort([5653, 5848, 4107, 2802, 6050, 1034, 2435, 5952]), [5653, 5848, 4107, 2802, 6050, 1034, 2435, 5952])
Test.assert_equals(number_len_sort([3587, 6762, 6215, 6995, 8731, 7989, 4913, 5251]), [3587, 6762, 6215, 6995, 8731, 7989, 4913, 5251])
Test.assert_equals(number_len_sort([6826, 5156, 8915, 4002]), [6826, 5156, 8915, 4002])
Test.assert_equals(number_len_sort([1280, 4939, 9179, 551, 9712, 6871]), [551, 1280, 4939, 9179, 9712, 6871])
Test.assert_equals(number_len_sort([8798, 8615, 1035, 4647, 8706, 7017, 9221, 6120]), [8798, 8615, 1035, 4647, 8706, 7017, 9221, 6120])
Test.assert_equals(number_len_sort([2744, 8325, 9185, 7703, 9732, 9603, 3817, 4448, 7025]), [2744, 8325, 9185, 7703, 9732, 9603, 3817, 4448, 7025])
Test.assert_equals(number_len_sort([7297, 2434, 9661, 9883, 9273]), [7297, 2434, 9661, 9883, 9273])
Test.assert_equals(number_len_sort([4950, 6059, 6961, 5026]), [4950, 6059, 6961, 5026])
Test.assert_equals(number_len_sort([7824, 187, 8454, 5269, 5576, 9835, 4142, 5154, 2682]), [187, 7824, 8454, 5269, 5576, 9835, 4142, 5154, 2682])
Test.assert_equals(number_len_sort([7168, 2449, 5870]), [7168, 2449, 5870])
Test.assert_equals(number_len_sort([4227, 2439]), [4227, 2439])
Test.assert_equals(number_len_sort([7123, 3851, 5730]), [7123, 3851, 5730])
Test.assert_equals(number_len_sort([1782]), [1782])
Test.assert_equals(number_len_sort([3940, 4334]), [3940, 4334])
Test.assert_equals(number_len_sort([9834, 9404, 1736, 2429, 500, 1446, 668, 2993, 2981, 9442]), [500, 668, 9834, 9404, 1736, 2429, 1446, 2993, 2981, 9442])
Test.assert_equals(number_len_sort([9164, 2647, 4861, 7721, 1198]), [9164, 2647, 4861, 7721, 1198])
Test.assert_equals(number_len_sort([4144, 1983]), [4144, 1983])
Test.assert_equals(number_len_sort([6562, 8367, 3499, 7010]), [6562, 8367, 3499, 7010])
Test.assert_equals(number_len_sort([8581, 2111, 9257, 4423, 3217, 9852, 2313, 4073, 2487]), [8581, 2111, 9257, 4423, 3217, 9852, 2313, 4073, 2487])
Test.assert_equals(number_len_sort([7309]), [7309])
Test.assert_equals(number_len_sort([9641, 4306, 9064]), [9641, 4306, 9064])
Test.assert_equals(number_len_sort([6245, 4677, 792, 9823, 3366]), [792, 6245, 4677, 9823, 3366])
Test.assert_equals(number_len_sort([4038, 4156]), [4038, 4156])
Test.assert_equals(number_len_sort([5429, 274, 256, 3437, 3222, 3294, 5648, 3281, 6696, 1883]), [274, 256, 5429, 3437, 3222, 3294, 5648, 3281, 6696, 1883])
Test.assert_equals(number_len_sort([6509, 6244, 4466, 7738, 1935, 9724, 6590]), [6509, 6244, 4466, 7738, 1935, 9724, 6590])
Test.assert_equals(number_len_sort([1001, 5842, 4261, 969]), [969, 1001, 5842, 4261])
Test.assert_equals(number_len_sort([7139]), [7139])
Test.assert_equals(number_len_sort([6623, 9247, 2175, 3306, 558, 6236, 9709, 643, 9737]), [558, 643, 6623, 9247, 2175, 3306, 6236, 9709, 9737])
Test.assert_equals(number_len_sort([1139, 1756, 772]), [772, 1139, 1756])

Test.summary()


def is_good_match(lst):
    if len(lst) % 2 != 0:
        return "bad match"
    else:
        return [a + b for a, b in zip(lst[::2], lst[1::2])]


Test.assert_equals(is_good_match([1, 2, 4, 7]), [3, 11])
Test.assert_equals(is_good_match([1, 2, 4]), "bad match")
Test.assert_equals(is_good_match([5, 7, 9, -1, 4, 2]), [12, 8, 6])
Test.assert_equals(is_good_match([1, 2, 3, 4, 5, 6]), [3, 7, 11])
Test.assert_equals(is_good_match([3, 6, 7, 9, -1]), "bad match")
Test.assert_equals(is_good_match([5, 7, 9, -1, 4, 2, 9]), "bad match")
Test.assert_equals(is_good_match([1, -1, 1, -1, 1, -1]), [0,0,0])


Test.summary()


def in_box(lst):
    return any("*" in row[1:-1] for row in lst[1:-1])


Test.assert_equals(in_box([
		"###", 
		"# #", 
		"###"
	]), False)

Test.assert_equals(in_box([
		"####", 
		"#  #", 
		"#  #", 
		"####"
	]), False)

Test.assert_equals(in_box([
		"#####", 
		"#   #", 
		"#   #", 
		"#   #", 
		"#####"
	]), False)

Test.assert_equals(in_box([
		"###", 
		"#*#", 
		"###"
	]), True)

Test.assert_equals(in_box([
		"####", 
		"# *#", 
		"#  #", 
		"####"
	]), True)

Test.assert_equals(in_box([
		"#####", 
		"#  *#", 
		"#   #", 
		"#   #", 
		"#####"
	]), True)

Test.assert_equals(in_box([
		"#####", 
		"#   #", 
		"# * #", 
		"#   #", 
		"#####"
	]), True)

Test.assert_equals(in_box([
		"#####", 
		"#   #", 
		"#   #", 
		"# * #", 
		"#####"
	]), True)

Test.assert_equals(in_box([
		"#####", 
		"#*  #", 
		"#   #", 
		"#   #", 
		"#####"
	]), True)

Test.assert_equals(in_box([
	"*####",
	"# #",
	"# #*",
	"####" 
]), False)


Test.summary()


def unique_in_order(sequence):
    result = []

    for i, item in enumerate(sequence):
        if i == 0 or item != sequence[i - 1]:
            result.append(item)

    return result


Test.assert_equals(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])
Test.assert_equals(unique_in_order("ABBCcAD"), ["A", "B", "C", "c", "A", "D"])
Test.assert_equals(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])
Test.assert_equals(unique_in_order("12333355555522211133"), ["1", "2", "3", "5", "2", "1", "3"])
Test.assert_equals(unique_in_order("uuUfffFgGggYtt76%5$$$"), ["u", "U", "f", "F", "g", "G", "g", "Y", "t", "7", "6", "%", "5", "$"])
Test.assert_equals(unique_in_order(["1", "2", "2", "3", "3"]), ["1", "2", "3"])
Test.assert_equals(unique_in_order([3, 7, 3, 8, 4]), [3, 7, 3, 8, 4])
Test.assert_equals(unique_in_order("ABC"), ["A", "B", "C"])
Test.assert_equals(unique_in_order("$$$%%%$$$%%%"), ["$", "%", "$", "%"])
Test.assert_equals(unique_in_order([1, 1, 1, "A", "B", "B"]), [1, "A", "B"])

Test.summary()

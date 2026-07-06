import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test




def get_case(txt):
    if txt.islower():
        return "lower"
    elif txt.isupper():
        return "upper"
    else:
        return "mixed"

Test.assert_equals(get_case("whisper..."), "lower")
Test.assert_equals(get_case("SHOUT!"), "upper")
Test.assert_equals(get_case("Indoor Voice"), "mixed")
Test.assert_equals(get_case("324324Indoor66453546Voice434"), "mixed")
Test.assert_equals(get_case("!!!!SHOUT!!!!"), "upper")
Test.assert_equals(get_case("......313whisper2131232..."), "lower")


def hash_plus_count(txt):
    return [txt.count("#"), txt.count("+")]



Test.assert_equals(hash_plus_count("####"), [4, 0])
Test.assert_equals(hash_plus_count("#"), [1, 0])
Test.assert_equals(hash_plus_count("+++++++"), [0, 7])
Test.assert_equals(hash_plus_count("++"), [0, 2])
Test.assert_equals(hash_plus_count("#+#+"), [2, 2])
Test.assert_equals(hash_plus_count("###+"), [3, 1])
Test.assert_equals(hash_plus_count("##+++#"), [3, 3])
Test.assert_equals(hash_plus_count("#+++#+#++#"), [4, 6])
Test.assert_equals(hash_plus_count(""), [0, 0])


def find_letters(word):
    return [c for c in word if word.count(c) == 1]


Test.assert_equals(find_letters("monopoly"), ["m", "n", "p", "l", "y"])
Test.assert_equals(find_letters("balloon"), ["b", "a", "n"])
Test.assert_equals(find_letters("analysis"),  ["n", "l", "y", "i"])
Test.assert_equals(find_letters("summer"), ["s", "u", "e", "r"])
Test.assert_equals(find_letters("apple"), ["a", "l", "e"])
Test.assert_equals(find_letters("commission"), ["c", "n"])
Test.assert_equals(find_letters("fox"), ["f", "o", "x"])


def height(side):
    h = (side * (3 ** 0.5) / 2) * 10
    return f"{h:.1f} mm"

Test.assert_equals(height(2), "17.3 mm")
Test.assert_equals(height(5), "43.3 mm")
Test.assert_equals(height(6.2), "53.7 mm")
Test.assert_equals(height(8.7), "75.3 mm")
Test.assert_equals(height(10), "86.6 mm")
Test.assert_equals(height(13), "112.6 mm")
Test.assert_equals(height(18.5), "160.2 mm")


def add_parity_bit(b):
    x = b.count("1")

    if x % 2 == 0:
        return b + "0"
    else:
        return b + "1"


Test.assert_equals(add_parity_bit("0010110"), "00101101")
Test.assert_equals(add_parity_bit("1100000"), "11000000")
Test.assert_equals(add_parity_bit("1111111"), "11111111")
Test.assert_equals(add_parity_bit("1010011"), "10100110")


def is_boiling(temp):
    if temp[-1] == "C":
        return int(temp[:-1]) >= 100
    elif temp[-1] == "F":
        return int(temp[:-1]) >= 212
    else:
        return False
    



Test.assert_equals(is_boiling("212F"), True)
Test.assert_equals(is_boiling("100C"), True)
Test.assert_equals(is_boiling("0F"), False)
Test.assert_equals(is_boiling("-1F"), False)
Test.assert_equals(is_boiling("213F"), True)
Test.assert_equals(is_boiling("104C"), True)
Test.assert_equals(is_boiling("-10F"), False)
Test.assert_equals(is_boiling("120F"), False)


def reverse_capitalize(txt):
    return txt[::-1].upper()


Test.assert_equals(reverse_capitalize("edabit"), "TIBADE")
Test.assert_equals(reverse_capitalize("abc"), "CBA")
Test.assert_equals(reverse_capitalize("hellothere") ,"EREHTOLLEH")
Test.assert_equals(reverse_capitalize("input") , "TUPNI")
Test.assert_equals(reverse_capitalize("indubitably") , "YLBATIBUDNI")


def back_to_home(directions):
    x = directions.count("N") - directions.count("S")
    y = directions.count("E")  - directions.count("W")

    return x == 0 and y == 0


Test.assert_equals(back_to_home("NNNN"), False)
Test.assert_equals(back_to_home("NENESSWW"), True)
Test.assert_equals(back_to_home("NEESSW"), False)
Test.assert_equals(back_to_home("EEWE"), False)
Test.assert_equals(back_to_home("NNSSEEEWWWEW"), True)
Test.assert_equals(back_to_home("NNNNWW"), False)

def space_me_out(s):
    return " ".join(s)


Test.assert_equals(space_me_out("space"), "s p a c e")
Test.assert_equals(space_me_out("far out"), "f a r   o u t")
Test.assert_equals(space_me_out("elongated musk"), "e l o n g a t e d   m u s k")
Test.assert_equals(space_me_out("long"), "l o n g")
Test.assert_equals(space_me_out("123"), "1 2 3")
Test.assert_equals(space_me_out("a1b2c3"), "a 1 b 2 c 3")


def calculate_scores(txt):
    return [txt.count("A"), txt.count("B"), txt.count("C")]


Test.assert_equals(calculate_scores("AAB"), [2, 1, 0])
Test.assert_equals(calculate_scores("ABC"), [1, 1, 1])
Test.assert_equals(calculate_scores("ABCBACC"), [2, 2, 3])
Test.assert_equals(calculate_scores("CCBBBB"), [0, 4, 2])
Test.assert_equals(calculate_scores("CCAABBAABBCC"), [4, 4, 4])
Test.assert_equals(calculate_scores("A"), [1, 0, 0])
Test.assert_equals(calculate_scores(""), [0, 0, 0])
Test.assert_equals(calculate_scores("ACCCA"), [2, 0, 3])


def reverse_and_not(i):
    return int(str(i)[::-1] + str(i))



Test.assert_equals(reverse_and_not(123), 321123)
Test.assert_equals(reverse_and_not(123456789), 987654321123456789)
Test.assert_equals(reverse_and_not(496), 694496)
Test.assert_equals(reverse_and_not(307), 703307)
Test.assert_equals(reverse_and_not(500), 5500)
Test.assert_equals(reverse_and_not(321), 123321)
Test.assert_equals(reverse_and_not(564), 465564)
Test.assert_equals(reverse_and_not(66), 6666)
Test.assert_equals(reverse_and_not(553), 355553)
Test.assert_equals(reverse_and_not(518), 815518)
Test.assert_equals(reverse_and_not(152), 251152)
Test.assert_equals(reverse_and_not(273), 372273)
Test.assert_equals(reverse_and_not(603), 306603)
Test.assert_equals(reverse_and_not(864), 468864)
Test.assert_equals(reverse_and_not(170), 71170)
Test.assert_equals(reverse_and_not(96), 6996)
Test.assert_equals(reverse_and_not(869), 968869)
Test.assert_equals(reverse_and_not(960), 69960)
Test.assert_equals(reverse_and_not(471), 174471)
Test.assert_equals(reverse_and_not(925), 529925)
Test.assert_equals(reverse_and_not(235), 532235)
Test.assert_equals(reverse_and_not(389), 983389)
Test.assert_equals(reverse_and_not(293), 392293)
Test.assert_equals(reverse_and_not(586), 685586)
Test.assert_equals(reverse_and_not(218), 812218)
Test.assert_equals(reverse_and_not(262), 262262)
Test.assert_equals(reverse_and_not(610), 16610)
Test.assert_equals(reverse_and_not(75), 5775)
Test.assert_equals(reverse_and_not(699), 996699)
Test.assert_equals(reverse_and_not(298), 892298)
Test.assert_equals(reverse_and_not(532), 235532)
Test.assert_equals(reverse_and_not(211), 112211)
Test.assert_equals(reverse_and_not(602), 206602)
Test.assert_equals(reverse_and_not(804), 408804)
Test.assert_equals(reverse_and_not(195), 591195)
Test.assert_equals(reverse_and_not(271), 172271)
Test.assert_equals(reverse_and_not(449), 944449)
Test.assert_equals(reverse_and_not(938), 839938)
Test.assert_equals(reverse_and_not(257), 752257)
Test.assert_equals(reverse_and_not(205), 502205)
Test.assert_equals(reverse_and_not(345), 543345)
Test.assert_equals(reverse_and_not(365), 563365)
Test.assert_equals(reverse_and_not(112), 211112)
Test.assert_equals(reverse_and_not(792), 297792)
Test.assert_equals(reverse_and_not(777), 777777)
Test.assert_equals(reverse_and_not(759), 957759)
Test.assert_equals(reverse_and_not(239), 932239)
Test.assert_equals(reverse_and_not(469), 964469)
Test.assert_equals(reverse_and_not(953), 359953)
Test.assert_equals(reverse_and_not(574), 475574)
Test.assert_equals(reverse_and_not(155), 551155)
Test.assert_equals(reverse_and_not(238), 832238)


def variable_valid(var):
    if var[0].isdigit() or " " in var:
        return False
    else:
        return True
 

Test.assert_equals(variable_valid("result"), True)
Test.assert_equals(variable_valid("odd_nums"), True)
Test.assert_equals(variable_valid("2TimesN"), False)
Test.assert_equals(variable_valid("rather_long_variable_name"), True)
Test.assert_equals(variable_valid("count spaces"), False)
Test.assert_equals(variable_valid("nTimes2"), True)



def keyboard_mistakes(txt):
    return txt.replace("1", "I").replace("4", "A").replace("0", "O").replace("5", "S")


Test.assert_equals(keyboard_mistakes("MUB45H1R"), "MUBASHIR")
Test.assert_equals(keyboard_mistakes("DUBL1N"), "DUBLIN")
Test.assert_equals(keyboard_mistakes("51NG4P0RE"), "SINGAPORE")
Test.assert_equals(keyboard_mistakes("P4K15T4N"), "PAKISTAN")
Test.assert_equals(keyboard_mistakes("P4R15"), "PARIS")


def retrieve_major(semver):
    return semver.split(".")[0]
	

def retrieve_minor(semver):
    return semver.split(".")[1] 

def retrieve_patch(semver):
    return semver.split(".")[2]
	

Test.assert_equals(retrieve_major("6.1.9"), "6")
Test.assert_equals(retrieve_minor("6.1.9"), "1")
Test.assert_equals(retrieve_patch("6.1.9"), "9")
Test.assert_equals(retrieve_major("2.1.0"), "2")
Test.assert_equals(retrieve_minor("2.1.0"), "1")
Test.assert_equals(retrieve_patch("2.1.0"), "0")
Test.assert_equals(retrieve_major("5.12.13"), "5")
Test.assert_equals(retrieve_minor("5.12.13"), "12", 'should work with 2-digit version numbers')
Test.assert_equals(retrieve_patch("5.12.13"), "13", 'should work with 2-digit version numbers')





def sub_reddit(link):
    return link.split("/r/")[1].rsplit('/')[0]


Test.assert_equals(sub_reddit("https://www.reddit.com/r/relationships/"), "relationships")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/mildlyinteresting/"), "mildlyinteresting")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/funny/"), "funny")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/CrappyDesign/"), "CrappyDesign")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/confession/"), "confession")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/AskMen/"), "AskMen")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/comics/"), "comics")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/lifehacks/"), "lifehacks")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/wholesomememes/"), "wholesomememes")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/iamverysmart/"), "iamverysmart")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/starterpacks/"), "starterpacks")
Test.assert_equals(sub_reddit("https://www.reddit.com/r/awww/"), "awww")












Test.summary()

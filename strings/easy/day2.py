import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test


def relation_to_luke(name):
    family = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid"
    }
    return f"Luke, I am your {family.get(name, 'unknown')}."


Test.assert_equals(relation_to_luke("Darth Vader"), "Luke, I am your father.")
Test.assert_equals(relation_to_luke("Leia"), "Luke, I am your sister.")
Test.assert_equals(relation_to_luke("Han"), "Luke, I am your brother in law.")
Test.assert_equals(relation_to_luke("R2D2"), "Luke, I am your droid.")


def mood_today(mood="neutral"):
    return f"Today, I am feeling {mood}"


Test.assert_equals(mood_today("happy"), "Today, I am feeling happy")
Test.assert_equals(mood_today("sad"), "Today, I am feeling sad")
Test.assert_equals(mood_today("very happy"), "Today, I am feeling very happy")
Test.assert_equals(mood_today("rather empty inside"), "Today, I am feeling rather empty inside")
Test.assert_equals(mood_today("confused"), "Today, I am feeling confused")
Test.assert_equals(mood_today(), "Today, I am feeling neutral")


def count_vowels(txt):
    return sum(1 for c in txt.lower() if c in "aeiou")


Test.assert_equals(count_vowels("Celebration"), 5)
Test.assert_equals(count_vowels("Palm"), 1)
Test.assert_equals(count_vowels("Prediction"), 4)
Test.assert_equals(count_vowels("Suite"), 3)
Test.assert_equals(count_vowels("Quote"), 3)
Test.assert_equals(count_vowels("Portrait"), 3)
Test.assert_equals(count_vowels("Steam"), 2)
Test.assert_equals(count_vowels("Tape"), 2)
Test.assert_equals(count_vowels("Nightmare"), 3)
Test.assert_equals(count_vowels("Convention"), 4)


def correct_signs(txt):
    return eval(txt)

Test.assert_equals(correct_signs("3 < 7 < 11"), True)
Test.assert_equals(correct_signs("13 > 44 > 33 > 1"), False)
Test.assert_equals(correct_signs("1 < 2 < 6 < 9 > 3"), True)
Test.assert_equals(correct_signs("4 > 3 > 2 > 1"), True)
Test.assert_equals(correct_signs("5 < 7 > 1"), True)
Test.assert_equals(correct_signs("5 > 7 > 1"), False)
Test.assert_equals(correct_signs("9 < 9"), False)


def replace_vowels(txt, ch):
    return "".join(ch if c in "aeiou" else c for c in txt)



Test.assert_equals(replace_vowels("the aardvark", "#"), "th# ##rdv#rk")
Test.assert_equals(replace_vowels("minnie mouse", "?"), "m?nn?? m??s?")
Test.assert_equals(replace_vowels("shakespeare", "*"), "sh*k*sp**r*")
Test.assert_equals(replace_vowels("all is fair in love and war", "<"), "<ll <s f<<r <n l<v< <nd w<r")
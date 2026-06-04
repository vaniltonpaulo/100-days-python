import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test

def bool_to_string(flag):
    return str(flag)

print(bool_to_string(True))  # ➞ "True"
print(bool_to_string(False))  # ➞ "False"



def name_string(name):
	b = "Edabit"
	result = name + b
	return result


print(name_string("Mubashir"))  # ➞ "MubashirEdabit"

print(name_string("Matt"))  # ➞ "MattEdabit"

print(name_string("python"))  # ➞ "pythonEdabit"


def to_int(txt):
      return int(txt)
	

def to_str(num):
      return str(num)


print(to_int("77"))  # ➞ 77

print(to_int("532"))  # ➞ 532

print(to_str(77))  # ➞ "77"

print(to_str(532))  # ➞ "532"


def greeting(name):
    if name == "Mubashir":
        return "Hello, my Love!"
    return "Hello, " + name + "!"
	

print(greeting("Matt"))  # ➞ "Hello, Matt!"

print(greeting("Helen"))  # ➞ "Hello, Helen!"

print(greeting("Mubashir"))  # ➞ "Hello, my Love!"


def owofied(sentence):
     return sentence.replace('i','wi').replace("e","we") + " owo"



print(owofied("I'm gonna ride 'til I can't no more"))
# ➞ "I'm gonna rwidwe 'twil I can't no morwe owo"

print(owofied("Do you ever feel like a plastic bag"))
# ➞ "Do you wevwer fwewel lwikwe a plastwic bag owo"

print(owofied("Cause baby you're a firework"))
# ➞ "Causwe baby you'rwe a fwirwework owo"

print(owofied("Shine bright like a diamond"))


def is_identical(s):
     x = list(s)
     return x.count(x[0]) == len(x)


print(is_identical("aaaaaa"))  # ➞ True

print(is_identical("aabaaa"))  # ➞ False

print(is_identical("ccccca"))  # ➞ False

print(is_identical("kk"))  # ➞ True



def reverse_psychology(s):
     if s == "":
          return "Do not do anything."
     else:
          return "Do not " + s + "."
	


print(reverse_psychology("wash the dishes"))  # ➞ "Do not wash the dishes."

print(reverse_psychology("eat your lunch"))  # ➞ "Do not eat your lunch."

print(reverse_psychology("go to school"))  # ➞ "Do not go to school."

print(reverse_psychology(""))  # ➞ "Do not do anything."



def match(s1, s2):
     return s1.lower() == s2.lower()



print(match("hello", "hELLo"))  # ➞ True

print(match("motive", "emotive"))  # ➞ False

print(match("venom", "VENOM"))  # ➞ True

print(match("mask", "mAskinG"))  # ➞ False



def modify_last(txt, n):
     return txt[:-1] + txt[-1]  * n


print(modify_last("Hello", 3))  # ➞ "Hellooo"

print(modify_last("hey", 6))  # ➞ "heyyyyyy"

print(modify_last("excuse me what?", 5))  # ➞ "excuse me what?????"


def is_it_true(relation): 
    y = relation.replace("=", "==")     
    return eval(y)

print(is_it_true("2=2"))  # ➞ True

print(is_it_true("8<7"))  # ➞ False

print(is_it_true("5=13"))  # ➞ False

print(is_it_true("15>4"))  # ➞ True


def how_many_times(num):
     return "Eda" + "a" * num + "bit"


print(how_many_times(5))  # ➞ "Edaaaaabit"

print(how_many_times(0))  # ➞ "Edbit"

print(how_many_times(12))  # ➞ "Edaaaaaaaaaaaabit"


def has_spaces(txt):
     return " " in txt


print(has_spaces("hello"))  # ➞ False

print(has_spaces("hello, world"))  # ➞ True

print(has_spaces(" "))  # ➞ True

print(has_spaces(""))  # ➞ False

print(has_spaces(",./!@#"))  # ➞ False



def create_id(firstname, lastname):
     return firstname[0].lower() + lastname[0].upper() +lastname[1:3].lower()



print(create_id("mary", "lamb")) # ➞ "mLam"

print(create_id("John", "SMITH")) # ➞ "jSmi"

print(create_id("mary", "smith")) # ➞ "mSmi"

print(create_id("mary","smith")) # ➞ "mSmi"

print(create_id("S","WORKING")) # ➞ "sWor" 

print(create_id("joHN","wAShington")) # ➞ "jWas"   


def check_title(txt):
     return txt.istitle()
     
     


print(check_title("A Mind Boggling Achievement"))  # ➞ True

print(check_title("A Simple Python Program!"))  # ➞ True

print(check_title("Water is transparent"))  # ➞ False
print(check_title("We Love to relax"))  # ➞ False
print(check_title("I want To eat bread"))  # ➞ False



def count_claps(txt):
     return txt.count("C")



Test.assert_equals(count_claps("ClaClaClaClap!"), 4)
Test.assert_equals(count_claps("ClClClaClaClaClap!"), 6)
Test.assert_equals(count_claps("CCClaClClap!Clap!ClClClap!"), 9)
Test.assert_equals(count_claps("ClCCClaClaClaClCClap!CClaClap!Clap!ClClClClaClaClap!Clap!ClClCClap!Clap!ClClap!ClaCClClap!ClClap!Clap!CClClaClaClaCClaCClaClClaCCCClaClap!Clap!ClaClaClap!ClaClap!CClap!Clap!ClClap!"), 61)
Test.assert_equals(count_claps("Clap!ClClaClap!ClaClap!CClap!ClClClap!CClaClap!CClap!ClClap!ClaClaClClap!ClaClap!ClClCClaClaCClaCCCCClClCClap!ClaCClaClCClap!Clap!ClaClaClaCClaClap!"), 52)
Test.assert_equals(count_claps("Clap!CClaClClap!ClCClCCClaCClap!ClCCClCClClap!ClClClap!CClap!CClCClap!ClCClap!Clap!Clap!Clap!ClClap!Clap!CClaClClap!ClaClaClaClCClClaClClap!ClaClClaClap!ClaClap!CClClClap!ClClaClClap!Clap!ClaClaClaClaClClap!CClaClClaCClap!ClClClClClap!Clap!CClClap!ClClap!ClaClap!CClClaClaClap!Clap!"), 97)
Test.assert_equals(count_claps("CClCClaCClap!Clap!ClaClap!ClCCClap!ClClClClap!ClaClCClClaClap!"), 23)
Test.assert_equals(count_claps("Clap!Clap!ClClCClCClClaClaClaCClaClClaClClClClap!CClap!ClClap!ClClClaClaClClaClaClaClaCClClaClap!"), 36)
Test.assert_equals(count_claps("ClaCCClClCClClaCClCClap!ClaClClaClap!Clap!ClClClClap!Clap!CClap!CClaClClaClCClaClap!ClaClaClaClap!Clap!ClClap!CCClap!ClClaClap!CClClClap!CClaClaClClaClap!ClClap!ClaCClaClap!Clap!Clap!Clap!CClaCCCClap!ClaClap!ClClap!Clap!CClaClaClaClap!CClaCClap!Clap!CClaCClaClaCClaCClap!"), 94)
Test.assert_equals(count_claps("CClClap!Clap!CClCClClaCClaClaClap!ClaClaClaCCCClap!CCClClap!Clap!ClaClaClap!ClClClap!ClCCClap!ClaClaClap!CClap!ClaClap!CClClClap!CClap!CClClaCClClap!ClaClap!ClaClClClCClap!ClaClClap!ClaClaCClap!CClClaClClap!ClaClaClClaClClaClaClap!"), 82)
Test.assert_equals(count_claps("ClaCCClCClaClClaClCClaClaClap!Clap!CClaClap!ClaClap!Clap!ClaClap!Clap!"), 23)
Test.assert_equals(count_claps("CClClaClClaClClap!Clap!Clap!ClClaClap!ClClClClaClap!CClap!ClaClaCCClap!ClClap!CClap!Clap!Clap!ClaClaClap!ClaClClClaClaClap!ClaClaClap!ClClCClaClaCClClaClap!Clap!Clap!CClClaClaClaClaClCClClaClaCClaClap!ClCClClClap!Clap!Clap!Clap!Clap!CClaClap!Clap!CCClaClCClClaClClClaClaClaClaCClap!Clap!"), 96)
Test.assert_equals(count_claps("Clap!ClaClCClaClap!ClCClap!ClClClaClap!ClaClaCClap!ClaClaClap!ClaCClap!Clap!CClClClap!ClClCClaCClCClaCClClClClaClap!ClClaCClap!CCCClap!Clap!ClClap!ClaCClaCClClap!ClClaClap!ClClaClaClaClaCCClClap!CClaClaClap!Clap!ClClap!"), 78)
Test.assert_equals(count_claps("Clap!ClaClCClaClaClap!CClaClap!CCClCClap!Clap!Clap!Clap!ClClap!Clap!ClaClaClClap!Clap!ClaClaClap!CClaClap!CCClClap!ClaClaClap!ClClaClaClaClaClap!CClap!ClaClCClaClap!CClClCClaClap!Clap!CClaCClap!"), 63)
Test.assert_equals(count_claps("Clap!CClaClap!ClClap!ClClClap!ClaCClap!ClaCClClap!CClap!CClClaClap!ClaClaClCCClap!Clap!CClClaClCClaClaClClap!Clap!CClaCClaCClap!ClaCClClCClap!CClap!CClap!ClaClaClaClaClap!ClClap!CClaClaClaClClaClClCClClCClClaClaCClClap!"), 80)
Test.assert_equals(count_claps("CClaCClClap!Clap!Clap!Clap!Clap!Clap!Clap!ClClClap!CClap!CClap!CCClaClClClClClaCClaClap!ClClap!CClaClap!Clap!CCClaClap!Clap!CClClClaClaClaClap!ClaCClap!ClClaClaCClClap!CClap!ClaClap!"), 60)
Test.assert_equals(count_claps("ClaCCClap!"), 4)
Test.assert_equals(count_claps("ClaClap!ClaClaClap!Clap!"), 6)
Test.assert_equals(count_claps("CClap!ClaClaClClap!Clap!ClaCCClap!ClClaClap!CClap!CClap!ClaClClaCClaClap!ClaClap!ClaClClaClaCCClClaClaClap!Clap!"), 37)
Test.assert_equals(count_claps("ClClaCClap!ClaCClaClap!Clap!Clap!ClaClClap!ClClaClaClClaClaClaCCClClClClClap!"), 27)
Test.assert_equals(count_claps("ClClClCClClap!Clap!CCCClap!ClCCClClap!CCClap!Clap!Clap!CClap!ClaClaCClaCClaClaClaClClap!ClaClCCClClaClap!ClClaClaCClCCClClClap!Clap!ClaClap!ClaClaCClap!ClCCClaClap!ClaClap!CClap!CClaClClaClCClaClap!CClClap!ClClap!Clap!CClap!CClaClaClClaClap!"), 88)
Test.assert_equals(count_claps("ClClCClClClaClClCClap!ClCClap!ClaClaClClap!ClaCClClap!ClClaClap!ClaClaClaClap!Clap!Clap!CCCClaClaClaClaClaCClCClaClaClap!Clap!CCCClap!ClaClap!CCClaClaClaClap!ClClClap!CClCCCClap!Clap!CClClClaClap!ClClaCClClap!ClaClClap!ClaClap!ClCClaClaCClap!"), 88)
Test.assert_equals(count_claps("ClClap!Clap!CCClClClaClClClClap!Clap!CClap!ClClap!ClClaCCClap!"), 22)
Test.assert_equals(count_claps("ClaClaClClClaCClap!ClaClaCCClaClaClClap!CClCClCClClClClap!ClaClap!Clap!ClaCCClap!ClCCClaClClClaCCClaClCClClaClap!ClClaClClaClap!ClClap!Clap!ClaClaClClap!"), 58)
Test.assert_equals(count_claps("ClaCClClClClaClClap!ClClap!CCClaCCClClCCClaClap!Clap!CClClClap!ClaCClClaCClaCClClap!ClClClClaCClaClap!Clap!"), 43)
Test.assert_equals(count_claps("ClaClCClClCClCClaCCClap!ClaClaCClap!ClaClap!CClaClaClClaCClClaClaClCCClaClap!ClClap!Clap!Clap!ClaCCClap!ClClaClaClap!ClaClap!CCClap!CClap!CClClap!"), 54)
Test.assert_equals(count_claps("Clap!ClaCCCCCClClaCCCClaClaClClap!CClaCClaCClap!CClap!CClCClClap!CCCCClaClap!"), 35)
Test.assert_equals(count_claps("ClClaClap!Clap!ClCClaClaCClaCClaClap!CCClaCClaClClap!Clap!ClCCCClaClaClap!Clap!ClaClap!ClaClClap!ClCClCClaClClap!CClaClap!ClClClaCClaCClap!Clap!ClCClCClap!ClaCCClClap!Clap!Clap!CClaClaClap!ClaCClaCClap!"), 73)
Test.assert_equals(count_claps("CClaClClaClap!ClClClaCClaClaCClCClCClaClaCClaClap!CCCCClap!ClaCClClaClClap!ClClClap!ClCClaClCClClClap!CClap!ClaClClap!ClCClap!"), 51)
Test.assert_equals(count_claps("ClaClaClaCClClap!ClaClap!Clap!ClCCCClaClap!Clap!CCClClClaClaCClClap!CClClaClClap!ClCCClaClClap!Clap!CClaCCCClClap!"), 44)
Test.assert_equals(count_claps("CClClap!ClClCClaClClaClaClap!ClaCClClaClaClaClaClap!ClClaClap!Clap!CClap!CClaClClap!ClClap!CClaClClap!ClaCCClap!CCClaClaClClClaClaClClap!CCClClaClClClClap!ClClap!ClaClClClap!Clap!CClaClaClaCClap!Clap!Clap!ClaClClClap!CClaClaClaClaClaCClClClaClap!ClClap!ClClaCClaClaCClClap!Clap!"), 98)
Test.assert_equals(count_claps("ClaCClaClap!CClap!ClClaClClaClaClaClCClaCClap!"), 17)
Test.assert_equals(count_claps("ClaClClap!"), 3)
Test.assert_equals(count_claps("ClClaClap!CClaCClClap!"), 8)
Test.assert_equals(count_claps("ClCClaClaClap!Clap!ClaCCClap!CClCClaClClap!CClClap!ClClCCCCClaCClClClaClClCClaClap!Clap!"), 36)
Test.assert_equals(count_claps("Clap!CClaCCCClClaClaClaClap!ClClaClClap!"), 15)
Test.assert_equals(count_claps("CClap!ClCCCCClClaClap!ClClClap!CClap!ClaClaClaClCCClCCClaClClap!Clap!CClaClClCClap!ClaClClap!ClCClaClaClap!"), 42)
Test.assert_equals(count_claps("Clap!ClaCClap!CCCCClaClap!ClClaCClClap!ClaClClap!ClaClClaClaClaClCCCClaClaCClap!Clap!ClaCCClap!ClClap!ClClap!ClClap!CClClClClap!Clap!CClaCClClClap!ClaCClClaCCClClap!CCClap!"), 65)
Test.assert_equals(count_claps("Clap!ClCClClap!CCClap!ClClap!ClClaClaClap!ClCClClClaClClap!ClCClap!Clap!Clap!ClCClap!ClCCClCClap!Clap!ClClCClCClap!ClCClaClaClCClap!"), 49)
Test.assert_equals(count_claps("ClCClap!ClaClap!CCClClCCClaClClCClaClClap!CClap!CClaClCClClap!ClClap!"), 28)
Test.assert_equals(count_claps("Clap!ClaClaCClap!"), 5)
Test.assert_equals(count_claps("ClClap!ClClap!ClaCCClap!ClClCClaClaClCClap!Clap!Clap!ClClaCClClaClap!Clap!ClClClClap!ClCCCClaClClap!Clap!ClClClap!ClaCClap!CClaClap!Clap!ClClClaClClClClaClaClClaClaClClClaCCClap!ClaClap!Clap!ClClClap!Clap!Clap!"), 72)
Test.assert_equals(count_claps("CClaCClCCClClClap!ClClaCCClap!Clap!Clap!ClClCClClClClaClaCClap!ClClClap!CClap!ClaClClaCCClClaClClap!CClCCCClaClaClCCClap!CClap!Clap!ClaClaClClaClClClaClaCClClap!Clap!CCClaClap!CClClaCClap!ClClClap!Clap!ClaClaClClClClap!Clap!ClaClap!"), 88)
Test.assert_equals(count_claps("CClClaCClaClClClaClaClap!Clap!ClaClaCClClaClaCClCClap!"), 21)
Test.assert_equals(count_claps("CClap!ClaClap!ClClap!CClaClClaClClap!CCClap!CClCCClap!CClap!Clap!ClClap!ClClap!Clap!ClClap!ClClClaClaCClaClaClCClap!ClaClap!CClap!ClaCClClap!Clap!Clap!Clap!ClClap!ClClClaCCClClap!ClaCCClaClCCClaClap!"), 69)
Test.assert_equals(count_claps("CClClap!Clap!ClCCClaClClCClClap!ClClClaCCClClaClaCClap!ClClap!Clap!ClClaClClClaCClaClClClaClClClaCClaClCClap!ClCCClClCClap!CCClClap!CClaClClap!ClCClClaClaClaClap!Clap!CClClap!ClaCClaClClClCClap!ClaClClClaClaCClaClap!"), 86)
Test.assert_equals(count_claps("Clap!Clap!ClClap!Clap!CClClaClaCClCClClap!ClClaCClClClCClaClClClaClClCClaCClClClap!ClaClap!ClClaClCCClaClaClaCCClaClap!"), 47)
Test.assert_equals(count_claps("ClaClaClClClap!Clap!ClClClClap!"), 10)
Test.assert_equals(count_claps("ClaClap!CClap!ClClClClap!CClaClClClap!CCClaClaClap!ClaClap!CClaCClClClaClap!ClClClClCClaCClap!ClClap!Clap!"), 38)
Test.assert_equals(count_claps("CCClaClClClClap!Clap!ClCCClClClaClCClCCClClap!"), 21)
Test.assert_equals(count_claps("ClClap!"), 2)
Test.assert_equals(count_claps("Clap!CCClClClaClap!ClaCClClap!CClClaClClaClap!Clap!ClaClap!"), 20)
Test.assert_equals(count_claps("ClaClap!CClaClaClap!CClClClap!ClCClap!Clap!Clap!"), 15)
Test.assert_equals(count_claps("ClaCClap!ClClap!ClaCClClaClap!Clap!Clap!"), 12)
Test.assert_equals(count_claps("ClClap!ClaClaCCClaClCClap!CClap!ClaClClaClap!CClClap!ClClap!ClaCClaCClaClaClCClaClaClaClClap!ClClap!CClaClap!Clap!CClap!ClCClap!ClaClaClap!ClaClap!ClClClCCClClaCCClaClClaClClClClaClClaClClap!ClaClap!CCClCClaCClClap!ClaClaClap!"), 83)
Test.assert_equals(count_claps("ClCClCClap!Clap!ClaClaClap!ClaCClClClap!ClaClaClaClap!ClClaClap!ClCCCClaCCClaClap!CClap!ClClap!ClaClap!CCCCClaClap!Clap!"), 43)
Test.assert_equals(count_claps("Clap!ClClClCClap!ClClap!ClClap!ClaClaClap!CClap!"), 15)
Test.assert_equals(count_claps("ClaClClap!ClCClaCClap!ClClap!CClaClap!CClClaCClaClap!CClaClaClaCCCCClap!CClaClaClClaClClap!ClClap!ClCClap!Clap!ClClap!CClClaClClap!CClaCClap!CClClap!ClaCClap!Clap!ClaClap!Clap!Clap!ClaClClap!Clap!Clap!ClClaClaClap!CClaClCClap!ClClClClaClaCClaClClClClap!"), 88)
Test.assert_equals(count_claps("ClClCClap!ClaClClaCCClaClaCClaClap!CClaClap!ClaCClClaClaClClap!ClaClaClClap!ClClCClaCClClap!"), 35)
Test.assert_equals(count_claps("ClaClClClap!Clap!ClClaClClaClaCClClaClap!ClaClClClaClClaClClaClClClaClCClaClap!CCCClap!Clap!CClap!Clap!ClaClap!CClap!ClClap!CClClClaClap!ClClCClaClClap!ClaClClaClaClCClClClap!ClClaClap!Clap!ClaCClClClaCClap!Clap!ClClaClClClClaClClap!ClClap!"), 85)
Test.assert_equals(count_claps("CClaClaClaClap!Clap!Clap!"), 7)
Test.assert_equals(count_claps("Clap!ClClClaClaClCClap!"), 8)
Test.assert_equals(count_claps("ClClap!Clap!Clap!CClCClap!Clap!Clap!CClClaCClap!ClaClap!Clap!ClClaClClCClap!"), 24)
Test.assert_equals(count_claps("ClCClap!ClaClaClap!CClap!Clap!ClaClap!ClaClClap!Clap!ClClaClap!ClClClaClaClaClaClaClaClap!"), 27)
Test.assert_equals(count_claps("CClap!ClaClClap!ClCClap!CClaCClClaClClap!CClap!CCCClClaClClap!CCClaClaClap!CCClap!Clap!Clap!Clap!ClClaCCCClaClClap!ClaClap!ClaClClaClap!Clap!ClaCClap!Clap!ClClClap!Clap!ClClaCClClaClap!Clap!Clap!ClCCClClap!Clap!ClCClCCClaClap!ClaCCClClClCCClClClaClaClap!Clap!ClaClaCClaClap!"), 98)
Test.assert_equals(count_claps("Clap!ClClClaCClap!CClap!ClaCClaClCClap!Clap!CClaCClCCClClClap!ClaClaCCCClClaCClaClClap!CClCClClap!Clap!CCClaClaClClaClaClap!Clap!ClCClaClaClClClap!Clap!ClaClClap!ClClClap!ClaClap!CCClap!ClaClap!ClClap!Clap!ClaClap!ClClClap!Clap!Clap!ClaCCClap!CClap!ClClaCClaClaClap!ClaCClap!ClaClCCClap!"), 101)
Test.assert_equals(count_claps("CCCCClClClap!ClaCClClClClaClClClaClClaClaClCCClap!ClClaCClap!CClap!Clap!ClaClap!Clap!Clap!"), 34)
Test.assert_equals(count_claps("ClClap!ClCClap!CClaClap!ClCClaCCClap!ClClap!CClap!CCClaClap!Clap!CClaClap!Clap!ClaClaClap!ClaClClClClaClCCCClap!CClap!CClap!CClaClClClClaClaClClClCClCClap!ClaCCClClClCCClClap!CClClap!Clap!ClaCClap!ClaClaCClaClap!ClaClaClap!"), 83)
Test.assert_equals(count_claps("Clap!Clap!Clap!ClClClCClClClap!Clap!Clap!ClClClClaClap!ClClClaClap!ClaClap!ClCClap!Clap!ClCClaCClClaClCCClClaCClCClCClaClap!Clap!CClaClap!ClClap!Clap!CCClap!CClaCClClClClap!ClClap!Clap!ClaClaClaCClap!ClClClap!Clap!Clap!"), 75)
Test.assert_equals(count_claps("Clap!ClaCClaClClap!ClCClaClClClap!ClClap!Clap!Clap!CClap!ClaClCClaClCClap!Clap!ClaClaClaClaClaClClap!CClCCClaCClap!ClaCClClaCCClClap!CClClCClaClap!ClaClCClCClap!ClaClCClClClap!ClClaClap!ClClap!ClCClaClClaCClaClaClClCClap!Clap!CClap!"), 86)
Test.assert_equals(count_claps("ClaCClap!ClClaCCClap!Clap!ClaClap!"), 11)
Test.assert_equals(count_claps("Clap!ClaClap!ClaClap!ClCClaClap!Clap!CCClaClaClap!ClaClaClap!ClClaCClClaCClaClClap!ClClClap!ClCClClCClap!Clap!"), 37)
Test.assert_equals(count_claps("ClClaClClaClaCClClap!ClaClaClaCClap!CCClClap!ClClaCClClaClaClaClap!ClaCCClaClaClap!ClaCClaClap!"), 35)
Test.assert_equals(count_claps("ClClaClClap!ClClaClap!Clap!ClaClClClap!ClaClap!ClaCCClap!Clap!ClClap!ClClaCClClCClClClaClap!ClClClCClaClap!CClap!ClClClap!ClCCClap!Clap!CClClCClaCClCClaClClap!CClaCCClap!CCClaClClap!ClaClClap!Clap!ClaClClap!ClaClaClap!Clap!ClaClap!ClClCClaCClaClClap!"), 89)
Test.assert_equals(count_claps("ClaClaClClap!ClaClCCClaClaCClap!CClCClap!Clap!"), 17)
Test.assert_equals(count_claps("CCClaCClap!ClClaClaClaClaClaClaCClaClap!Clap!CClClap!CClClaClap!Clap!ClClClaClaCClaCClaClClap!ClClClap!CClaClaClaClap!Clap!ClClap!Clap!ClaCClClClap!ClaClaClap!CCClClap!Clap!ClCCClClaClClCClap!ClaClap!"), 70)
Test.assert_equals(count_claps("ClCClaClap!ClClClClap!ClaClaCClaClClClap!CClCClCClClap!CClCClClClClaClCClap!CClaCCCCCClClap!ClaClaClaClClaClaClClaCClClap!Clap!CCClaClClaClap!ClCClap!CClClap!Clap!ClaClClap!CClaClaClap!CClClaClap!Clap!"), 78)
Test.assert_equals(count_claps("Clap!ClaClClCClaClCClaClClaClap!Clap!"), 13)
Test.assert_equals(count_claps("CClClap!Clap!CClaClap!ClaClap!ClCCClaClClap!ClaCClClaCClap!ClaClClClap!CClap!Clap!"), 28)
Test.assert_equals(count_claps("ClClaClap!CCClClClaCCClCClClap!ClaClCClaClClap!ClaClap!ClClaCClClaClaClaCClClaClap!ClClaClap!Clap!CCClClaClap!Clap!CClClClClClaClClCClClaCClap!Clap!ClaClaClCClap!Clap!ClaClaClClap!CClaCClaCClaClClaClap!CClap!ClCClap!CClCClaClaClClaClaClap!Clap!Clap!ClClaClap!Clap!"), 96)
Test.assert_equals(count_claps("ClaClap!ClaClCClClClClap!Clap!CClaClap!Clap!CCClaClaCClaCCCCClaClaClaCClClClaClap!ClClap!CClaCClClClap!ClaClCCCClap!ClClClaClClaClClap!"), 53)
Test.assert_equals(count_claps("ClClap!CClap!Clap!CClaCClClaCClClCClap!"), 15)
Test.assert_equals(count_claps("CClCClap!ClClap!ClCClaClap!Clap!CClaClaClaClClClap!"), 18)
Test.assert_equals(count_claps("ClaClCClaCClaClaClClaClClaClap!ClaCCClClaClap!Clap!CClap!ClCClap!CClClClap!ClClap!CClClap!"), 33)
Test.assert_equals(count_claps("ClaClap!ClClClap!ClClaClaCCCClaClClap!Clap!ClaClaClap!ClClap!Clap!CClap!Clap!CClClClap!ClaClCClap!Clap!ClClap!ClaCClap!Clap!"), 39)
Test.assert_equals(count_claps("ClClap!CCClap!ClClaClaCClCCClap!ClCCCClaClClaClap!ClClClaClClClaCCClaClap!Clap!Clap!ClCClaClaClap!ClaClCCClClClaClClClap!Clap!Clap!ClaCClap!ClClCClaClap!Clap!CClaClap!Clap!"), 63)
Test.assert_equals(count_claps("ClaClClCClClClap!ClaClaClap!Clap!ClClap!ClCClap!ClClap!ClaClap!ClaCClaClap!CClaClap!ClaClClaClaClap!ClClaClap!ClaCClap!CClClaCClap!Clap!CCClClCCCClClClClaCClClap!"), 58)
Test.assert_equals(count_claps("ClaClap!ClaClClap!ClCClClClaCClap!ClCClaClaClaClaClaCClap!ClClap!Clap!ClClaClCClap!ClaCClaClap!Clap!Clap!CClaCClClap!Clap!CClaClap!ClClClClaClap!ClaClap!"), 51)
Test.assert_equals(count_claps("ClCClCClCClClap!ClaClap!ClClaCCClCClaClaClap!CCClaClClap!ClClap!ClaClap!CClap!Clap!ClaClClaClap!Clap!ClClCClaClClClaClaClaClap!"), 46)
Test.assert_equals(count_claps("CClClClap!CCClap!CClap!Clap!CClClap!CCClaClClaCClap!ClaCClClCClap!Clap!CClap!ClaCClaClaClaClap!"), 35)
Test.assert_equals(count_claps("ClaCClaClap!CClCCClap!ClClap!CClap!Clap!ClCClCCCClCClap!ClaClClCCClaClap!"), 30)
Test.assert_equals(count_claps("CClaClClap!CClClClap!ClaClap!CClClClClaClaCCClaClaClap!Clap!Clap!ClaCClap!ClClCClap!ClaClClCCCClap!ClaClap!Clap!CCCCClaClap!CClap!Clap!ClaClClap!ClaClClaClClClap!Clap!"), 59)
Test.assert_equals(count_claps("ClClap!ClClaCClaCClap!CCCClap!Clap!ClClClap!Clap!Clap!ClCCClaClClCCClap!ClClap!CCClClap!ClaClap!ClaClap!ClCClap!Clap!ClaClCClClCClap!ClaCClCClap!Clap!Clap!ClClClClap!ClaCClaClaClCClClaClap!CClap!CCCCClaClap!ClaClap!"), 78)
Test.assert_equals(count_claps("ClClaClap!ClaClaClap!Clap!Clap!Clap!ClaClaClap!ClaCClaClap!ClClClap!Clap!CClaClap!CClClaClClCClap!ClaClap!ClClaClap!ClCCClaClCClap!ClCClClaClap!ClClaClap!Clap!Clap!Clap!ClCClap!ClClClaClap!Clap!Clap!ClaCClaClClaClCClClap!ClClCCClCClaClCClCCClClaClaClaClap!CClClClap!"), 92)
Test.assert_equals(count_claps("CClClap!ClClap!ClaClap!ClaCCCClaClaCClap!CClap!CClClaClap!CClap!ClClClaClClaClap!CClClaCClap!ClClaCClClaClap!CClap!CClClap!CClap!Clap!Clap!ClClClap!ClClaClap!CCClap!CCClCClCClCClaClaClClaClaClap!"), 72)
Test.assert_equals(count_claps("CCClaClap!CClaClClaClaCClaClClap!ClaCClCClaCClClClaClaCClaCCCClClap!ClaClaClaCClap!ClaClClaClClap!Clap!CClaCClap!CClClap!Clap!ClaCCClCClClap!ClaClaClaCCClaClaClaClCCClaClCClClap!"), 72)
Test.assert_equals(count_claps("ClCClap!ClaClaClCClap!CClap!Clap!ClClCCClClap!CCCClClClaClap!Clap!Clap!ClClaClClaClap!ClCCClaClap!CClClaCCClap!Clap!Clap!CClClaClap!Clap!ClaClCClap!ClCCClap!ClaClap!CCClaClap!CCClaClap!CClaClClaClaClaClap!Clap!CClap!Clap!Clap!Clap!ClClap!"), 82)
Test.assert_equals(count_claps("CClCCCCClap!CClap!Clap!CClap!ClaClaCCCClaClap!Clap!Clap!ClClap!CClaClaClaClaCClap!CClap!ClaCCClClaClClCCClaClaClCClaCCClap!"), 49)
Test.assert_equals(count_claps("ClClaClap!ClaCClaClaClap!Clap!CClClaClap!ClaClap!ClaClClaClaClap!ClaCClCCClaClaCClCClClap!ClCClap!ClClaClaClCClaClap!ClaClClaCCClap!ClaClap!ClClaClap!CClCClap!ClaClap!ClaClCClaClaCClap!ClClClap!Clap!CClClap!Clap!ClClaCClaCClaClap!Clap!CCClaClaClClap!Clap!ClCClClaClaClaClClClCClap!"), 100)
Test.assert_equals(count_claps("ClClap!ClCClClClap!CCClaCCCClaClCClClaClClClaClap!ClaClap!ClCClClap!ClaClap!ClaClClClap!ClCClaCClClap!ClClClClap!ClaClClaClap!ClClClaCClaClClaCClap!CClClap!ClaClap!Clap!ClaCClap!ClaClClap!CClClClaClCClaClaClaCClap!ClaClap!CClap!"), 84)
Test.assert_equals(count_claps("ClaClCClap!Clap!ClaClaClaClap!ClaClap!CClClap!ClaClCClaClClCCClClClClaClap!Clap!CClap!Clap!ClaCClaClClaCClap!ClClCCClaClClaClaCCClClap!Clap!CClaClap!CClap!ClClClap!ClaClaCClaCClClaClaClClaCClClap!ClCCClClap!ClCClap!CClaClaClap!Clap!ClaClap!ClCClaClap!Clap!"), 92)
Test.assert_equals(count_claps("ClCClap!Clap!Clap!ClaCClap!Clap!ClaClaClaClap!Clap!ClaClClap!"), 17)
Test.assert_equals(count_claps("ClClap!CClap!ClClaClaClClClClaClaClap!CCClaClaClaClap!ClClaClap!Clap!ClCClaCClap!ClClaCClaClap!Clap!ClaClaClap!ClaClap!CClap!ClCClap!ClClap!ClaClaClaClaClaClap!CClClClaCClap!CClaCCClaCClap!Clap!CCCClap!ClClClaCClap!Clap!ClaClClap!ClaClCClClap!"), 84)
Test.summary()



def repeat_string(txt, n):
    if isinstance(txt,str):
        return txt * n
    else:
         return "Not A String !!"
    

Test.assert_equals(repeat_string("Mubashir", 2), "MubashirMubashir")
Test.assert_equals(repeat_string("Matt", 3), "MattMattMatt")
Test.assert_equals(repeat_string(1990, 7), "Not A String !!")
Test.assert_equals(repeat_string("*", 3), "***")
Test.assert_equals(repeat_string("Hello", 11), "HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello")
Test.assert_equals(repeat_string("243624", 22), "243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624")
Test.assert_equals(repeat_string([], 3), "Not A String !!")
Test.assert_equals(repeat_string({}, 3), "Not A String !!")
Test.assert_equals(repeat_string(24, 3), "Not A String !!")
Test.assert_equals(repeat_string(True, 3), "Not A String !!")
Test.assert_equals(repeat_string("Hello", 0), "")
# Mubashir
Test.summary()




def potatoes(potato):
    return potato.count("potato")


Test.assert_equals(potatoes("potato"), 1)
Test.assert_equals(potatoes("potatopotatocherry"),2 )
Test.assert_equals(potatoes("potatopotatopotatoorange"), 3)
Test.assert_equals(potatoes("potatopotatobananapotatopotato"), 4)
Test.assert_equals(potatoes("potatopotatomangopotatopotatopotato"), 5)
Test.assert_equals(potatoes("potatocucumberpotatopotatopotatopotatopotato"), 6)
Test.summary()



import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test


def is_empty(s):
    return not s


Test.assert_equals(is_empty(""), True)
Test.assert_equals(is_empty(" "), False)
Test.assert_equals(is_empty("            "), False)
Test.assert_equals(is_empty("38215"), False)
Test.assert_equals(is_empty("afjabsdf"), False)
Test.assert_equals(is_empty("!?@&"), False)


def repetition(txt, n):
    return txt * n



Test.assert_equals(repetition("soccer", 2), "soccersoccer")
Test.assert_equals(repetition("ab", 3), "ababab")
Test.assert_equals(repetition("bonita", 1), "bonita")
Test.assert_equals(repetition("ciao", 4), "ciaociaociaociao")
Test.assert_equals(repetition("amigo", 5), "amigoamigoamigoamigoamigo")
Test.assert_equals(repetition("torque", 2), "torquetorque")


def first_last(name):
    return name[0] + name[-1]


Test.assert_equals(first_last("ganesh"), "gh")
Test.assert_equals(first_last("kali"), "ki")
Test.assert_equals(first_last("shiva"), "sa")
Test.assert_equals(first_last("vishnu"), "vu")
Test.assert_equals(first_last("durga"), "da")
Test.assert_equals(first_last("brahma"), "ba")

def num_to_dashes(num):
    return "-" * num


Test.assert_equals(num_to_dashes(1),"-")
Test.assert_equals(num_to_dashes(2),"--")
Test.assert_equals(num_to_dashes(3),"---")
Test.assert_equals(num_to_dashes(4),"----")
Test.assert_equals(num_to_dashes(5),"-----")
Test.assert_equals(num_to_dashes(6),"------")
Test.assert_equals(num_to_dashes(7),"-------")
Test.assert_equals(num_to_dashes(8),"--------")
Test.assert_equals(num_to_dashes(9),"---------")
Test.assert_equals(num_to_dashes(10),"----------")
Test.assert_equals(num_to_dashes(11),"-----------")
Test.assert_equals(num_to_dashes(12),"------------")
Test.assert_equals(num_to_dashes(13),"-------------")
Test.assert_equals(num_to_dashes(14),"--------------")
Test.assert_equals(num_to_dashes(15),"---------------")
Test.assert_equals(num_to_dashes(16),"----------------")
Test.assert_equals(num_to_dashes(17),"-----------------")
Test.assert_equals(num_to_dashes(18),"------------------")
Test.assert_equals(num_to_dashes(19),"-------------------")
Test.assert_equals(num_to_dashes(20),"--------------------")
Test.assert_equals(num_to_dashes(21),"---------------------")
Test.assert_equals(num_to_dashes(22),"----------------------")
Test.assert_equals(num_to_dashes(23),"-----------------------")
Test.assert_equals(num_to_dashes(24),"------------------------")
Test.assert_equals(num_to_dashes(25),"-------------------------")
Test.assert_equals(num_to_dashes(26),"--------------------------")
Test.assert_equals(num_to_dashes(27),"---------------------------")
Test.assert_equals(num_to_dashes(28),"----------------------------")
Test.assert_equals(num_to_dashes(29),"-----------------------------")
Test.assert_equals(num_to_dashes(30),"------------------------------")
Test.assert_equals(num_to_dashes(31),"-------------------------------")
Test.assert_equals(num_to_dashes(32),"--------------------------------")
Test.assert_equals(num_to_dashes(33),"---------------------------------")
Test.assert_equals(num_to_dashes(34),"----------------------------------")
Test.assert_equals(num_to_dashes(35),"-----------------------------------")
Test.assert_equals(num_to_dashes(36),"------------------------------------")
Test.assert_equals(num_to_dashes(37),"-------------------------------------")
Test.assert_equals(num_to_dashes(38),"--------------------------------------")
Test.assert_equals(num_to_dashes(39),"---------------------------------------")
Test.assert_equals(num_to_dashes(40),"----------------------------------------")
Test.assert_equals(num_to_dashes(41),"-----------------------------------------")
Test.assert_equals(num_to_dashes(42),"------------------------------------------")
Test.assert_equals(num_to_dashes(43),"-------------------------------------------")
Test.assert_equals(num_to_dashes(44),"--------------------------------------------")
Test.assert_equals(num_to_dashes(45),"---------------------------------------------")
Test.assert_equals(num_to_dashes(46),"----------------------------------------------")
Test.assert_equals(num_to_dashes(47),"-----------------------------------------------")
Test.assert_equals(num_to_dashes(48),"------------------------------------------------")
Test.assert_equals(num_to_dashes(49),"-------------------------------------------------")
Test.assert_equals(num_to_dashes(50),"--------------------------------------------------")
Test.assert_equals(num_to_dashes(51),"---------------------------------------------------")
Test.assert_equals(num_to_dashes(52),"----------------------------------------------------")
Test.assert_equals(num_to_dashes(53),"-----------------------------------------------------")
Test.assert_equals(num_to_dashes(54),"------------------------------------------------------")
Test.assert_equals(num_to_dashes(55),"-------------------------------------------------------")
Test.assert_equals(num_to_dashes(56),"--------------------------------------------------------")
Test.assert_equals(num_to_dashes(57),"---------------------------------------------------------")
Test.assert_equals(num_to_dashes(58),"----------------------------------------------------------")
Test.assert_equals(num_to_dashes(59),"-----------------------------------------------------------")
Test.assert_equals(num_to_dashes(60),"------------------------------------------------------------")


def is_plural(word):
    return True if word[-1] == "s" else False


Test.assert_equals(is_plural("dudes"), True)
Test.assert_equals(is_plural("flowers"), True)
Test.assert_equals(is_plural("checks"), True)
Test.assert_equals(is_plural("varies"), True)
Test.assert_equals(is_plural("efforts"), True)
Test.assert_equals(is_plural("mood"), False)
Test.assert_equals(is_plural("whiteboard"), False)
Test.assert_equals(is_plural("cow"), False)
Test.assert_equals(is_plural("word"), False)
Test.assert_equals(is_plural("love"), False)
Test.assert_equals(is_plural("silly"), False)


def is_last_character_n(word):
    return True if word[-1] == "n" else False



Test.assert_equals(is_last_character_n("Aiden"), True)
Test.assert_equals(is_last_character_n("Roxy"), False)
Test.assert_equals(is_last_character_n("Bert"), False)
Test.assert_equals(is_last_character_n("Dean"), True)
Test.assert_equals(is_last_character_n("Ian"), True)
Test.assert_equals(is_last_character_n("Brian"), True)
Test.assert_equals(is_last_character_n("Daniel"), False)


def eq(evaluate):
    return eval(evaluate)



Test.assert_equals(eq("1+2"), 3)
Test.assert_equals(eq("6/(9-7)"), 3)
Test.assert_equals(eq("3+2-4"), 1)
Test.assert_equals(eq("3*4+1"), 13)
Test.assert_equals(eq("5*8-4*9"), 4)
Test.assert_equals(eq("3**7"), 2187)
Test.assert_equals(eq("(6**3)+3"), 219)


def add(char, txt):
    return txt.replace(" ",char)


Test.assert_equals(add("#", "hello world"), "hello#world")
Test.assert_equals(add("R", "python is fun"), "pythonRisRfun")
Test.assert_equals(add("*", "use .join() for this challenge"), "use*.join()*for*this*challenge")
Test.assert_equals(add("#", " "), "#")


def new_word(word):
    return word[1:]


Test.assert_equals(new_word("pokhara"), "okhara")
Test.assert_equals(new_word("biratnagar"), "iratnagar")
Test.assert_equals(new_word("nepal"), "epal")
Test.assert_equals(new_word("damak"), "amak")
Test.assert_equals(new_word("itahari"), "tahari")
Test.assert_equals(new_word("rasuwa"), "asuwa")
Test.assert_equals(new_word("rolpa"), "olpa")


def is_safe_bridge(s):
    return " " not in s


Test.assert_equals(is_safe_bridge("####"), True)
Test.assert_equals(is_safe_bridge("## ####"), False)
Test.assert_equals(is_safe_bridge("#"), True)
Test.assert_equals(is_safe_bridge("# #"), False)


Test.assert_equals(template.format("John", "Joe"), "Joe hit John and then John hit Joe.")
Test.assert_equals(template.format("Peter", "Pan"), "Pan hit Peter and then Peter hit Pan.")
Test.assert_equals(template.format("Eda", "Bit"), "Bit hit Eda and then Eda hit Bit.")
Test.assert_equals(template.format("Pikachu", "Raichu"), "Raichu hit Pikachu and then Pikachu hit Raichu.")


















Test.summary()
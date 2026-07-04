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

template = "{1} hit {0} and then {0} hit {1}."


Test.assert_equals(template.format("John", "Joe"), "Joe hit John and then John hit Joe.")
Test.assert_equals(template.format("Peter", "Pan"), "Pan hit Peter and then Peter hit Pan.")
Test.assert_equals(template.format("Eda", "Bit"), "Bit hit Eda and then Eda hit Bit.")
Test.assert_equals(template.format("Pikachu", "Raichu"), "Raichu hit Pikachu and then Pikachu hit Raichu.")


def greater_than_one(frac):
    return eval(frac) > 1



Test.assert_equals(greater_than_one("1/2"), False)
Test.assert_equals(greater_than_one("7/4"), True)
Test.assert_equals(greater_than_one("10/10"), False)
Test.assert_equals(greater_than_one("12/30"), False)
Test.assert_equals(greater_than_one("28/3"), True)
Test.assert_equals(greater_than_one("35/31"), True)
Test.assert_equals(greater_than_one("11/27"), False)
Test.assert_equals(greater_than_one("42/32"), True)
Test.assert_equals(greater_than_one("34/15"), True)
Test.assert_equals(greater_than_one("16/16"), False)
Test.assert_equals(greater_than_one("38/41"), False)
Test.assert_equals(greater_than_one("45/43"), True)
Test.assert_equals(greater_than_one("13/38"), False)
Test.assert_equals(greater_than_one("43/2"), True)
Test.assert_equals(greater_than_one("16/31"), False)
Test.assert_equals(greater_than_one("41/15"), True)
Test.assert_equals(greater_than_one("2/38"), False)
Test.assert_equals(greater_than_one("37/21"), True)


def wumbo(words):
    return words.replace("M","W")



Test.assert_equals(wumbo("WHAT DO YOU MEAN WE'RE OUT OF MONEY"), "WHAT DO YOU WEAN WE'RE OUT OF WONEY", "You do not Wumbo.")
Test.assert_equals(wumbo("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ABCDEFGHIJKLWNOPQRSTUVWXYZ", "You do not Wumbo.")
Test.assert_equals(wumbo("1 WUMBO 2 WUMBO 3 WUMBO 4"), "1 WUWBO 2 WUWBO 3 WUWBO 4", "You do not Wumbo.")


def bomb(txt):
    txt = txt.lower()
    if "bomb" in txt:
        return "Duck!!!"
    else:
        return "There is no bomb, relax."



Test.assert_equals(bomb("There is a bomb."), "Duck!!!")
Test.assert_equals(bomb("Hey, did you find it?"), "There is no bomb, relax.")
Test.assert_equals(bomb("Hey, did you think there is a bomb?"), "Duck!!!")
Test.assert_equals(bomb("This goes boom!!!"), "There is no bomb, relax.")
Test.assert_equals(bomb("Hey, did you find the BoMb?"), "Duck!!!")
Test.assert_equals(bomb("Commotion in the third, a bomb is found!"), "Duck!!!")


def char_count(txt1, txt2):
    return txt2.count(txt1)



Test.assert_equals(char_count('a', 'edabit'), 1)
Test.assert_equals(char_count('b', 'big fat bubble'), 4)
Test.assert_equals(char_count('c', 'Chamber of secrets'), 1)
Test.assert_equals(char_count('f', 'frank and his friends have offered five foxes for sale'), 7)
Test.assert_equals(char_count('x', 'edabit'), 0)
Test.assert_equals(char_count('a', 'Adam and Eve bit the apple and found a snake'), 6)
Test.assert_equals(char_count('s', 'sssssssssssssssssssssssss'), 25)
Test.assert_equals(char_count('7', '10795426697'), 2)


def get_word(left, right):
    return (left + right).capitalize()


Test.assert_equals(get_word("maga", "zine"), "Magazine")
Test.assert_equals(get_word("reli", "able"), "Reliable")
Test.assert_equals(get_word("impl", "icit"), "Implicit")
Test.assert_equals(get_word("docu", "ment"), "Document")
Test.assert_equals(get_word("oppo", "site"), "Opposite")
Test.assert_equals(get_word("offi", "cial"), "Official")
Test.assert_equals(get_word("disa", "gree"), "Disagree")
Test.assert_equals(get_word("acci", "dent"), "Accident")
Test.assert_equals(get_word("omis", "sion"), "Omission")
Test.assert_equals(get_word("vigo", "rous"), "Vigorous")
Test.assert_equals(get_word("pred", "ator"), "Predator")
Test.assert_equals(get_word("prog", "ress"), "Progress")
Test.assert_equals(get_word("inva", "sion"), "Invasion")
Test.assert_equals(get_word("fare", "well"), "Farewell")
Test.assert_equals(get_word("majo", "rity"), "Majority")
Test.assert_equals(get_word("pers", "onal"), "Personal")
Test.assert_equals(get_word("sequ", "ence"), "Sequence")
Test.assert_equals(get_word("gove", "rnor"), "Governor")
Test.assert_equals(get_word("igno", "rant"), "Ignorant")
Test.assert_equals(get_word("fini", "shed"), "Finished")


def number_syllables(word):
    return word.count("-") + 1



Test.assert_equals(number_syllables("buf-fet"), 2)
Test.assert_equals(number_syllables("beau-ti-ful"), 3)
Test.assert_equals(number_syllables("mon-u-men-tal"), 4)
Test.assert_equals(number_syllables("on-o-mat-o-poe-ia"), 6)
Test.assert_equals(number_syllables("o-ver-ly"), 3)
Test.assert_equals(number_syllables("pas-try"), 2)
Test.assert_equals(number_syllables("flu-id"), 2)
Test.assert_equals(number_syllables("syl-la-ble"), 3)


def find_index(lst, txt):
    return lst.index(txt)



Test.assert_equals(find_index(['ght', 'edabit', 'testcase', 'hello'], 'testcase'), 2)
Test.assert_equals(find_index(['HfjhB', 'Ok', 'smile', '12345'], '12345'), 3)
Test.assert_equals(find_index(['a', 'b', 'c', 'd', 'e', 'f'], 'f'), 5)



def amazing_edabit(s):
    return s.replace("amazing","not amazing") if "edabit" not in s.lower() else s


Test.assert_equals(amazing_edabit("edabit is amazing."), "edabit is amazing.")
Test.assert_equals(amazing_edabit("Mubashir is amazing."), "Mubashir is not amazing.")
Test.assert_equals(amazing_edabit("Trump is amazing."), "Trump is not amazing.")
Test.assert_equals(amazing_edabit("Infinity is amazing."), "Infinity is not amazing.")
Test.assert_equals(amazing_edabit("Mubashir and edabit are amazing."), "Mubashir and edabit are amazing.")
Test.assert_equals(amazing_edabit("Matt is amazing."), "Matt is not amazing.")
Test.assert_equals(amazing_edabit("Helen is amazing."), "Helen is not amazing.")
Test.assert_equals(amazing_edabit("Python and edabit are amazing."), "Python and edabit are amazing.")
Test.assert_equals(amazing_edabit("C++ is amazing."), "C++ is not amazing.")
Test.assert_equals(amazing_edabit("javascript is amazing."), "javascript is not amazing.")
Test.assert_equals(amazing_edabit("java is amazing."), "java is not amazing.")
Test.assert_equals(amazing_edabit("ruby is amazing."), "ruby is not amazing.")
Test.assert_equals(amazing_edabit("SQL is amazing."), "SQL is not amazing.")
Test.assert_equals(amazing_edabit("CSS is amazing."), "CSS is not amazing.")
Test.assert_equals(amazing_edabit("Pakistan is amazing. edabit"), "Pakistan is amazing. edabit")
Test.assert_equals(amazing_edabit("You and edabit are amazing."), "You and edabit are amazing.")
Test.assert_equals(amazing_edabit("Matt and edabit are amazing."), "Matt and edabit are amazing.")
Test.assert_equals(amazing_edabit("Helen and edabit are amazing."), "Helen and edabit are amazing.")
Test.assert_equals(amazing_edabit("Everyone is amazing."), "Everyone is not amazing.")
Test.assert_equals(amazing_edabit("Swift and edabit are amazing."), "Swift and edabit are amazing.")


def remove_numbers(string):
    return "".join(i for i in string if not i.isdigit())



Test.assert_equals(remove_numbers("mubashir1"), "mubashir")
Test.assert_equals(remove_numbers("12ma23tt"), "matt")
Test.assert_equals(remove_numbers("e1d2a3b4i5t6"), "edabit")
Test.assert_equals(remove_numbers("pakistan007"), "pakistan")
Test.assert_equals(remove_numbers("ai4653rf53or4235ce"), "airforce")
#Mubashir


def generation(x, y):
    g = {
        -3: {"m": "great grandfather", "f": "great grandmother"},
        -2: {"m": "grandfather", "f": "grandmother"},
        -1: {"m": "father", "f": "mother"},
        0: {"m": "me!", "f": "me!"},
        1: {"m": "son", "f": "daughter"},
        2: {"m": "grandson", "f": "granddaughter"},
        3: {"m": "great grandson", "f": "great granddaughter"},
    }
    return g[x][y]
        


Test.assert_equals(generation(-3, "m"), "great grandfather", "3 generations before you, male...\n")
Test.assert_equals(generation(1, "f"), "daughter", "1 generation after you, female...\n")
Test.assert_equals(generation(-3, "f"), "great grandmother")
Test.assert_equals(generation(-2, "m"), "grandfather")
Test.assert_equals(generation(-2, "f"), "grandmother")
Test.assert_equals(generation(-1, "m"), "father")
Test.assert_equals(generation(-1, "f"), "mother")
Test.assert_equals(generation(0, "f"), "me!")
Test.assert_equals(generation(1, "m"), "son")
Test.assert_equals(generation(1, "f"), "daughter")
Test.assert_equals(generation(2, "m"), "grandson")
Test.assert_equals(generation(2, "f"), "granddaughter")
Test.assert_equals(generation(3, "m"), "great grandson")
Test.assert_equals(generation(3, "f"), "great granddaughter")
Test.assert_equals(generation(0, "m"), "me!")
# Author: Jeroen Ndh


def same_case(txt):
    return txt.islower() or txt.isupper()


Test.assert_equals(same_case("HELLO"), True)
Test.assert_equals(same_case("HEllo"), False)
Test.assert_equals(same_case("mArmALadE"), False)
Test.assert_equals(same_case("marmalade"), True)
Test.assert_equals(same_case("MARMALADE"), True)
Test.assert_equals(same_case("ketchUP"), False)
Test.assert_equals(same_case("pickle"), True)
Test.assert_equals(same_case("MUSTARD"), True)

def count_syllables(txt):
    return len(txt) // 2


Test.assert_equals(count_syllables("Hehehehehehe"), 6)
Test.assert_equals(count_syllables("bobobobobobobobo"), 8)
Test.assert_equals(count_syllables("NANANANA"), 4)
Test.assert_equals(count_syllables("lelelele"), 4)
Test.assert_equals(count_syllables("momomomomomomomomo"), 9)
Test.assert_equals(count_syllables("WiWiWiWiWiWiWiWiWiWi"), 10)
Test.assert_equals(count_syllables("RURURURURURUrurururuRURU"), 12)
Test.assert_equals(count_syllables("go"), 1)
Test.assert_equals(count_syllables("dede"), 2)


def forbidden_letter(char, lst):
    return not  any(char in i for i in lst)

Test.assert_equals(forbidden_letter('e', ['rinse', 'and', 'repeat']), False)
Test.assert_equals(forbidden_letter('d', ['python', 'javascript', 'ruby', 'fortran']), True)
Test.assert_equals(forbidden_letter('a', ['spoon', 'fork', 'knife']), True)
Test.assert_equals(forbidden_letter('b', ['test', 'dot', 'assert', 'equals']), True)
Test.assert_equals(forbidden_letter('i', ['rock', 'paper', 'scissors']), False)
Test.assert_equals(forbidden_letter('t', []), True)


#nice


Test.summary()
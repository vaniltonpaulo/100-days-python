import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test


def chatroom_status(users):
    if not users:
        return "no one online"
    elif len(users) == 1:
        return f"{users[0]} online"
    elif len(users) == 2:
        return f"{users[0]} and {users[1]} online"
    else:
        return f"{users[0]}, {users[1]} and {len(users[2:])} more online"



Test.assert_equals(chatroom_status([]), "no one online")
Test.assert_equals(chatroom_status(["becky325"]), "becky325 online")
Test.assert_equals(chatroom_status(["becky325", "malcolm888"]), "becky325 and malcolm888 online")
Test.assert_equals(chatroom_status(["becky325", "malcolm888", "fah32fa"]), "becky325, malcolm888 and 1 more online")
Test.assert_equals(chatroom_status(["paRIE_to"]), "paRIE_to online")
Test.assert_equals(chatroom_status(["s234f", "mailbox2"]), "s234f and mailbox2 online")
Test.assert_equals(chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]), "pap_ier44, townieBOY and 4 more online")


def count_palindromes(num1, num2):
    result = 0
    for i in range(num1, num2 + 1):
        if str(i)  == str(i)[::-1]:
            result += 1
    return result 


Test.assert_equals(count_palindromes(1, 10), 9)
Test.assert_equals(count_palindromes(555, 556), 1)
Test.assert_equals(count_palindromes(878, 898), 3)
Test.assert_equals(count_palindromes(8, 34), 5)
Test.assert_equals(count_palindromes(1550, 1556), 1)



def sum_of_evens(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] % 2 == 0:
                result += lst[i][j]
    return result




Test.assert_equals(sum_of_evens([
		[1, 5, 1, 3], 
		[4, 1, 2, 0], 
		[6, 9, 7, 4], 
		[5, 1, 2, 6]
	]), 24)
	
Test.assert_equals(sum_of_evens([
		[1, 0, 1],
		[33, 1, 2],
		[15, 9, 1],
		[5, 1, 979]
	]), 2)
	
Test.assert_equals(sum_of_evens([
		[2, 19, 5, 43], 
		[67, 2, 0, 12]
	]), 16)
	
Test.assert_equals(sum_of_evens([
		[1, 3, 7, 9], 
		[11, 13, 15, 17], 
		[19, 21, 23, 25]
	]), 0)

Test.assert_equals(sum_of_evens([
		[], 
		[], 
		[]
	]), 0)


# def split(txt):
#     txt = txt.split()




# Test.assert_equals(split("abcde"), "aebcd")
# Test.assert_equals(split("Hello!"), "eoHll!")
# Test.assert_equals(split("What's the time?"), "aeieWht's th tm?")



def hacker_speak(txt):
    return txt.replace("a","4").replace("e","3").replace("i","1").replace("o","0").replace("s","5")



Test.assert_equals(hacker_speak("javascript is cool"), "j4v45cr1pt 15 c00l")
Test.assert_equals(hacker_speak("become a coder"), "b3c0m3 4 c0d3r")
Test.assert_equals(hacker_speak("hi there"), "h1 th3r3")
Test.assert_equals(hacker_speak("programming is fun"), "pr0gr4mm1ng 15 fun")
Test.assert_equals(hacker_speak("keep on practicing"), "k33p 0n pr4ct1c1ng")

Test.summary()


# def century(year):
#     cent = year //100 +1
#     if 
#     return f"{cent}th century"


# Test.assert_equals(century(1756), "18th century")
# Test.assert_equals(century(1555), "16th century")
# Test.assert_equals(century(1000), "10th century")
# Test.assert_equals(century(1001), "11th century")
# Test.assert_equals(century(2005), "21st century")
# Test.assert_equals(century(1789), "18th century")
# Test.assert_equals(century(1510), "16th century")
# Test.assert_equals(century(1615), "17th century")
# Test.assert_equals(century(2000), "20th century")
# Test.assert_equals(century(1997), "20th century")
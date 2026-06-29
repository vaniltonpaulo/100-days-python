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
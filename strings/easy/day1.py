import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
from test_utils import Test



def upload_count(dates, month):
    count = 0
    for date in dates:
         if date.startswith(month):
              count = count + 1
    return count


Test.assert_equals(upload_count(['Dec 10', 'Dec 10', 'Dec 9', 'Dec 9', 'Dec 9', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 5', 'Dec 5', 'Dec 5', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 3', 'Dec 3', 'Dec 3', 'Dec 2', 'Dec 2', 'Dec 2', 'Dec 1', 'Dec 1', 'Dec 1', 'Dec 1','Nov 30', 'Nov 30', 'Nov 28', 'Nov 28', 'Nov 27', 'Nov 27', 'Nov 27', 'Nov 26', 'Nov 26', 'Nov 25', 'Nov 25', 'Nov 25', 'Nov 25', 'Nov 24', 'Nov 24', 'Nov 23', 'Nov 23', 'Nov 23', 'Nov 21', 'Nov 21', 'Nov 20', 'Nov 20', 'Nov 20', 'Nov 19', 'Nov 19', 'Nov 19', 'Nov 18', 'Nov 18', 'Nov 17', 'Nov 17', 'Nov 17', 'Nov 16', 'Nov 16', 'Nov 16', 'Nov 16', 'Nov 15', 'Nov 15', 'Nov 14', 'Nov 14', 'Nov 14', 'Nov 13', 'Nov 13', 'Nov 13', 'Nov 13', 'Nov 12', 'Nov 12', 'Nov 12', 'Nov 11', 'Nov 11', 'Nov 11', 'Nov 11', 'Nov 10', 'Nov 10', 'Nov 10', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 8', 'Nov 7', 'Nov 7', 'Nov 7', 'Nov 6', 'Nov 6', 'Nov 5', 'Nov 5', 'Nov 4', 'Nov 4', 'Nov 4', 'Nov 4', 'Nov 3', 'Nov 3', 'Nov 3', 'Nov 2', 'Nov 2', 'Nov 2', 'Nov 2', 'Nov 1', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 30', 'Oct 29', 'Oct 29', 'Oct 28', 'Oct 28', 'Oct 28', 'Oct 27', 'Oct 27', 'Oct 26', 'Oct 26', 'Oct 26', 'Oct 25', 'Oct 24', 'Oct 24', 'Oct 24', 'Oct 23', 'Oct 23', 'Oct 23', 'Oct 22', 'Oct 22', 'Oct 22', 'Oct 21', 'Oct 20', 'Oct 20', 'Oct 20', 'Oct 20', 'Oct 19', 'Oct 19', 'Oct 19', 'Oct 18', 'Oct 17', 'Oct 17', 'Oct 17', 'Oct 17', 'Oct 16', 'Oct 16', 'Oct 15', 'Oct 15', 'Oct 14', 'Oct 14', 'Oct 13', 'Oct 13', 'Oct 13', 'Oct 12', 'Oct 12', 'Oct 10', 'Oct 10', 'Oct 10', 'Oct 9', 'Oct 9', 'Oct 9', 'Oct 8', 'Oct 8', 'Oct 7', 'Oct 7', 'Oct 6', 'Oct 6','Oct 5', 'Oct 5', 'Oct 3', 'Oct 3', 'Oct 3', 'Oct 2', 'Oct 2', 'Oct 2', 'Oct 2', 'Oct 1', 'Oct 1', 'Sept 30', 'Sept 30', 'Sept 29', 'Sept 29', 'Sept 29', 'Sept 28', 'Sept 28', 'Sept 26', 'Sept 26', 'Sept 25', 'Sept 24', 'Sept 24', 'Sept 23', 'Sept 23', 'Sept 23', 'Sept 22', 'Sept 22', 'Sept 22', 'Sept 21', 'Sept 21', 'Sept 20', 'Sept 19', 'Sept 19', 'Sept 19', 'Sept 18', 'Sep 18'], "Nov"), 79)
Test.assert_equals(upload_count(['Dec 10', 'Dec 10', 'Dec 9', 'Dec 9', 'Dec 9', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 5', 'Dec 5', 'Dec 5', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 3', 'Dec 3', 'Dec 3', 'Dec 2', 'Dec 2', 'Dec 2', 'Dec 1', 'Dec 1', 'Dec 1', 'Dec 1','Nov 30', 'Nov 30', 'Nov 28', 'Nov 28', 'Nov 27', 'Nov 27', 'Nov 27', 'Nov 26', 'Nov 26', 'Nov 25', 'Nov 25', 'Nov 25', 'Nov 25', 'Nov 24', 'Nov 24', 'Nov 23', 'Nov 23', 'Nov 23', 'Nov 21', 'Nov 21', 'Nov 20', 'Nov 20', 'Nov 20', 'Nov 19', 'Nov 19', 'Nov 19', 'Nov 18', 'Nov 18', 'Nov 17', 'Nov 17', 'Nov 17', 'Nov 16', 'Nov 16', 'Nov 16', 'Nov 16', 'Nov 15', 'Nov 15', 'Nov 14', 'Nov 14', 'Nov 14', 'Nov 13', 'Nov 13', 'Nov 13', 'Nov 13', 'Nov 12', 'Nov 12', 'Nov 12', 'Nov 11', 'Nov 11', 'Nov 11', 'Nov 11', 'Nov 10', 'Nov 10', 'Nov 10', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 8', 'Nov 7', 'Nov 7', 'Nov 7', 'Nov 6', 'Nov 6', 'Nov 5', 'Nov 5', 'Nov 4', 'Nov 4', 'Nov 4', 'Nov 4', 'Nov 3', 'Nov 3', 'Nov 3', 'Nov 2', 'Nov 2', 'Nov 2', 'Nov 2', 'Nov 1', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 30', 'Oct 29', 'Oct 29', 'Oct 28', 'Oct 28', 'Oct 28', 'Oct 27', 'Oct 27', 'Oct 26', 'Oct 26', 'Oct 26', 'Oct 25', 'Oct 24', 'Oct 24', 'Oct 24', 'Oct 23', 'Oct 23', 'Oct 23', 'Oct 22', 'Oct 22', 'Oct 22', 'Oct 21', 'Oct 20', 'Oct 20', 'Oct 20', 'Oct 20', 'Oct 19', 'Oct 19', 'Oct 19', 'Oct 18', 'Oct 17', 'Oct 17', 'Oct 17', 'Oct 17', 'Oct 16', 'Oct 16', 'Oct 15', 'Oct 15', 'Oct 14', 'Oct 14', 'Oct 13', 'Oct 13', 'Oct 13', 'Oct 12', 'Oct 12', 'Oct 10', 'Oct 10', 'Oct 10', 'Oct 9', 'Oct 9', 'Oct 9', 'Oct 8', 'Oct 8', 'Oct 7', 'Oct 7', 'Oct 6', 'Oct 6','Oct 5', 'Oct 5', 'Oct 3', 'Oct 3', 'Oct 3', 'Oct 2', 'Oct 2', 'Oct 2', 'Oct 2', 'Oct 1', 'Oct 1', 'Sept 30', 'Sept 30', 'Sept 29', 'Sept 29', 'Sept 29', 'Sept 28', 'Sept 28', 'Sept 26', 'Sept 26', 'Sept 25', 'Sept 24', 'Sept 24', 'Sept 23', 'Sept 23', 'Sept 23', 'Sept 22', 'Sept 22', 'Sept 22', 'Sept 21', 'Sept 21', 'Sept 20', 'Sept 19', 'Sept 19', 'Sept 19', 'Sept 18', 'Sep 18'], "Dec"), 36)
Test.assert_equals(upload_count(['Dec 10', 'Dec 10', 'Dec 9', 'Dec 9', 'Dec 9', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 5', 'Dec 5', 'Dec 5', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 3', 'Dec 3', 'Dec 3', 'Dec 2', 'Dec 2', 'Dec 2', 'Dec 1', 'Dec 1', 'Dec 1', 'Dec 1','Nov 30', 'Nov 30', 'Nov 28', 'Nov 28', 'Nov 27', 'Nov 27', 'Nov 27', 'Nov 26', 'Nov 26', 'Nov 25', 'Nov 25', 'Nov 25', 'Nov 25', 'Nov 24', 'Nov 24', 'Nov 23', 'Nov 23', 'Nov 23', 'Nov 21', 'Nov 21', 'Nov 20', 'Nov 20', 'Nov 20', 'Nov 19', 'Nov 19', 'Nov 19', 'Nov 18', 'Nov 18', 'Nov 17', 'Nov 17', 'Nov 17', 'Nov 16', 'Nov 16', 'Nov 16', 'Nov 16', 'Nov 15', 'Nov 15', 'Nov 14', 'Nov 14', 'Nov 14', 'Nov 13', 'Nov 13', 'Nov 13', 'Nov 13', 'Nov 12', 'Nov 12', 'Nov 12', 'Nov 11', 'Nov 11', 'Nov 11', 'Nov 11', 'Nov 10', 'Nov 10', 'Nov 10', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 8', 'Nov 7', 'Nov 7', 'Nov 7', 'Nov 6', 'Nov 6', 'Nov 5', 'Nov 5', 'Nov 4', 'Nov 4', 'Nov 4', 'Nov 4', 'Nov 3', 'Nov 3', 'Nov 3', 'Nov 2', 'Nov 2', 'Nov 2', 'Nov 2', 'Nov 1', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 30', 'Oct 29', 'Oct 29', 'Oct 28', 'Oct 28', 'Oct 28', 'Oct 27', 'Oct 27', 'Oct 26', 'Oct 26', 'Oct 26', 'Oct 25', 'Oct 24', 'Oct 24', 'Oct 24', 'Oct 23', 'Oct 23', 'Oct 23', 'Oct 22', 'Oct 22', 'Oct 22', 'Oct 21', 'Oct 20', 'Oct 20', 'Oct 20', 'Oct 20', 'Oct 19', 'Oct 19', 'Oct 19', 'Oct 18', 'Oct 17', 'Oct 17', 'Oct 17', 'Oct 17', 'Oct 16', 'Oct 16', 'Oct 15', 'Oct 15', 'Oct 14', 'Oct 14', 'Oct 13', 'Oct 13', 'Oct 13', 'Oct 12', 'Oct 12', 'Oct 10', 'Oct 10', 'Oct 10', 'Oct 9', 'Oct 9', 'Oct 9', 'Oct 8', 'Oct 8', 'Oct 7', 'Oct 7', 'Oct 6', 'Oct 6','Oct 5', 'Oct 5', 'Oct 3', 'Oct 3', 'Oct 3', 'Oct 2', 'Oct 2', 'Oct 2', 'Oct 2', 'Oct 1', 'Oct 1', 'Sept 30', 'Sept 30', 'Sept 29', 'Sept 29', 'Sept 29', 'Sept 28', 'Sept 28', 'Sept 26', 'Sept 26', 'Sept 25', 'Sept 24', 'Sept 24', 'Sept 23', 'Sept 23', 'Sept 23', 'Sept 22', 'Sept 22', 'Sept 22', 'Sept 21', 'Sept 21', 'Sept 20', 'Sept 19', 'Sept 19', 'Sept 19', 'Sept 18'], "Sept"), 25)
Test.assert_equals(upload_count(['Dec 10', 'Dec 10', 'Dec 9', 'Dec 9', 'Dec 9', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 8', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 7', 'Dec 5', 'Dec 5', 'Dec 5', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 4', 'Dec 3', 'Dec 3', 'Dec 3', 'Dec 2', 'Dec 2', 'Dec 2', 'Dec 1', 'Dec 1', 'Dec 1', 'Dec 1','Nov 30', 'Nov 30', 'Nov 28', 'Nov 28', 'Nov 27', 'Nov 27', 'Nov 27', 'Nov 26', 'Nov 26', 'Nov 25', 'Nov 25', 'Nov 25', 'Nov 25', 'Nov 24', 'Nov 24', 'Nov 23', 'Nov 23', 'Nov 23', 'Nov 21', 'Nov 21', 'Nov 20', 'Nov 20', 'Nov 20', 'Nov 19', 'Nov 19', 'Nov 19', 'Nov 18', 'Nov 18', 'Nov 17', 'Nov 17', 'Nov 17', 'Nov 16', 'Nov 16', 'Nov 16', 'Nov 16', 'Nov 15', 'Nov 15', 'Nov 14', 'Nov 14', 'Nov 14', 'Nov 13', 'Nov 13', 'Nov 13', 'Nov 13', 'Nov 12', 'Nov 12', 'Nov 12', 'Nov 11', 'Nov 11', 'Nov 11', 'Nov 11', 'Nov 10', 'Nov 10', 'Nov 10', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 9', 'Nov 8', 'Nov 7', 'Nov 7', 'Nov 7', 'Nov 6', 'Nov 6', 'Nov 5', 'Nov 5', 'Nov 4', 'Nov 4', 'Nov 4', 'Nov 4', 'Nov 3', 'Nov 3', 'Nov 3', 'Nov 2', 'Nov 2', 'Nov 2', 'Nov 2', 'Nov 1', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 31', 'Oct 30', 'Oct 29', 'Oct 29', 'Oct 28', 'Oct 28', 'Oct 28', 'Oct 27', 'Oct 27', 'Oct 26', 'Oct 26', 'Oct 26', 'Oct 25', 'Oct 24', 'Oct 24', 'Oct 24', 'Oct 23', 'Oct 23', 'Oct 23', 'Oct 22', 'Oct 22', 'Oct 22', 'Oct 21', 'Oct 20', 'Oct 20', 'Oct 20', 'Oct 20', 'Oct 19', 'Oct 19', 'Oct 19', 'Oct 18', 'Oct 17', 'Oct 17', 'Oct 17', 'Oct 17', 'Oct 16', 'Oct 16', 'Oct 15', 'Oct 15', 'Oct 14', 'Oct 14', 'Oct 13', 'Oct 13', 'Oct 13', 'Oct 12', 'Oct 12', 'Oct 10', 'Oct 10', 'Oct 10', 'Oct 9', 'Oct 9', 'Oct 9', 'Oct 8', 'Oct 8', 'Oct 7', 'Oct 7', 'Oct 6', 'Oct 6','Oct 5', 'Oct 5', 'Oct 3', 'Oct 3', 'Oct 3', 'Oct 2', 'Oct 2', 'Oct 2', 'Oct 2', 'Oct 1', 'Oct 1', 'Sept 30', 'Sept 30', 'Sept 29', 'Sept 29', 'Sept 29', 'Sept 28', 'Sept 28', 'Sept 26', 'Sept 26', 'Sept 25', 'Sept 24', 'Sept 24', 'Sept 23', 'Sept 23', 'Sept 23', 'Sept 22', 'Sept 22', 'Sept 22', 'Sept 21', 'Sept 21', 'Sept 20', 'Sept 19', 'Sept 19', 'Sept 19', 'Sept 18', 'Sep 18'], "Oct"), 73)
Test.summary()


def reverse(txt):
     return txt[::-1].swapcase()


Test.assert_equals(reverse("Hello World"), "DLROw OLLEh")
Test.assert_equals(reverse("ReVeRsE"), "eSrEvEr")
Test.assert_equals(reverse(""), "")
Test.assert_equals(reverse("Radar"), "RADAr")


def double_char(txt):
     return ''.join([s*2 for s in txt])


Test.assert_equals(double_char("String"), "SSttrriinngg")
Test.assert_equals(double_char("Hello World!"), "HHeelllloo  WWoorrlldd!!")
Test.assert_equals(double_char("1234!_ "), "11223344!!__  ")
Test.assert_equals(double_char("##^&%%*&%%$#@@!"), "####^^&&%%%%**&&%%%%$$##@@@@!!")
Test.assert_equals(double_char("scandal"), "ssccaannddaall")
Test.assert_equals(double_char("economics"), "eeccoonnoommiiccss")
Test.assert_equals(double_char(" "), "  ")
Test.assert_equals(double_char("_______"), "______________")
Test.assert_equals(double_char("equip gallon read"), "eeqquuiipp  ggaalllloonn  rreeaadd")
Test.assert_equals(double_char("baby increase"), "bbaabbyy  iinnccrreeaassee")
Test.summary()  


def error(n):
     error = {
          1: "Check the fan: e1",
          2: "Emergency stop: e2",
          3: "Pump Error: e3",
          4: "c: e4",
          5: "Temperature Sensor Error: e5"
     }
     return error.get(n,101)

Test.assert_equals(error(1), "Check the fan: e1")
Test.assert_equals(error(2), "Emergency stop: e2")
Test.assert_equals(error(3), "Pump Error: e3")
Test.assert_equals(error(4), "c: e4")
Test.assert_equals(error(5), "Temperature Sensor Error: e5")
Test.assert_equals(error(-1000), 101)
Test.summary()


def card_hide(card):
    return "*" * (len(card) - 4) + card[-4:]

Test.assert_equals(card_hide("1234123456785678"), "************5678")
Test.assert_equals(card_hide("8754456321113213"), "************3213")
Test.assert_equals(card_hide("35123413355523"), "**********5523")
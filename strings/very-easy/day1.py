
def string_int(txt):
    return int(txt)

print(string_int("6"))  # ➞ 6
print(string_int("1000"))  # ➞ 1000
print(string_int("12"))  # ➞ 12

def give_me_something(a):
    return "something" + " " + a

print(give_me_something("is better than nothing"))  # ➞ "something is better than nothing"
print(give_me_something("Bob Jane"))  # ➞ "something Bob Jane"
print(give_me_something("something"))  # ➞ "something something"


def comp(txt1, txt2):
    return len(txt1) == len(txt2)

print(comp("AB", "CD"))  # ➞ True
print(comp("ABC", "DE"))  # ➞ False
print(comp("hello", "edabit"))  # ➞ False


def concat_name(first_name, last_name):
    return last_name + ", " + first_name

print(concat_name("First", "Last"))  # ➞ "Last, First"
print(concat_name("John", "Doe"))  # ➞ "Doe, John"

print(concat_name("Mary", "Jane"))  # ➞ "Jane, Mary"


def front3(txt):
    if len(txt) < 3:
        return txt * 3
    else:
        return txt[:3] * 3

print(front3("Python"))  # ➞ "PytPytPyt"
print(front3("Cucumber"))  # ➞ "CucCucCuc"

print(front3("bioshock"))  # ➞ "biobiobio"

print(front3("Z"))  # ➞ "ZZZ"
print(front3('duh'))  # ➞ "duhduhduh"
print(front3(''))  # ➞ ""  



def long_burp(num):
    num = num - 1
    return "Bur" + "r" * num + "p"
print(long_burp(3))  # ➞ "Burrrp"
print(long_burp(5))  # ➞ "Burrrrrp"
print(long_burp(9))  # ➞ "Burrrrrrrrrp"


def count_d(sentence):
    return sentence.lower().count("d")

print(count_d("My friend Dylan got distracted in school."))  # ➞ 4
print(count_d("Debris was scattered all over the yard."))  # ➞ 3

print(count_d("The rodents hibernated in their den."))  # ➞ 3


a = "John"
b = "Joe"
c = "Jack"
template = "Their names were: {}, {} and {}."
print(template.format(a, b,c))


def googlify(n):
    return "G" + "o" * n + "gle" if n > 0 else "invalid"

print(googlify(10))  # ➞ "Goooooooooogle"
print(googlify(23))  # ➞ "Gooooooooooooooooooooooogle"
print(googlify(2))  # ➞ "Google"

print(googlify(-2))  #   ➞ "invalid"


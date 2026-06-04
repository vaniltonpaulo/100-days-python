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


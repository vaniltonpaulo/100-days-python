#Array very easy

def get_sum_of_elements(lst):
    return sum(lst)


print(get_sum_of_elements([2, 7, 4])) # ➞ 13

print(get_sum_of_elements([45, 3, 0])) # ➞ 48

print(get_sum_of_elements([-2, 84, 23])) # ➞ 105


def list_less_than_100(lst):
    return sum(lst) <100


print(list_less_than_100([5, 57])) # ➞ True

print(list_less_than_100([77, 30])) # ➞ False

print(list_less_than_100([0])) # ➞ True

print(list_less_than_100([25, 50, 25])) # ➞ False

def make_pair(num1, num2):
    return [num1,num2]


print(make_pair(1, 2)) # ➞ [1, 2]

print(make_pair(51, 21)) # ➞ [51, 21]

print(make_pair(512124, 215)) # ➞ [512124, 215]


def even_or_odd(lst):
    x = sum(lst)
    return "even" if x % 2 == 0 else "odd" 



print(even_or_odd([0])) # ➞ "even"

print(even_or_odd([1])) # ➞ "odd"

print(even_or_odd([])) # ➞ "even"

print(even_or_odd([0, 1, 5])) # ➞ "even"
print(even_or_odd([-1023, -1, 3])) # ➞ "odd"

def check(lst, el):
    return el in lst

print(check([1, 2, 3, 4, 5], 3)) # ➞ True

print(check([1, 1, 2, 1, 1], 3)) # ➞ False

print(check([5, 5, 5, 6], 5)) # ➞ True

print(check([], 5)) # ➞ False


def check_equals(lst1, lst2):
	if lst1 == lst2:
		return True
	else:
		return False

print(check_equals([1, 2], [1, 3])) # ➞ False

print(check_equals([1, 2], [1, 2])) # ➞ True

print(check_equals([4, 5, 6], [4, 5, 6])) # ➞ True

print(check_equals([4, 7, 6], [4, 5, 6])) # ➞ False

print(check_equals([1, 12], [11, 2])) # ➞ False


def sum_lst(lst):
    return sum(lst)

print(sum_lst([1, 2, 3, 4, 5])) # ➞ 15

print(sum_lst([-1, 0, 1])) # ➞ 0

print(sum_lst([0, 4, 8, 12])) # ➞ 24


def half_quarter_eighth(n):
     return [n/2, n/4, n/8]

print(half_quarter_eighth(6)) # ➞ [3, 1.5, 0.75]

print(half_quarter_eighth(22)) # ➞ [11, 5.5, 2.75]

print(half_quarter_eighth(25)) # ➞ [12.5, 6.25, 3.125]


# Control flow very easy

def calculate_fuel(n):
    return int(n * 10)

print(calculate_fuel(15)) # ➞ 150

print(calculate_fuel(23.5)) # ➞ 235

print(calculate_fuel(3)) # ➞ 100


def flip(y):
    return 1 if y == 0 else 0

print(flip(1)) # ➞ 0

print(flip(0)) # ➞ 1


def transform(lst):
    for i in list(range(len(lst))):
        lst[i] = lst[i] - 1 if lst[i] % 2 == 0 else lst[i] + 1
    return lst

print(transform([1, 2, 3, 4, 5])) # ➞ [2, 1, 4, 3, 6]

print(transform([3, 3, 4, 3])) # ➞ [4, 4, 3, 4]

print(transform([2, 2, 0, 8, 10])) # ➞ [1, 1, -1, 7, 9]

print(transform([9, 13, 15, 5, 2, 11])) # ➞ [10, 14, 16, 6, 1, 12]

def asc_des_none(lst, s):
    if s == "Asc":
        return sorted(lst)
    elif s == "Des":
        return sorted(lst, reverse = True)
    else:
        return lst 


print(asc_des_none([4, 3, 2, 1], "Asc" )) # ➞ [1, 2, 3, 4]

print(asc_des_none([7, 8, 11, 66], "Des")) # ➞ [66, 11, 8, 7]

print(asc_des_none([1, 2, 3, 4], "None")) # ➞ [1, 2, 3, 4]

def name_shuffle(txt):
     return " ".join(txt.split()[::-1])


print(name_shuffle("Donald Trump")) # ➞ "Trump Donald"

print(name_shuffle("Rosie O'Donnell")) # ➞ "O'Donnell Rosie"

print(name_shuffle("Seymour Butts")) # ➞ "Butts Seymour"


def missing_num(lst):
     for i in range(1,11):
          if i not in lst:
                return i


print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])) # ➞ 5

print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8])) # ➞ 10

print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9])) # ➞ 7


def alphabet_soup(txt):
    return "".join(sorted(txt))

print(alphabet_soup("hello")) # ➞ "ehllo"

print(alphabet_soup("edabit")) # ➞ "abdeit"

print(alphabet_soup("hacker")) # ➞ "acehkr"

print(alphabet_soup("geek")) # ➞ "eegk"

print(alphabet_soup("javascript")) # ➞ "aacijprstv"

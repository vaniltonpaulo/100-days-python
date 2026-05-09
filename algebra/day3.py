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
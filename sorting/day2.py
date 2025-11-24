#VERY EASY  --> WE finished this section
def findLargestNum(nums):
    return max(nums)


print(findLargestNum([4, 5, 1, 3]))
print(findLargestNum([1000, 1001, 857, 1]))

def find_smallest_num(lst):
    return min(lst)

print(find_smallest_num([34, 15, 88, 2]))

def sort_nums_ascending(lst):
    return sorted(lst)

print(sort_nums_ascending([1, 2, 10, 50, 5]))


def sort_word(word):
    result =  sorted(list(word))
    return "".join(result)


print(sort_word("Unpredictable"))
print(sort_word("about"))
print(sort_word("administration"))




def age_difference(ages):
    parent_one = sorted(ages)[-1]
    parent_two = sorted(ages)[-2]
    result =  parent_one - parent_two
    if result == 0:
        return "No age difference between spouses."
    return f'{result} year'

print(age_difference([29, 1, 6, 8, 28]) )
print(age_difference([43, 86, 49, 86]))
print(age_difference([2, 4, 6, 32, 27]) )


def zip_it(women, men):
    if len(men) != len(women):
        return "sizes don't match"
    return tuple(zip(women, men))

print(zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh"]))

print(zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh", "Tim"]))


str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "abcdefghijklmnopqrstuvwxyz"


def longest_string(str1, str2):
    x = set(str1 + str2)
    result = sorted(x)
    return ''.join(result)

print(longest_string(str1, str2))
print(longest_string("", ""))
print(longest_string("inmanylanguages", "theresapairoffunctions"))

def even_odd_string(txt):
    even = txt[::2]
    odd = txt[1::2]
    return even + " "+ odd

print(even_odd_string("mubashir"))
print(even_odd_string("edabit"))
print(even_odd_string("SUBDERMATOGLYPHIC"))

def reverse(txt):
    return txt[::-1]

print(reverse("The quick brown fox."))
print(reverse("#$*+-=:;/\\@<>?_][`{}|~^'&%$#\"!"))

def findLargestNums(lst):
    return list(map(max, lst))


print(findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]))
print(findLargestNums([[0, 0, 0, 0], [3, 3, 3, 3], [-2, -2]]))

def list_values_types(lst):
    return list(map(type, lst))

print(list_values_types([["hello" , 1] , 10]))
print(list_values_types(["shashwat", 10, 90]))
print(list_values_types([False, False, "true"]))
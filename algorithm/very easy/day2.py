# VERY EASY
def next_edge(side1, side2):
    result = (side1 + side2) - 1
    return result

print(next_edge(7, 2))
print(next_edge(10, 4))


def animals(chickens, cows, pigs):
    c = chickens * 2
    p = pigs * 4
    co = cows * 4
    return sum([c, p, co])

print(animals(2, 3, 5))
print(animals(1, 2, 3))

def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif sum([a, b]) == 10:
        return True
    else:
        return False

print(makes10(9, 10))
print(makes10(8, 3))
print(makes10(10, 10))


def frames(minutes, fps):
    result = minutes * fps * 60
    return result

print(frames(10, 25))
print(frames(419, 70))


def even_or_odd(lst):
    if sum(lst) % 2 == 0:
        return "even"
    else:
        return "odd"

print(even_or_odd([0]))
print(even_or_odd([]))
even_or_odd([0, -1, -5])

def ctoa(char):
    return ord(char)

print(ctoa("A"))
print(ctoa("["))

def area_shape(base, height, shape):
    if shape == "triangle":
        return int(base * height * 0.5)
    else:
        return base * height



print(area_shape(2, 3, "triangle"))
print(area_shape(8, 6, "parallelogram"))


def accept_into_movie(age, is_supervised):
    if is_supervised:
        return True
    elif age >= 15:
        return True
    else:
        return False

print(accept_into_movie(14, True))
print(accept_into_movie(14.99999, False))
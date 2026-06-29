s = "()[]{}"

stack = []

pairs = {
    ")": "(",
    "}": "{",
    "]": "["
}

valid = True

for char in s:
    if char in "({[":
        stack.append(char)
    else:
        if not stack:
            valid = False
            break

        last_open = stack.pop()

        if last_open != pairs[char]:
            valid = False
            break

if stack:
    valid = False

print(valid)
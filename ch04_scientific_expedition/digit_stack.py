def digit_stack(commands):
    ret = 0
    stack = []

    for cmd in commands:
        if 'PUSH' in cmd:
            vl = int(cmd.split(' ')[1])
            stack.append(vl)
        elif 'POP' in cmd:
            try:
                vl = stack.pop()
            except IndexError:
                vl = 0
            ret += vl
        elif 'PEEK' in cmd:
            try:
                vl = stack[-1]
            except IndexError:
                vl = 0
            ret += vl

    return ret


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"

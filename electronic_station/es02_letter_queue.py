def letter_queue(commands):
    queue = list()

    for cmd in commands:
        if 'PUSH' in cmd:
            val = cmd.split(' ')[1]
            queue.append(val)
        elif cmd == 'POP':
            try:
                queue.pop(0)
            except IndexError:
                pass

    return ''.join(queue)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"

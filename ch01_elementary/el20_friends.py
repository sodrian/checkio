class Friends(object):
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)
            return True
        else:
            return False

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        ret = set()
        for c in self.connections:
            c = list(c)
            ret.add(c[0])
            ret.add(c[1])
        return ret

    def connected(self, name):
        ret = set()
        for c in self.connections:
            c = list(c)
            if c[0] == name:
                ret.add(c[1])
            elif c[1] == name:
                ret.add(c[0])
        return ret


if __name__ == '__main__':
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"

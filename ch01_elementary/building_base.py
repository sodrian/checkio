class Building(object):
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_we = width_WE
        self.width_ns = width_NS
        self.height = height

    def corners(self):
        nw = (self.south + self.width_ns, self.west)
        ne = (self.south + self.width_ns, self.west + self.width_we)
        sw = (self.south, self.west)
        se = (self.south, self.west + self.width_we)

        d = dict()
        d['north-west'] = nw
        d['north-east'] = ne
        d['south-west'] = sw
        d['south-east'] = se

        return d

    def area(self):
        return self.width_ns * self.width_we

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return 'Building(%s, %s, %s, %s, %s)' % (
            self.south,
            self.west,
            self.width_we,
            self.width_ns,
            self.height)


if __name__ == '__main__':
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"

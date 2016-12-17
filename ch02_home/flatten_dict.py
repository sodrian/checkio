def flatten(dictionary):
    res = dict()
    for k1, v1 in dictionary.items():
        if isinstance(v1, str):
            res[k1] = v1
        elif isinstance(v1, dict) and not v1:
            res[k1] = ''
        elif isinstance(v1, dict) and v1:
            v1 = flatten(v1)
            for k2, v2 in v1.items():
                res['{}/{}'.format(k1, k2)] = v2
    return res


if __name__ == '__main__':
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
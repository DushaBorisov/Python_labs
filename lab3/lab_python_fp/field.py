def field(items, *args):
    assert len(args) > 0
    res = []
    if len(args) == 1:
        for el in items:
            if el.get(args[0]) is not None:
                res.append(el.get(args[0]))

    else:
        for el in items:
            map_help = {}
            for arg in args:
                if el.get(arg) is not None:
                    map_help[arg] = el.get(arg)
            res.append(map_help)

    print(*res, sep=', ')

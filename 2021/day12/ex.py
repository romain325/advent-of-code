f = open("input2")

graph = {}
test = [path.strip().split("-") for path in f]


def setdict(k, v):
    val = graph.setdefault(k, [])
    val.append(v)


for path in test:
    setdict(path[0], path[1])
    setdict(path[1], path[0])


def discover(entry, visited, way):
    if entry == "end":
        print(way)
        return 1
    path_cnt = 0
    for linked in graph[entry]:
        if linked not in visited:
            cp = visited.copy()
            if linked.islower():
                cp.append(linked)
            way.append(linked)
            path_cnt = path_cnt + discover(linked, cp, way.copy())
    return path_cnt


# print(discover("start", ["start"], ["start"]))


def discover_with_precisions(entry, visited):
    if entry == "end":
        return 1
    path_cnt = 0
    for linked in graph[entry]:
        if linked == 'start':
            continue
        if "twice" not in visited or linked not in visited:
            cp = visited.copy()
            if linked.islower():
                cp.append(linked if linked not in visited else "twice")
            path_cnt = path_cnt + discover_with_precisions(linked, cp)
    return path_cnt


print(discover_with_precisions("start", ["start"]))

import re
from collections import defaultdict

with open("input.txt") as file_in:
    connections = []
    for line in file_in:
        connections.append(line.strip())

#connections = ['kh-tc', 'qp-kh', 'de-cg', 'ka-co', 'yn-aq', 'qp-ub', 'cg-tb', 'vc-aq', 'tb-ka', 'wh-tc', 'yn-cg', 'kh-ub', 'ta-co', 'de-co', 'tc-td', 'tb-wq', 'wh-td', 'ta-ka', 'td-qp', 'aq-cg', 'wq-ub', 'ub-vc', 'de-ta', 'wq-aq', 'wq-vc', 'wh-yn', 'ka-de', 'kh-ta', 'co-tc', 'wh-qp', 'tb-vc', 'td-yn']


def build_graph(connections):
    graph = defaultdict(list)
    for i in range(len(connections)):
        con1, con2 = connections[i].split('-')
        graph[con1].append(con2)
        graph[con2].append(con1)
    return graph


def dfs(graph, node):
    connected = graph[node]
    res = []
    for adj in connected:
        for parent in graph[adj]:
            if node in graph[parent]:
                res.append((node, adj, parent))
    return res


graph = build_graph(connections)

res = set()
for node in graph:
    dfs_res = dfs(graph, node)
    for x in dfs_res:
        res.add(frozenset(x))

counter = 0
for x in res:
    for y in x:
        if re.search('t[a-z]', y):
            counter += 1
            break

print(counter)

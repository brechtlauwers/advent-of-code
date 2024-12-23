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

# greedy algo
def find_clique(graph, node):
    connected = graph[node]
    clique = [node]
    
    for v in graph:
        adj = graph[v]
        if(all(x in adj for x in clique)):
            clique.append(v)
    return clique


graph = build_graph(connections)

res = set()
max_clique = []
for node in graph:
    clique = find_clique(graph, node)
    if len(clique) > len(max_clique):
        max_clique = clique


print(','.join(sorted(max_clique)))


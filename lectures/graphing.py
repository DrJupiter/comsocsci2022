#%%
import networkx as nx

# The vector k whose elements are the degrees k,
# i of all nodes i = 1, 2,..., N

#%%
uG = nx.Graph()
uG.degree

nodes = [1,2,3,4,5,6]
edges = [(1,2),(1,3),(1,4),(1,6),
        (2,3),(2,4),
        (3,6)]

uG.add_nodes_from(nodes)

for x,y in edges:
    uG.add_edge(x,y)

#%%
dG = nx.DiGraph()
dG.degree

nodes = [1,2,3,4,5,6]
edges_di = [(1,2)
        ,(2,3),(2,4)
        ,(3,1),(3,2)
        ,(4,1)
        ,(6,1),(6,3)]

dG.add_nodes_from(nodes)

for x,y in edges:
    dG.add_edge(x,y)
#%%

print(uG.edges)
print(dG.edges)

#%%

print("undirected graph adj M: \n",nx.adjacency_matrix(uG).todense())
print("directed graph adj M: \n",nx.adjacency_matrix(dG).todense())

#%%

for line in nx.generate_edgelist(uG):
    print(line[0],line[2],"->")

# [print(line[:3]) for line in nx.generate_edgelist(uG)]

# nx.draw(dG)

#%%

print("avg clustering value for the undirected graph",
        sum(nx.clustering(uG).values())/len(nodes))

print("avg clustering value for the directed graph",
        sum(nx.clustering(dG).values())/len(nodes))


#%%

### Switch 5 and 6
def edge_mutal_replace(list,val1,val2):
    mutated_list = list
    for i, edge in enumerate(list):
        if edge[0] == val1:
            mutated_list[i] = (val2,edge[1])
        if edge[0] == val2:
            mutated_list[i] = (val1,edge[1])
        if edge[1] == val1:
            mutated_list[i] = (edge[0],val2)
        if edge[1] == val2:
            mutated_list[i] = (edge[0],val1)

    return mutated_list

uG_s = nx.Graph()
uG_s.degree
uG_s.add_nodes_from(nodes)
for x,y in edge_mutal_replace(edges,5,6):
    uG_s.add_edge(x,y)

dG_s = nx.Graph()
dG_s.degree
dG_s.add_nodes_from(nodes)
for x,y in edge_mutal_replace(edges_di,5,6):
    dG_s.add_edge(x,y)

print("undirected graph adj M: \n",nx.adjacency_matrix(uG).todense(),"\n->\n",nx.adjacency_matrix(uG_s).todense())
print(" ")
print("directed graph adj M: \n",nx.adjacency_matrix(dG).todense(),"\n->\n",nx.adjacency_matrix(dG_s).todense())

#%%

# As both the adjacency matrix and the link lists (understood here as the adjacency list)
# are describe exactly the same data, the only difference is the formatting. Thus it is not possible to infer more information from one approch than the other.


#%%

def get_moves(graph, x):
    return [act for state,act in graph.edges(x)]

possible_movesets = []
for act1 in get_moves(uG,1):
    for act2 in get_moves(uG,act1):
        for act3 in get_moves(uG,act2):
            possible_movesets.append([1,act1,act2,act3])

counter = 0
for move_set in possible_movesets:
    if move_set[-1] == 3:
        counter += 1
        # print(move_set)
counter

#%%

possible_movesets = []
for act1 in get_moves(uG,1):
    for act2 in get_moves(uG,act1):
        for act3 in get_moves(uG,act2):
            for act4 in get_moves(uG,act3):
                possible_movesets.append([1,act1,act2,act3,act4])

counter = 0
for move_set in possible_movesets:
    if move_set[-1] == 3:
        counter += 1
        # print(move_set)
counter







#%%
##### Bipartite

G = nx.Graph()

nodes = [1,2,3,4,5,6,7,8,9,10,11]
edges = [(1,7),
        (2,9),
        (3,7),(3,8),(3,9),
        (4,9),(4,10),
        (5,9),(5,11),
        (6,11)]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

nx.adjacency_matrix(G).todense()

#%%

B = nx.project(G,nodes)

B_am = nx.adjacency_matrix(B)

proj_purple_G = nx.from_numpy_matrix(B_am.todense()[:6,:6])
proj_green_G = nx.from_numpy_matrix(B_am.todense()[6:,6:])
print(nx.adjacency_matrix(proj_purple_G).todense())
print(nx.adjacency_matrix(proj_green_G).todense())

# nx.draw(B)
# nx.draw(G)

degrees = [y for _,y in list(G.degree)]
print("avg degrees purple",sum(degrees[:6])/6,"\navg degrees green",sum(degrees[6:])/5)


degrees_purple = [y for _,y in list(proj_purple_G.degree)]
degrees_green = [y for _,y in list(proj_green_G.degree)]

print("avg degrees projec purple",sum(degrees_purple)/6,"\navg degrees projec green",sum(degrees_green)/5)


#%%

# N1 and N2
# max number of edges = N1*N2 (*2 if directional)

# difference if N = N1+N2
# unformable links = N^2/2 - N1*N2 (N^2 -2*N1*N2 if directional)

# if N1 << N2
# then the network is more likely to be sparse, as there are few possible connectins


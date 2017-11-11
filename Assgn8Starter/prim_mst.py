from undirected_graph import Graph
import heapq
import sys

def write_tree_edges_to_file(edges, filename):
    # TODO write out the edges, one per line. The same format as produced by generate_mst_input
    with open(filename, mode='w') as f:
        for v1, v2, w in edges:
            f.write("{} {} {}\n".format(v1, v2, w))

def read_weighted_undirected_graph(filename):
    g = Graph()
    with open(filename) as f:
        for line in f:
            try:
                v1, v2, w = line.split()
                g.add_edge(v1, v2, {'weight': int(w)})
            except:
                pass
    return g

def initialize_disjoint_set(items):
    return {item: None for item in items}




# Do not change this function's name or the arguments it takes. Also, do not change
# that it writes out the results at the end.
# This is the full contract of you code (this function in this file). Otherwise,
# please feel free to create helpers, modify provided code, create new helper files, etc.
# Whatever you turn in is what we will grade (ie we won't provide any files or overwrite
# any of yours)
# Have fun!
def compute_mst(filename):
    '''Use Prim's algorithm to compute the minimum spanning tree of the weighted undirected graph
    described by the contents of the file named filename.'''

    graph_holder = read_weighted_undirected_graph(filename)
    edges = [(graph_holder.attributes_of(v, u)['weight'], v, u) for u,v in graph_holder.get_edges()]
    edges.sort()

    PARENT = {}
    KEY = {}

    for x in graph_holder.get_nodes():
        PARENT[x]= None
        KEY[x] = 99999

    A={}
    start = edges[0][1]
    KEY[start]=0

    que = list(graph_holder.get_nodes())
    print(que)
    while len(que) != 0:
        u = min_from_que(KEY, que)
        que.remove(u)
        print(que)
        if(PARENT[u] != None):
            A[u] = PARENT[u]
        neigh = list(graph_holder.neighbors(u))
        for x in neigh:
            if x in que and graph_holder.attributes_of(u,x)['weight'] < KEY[x]:
                PARENT[x]= u
                KEY[x]= graph_holder.attributes_of(u,x)['weight']

    print(graph_holder.attributes_of(u,neigh[0])['weight'])
    print(A)
    for x in A.keys():
        print(graph_holder.attributes_of(x,A[x]))




def min_from_que(dict, q):
    min = 99999
    final = ""
    print(q)
    for x in q:
        if dict[x] < min:
            min = dict[x]
            final = x
    return final






    #tree_edges = []
    # TODO compute the edges of a minimum spanning tree
    #write_tree_edges_to_file(tree_edges, filename + '.mst')



if __name__ == "__main__":
    compute_mst("test10")
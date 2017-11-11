from undirected_graph import Graph
from operator import itemgetter
import time

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


def list_print_prep(A, graph_holder):
    l = []
    for x in A.keys():
        l.append(list([x, A[x], graph_holder.attributes_of(x,A[x])['weight']]))
    l = sorted(l, key=itemgetter(2))
    return l


def min_from_que(dict, q):
    min = 99999
    final = ""
    for x in q:
        if dict[x] < min:
            min = dict[x]
            final = x
    return final


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

    # reading in the file
    graph_holder = read_weighted_undirected_graph(filename)
    edges = [(graph_holder.attributes_of(v, u)['weight'], v, u) for u,v in graph_holder.get_edges()]
    edges.sort()

    # ***START OF PRIM'S***

    # dictionaries that hold the parents and keys
    PARENT = {}
    KEY = {}

    # for all G.V I set the pi aka(PARENT) = null and key aka(KEY) = 99999(larger than 50000)
    for x in graph_holder.get_nodes():
        PARENT[x]= None
        KEY[x] = 99999

    # A will be a dictionary that holds the final list of edges (MST)
    A={}

    # make a starting node by setting it's weight to 0
    start = edges[0][1]
    KEY[start]=0

    # make a que of all vertexes(G.V)
    que = list(graph_holder.get_nodes())

    # Go through each vertex
    while len(que) != 0:
        u = min_from_que(KEY, que)                                      # finds the smallest edge in Queue puts into u
        que.remove(u)
        if(PARENT[u] != None):                                          # puts the parent into A(MST)
            A[u] = PARENT[u]

        neigh = list(graph_holder.neighbors(u))                         # gets list of u's neighbors puts into neigh

        for x in neigh:                                                 # goes through u's neighbors(G.Adj[u]) and
            if x in que and graph_holder.attributes_of(u,x)['weight'] < KEY[x]:   # changes u.key if weight is less
                PARENT[x]= u
                KEY[x]= graph_holder.attributes_of(u,x)['weight']

    # ***END OF PRIM'S***
    # A holds the complete MST

    # printing
    tree_edges = list_print_prep(A, graph_holder)
    write_tree_edges_to_file(tree_edges, filename + '.mst')


def compute_mst_time(filename, time1):
    '''Use Prim's algorithm to compute the minimum spanning tree of the weighted undirected graph
    described by the contents of the file named filename.'''

    # reading in the file
    graph_holder = read_weighted_undirected_graph(filename)
    edges = [(graph_holder.attributes_of(v, u)['weight'], v, u) for u, v in graph_holder.get_edges()]
    edges.sort()

    # actual start of Prims
    start_time = time.clock()
    PARENT = {}
    KEY = {}


    for x in graph_holder.get_nodes():
        PARENT[x] = None
        KEY[x] = 99999

    A = {}
    start = edges[0][1]
    KEY[start] = 0

    que = list(graph_holder.get_nodes())
    while len(que) != 0:
        u = min_from_que(KEY, que)
        que.remove(u)
        if (PARENT[u] != None):
            A[u] = PARENT[u]
        neigh = list(graph_holder.neighbors(u))
        for x in neigh:
            if x in que and graph_holder.attributes_of(u, x)['weight'] < KEY[x]:
                PARENT[x] = u
                KEY[x] = graph_holder.attributes_of(u, x)['weight']
    end_time =time.clock()

    end_time -= start_time

    print(time1,"took:")
    print("{0:.5f}".format(round(end_time,5)))


if __name__ == "__main__":
    compute_mst_time("test5",5)
    compute_mst_time("test50", 50)
    compute_mst_time("test100", 100)
    compute_mst_time("test200", 200)
    compute_mst_time("test500", 500)
    compute_mst_time("test1000", 1000)
    compute_mst_time("test2500", 2500)
    compute_mst_time("test5000", 5000)
    compute_mst("test5")
    compute_mst("test50")
    compute_mst("test100")
    compute_mst("test200")
    compute_mst("test500")
    compute_mst("test1000")
    compute_mst("test2500")
    compute_mst("test5000")
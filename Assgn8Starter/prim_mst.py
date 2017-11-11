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


def tree_contains(tree, node):
    for x in tree:
        #print(x[2])
        if x[1] == node and x[2] != None:
            return True
    return False



def change_tree(tre, nod1, nod2, weig):
    for x in range(len(tre)):
        if tre[x][1] == nod1:
            tre[x][0]= weig
            tre[x][2] = nod2
            return tre


    return tre


def less_weight(tre, nod1, weig):
    for x in tre:
        if x[1] == nod1:
            if x[0] > weig:
                return True
    return False


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
    node_sets = initialize_disjoint_set(graph_holder.get_nodes())
    node_count = len(node_sets)
    edges = [(graph_holder.attributes_of(v, u)['weight'], v, u) for u,v in graph_holder.get_edges()]
    edges.sort()
    tree = []
    holder = set()

    PARENT = {}
    KEY = {}

    for x in graph_holder.get_nodes():
        PARENT[x]= None
        KEY[x] = 99999
    #print(PARENT)
    #print(edges)

    #print(KEY)
    A={}
    start = edges[0][1]
    KEY[start]=0
    #print(KEY)
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



    '''for y in list(graph_holder.get_nodes()):
        tree.append([99999,y,None])
    tree[0][0]=0
    que = []
    for y in edges:
        if y[1] == tree[0][1]:
            heapq.heappush(que,y)
            holder.add(y)
    #print(que)
    while len(que) != 0:
        #print(que)
        weight, tree_node, node = heapq.heappop(que)

        #print(que)
        #print(weight, tree_node, node)
        #print(tree_node)
        #print(graph_holder.neighbors(tree_node))
        for x in graph_holder.neighbors(tree_node):
            if(not tree_contains(tree,x)):
                #print(tree)
                tree = change_tree(tree,tree_node, node,weight)
                #print(tree)
                for y in edges:
                    #print(que)
                    if y[1] == node:
                        if(not check_in(y, holder)):
                            heapq.heappush(que, y)
                            holder.add(y)


            elif(less_weight(tree,tree_node, weight)):
                #print(tree)
                tree = change_tree(tree, tree_node, node, weight)
                #print(tree)
                #print()
                for y in edges:
                    if y[1] == node:
                        if (not check_in(y,holder)):
                            heapq.heappush(que, y)
                            holder.add(y)

            else:
                pass

    print(tree)
    print(que)'''

def check_in(inside, s):
    if(inside in s):
        return True

    x = inside[0]
    y = inside[1]
    z = inside[2]
    holder = (x,z,y)

    if(holder in s):
        return True

    return False



    #tree_edges = []
    # TODO compute the edges of a minimum spanning tree
    #write_tree_edges_to_file(tree_edges, filename + '.mst')



if __name__ == "__main__":
    compute_mst("test10")
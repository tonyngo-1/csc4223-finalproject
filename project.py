import networkx as nx

def nodes_connected(u, v):
    return u in nx.neighbors(v)

def main():
    degreeG1 = 0
    degreeG2 = 0

    # Read in both edge list G1, G2
    G1 = nx.read_edgelist("seed_G1.edgelist")
    G2 = nx.read_edgelist("seed_G2.edgelist")

    # print(G1.number_of_edges(0,330))

    G1check = list(G1.edges('0'))

    for i in G1check:
        degreeG1 += 1

    G2check = list(G2.edges('0'))

    for i in G2check:
        degreeG2 += 1

    print(degreeG1)
    print(degreeG2)



    # if (int(G1.edges('0'))):
    #     degreeG1+= 1

    # print("degree g1 = " + degreeG1)
    # G = nx.path_graph(4)
    # G.number_of_edges()

    # Read in adjacency list
    # d = {}
    # with open("seed_node_pairs.txt") as f:
    #     for line in f:
    #         (key, val) = line.split()
    #         d[int(key)] = val
    # print(d)

    # Get list of matched neighbors
    

    # # Check if nodes edges are connected
    # if (nx.is_k_edge_connected(G1, k=1)):
    #     degreeG1 += 1

    # # Check if nodes edges are connected
    # if (nx.is_k_edge_connected(G2, k=1)):
    #     degreeG2 += 1

    # # threshold = 0.5
    




if __name__ == "__main__":
    main()
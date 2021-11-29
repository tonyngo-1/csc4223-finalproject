import networkx as nx

def nodes_connected(u, v):
    return u in nx.neighbors(v)

def main():
    degreeG1 = 0
    degreeG2 = 0

    # Read in both edge list G1, G2
    G1 = nx.read_edgelist("seed_G1.edgelist")
    G2 = nx.read_edgelist("seed_G2.edgelist")

    # Read in adjacency list
    d = {}
    with open("seed_node_pairs.txt") as f:
        for line in f:
            (key, val) = line.split()
            d[int(key)] = val

    print(d)

    # Get list of nodes that aren't connected
    nodes_connected("a", "d")

    nodes_connected("a", "c")





    # # Check if nodes edges are connected
    # if (nx.is_k_edge_connected(G1, k=1)):
    #     degreeG1 += 1

    # # Check if nodes edges are connected
    # if (nx.is_k_edge_connected(G2, k=1)):
    #     degreeG2 += 1

    # # threshold = 0.5
    




if __name__ == "__main__":
    main()
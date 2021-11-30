import networkx as nx
import math 
from random import randrange

def nodes_connected(u, v):
    return u in nx.neighbors(v)

def main():
    matchingNeighbors = 0
    degreeG1 = 0
    degreeG2 = 0
    edge1 = randrange(4091)
    edge2 = randrange(4091)

    # Read in adjacency list
    pairs_dict = {}
    with open("seed_node_pairs.txt") as f:
        for line in f:
            (key, val) = line.split()
            pairs_dict[int(key)] = val

    # Read in both edge list G1, G2
    G1 = nx.read_edgelist("seed_G1.edgelist")
    G2 = nx.read_edgelist("seed_G2.edgelist")

    G1check = list(G1.edges(edge1))
    G2check = list(G2.edges(edge2))


    for i in G1check:
        for j in pairs_dict:
            # Checks to see if the node in G1 exists within seed node pairs
            if (int(i[1]) == int(j)):
                for k in G2check:
                    # Checks to see if the node in G2 exists within the seed node pairs
                    if (int(k[0]) == int(pairs_dict[j])):
                        matchingNeighbors += 1

    for i in G1check:
        degreeG1 += 1


    for i in G2check:
        degreeG2 += 1

    threshold = 0.5
    score_calc = matchingNeighbors / (math.sqrt(degreeG1) * math.sqrt(degreeG2))

    if (score_calc > threshold):
        pairs_dict[edge1] = edge2

if __name__ == "__main__":
    main()
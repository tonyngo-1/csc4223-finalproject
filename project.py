import networkx as nx
import math 
from random import randrange

def main():
    matchingNeighbors = 0
    degreeG1 = 0
    degreeG2 = 0

    # Read in adjacency list
    pairs_dict = {}
    with open("seed_node_pairs.txt") as f:
        for line in f:
            (key, val) = line.split()
            pairs_dict[int(key)] = val

    # Read in both edge list G1, G2
    G1 = nx.read_edgelist("seed_G1.edgelist")
    G2 = nx.read_edgelist("seed_G2.edgelist")

    # Iterate through 1000 times
    for x in range(1000):
        # Check edges against random values that exist within the set
        edge1 = str(randrange(4091))
        edge2 = str(randrange(4091))

        # Check if pair already exists within seed_node_pairs.txt file, if so, skip iteration in loop
        for i in pairs_dict:
            if (edge1 == int(i)):
                if (edge2 == int(pairs_dict[i])):
                    continue

        # Get the edges of each graph and turn into an iterable list
        G1check = list(G1.edges(edge1))
        G2check = list(G2.edges(edge2))

        for i in G1check:
            for j in pairs_dict:
                # Checks to see if the node in G1 exists within the first value of the seed node pair (aka the key in this case)
                if (int(i[1]) == int(j)):
                    for k in G2check:
                        # Checks to see if the node in G2 exists within the seed node pairs, if so, add matching neighbors
                        if (int(k[1]) == int(pairs_dict[j])):
                            matchingNeighbors += 1

        # Iterate through the list of edges in G1 to get the degree of connections
        for i in G1check:
            degreeG1 += 1

        # Iterate through the list of edges in G2 to get the degree of connections
        for i in G2check:
            degreeG2 += 1

        # Threshold
        threshold = 0.005

        # Score Calculation
        score_calc = matchingNeighbors / (math.sqrt(degreeG1) * math.sqrt(degreeG2))

        # Add to dictionary if score calculation exceeds threshold value
        if (score_calc > threshold):
            pairs_dict[edge1] = (edge2)
    
    # Write results into new file project_results.txt
    with open("project_results.txt", 'w') as f: 
        for key, value in pairs_dict.items(): 
            f.write('%s %s\n' % (key, value))


if __name__ == "__main__":
    main()
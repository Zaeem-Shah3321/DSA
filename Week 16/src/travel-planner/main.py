from graph import Graph
from algos import dijkstra
import os

def load_locations(file_path):
    graph = Graph()
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            location = parts[0]
            graph.add_node(location)
            for i in range(1, len(parts), 2):
                neighbor = parts[i]
                weight = int(parts[i + 1])
                graph.add_edge(location, neighbor, weight)
    return graph

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'F:\DSA\Week 16\data\locations.csv')
    graph = load_locations(file_path)
    
    start = input("Enter the starting location: ")
    end = input("Enter the destination location: ")
    
    distances = dijkstra(graph, start)
    print(f"Shortest distance from {start} to {end} is {distances[end]}")

if __name__ == "__main__":
    main()
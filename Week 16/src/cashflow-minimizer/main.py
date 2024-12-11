from graph import Graph
from algos import minimize_cash_flow
import os

def load_transactions(file_path):
    graph = Graph()
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            from_person = parts[0]
            to_person = parts[1]
            amount = int(parts[2])
            graph.add_edge(from_person, to_person, amount)
    return graph

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../../data/transactions.csv')
    graph = load_transactions(file_path)
    
    transactions = minimize_cash_flow(graph)
    for debtor, creditor, amount in transactions:
        print(f"{debtor} pays {creditor} {amount}")

if __name__ == "__main__":
    main()
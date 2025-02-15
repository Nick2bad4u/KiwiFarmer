import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import json
import os

# Load data from the JSON file
def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

# Plot follower network
def plot_follower_network(data, output_dir):
    try:
        G = nx.Graph()

        for user_id, user_info in data['users'].items():
            if 'followers' in user_info:
                for follower_id, follower_info in user_info['followers'].items():
                    follower_name = follower_info['user_name']
                    user_name = user_info['user_username']
                    G.add_edge(user_name, follower_name)

        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, k=0.1)  # Positions for all nodes
        nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=8, font_weight="bold", edge_color='gray')
        plt.title('Follower Network')
        output_path = os.path.join(output_dir, 'follower_network.png')
        plt.savefig(output_path)
        plt.close()
    except KeyError as e:
        print(f"KeyError: {e}")
        print("Available keys in data:", data.keys())

# Example usage
if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kiwifarms_reorganized_database.json')
    data = load_data(file_path)

    if data:
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data_visuals')
        os.makedirs(output_dir, exist_ok=True)

        # Plot follower network
        plot_follower_network(data, output_dir)
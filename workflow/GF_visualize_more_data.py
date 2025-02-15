import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from datetime import datetime
import json
import os
from wordcloud import WordCloud
from textblob import TextBlob
import logging

# Configure logging
logging.basicConfig(filename='visualization.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load data from the JSON file
def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        logging.info(f"Data loaded successfully from {file_path}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return None

# Plot user messages over time
def plot_user_messages_over_time(data, output_dir):
    try:
        messages = []
        for thread_id, thread_info in data['threads'].items():
            for message in thread_info['messages']:
                timestamp = message['timestamp']
                date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                messages.append({'date': date, 'thread_id': thread_id})
        messages_df = pd.DataFrame(messages)
        messages_df['date'] = pd.to_datetime(messages_df['date'])
        messages_df.set_index('date', inplace=True)
        messages_count = messages_df.groupby('date').count()['thread_id']
        messages_count.plot(kind='bar', figsize=(12, 6))
        plt.title('Messages Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Messages')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout(pad=2)
        output_path = os.path.join(output_dir, 'messages_over_time.png')
        plt.savefig(output_path)
        plt.close()
        logging.info("User messages over time plot saved successfully")
    except Exception as e:
        logging.error(f"Error plotting user messages over time: {e}")

# Plot user activity heatmap
def plot_user_activity_heatmap(data, output_dir):
    try:
        messages = []
        for thread_id, thread_info in data['threads'].items():
            for message in thread_info['messages']:
                timestamp = message['timestamp']
                dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                messages.append({'hour': dt.hour, 'weekday': dt.weekday()})
        messages_df = pd.DataFrame(messages)
        heatmap_data = messages_df.groupby(['weekday', 'hour']).size().unstack(fill_value=0)
        plt.figure(figsize=(12, 6))
        sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt="d")
        plt.title('User Activity Heatmap')
        plt.xlabel('Hour of Day')
        plt.ylabel('Day of Week')
        plt.yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5],
                   ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], rotation=0)
        output_path = os.path.join(output_dir, 'user_activity_heatmap.png')
        plt.savefig(output_path)
        plt.close()
        logging.info("User activity heatmap plot saved successfully")
    except Exception as e:
        logging.error(f"Error plotting user activity heatmap: {e}")

# Generate word cloud
def generate_word_cloud(data, output_dir):
    try:
        text = ' '.join(message['content'] for thread in data['threads'].values() for message in thread['messages'])
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud of Messages')
        output_path = os.path.join(output_dir, 'word_cloud.png')
        plt.savefig(output_path)
        plt.close()
        logging.info("Word cloud plot saved successfully")
    except Exception as e:
        logging.error(f"Error generating word cloud: {e}")

# Perform sentiment analysis and plot sentiment distribution
def plot_sentiment_distribution(data, output_dir):
    try:
        sentiments = []
        for thread in data['threads'].values():
            for message in thread['messages']:
                text = message['content']
                blob = TextBlob(text)
                sentiments.append(blob.sentiment.polarity)
        plt.figure(figsize=(10, 6))
        sns.histplot(sentiments, bins=20, kde=True)
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment Polarity')
        plt.ylabel('Frequency')
        output_path = os.path.join(output_dir, 'sentiment_distribution.png')
        plt.savefig(output_path)
        plt.close()
        logging.info("Sentiment distribution plot saved successfully")
    except Exception as e:
        logging.error(f"Error plotting sentiment distribution: {e}")

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
        plt.figure(figsize=(30, 16))
        pos = nx.spring_layout(G, k=0.1)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=8, font_weight="bold", edge_color='gray')
        plt.title('Follower Network')
        output_path = os.path.join(output_dir, 'follower_network.png')
        plt.savefig(output_path)
        plt.close()
        logging.info("Follower network plot saved successfully")
    except KeyError as e:
        logging.error(f"KeyError plotting follower network: {e}")
    except Exception as e:
        logging.error(f"Error plotting follower network: {e}")

# Plot top contributors
def plot_top_contributors(data, output_dir):
    try:
        user_message_counts = {}
        user_names = {user_id: user_info['user_username'] for user_id, user_info in data['users'].items()}
        for thread_id, thread_info in data['threads'].items():
            for message in thread_info['messages']:
                user_id = message['user_id']
                if user_id not in user_message_counts:
                    user_message_counts[user_id] = 0
                user_message_counts[user_id] += 1
        top_contributors = sorted(user_message_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        top_contributors_df = pd.DataFrame(top_contributors, columns=['user_id', 'message_count'])
        top_contributors_df['user_name'] = top_contributors_df['user_id'].apply(lambda x: user_names.get(str(x), 'Unknown'))
        top_contributors_df['user_label'] = top_contributors_df['user_id'].astype(str) + '\n' + top_contributors_df['user_name']
        top_contributors_df.plot(kind='bar', x='user_label', y='message_count', figsize=(12, 6))
        plt.title('Top Contributors')
        plt.xlabel('User ID and Name')
        plt.ylabel('Number of Messages')
        plt.tight_layout(pad=2)
        output_path = os.path.join(output_dir, 'top_contributors.png')
        plt.savefig(output_path)
        plt.close()
        logging.info("Top contributors plot saved successfully")
    except Exception as e:
        logging.error(f"Error plotting top contributors: {e}")

# Plot user role distribution
def plot_user_role_distribution(data, output_dir):
    try:
        role_counts = {}
        for user_id, user_info in data['users'].items():
            role = user_info['user_role']
            if role not in role_counts:
                role_counts[role] = 0
            role_counts[role] += 1
        role_counts_df = pd.DataFrame(list(role_counts.items()), columns=['role', 'count'])
        role_counts_df.plot(kind='bar', x='role', y='count', figsize=(12, 6))
        plt.title('User Role Distribution')
        plt.xlabel('Role')
        plt.ylabel('Count')
        plt.tight_layout(pad=2)
        output_path = os.path.join(output_dir, 'user_role_distribution.png')
        plt.savefig(output_path)
        plt.close()
        logging.info("User role distribution plot saved successfully")
    except Exception as e:
        logging.error(f"Error plotting user role distribution: {e}")

# Plot follower network analysis
def plot_follower_network_analysis(data, output_dir):
    try:
        G = nx.Graph()
        for user_id, user_info in data['users'].items():
            if 'followers' in user_info:
                for follower_id, follower_info in user_info['followers'].items():
                    follower_name = follower_info['user_name']
                    user_name = user_info['user_username']
                    G.add_edge(user_name, follower_name)
        degree_centrality = nx.degree_centrality(G)
        degree_centrality_sorted = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
        degree_centrality_df = pd.DataFrame(degree_centrality_sorted, columns=['user_name', 'degree_centrality'])
        degree_centrality_df.plot(kind='bar', x='user_name', y='degree_centrality', figsize=(12, 6))
        plt.title('Top 10 Users by Degree Centrality in Follower Network')
        plt.xlabel('User Name')
        plt.ylabel('Degree Centrality')
        plt.tight_layout(pad=2)
        output_path = os.path.join(output_dir, 'follower_network_analysis.png')
        plt.savefig(output_path)
        plt.close()
        logging.info("Follower network analysis plot saved successfully")
    except KeyError as e:
        logging.error(f"KeyError plotting follower network analysis: {e}")
    except Exception as e:
        logging.error(f"Error plotting follower network analysis: {e}")

# Plot message length distribution
def plot_message_length_distribution(data, output_dir):
    try:
        message_lengths = []
        for thread in data['threads'].values():
            for message in thread['messages']:
                message_lengths.append(len(message['content']))
        plt.figure(figsize=(10, 6))
        sns.histplot(message_lengths, bins=20, kde=True)
        plt.title('Message Length Distribution')
        plt.xlabel('Message Length (characters)')
        plt.ylabel('Frequency')
        output_path = os.path.join(output_dir, 'message_length_distribution.png')
        plt.savefig(output_path)
        plt.close()
        logging.info("Message length distribution plot saved successfully")
    except Exception as e:
        logging.error(f"Error plotting message length distribution: {e}")

# Example usage
if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kiwifarms_reorganized_database.json')
    data = load_data(file_path)

    if data:
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data_visuals')
        os.makedirs(output_dir, exist_ok=True)

        # Plot user messages over time
        plot_user_messages_over_time(data, output_dir)

        # Plot user activity heatmap
        plot_user_activity_heatmap(data, output_dir)

        # Generate word cloud
        generate_word_cloud(data, output_dir)

        # Plot sentiment distribution
        plot_sentiment_distribution(data, output_dir)

        # Plot follower network
        plot_follower_network(data, output_dir)

        # Plot top contributors
        plot_top_contributors(data, output_dir)

        # Plot user role distribution
        plot_user_role_distribution(data, output_dir)

        # Plot follower network analysis
        plot_follower_network_analysis(data, output_dir)

        # Plot message length distribution
        plot_message_length_distribution(data, output_dir)
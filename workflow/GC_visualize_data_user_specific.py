import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
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

# Extract and plot user messages over time
def plot_user_messages_over_time(data, user_id, output_dir):
    try:
        messages = []
        for thread_id, thread_info in data['threads'].items():
            for message in thread_info['messages']:
                if message['user_id'] == user_id:
                    timestamp = message['timestamp']
                    date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                    messages.append({'date': date, 'thread_id': thread_id})
        if not messages:
            print(f"No messages found for user_id: {user_id}")
            return
        messages_df = pd.DataFrame(messages)
        messages_df['date'] = pd.to_datetime(messages_df['date'])
        messages_df.set_index('date', inplace=True)
        messages_count = messages_df.groupby('date').count()['thread_id']
        messages_count.plot(kind='bar', figsize=(12, 6))
        plt.title(f'User {user_id} Messages Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Messages')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout(pad=2)
        output_path = os.path.join(output_dir, f'user_{user_id}_messages_over_time.png')
        plt.savefig(output_path)
        plt.close()
    except KeyError as e:
        print(f"KeyError: {e}")
        print("Available keys in data:", data.keys())

# Extract and plot user activity heatmap
def plot_user_activity_heatmap(data, user_id, output_dir):
    try:
        messages = []
        for thread_id, thread_info in data['threads'].items():
            for message in thread_info['messages']:
                if message['user_id'] == user_id:
                    timestamp = message['timestamp']
                    dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                    messages.append({'hour': dt.hour, 'weekday': dt.weekday()})
        if not messages:
            print(f"No messages found for user_id: {user_id}")
            return
        messages_df = pd.DataFrame(messages)
        heatmap_data = messages_df.groupby(['weekday', 'hour']).size().unstack(fill_value=0)
        plt.figure(figsize=(12, 6))
        sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt="d")
        plt.title(f'User {user_id} Activity Heatmap')
        plt.xlabel('Hour of Day')
        plt.ylabel('Day of Week')
        plt.yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], rotation=0)
        output_path = os.path.join(output_dir, f'user_{user_id}_activity_heatmap.png')
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

        user_ids_to_visualize = [1, 2]  # Example user_ids, change as needed

        for user_id in user_ids_to_visualize:
            # Plot user messages over time
            plot_user_messages_over_time(data, user_id, output_dir)

            # Plot user activity heatmap
            plot_user_activity_heatmap(data, user_id, output_dir)
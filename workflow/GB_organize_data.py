"""_schema_
{
    "users": {
        "users": {
            "user_id_1": {
                "user_username": "string",
                "user_id": "integer",
                "user_image": "string (URL)",
                "user_messages": "integer",
                "user_reaction_score": "string",
                "user_points": "integer",
                "user_joined": "integer (timestamp)",
                "user_last_seen": "integer (timestamp)",
                "user_blurb": "string",
                "user_role": "string"
            },
            "user_id_2": {
                // same structure as user_id_1
            },
            // more users...
        },
        "followers": {
            "following": {
                "user_id_1": {
                    "follower_id_1": {
                        "user_name": "string",
                        "user_id": "integer"
                    },
                    "follower_id_2": {
                        // same structure as follower_id_1
                    },
                    // more followers...
                },
                "user_id_2": {
                    // same structure as user_id_1
                },
                // more followees...
            }
        },
        "user_id_1": {
            "trophies": [
                {
                    "points": "integer",
                    "name": "string",
                    "description": "string",
                    "date": "string (ISO 8601 date format)"
                },
                // more trophies...
            ]
        },
        "user_id_2": {
            // same structure as user_id_1
        },
        // more users with trophies...
    },
    "threads": {
        "thread_id_1": {
            "thread_id": "integer",
            "title": "string",
            "timestamp": "integer (timestamp)",
            "messages": [
                {
                    "user_name": "string",
                    "user_id": "integer",
                    "content": "string",
                    "timestamp": "string (datetime)"
                },
                // more messages...
            ]
        },
        "thread_id_2": {
            // same structure as thread_id_1
        },
        // more threads...
    }
}
"""

import json
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Path to the input JSON file in the parent directory
input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kiwifarms_combined_database.json')
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kiwifarms_reorganized_database.json')

# Function to read JSON data from a file
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            logging.info(f"Reading data from {file_path}")
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        raise

# Function to check if the contents of the new data already exist in the file
def is_duplicate(existing_data, new_data):
    return existing_data == new_data

# Function to reorganize the JSON data
def reorganize_data(data):
    try:
        users = data.get('users', {}).get('users', {})
        followers = data.get('users', {}).get('followers', {}).get('following', {})
        trophies = {k: v for k, v in data.get('users', {}).items() if k.isdigit()}

        # Attach followers and trophies to the corresponding users
        for user_id, user_data in users.items():
            if user_id in followers:
                user_data['followers'] = followers[user_id]
            if user_id in trophies:
                user_data['trophies'] = trophies[user_id]

        reorganized_data = {
            "users": users,
            "threads": data.get('threads', {})
        }

        logging.info("Data successfully reorganized")
        return reorganized_data

    except Exception as e:
        logging.error(f"An error occurred while reorganizing data: {e}")
        raise

# Function to write JSON data to a file
def write_json_file(file_path, data):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                existing_data = json.load(file)
                if is_duplicate(existing_data, data):
                    logging.info(f"Duplicate data found. No changes made to {file_path}")
                    return
        except (FileNotFoundError, json.JSONDecodeError):
            logging.warning(f"Failed to read existing file for duplication check: {file_path}")

    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logging.info(f"Reorganized JSON data has been written to {file_path}")
    except IOError as e:
        logging.error(f"An error occurred while writing to file: {file_path}, {e}")
        raise

# Read the input JSON data
input_json = read_json_file(input_file_path)

# Reorganize the JSON data
reorganized_json = reorganize_data(input_json)

# Output the reorganized JSON data
write_json_file(output_file_path, reorganized_json)
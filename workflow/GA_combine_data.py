import json

# Load JSON files
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

following = load_json('kiwifarms_following_20210224.json')
trophies = load_json('kiwifarms_trophies_20210224.json')
users = load_json('kiwifarms_users_20210224.json')
threads = load_json('kiwifarms_20210224.json')

# Combine data
database = {}

# Add users data
database['users'] = users

# Merge following data into users
for user_id, follow_list in following.items():
    if user_id in database['users']:
        database['users'][user_id]['following'] = follow_list
    else:
        database['users'][user_id] = {'following': follow_list}

# Merge trophies data into users
for user_id, trophy_data in trophies['trophies'].items():
    if user_id in database['users']:
        database['users'][user_id]['trophies'] = trophy_data['trophies_earned']
    else:
        database['users'][user_id] = {'trophies': trophy_data['trophies_earned']}

# Add threads data
database['threads'] = threads

# Remove duplicate entries in each section
def remove_duplicates(data):
    if isinstance(data, list):
        unique = []
        seen = set()
        for item in data:
            item_str = json.dumps(item, sort_keys=True)
            if item_str not in seen:
                unique.append(item)
                seen.add(item_str)
        return unique
    elif isinstance(data, dict):
        unique_dict = {}
        for key, value in data.items():
            unique_dict[key] = remove_duplicates(value)
        return unique_dict
    return data

database = remove_duplicates(database)

# Save the combined database
with open('kiwifarms_combined_database.json', 'w', encoding='utf-8') as outfile:
    json.dump(database, outfile, ensure_ascii=False, indent=4)

print("Combined database created successfully.")
import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Load combined database
database = load_json('kiwifarms_combined_database.json')

# Sort users by username
database['users'] = dict(sorted(database['users'].items(), key=lambda x: x[1]['user_username'].lower()))

# Sort following by user_id
database['following'] = dict(sorted(database['following'].items(), key=lambda x: x[0]))

# Sort trophies by user_id and then by points
database['trophies'] = dict(sorted(database['trophies'].items(), key=lambda x: (x[0], sorted(x[1]['trophies'], key=lambda t: t['points'], reverse=True))))

# Sort threads by thread_id
database['threads'] = dict(sorted(database['threads'].items(), key=lambda x: int(x[0])))

# Save the sorted database
save_json(database, 'kiwifarms_sorted_database.json')

print("Sorted database created successfully.")

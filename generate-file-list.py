import os
import random

# List of files and folders to ignore
ignore_list = [
    ".git",
    "node_modules",
    ".DS_Store",
    ".history",
    "styles"
]

def should_ignore(path, ignore_list):
    for ignore_item in ignore_list:
        if ignore_item in path.split(os.sep):
            return True
    return False

def generate_file_list(directory, ignore_list):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), directory)
            # Ignore specified files and folders
            if not should_ignore(file_path, ignore_list):
                file_list.append(file_path)
    return file_list

def get_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def generate_file_list_with_links(file_list, repo_url):
    file_list_html = []
    for file in file_list:
        color = get_random_color()
        file_url = f"{repo_url}/blob/main/{file}".replace("\\", "/")
        file_list_html.append(f'<a href="{file_url}" style="color: {color};">{file}</a>')
    return file_list_html

def save_file_list(file_list_html, output_file):
    with open(output_file, 'w') as f:
        f.write("## File List\n\n")
        f.write("Here is a list of files included in this repository:\n\n")
        for file in file_list_html:
            f.write(f"- {file}\n")

if __name__ == "__main__":
    directory = "."  # Change this to the root directory of your repository
    repo_url = "https://github.com/Nick2bad4u/KiwiFarmer"  # Change this to your GitHub repository URL
    output_file = "file_list.txt"

    file_list = generate_file_list(directory, ignore_list)
    file_list_html = generate_file_list_with_links(file_list, repo_url)
    save_file_list(file_list_html, output_file)

    print(f"File list saved to {output_file}")

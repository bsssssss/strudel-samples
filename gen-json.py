import os
import json


folder_name = os.path.basename(os.getcwd())

base_url = "https://raw.githubusercontent.com/bsssssss/strudel-samples/main"
full_url = f"{base_url}/{folder_name}"

def generate_json():

    data = {
        "_base": full_url
    }
    
    # Iterate through each directory in the current folder
    for dir_name, _, file_list in os.walk('.'):
        if dir_name == '.' or dir_name.startswith('./.'):
            continue
        dir_name = dir_name[2:]  # Remove the './' from the directory name
        data[dir_name] = []
        for file_name in file_list:
            if file_name.lower().endswith('.wav'):
                data[dir_name].append(f"{folder_name}/{dir_name}/{file_name}")
    with open('strudel.json', 'w') as json_file:
        # Minify if possible
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    generate_json()
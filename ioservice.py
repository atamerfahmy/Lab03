import json


# function to add to JSON
def write_json(new_data, mode="users", filename='data.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[mode].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


def write_new_json(new_data, filename='data.json'):
    new_file_data = {}

    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        print(type(new_data))
        new_file_data["users"] = file_data["users"]
        new_file_data["projects"] = new_data
        # Sets file's current position at offset.

        print(new_file_data)
        file.seek(0)
        # convert back to json.
    with open(filename, 'w') as open_file:
        json.dump(new_file_data, open_file, indent=4)


def read_json(mode="users", filename='data.json'):
    with open(filename, 'r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        return file_data[mode]


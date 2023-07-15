import json
def save(path : str, data : dict):
    with open(path, 'r') as f:
        retrieved_data = json.load(f)

    # Check if the entry with the same name already exists
    existing_index = next((index for index, p in enumerate(retrieved_data) if p['name'] == data['name']), None)
    if existing_index is not None:
        # Overwrite the existing entry with the new data
        retrieved_data[existing_index] = data
    else:
        # Append the new information to the list
        retrieved_data.append(data)

    # Save the updated information to the JSON file
    with open(path, 'w') as f:
        json.dump(retrieved_data, f)

def load(path : str, name : str):
    with open(path, 'r') as f:
        retrieved_data = json.load(f)
    # Find the entry with the matching name
    found = False
    for data in retrieved_data:
        if data['name'] == name:
            found = True
            break
    
    if found:
        return data
    else:
        return None
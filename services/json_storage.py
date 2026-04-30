import json
import os
import uuid

def get_full_path(file_path):
    # Ensure file_path is relative to the root directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, file_path)

def load_data(file_path):
    path = get_full_path(file_path)
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return []

def save_data(file_path, data):
    path = get_full_path(file_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving {file_path}: {e}")
        return False

def append_data(file_path, new_record):
    data = load_data(file_path)
    if 'id' not in new_record or not new_record['id']:
        new_record['id'] = str(uuid.uuid4())
    data.append(new_record)
    return save_data(file_path, data)

def update_data(file_path, record_id, updated_record):
    data = load_data(file_path)
    for i, record in enumerate(data):
        if record.get('id') == record_id:
            updated_record['id'] = record_id # Preserve ID
            data[i] = updated_record
            return save_data(file_path, data)
    return False

def delete_data(file_path, record_id):
    data = load_data(file_path)
    initial_length = len(data)
    data = [record for record in data if record.get('id') != record_id]
    if len(data) < initial_length:
        return save_data(file_path, data)
    return False

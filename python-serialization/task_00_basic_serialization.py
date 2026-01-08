#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    
    Parameters:
        data (dict): The Python dictionary to be serialized.
        filename (str): The name of the file where the data will be saved.
        
    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
        print(f"Data serialized and saved to '{filename}'.")

def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file into a Python dictionary.
    
    Parameters:
        filename (str): The name of the file containing the serialized data.
        
    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

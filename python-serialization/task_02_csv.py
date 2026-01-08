#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        return False
